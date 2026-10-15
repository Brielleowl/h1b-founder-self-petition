#!/usr/bin/env python3
"""Validate a case.json for an H-1B beneficiary-owner petition.

Usage: python validate_case.py case.json [--fix]

Checks date arithmetic, the 18-month limit, the LCA window, annualised pay, fee totals and
evidence filenames, and lists fields still null. With --fix it fills derivable fields
(annualized_pay, period_wage, specialty/owner hours, fees, petition.end default) in place.
Exit code 1 if any ERROR.
"""
import json, re, sys
from datetime import date, timedelta

FEES_SMALL = {"base": 460, "asylum": 300, "acwia": 750, "fraud": 500}
FEES_LARGE = {"base": 780, "asylum": 600, "acwia": 1500, "fraud": 500}
PREMIUM = 2965  # verify at uscis.gov/g-1055

errors, warns, info = [], [], []

def E(m): errors.append(m)
def W(m): warns.append(m)
def I(m): info.append(m)

def d(s):
    if not s: return None
    try: return date.fromisoformat(s)
    except ValueError:
        E(f"date not ISO YYYY-MM-DD: {s!r}"); return None

def add_months(dt, n):
    y, m = divmod(dt.month - 1 + n, 12)
    y += dt.year; m += 1
    last = [31, 29 if y % 4 == 0 and (y % 100 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    return date(y, m, min(dt.day, last))

def nulls(obj, path=""):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.startswith("_"): continue
            out += nulls(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj): out += nulls(v, f"{path}[{i}]")
    elif obj is None:
        out.append(path)
    return out

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    path = sys.argv[1]; fix = "--fix" in sys.argv
    c = json.load(open(path))
    P, B, L, T, F, X, R = (c.get(k, {}) for k in ("petitioner", "beneficiary", "lca", "petition", "funding", "evidence", "company_role"))

    # --- ownership
    pct = R.get("ownership_pct")
    if pct is None: E("company_role.ownership_pct missing")
    elif pct <= 50: E(f"ownership {pct}% is not a controlling interest (>50%) — the beneficiary-owner rule does not apply; file as an ordinary petition")

    # --- dates
    start, end = d(T.get("start")), d(T.get("end"))
    lfrom, lto = d(L.get("valid_from")), d(L.get("valid_to"))
    if start and not end and fix:
        end = add_months(start, 18) - timedelta(days=1); T["end"] = end.isoformat(); I(f"petition.end set to {end}")
    if start and end:
        if end <= start: E("petition.end must be after petition.start")
        limit = add_months(start, 18) - timedelta(days=1)
        if end > limit: E(f"petition.end {end} exceeds the 18-month limit ({limit}) for a first beneficiary-owner petition")
        elif end < limit: I(f"petition.end {end} is earlier than the 18-month maximum {limit}")
    if start and lfrom and start < lfrom: E(f"petition.start {start} is before LCA valid_from {lfrom}")
    if end and lto and end > lto: E(f"petition.end {end} is after LCA valid_to {lto}")
    if start and start < date.today(): W(f"petition.start {start} is in the past; USCIS may still accept it but the offer letter's 'or on receipt, if later' clause matters")
    sv = d(B.get("status_valid_until"))
    if sv and start and sv < start: W("current status expires before the requested start; portability/grace-period facts need checking")
    i94exp = d((B.get("i94") or {}).get("expires"))
    if sv and i94exp and sv != i94exp: W("beneficiary.status_valid_until != beneficiary.i94.expires — the I-94 date on the latest I-797A governs")
    rec = B.get("prior_h1b_receipts") or []
    if rec and sv:
        last_to = d(rec[-1].get("valid_to"))
        if last_to and sv == last_to: W("status_valid_until equals the I-797 validity end; the I-94 on the notice is usually ~10 days later — check")

    # --- wage / hours
    rate, hrs = L.get("wage_rate"), L.get("hours_per_week")
    if rate and hrs:
        ann = round(rate * hrs * 52)
        if T.get("annualized_pay") is None:
            if fix: T["annualized_pay"] = ann; I(f"annualized_pay set to {ann}")
            else: W(f"petition.annualized_pay missing; expected {ann}")
        elif abs(T["annualized_pay"] - ann) > 1: E(f"annualized_pay {T['annualized_pay']} != rate*hours*52 = {ann}")
        if start and end:
            weeks = (end - start).days / 7
            pw = round(rate * hrs * weeks)
            if T.get("period_wage") is None:
                if fix: T["period_wage"] = pw; I(f"period_wage set to {pw}")
            elif abs(T["period_wage"] - pw) > 300: W(f"period_wage {T['period_wage']} differs from rate*hours*weeks = {pw}")
        if L.get("full_time") and hrs < 35: W("full_time true but hours < 35")
        if not L.get("full_time") and hrs >= 35: W("full_time false but hours >= 35")
        sp, op = T.get("specialty_hours_pct"), T.get("owner_hours_pct")
        if sp is not None and sp <= 50: E("specialty_hours_pct must exceed 50 (majority on specialty duties)")
        if sp is not None and op is not None and sp + op != 100: E("specialty_hours_pct + owner_hours_pct != 100")
        if sp and fix and T.get("specialty_hours") is None:
            T["specialty_hours"] = round(hrs * sp / 100); T["owner_hours"] = hrs - T["specialty_hours"]
            I(f"specialty/owner hours set to {T['specialty_hours']}/{T['owner_hours']}")
        duties = (c.get("position") or {}).get("duties") or []
        dh = sum((x.get("hours") or 0) for x in duties)
        if duties and T.get("specialty_hours") and dh != T["specialty_hours"]:
            E(f"sum of duty hours {dh} != specialty_hours {T['specialty_hours']}")
        if (L.get("prevailing_wage") or 0) > (rate or 0): E("wage_rate below prevailing_wage")
    lvl = str(L.get("wage_level") or "")
    if lvl.upper() in ("I", "1") and (T.get("experience_years") or 0) > 0:
        E("Level I LCA with experience_years > 0 — contradictory; set experience_years to 0 or re-file the LCA at a higher level")

    # --- fees
    fte = (c.get("fees") or {}).get("fte") or (P.get("employees_total") or 0) + 1
    f = FEES_SMALL if fte <= 25 else FEES_LARGE
    i129 = sum(f.values()); total = i129 + (PREMIUM if T.get("premium_processing") else 0)
    fees = c.setdefault("fees", {})
    if fix:
        fees.update({"fte": fte, "i129_total": i129, "i907": PREMIUM if T.get("premium_processing") else 0, "total": total})
    elif fees.get("total") not in (None, total): W(f"fees.total {fees.get('total')} != computed {total} (verify at uscis.gov/g-1055)")
    I(f"fees: I-129 {i129} + I-907 {PREMIUM if T.get('premium_processing') else 0} = {total} (FTE {fte}); verify on G-1055")

    # --- evidence filenames
    for ex in (X.get("exhibits") or []):
        fn = ex.get("file")
        if ex.get("include") and not fn: W(f"exhibit {ex.get('letter')} included but no file")
        if fn and re.search(r"[,;]|\s", fn): E(f"filename {fn!r} contains a comma or whitespace — USCIS rejects it")

    # --- omissions
    om = (c.get("omit") or {}).get("employers_not_to_mention") or []
    for emp in om:
        for row in (B.get("employment") or []):
            if row.get("employer") and emp.lower() in row["employer"].lower():
                E(f"employment history lists {row['employer']!r} but omit list says not to mention it")

    # --- report
    for m in errors: print("ERROR ", m)
    for m in warns: print("WARN  ", m)
    for m in info: print("INFO  ", m)
    nl = [n for n in nulls(c) if not n.startswith("evidence") and not n.endswith(".dba") and ".ssn" not in n and ".middle_name" not in n and not n.endswith("employment[0].to")]
    if nl:
        print(f"NULL   {len(nl)} fields still unknown:")
        for n in nl: print("        ", n)
    if fix:
        json.dump(c, open(path, "w"), indent=2, ensure_ascii=False); print("fixed file written")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
