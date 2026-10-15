#!/usr/bin/env python3
"""Render the document templates from case.json.

Usage: python render_templates.py case.json [--out drafts/] [--docx]

Substitutes every {{dotted.key}} from case.json plus the computed keys listed in COMPUTED.
Unknown keys are left as "[DRAFT: key]" so nothing is silently blank. With --docx, also converts
each rendered .md to .docx with pandoc if it is installed (then edit/sign in Word and export PDF, or
use the docx skill).
"""
import json, os, re, subprocess, sys
from datetime import date

TEMPLATES = ["support-letter.md", "job-description.md", "offer-letter.md",
             "employment-agreement.md", "board-consent.md", "additional-information.md"]

def long_date(s):
    if not s: return None
    try:
        dt = date.fromisoformat(s); return f"{dt.strftime('%B')} {dt.day}, {dt.year}"
    except ValueError: return s

def money(n):
    return None if n is None else f"${n:,.0f}" if float(n).is_integer() else f"${n:,.2f}"

def addr(a):
    if not a: return None
    parts = [a.get("street")]
    if a.get("unit"): parts.append(a["unit"])
    city = ", ".join(x for x in [a.get("city"), f"{a.get('state','')} {a.get('zip','')}".strip()] if x)
    return ", ".join(x for x in parts + [city] if x)

STATES = {"CA": "California", "NY": "New York", "WA": "Washington", "TX": "Texas", "MA": "Massachusetts",
          "IL": "Illinois", "DE": "Delaware", "FL": "Florida", "CO": "Colorado", "GA": "Georgia", "NJ": "New Jersey",
          "PA": "Pennsylvania", "NC": "North Carolina", "VA": "Virginia", "OR": "Oregon", "AZ": "Arizona", "MD": "Maryland"}

