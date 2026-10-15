---
name: h1b-founder-self-petition
description: End-to-end helper for a startup founder self-filing their own H-1B petition as a beneficiary-owner (the company they majority-own is the petitioner). Use this whenever someone mentions H-1B self-sponsorship, "self-petition", "beneficiary-owner", "my own company sponsoring my H-1B", filing Form I-129 / I-907 for themselves, an LCA for a founder, or asks what documents a founder-petitioner needs — even if they only have a pile of incorporation papers and an old approval notice and don't know where to start. It takes company and immigration documents as input, builds a single case file, asks only the questions the documents cannot answer, drafts and cross-checks the support letter / job description / offer letter / board consent / business plan, then fills the online I-129 and I-907 in the petitioner's my.uscis.gov account through Chrome and stops at "Ready to pay and submit" so the human pays and submits.
---

# H-1B founder self-petition (beneficiary-owner)

A founder can be the H-1B beneficiary of a petition filed by the company they own, as long as the
company is the petitioner and the founder does specialty-occupation work most of the time
(8 CFR 214.2(h)(9)(iii)(E), effective January 17, 2025). The first such petition is limited to
18 months. This skill walks that whole process with the user, from a folder of PDFs to a filled
online petition waiting for payment.

The user has decided to do this without a lawyer. Treat them as a capable adult: give steps,
answers and drafts, not disclaimers. Point to official sources (USCIS, DOL, CFR) when a fact
matters.

## What "done" looks like

1. `case.json` in the working directory holds every fact the petition needs, each traceable to a
   document or an explicit user answer.
2. The filing package (support letter, job description, offer letter, board consent, business plan,
   evidence PDFs) is internally consistent — same dates, wage, hours, titles, degree wording everywhere.
3. The I-129 (and I-907, if premium processing) is filled in the company's my.uscis.gov account,
   evidence uploaded, draft PDF reviewed, and the Drafts list shows **"Ready to pay and submit"**.
4. The user pays and submits. You never click Pay / Submit, and never touch pay.gov.

## Hard rules

- **Never submit or pay.** The last browser action is leaving the case at "Ready to pay and submit".
  Payment comes from the company's own account (company card or bank); never suggest a personal card.
- **Every value traces to a source.** A date, number or name you type into the form must come from
  a document you read or an answer the user gave and that you recorded in `case.json`. Never guess.
- **Nothing confidential about third parties** goes into any filing document: a former employer's
  customers, contract values, internal project names. If the user asks to leave an employer or topic
  out, it stays out of every document and every form field.
- **Filenames**: letters, digits, hyphen, underscore, period. No commas, no spaces if avoidable —
  the USCIS uploader rejects commas.
- Speak the user's language in chat; the filing itself is English.

## Workflow

```
Phase 0  Screening     a few multiple-choice questions, no documents yet → are they in scope, what is missing
Phase 1  Intake        documents → case.json
Phase 2  Questions     only what the documents cannot answer
Phase 3  Drafting      templates → support letter, JD, offer, consent; consistency pass
Phase 4  Chrome        fill I-129 + I-907 in the company's my.uscis.gov account, upload evidence, review draft
Phase 5  Hand-off      stop at "Ready to pay and submit"; the user pays
```

### Phase 0 — Screening: five minutes, no documents

Before asking for a single file, find out whether this skill fits and what is still missing. Use a
multiple-choice question tool if the host offers one (AskUserQuestion in Claude); otherwise ask in
plain text, two batches of four. Keep the answers in `case.json` under `screening`.

Batch 1
1. **Current status** — H-1B with current employer / H-1B, employment ended within the last 60 days /
   F-1 OPT or STEM OPT / other (L-1, O-1, TN, outside the U.S.).
2. **Company** — incorporated with EIN / incorporated, no EIN yet / not incorporated yet.
3. **Ownership** — more than 50% / 50% or less.
4. **LCA** — certified / filed, waiting / not filed yet.

Batch 2
5. **Counted against the H-1B cap before** — yes (held H-1B via lottery or cap-exempt-then-counted) /
   no / not sure.
6. **Schedule and wage budget** — full-time / part-time; roughly how much the company can commit to
   payroll over 18 months.
7. **Premium processing** — yes / no.
8. **USCIS company account** — exists and the user can log in / not created yet.

Route on the answers, and say which route you took:
- Ownership ≤ 50% → the beneficiary-owner rule does not apply; the company can still petition as an
  ordinary employer. Say so; the rest of the skill still helps with documents and the form.