def computed(c):
    P, B, L, T, F, R, Po, X = (c.get(k, {}) for k in ("petitioner", "beneficiary", "lca", "petition", "funding", "company_role", "position", "evidence"))
    k = {}
    hrs = L.get("hours_per_week"); ft = L.get("full_time")
    sched = ("full-time" if ft else f"part-time, {hrs} hours per week") if hrs else None
    k["schedule_phrase"] = sched
    k["schedule_phrase_cap"] = sched[0].upper() + sched[1:] if sched else None
    basis = T.get("basis") or ""
    bp = basis.capitalize() + (" with extension of stay" if T.get("extension_of_stay") else "")
    k["basis_phrase"] = bp; k["basis_phrase_lower"] = bp[0].lower() + bp[1:] if bp else None
    k["extension_clause"] = ", with an extension of the Beneficiary's stay" if T.get("extension_of_stay") else ""
    k["today_long"] = long_date(date.today().isoformat())
    k["petitioner.address_line"] = addr(P.get("address"))
    k["petitioner.legal_name_upper"] = (P.get("legal_name") or "").upper()
    k["petitioner.entity_type_lower"] = (P.get("entity_type") or "corporation").lower().replace("c corporation", "corporation")
    k["petitioner.date_incorporated_long"] = long_date(P.get("date_incorporated"))
    k["beneficiary.full_name"] = " ".join(x for x in [B.get("given_name"), B.get("middle_name"), B.get("family_name")] if x)
    k["beneficiary.us_address_line"] = addr(B.get("us_address"))
    poss = B.get("pronoun_possessive") or "their"
    k["beneficiary.pronoun_subject"] = {"her": "she", "his": "he"}.get(poss, "they")
    k["beneficiary.pronoun_object"] = {"her": "her", "his": "him"}.get(poss, "them")
    k["beneficiary.status_valid_until_long"] = long_date(B.get("status_valid_until"))
    rec = B.get("prior_h1b_receipts") or []
    k["beneficiary.latest_receipt"] = rec[-1].get("receipt") if rec else None
    k["prior_receipts_inline"] = "; ".join(f"receipt {r.get('receipt')}, valid {r.get('valid_from')} to {r.get('valid_to')}" for r in rec) or None
    k["lca.worksite_line"] = addr(L.get("worksite"))
    ws = (L.get("worksite") or {}).get("state")
    k["lca.worksite.state_name"] = STATES.get(ws, ws)
    k["lca.wage_rate_fmt"] = money(L.get("wage_rate"))
    k["lca.valid_from_long"] = long_date(L.get("valid_from"))
    k["petition.start_long"] = long_date(T.get("start")); k["petition.end_long"] = long_date(T.get("end"))
    k["petition.annualized_pay_fmt"] = money(T.get("annualized_pay"))
    k["petition.period_wage_fmt"] = money(T.get("period_wage"))
    k["petition.period_cost_fmt"] = money(T.get("period_cost_with_employer_taxes"))
    k["petition.months_words"] = "eighteen"
    k["petition.pay_frequency_cap"] = (T.get("pay_frequency") or "semi-monthly").capitalize()
    ey = T.get("experience_years")
    k["experience_phrase"] = "no prior work experience" if not ey else f"{ey} years of prior work experience"
    k["experience_sentence"] = "No prior work experience is required." if not ey else f"{ey} years of related professional experience is required."
    k["company_role.director_title_lower"] = (R.get("director_title") or "director").lower()
    k["company_role.director_title_upper"] = (R.get("director_title") or "director").upper()
    for f in ("founder_contribution", "bank_balance", "raise_amount"):
        k[f"funding.{f}_fmt"] = money(F.get(f))
    k["funding.balance_date_long"] = long_date(F.get("balance_date"))
    ed = (B.get("education") or [{}])[0]
    k["education.highest_degree"] = ed.get("degree"); k["education.highest_field"] = ed.get("field")
    k["education.highest_school"] = ed.get("school"); k["education.highest_year"] = ed.get("year")
    # duties
    duties = Po.get("duties") or []
    n = len(duties); k["position.duty_count"] = n; k["position.owner_duty_n"] = n + 1
    sp, op = T.get("specialty_hours"), T.get("owner_hours")
    if duties and hrs:
        rows = [f"| {d.get('n')}. {d.get('title')} | {d.get('hours')} | {round(100*(d.get('hours') or 0)/hrs)}% |" for d in duties]
        rows.append(f"| **Specialty occupation duties** | **{sp}** | **{T.get('specialty_hours_pct')}%** |")
        rows.append(f"| {n+1}. {Po.get('owner_duty_title')} | {op} | {T.get('owner_hours_pct')}% |")
        rows.append(f"| **Total weekly hours** | **{hrs}** | **100%** |")
        k["duties_table"] = "| Duty | Hours per week | Share |\n|---|---|---|\n" + "\n".join(rows)
        secs = []
        for d in duties:
            secs.append(f"## 2.{d.get('n')} {d.get('title')} ({d.get('hours')} hours, {round(100*(d.get('hours') or 0)/hrs)}%)\n\n" + "\n".join(f"- {b}" for b in d.get("bullets", [])))
        k["duties_sections"] = "\n\n".join(secs)
        k["duties_inline"] = "; ".join((d.get("title") or "")[0].lower() + (d.get("title") or "")[1:] for d in duties)
        d500 = "; ".join(d.get("title") for d in duties) + f". About {T.get('specialty_hours_pct')}% of weekly hours on these specialty duties; the remainder on founder/officer duties (customer discovery, fundraising, administration). All hours paid at the LCA wage."
        k["duties_500"] = d500 if len(d500) <= 500 else d500[:497] + "..."
    ka = Po.get("knowledge_areas") or []
    if ka: k["knowledge_table"] = "| Knowledge area | Required for |\n|---|---|\n" + "\n".join(f"| {a.get('area')} | {a.get('duties')} |" for a in ka)
    wd = Po.get("why_degree") or []
    if wd: k["why_degree_paragraphs"] = "\n\n".join(wd)
    emp = B.get("employment") or []
    prev = next((e for e in emp if e.get("to")), None)
    po = (f"{prev.get('title')} specializing in {prev.get('summary')}; " if prev and prev.get("summary") else "")
    short = re.split(r",| by |; ", P.get("product_description") or "")[0].strip()
    po += f"founder, {P.get('signer', {}).get('title')} of {P.get('legal_name')}, developing {short}."
    po = po[0].upper() + po[1:]
    k["present_occupation_500"] = po if len(po) <= 500 else po[:497] + "..."
    ex = [e for e in (X.get("exhibits") or []) if e.get("include", True)]
    if ex: k["exhibit_index_table"] = "| Exhibit | Document |\n|---|---|\n" + "\n".join(f"| {e.get('letter')} | {e.get('title')} |" for e in ex)
    return k

def lookup(c, key):
    cur = c
    for part in key.split("."):
        if isinstance(cur, dict) and part in cur: cur = cur[part]
        else: return None
    return cur

def render(text, c, comp):
    def sub(m):
        key = m.group(1).strip()
        v = comp.get(key)
        if v is None: v = lookup(c, key)
        if v is None or v == "": return f"[DRAFT: {key}]"
        return str(v)
    return re.sub(r"\{\{([^}]+)\}\}", sub, text)

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    c = json.load(open(sys.argv[1]))
    out = "drafts"
    if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
    os.makedirs(out, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__)); tdir = os.path.join(os.path.dirname(here), "templates")
    comp = computed(c)
    slug = re.sub(r"[^A-Za-z0-9]+", "", (c.get("petitioner", {}).get("legal_name") or "Company").split(",")[0])
    for t in TEMPLATES:
        src = open(os.path.join(tdir, t), encoding="utf-8").read()
        src = re.sub(r"<!--.*?-->\n*", "", src, flags=re.S)
        txt = render(src, c, comp)
        name = f"{slug}-{t.replace('.md','').title().replace('-', '-')}.md"
        name = f"{slug}-" + "-".join(w.capitalize() for w in t[:-3].split("-")) + ".md"
        p = os.path.join(out, name); open(p, "w", encoding="utf-8").write(txt)
        drafts = len(re.findall(r"\[DRAFT:", txt)); print(f"wrote {p}  ({drafts} [DRAFT] markers)")
        if "--docx" in sys.argv:
            try: subprocess.run(["pandoc", p, "-o", p[:-3] + ".docx"], check=True); print(f"  -> {p[:-3]}.docx")
            except Exception as e: print("  pandoc failed:", e)

if __name__ == "__main__":
    main()