- F-1 / other status and never counted → cap-subject; needs the March registration. Out of scope for
  the filing phase; the document phases still apply.
- Not incorporated / no EIN → list the formation steps (incorporate, EIN, foreign qualification in
  the worksite state, bank account, bylaws + consents, stock issuance) and stop until they exist.
- LCA not certified → `references/lca-prep.md`; FEIN verification on FLAG first; come back when
  certified.
- No USCIS company account → create one at my.uscis.gov as the petitioner (company) before Phase 4;
  the beneficiary's personal account cannot file an I-129.
- H-1B ended more than 60 days ago → the grace period has lapsed; the petition can still be filed but
  change of status may be denied — tell the user plainly and continue if they want to.

Then explain the whole path in five lines (the table above) and ask for the documents.

### Phase 1 — Intake: documents → `case.json`

Ask the user to drop everything they have. `references/evidence-map.md` lists what to collect, which
upload category each document goes to, and the exhibit index the support letter uses.

The certified **LCA (ETA-9035)** is the gate. Without it the I-129 cannot be filed. If it is missing,
stop at `references/lca-prep.md` (prevailing wage, part-time, wage level, posting notice, public
access file) and come back when DOL has certified it.

Read every file (Read for PDFs and images; `pdftotext` for long PDFs; the docx skill for Word
files). Fill `templates/case.schema.json` → `case.json`. Rules that are easy to get wrong:

| Field | Rule |
|---|---|
| `beneficiary.status_valid_until` | The **I-94 expiry printed on the most recent I-797A** (usually 10 days after the I-797 validity end), not the I-797 end date. |
| `beneficiary.i94.number` | The I-94 number on the most recent I-797A; it should match CBP's online record. |
| `beneficiary.a_number` | "A" + 9 digits, printed on prior I-797s. Not the receipt number. |
| `petition.start` | ≥ LCA start, ≥ the date you expect to file. Do not tie it to the old employer's last day; H-1B portability lets work begin when USCIS receives the petition. |
| `petition.end` | ≤ LCA end **and** ≤ start + 18 months (first beneficiary-owner petition). Default: start + 18 months − 1 day. |
| `petition.annualized_pay` | wage × hours/week × 52 for part-time; this is what "rate of pay per year" expects. Explain it in Additional Information. |
| `petition.experience_years` | Wage Level I → 0. A Level I LCA with "2 years experience required" contradicts itself. |
| `petitioner.employees_us`, `gross_income`, `net_income` | 0 is a valid answer for a new company. Type `0`; a blank saves as blank. |
| `petitioner.naics` | What the business plan describes (software publisher 513210, custom programming 541511, …). |

Run `python scripts/validate_case.py case.json` yourself (never ask the user to run it; if you have no
code execution, do the same checks by hand from the script's docstring) — it checks the date arithmetic, LCA window,
18-month limit, annualized pay, fee total and filename rule, and prints what is still null.

### Phase 2 — Ask only what the documents cannot answer

Batch 2–4 questions per turn (AskUserQuestion in Claude, plain text elsewhere). Typical leftovers:

1. Petition type — change of employer + extension of stay? Premium processing?
2. Start/end dates (offer the computed default).
3. Hours split between specialty duties and owner duties (specialty must be the majority; 80/20 is
   a comfortable split). All hours are paid.
4. The degree-requirement sentence to use everywhere, e.g. "a bachelor's or higher degree in Computer
   Science, Cybersecurity, Computer Engineering, Information Security, or a closely related field".
5. Who signs for the company and with what title. A founder who is the sole director and
   President/CEO signs as that; the employer-employee "control" test no longer applies.
6. Employers or topics to omit everywhere.
7. Funding story: founder contribution + revenue timing + planned raise. Do not ask for personal bank
   statements or a founder funding-commitment letter unless the user offers; a company bank balance
   page is enough.
8. Which optional evidence they will submit (expert opinion letter, reference letters, pitch deck,
   website screenshots, job postings for parallel positions).

Record each answer in `case.json` before moving on. If the user is away, take the most reasonable
reading, note it at the top of your reply, and continue.

### Phase 3 — Draft and cross-check the package

Documents the package needs, with templates in `templates/`:

| Document | Template | Who signs |
|---|---|---|
| Support letter (the petition's argument) | `support-letter.md` | Company officer |
| Job description | `job-description.md` | none (annex) |
| Offer letter | `offer-letter.md` | Company + beneficiary |
| Employment agreement (optional) | `employment-agreement.md` | Company + beneficiary |
| Sole-director / board consent | `board-consent.md` | Director(s) |
| Business plan | `business-plan-outline.md` | none |
| I-129 free-text fields | `additional-information.md` | — |

Run `python scripts/render_templates.py case.json --out drafts/` yourself (or, without code
execution, fill the templates by hand); it substitutes every `{{field}}` from
`case.json` and leaves `[DRAFT: …]` markers where you must write prose (company description, why the
duties need a degree, funding narrative). Write those from the business plan and the user's answers,
then produce PDFs (docx skill → PDF, or pandoc). Templates are starting points; cut what does not
apply, keep the regulatory citations.

Then run the consistency pass in `references/consistency-checklist.md` across every document and
`case.json`, and report a table (item · documents · values · fix). The items that went wrong in real
filings: start date differing between offer letter and support letter; "2 years experience" in the JD
with a Level I LCA; "employment agreement" referenced in a letter when only an offer letter exists;
funding figures in the business plan not matching the support letter; a former employer's separation
date volunteered in the support letter; a Word-exported PDF with a stale table of contents.

Do not rewrite a document the user has frozen ("don't change the BP again"); fix the others to match it.

### Phase 4 — Fill the I-129 and I-907 in Chrome

Pre-flight, asked as one batch:
1. Claude in Chrome extension installed and allowed on my.uscis.gov?
2. Logged into the **company** USCIS account in that Chrome right now?
3. Evidence PDFs in one local folder — which path?
4. `case.json` has no ERROR from `validate_case.py`?

If any answer is no, fix that first; the browser phase is the one place where a missing
prerequisite costs the user a logged-out half-filled form.

Read `references/chrome-automation.md` first (tool loading in one call, page rhythm, what to do on
logout, upload mechanics). If the host has no browser tool that acts in the user's own Chrome
(Codex, ChatGPT), skip the driving and instead walk the user page by page: for each section, give
the exact values from `case.json` in the order the page asks, and have them paste; the answer key
is written for that use too. Then follow `references/i129-answer-key.md` section by section; it maps
each online question to a `case.json` field and gives the 500-character texts and Additional
Information notes. `references/evidence-map.md` says which PDF goes under which upload category.

Rhythm per page: read the page → fill → screenshot → Save/Next. Save the draft after every section.
After the last section, download the draft I-129 PDF and the petition summary and compare every field
to `case.json`; blanks in the draft PDF that the summary shows as saved are a rendering quirk — trust
the summary. Fix real gaps (the ones that recur: current H-status period "To" not marked Present,
A-Number blank, job description not uploaded, present-occupation text truncated, Additional
Information empty, field-of-study list shortened).

Premium processing is filed in the same flow: after the I-129 review page choose **"Finish and
continue to I-907"**, not pay-only; the two are paid together. Stop at the I-907 review page.

### Phase 5 — Hand off

Open My Company → Cases → Drafts and confirm the row reads **I-129 + I-907 · Ready to pay and
submit**. Tell the user:

1. The amount (see `references/fees.md`; $4,975 for a ≤25-employee petitioner with premium processing
   as of 2026) and that the card's limit must cover it — a declined card shows as **HTTP 500** on the
   USCIS payment page with a *Failed* transaction at the bank, and nothing is submitted.
2. View draft → Pay and submit → pay with the company card.
3. Afterwards: Submitted (1), receipt number IOE…, confirmation email, I-797C under Notices.

Then walk them through `references/post-filing.md`: portability start, payroll on the start date,
public access file, what the premium-processing approval email means, checking the I-797A's I-94.

## Where things are

- `references/i129-answer-key.md` — every I-129 / I-907 section, field by field
- `references/evidence-map.md` — documents to collect, upload categories, exhibit index
- `references/consistency-checklist.md` — the cross-document review
- `references/chrome-automation.md` — driving my.uscis.gov with the Chrome tools
- `references/fees.md` — fee table and how to verify it
- `references/lca-prep.md` — what to do before the LCA is certified
- `references/post-filing.md` — receipt → approval → first payroll
- `references/legal-basis.md` — the regulations and official pages cited
- `references/lessons-learned.md` — decisions from a real founder filing approved in 2026
- `templates/` — case schema, example case, document templates
- `scripts/validate_case.py`, `scripts/render_templates.py`
