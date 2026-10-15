# I-129 / I-907 online answer key (H-1B, beneficiary-owner)

The online I-129 at my.uscis.gov is organised as a sequence of sections. USCIS renames and reorders
questions from time to time, so this key maps *meaning* → `case.json` field. Read each page before
filling it. Where the key gives text, keep it inside the page's character limit (most free-text
fields are 500 characters).

Contents
1. Getting started / basis for classification
2. Petitioner information
3. Beneficiary information
4. Employment and position information
5. H-1B data collection and numerical limitation
6. Evidence
7. Additional information
8. Declarations and signature
9. I-907 premium processing
10. Draft review

## 1. Getting started / basis for classification

| Question (meaning) | Answer |
|---|---|
| Classification | H-1B, specialty occupation |
| Basis for classification | **Change of employer** if the beneficiary is currently in H-1B status with another employer (even if already separated and within the 60-day grace period). **New employment** only if not currently in H-1B status. |
| Requested action | Change/extend status in the United States (not consular notification) when the requested period runs past the current I-94 or the beneficiary wants to stay. Choose consular only if the user said so. |
| Number of workers | 1 |
| Requested period | `petition.start` – `petition.end` |
| Cap subject? | No — `beneficiary.previously_counted_against_cap` = true. The exemption basis is INA 214(g)(7): previously counted; cite the prior receipt numbers from `beneficiary.prior_h1b_receipts`. A master's-cap exemption is **not** the basis here; that only applies to someone never counted. |
| Beneficiary is in the U.S.? | Yes |

## 2. Petitioner information

| Field | Source |
|---|---|
| Legal name | `petitioner.legal_name`, exactly as on the incorporation certificate, including ", Inc." |
| DBA | `petitioner.dba` or none |
| EIN | `petitioner.ein` |
| Type of business / entity | C corporation / LLC as incorporated |
| Year established | year of incorporation |
| State of incorporation | `petitioner.state_of_incorporation` |
| NAICS | `petitioner.naics` |
| Address | `petitioner.address` (= worksite unless the user says otherwise); mailing same |
| Employees in the U.S. / worldwide | `petitioner.employees_us` / `employees_total` — **type 0**, don't leave blank |
| Gross annual income / net annual income | 0 for a pre-revenue company; type 0 |
| H-1B dependent employer | No (fewer than 26 employees and fewer than 8 H-1Bs) |
| Willful violator | No |
| Contact / signer | `petitioner.signer.name`, `.title`, phone, email. The petitioner is the employer, not an agent or attorney. |
| Petitioner is a nonprofit / government research org | No |

## 3. Beneficiary information

| Field | Source |
|---|---|
| Family / given / middle name | as on passport; "NMN" is not needed, leave middle blank |
| Other names used | preferred English name, maiden name |
| Date of birth, country of birth, citizenship, gender | passport |
| A-Number | `beneficiary.a_number` — fill it; it is on prior I-797s |
| SSN | if any |
| Passport number, country, issue, expiry | passport |
| Date of last arrival, I-94 number, status at entry | CBP I-94 record for the arrival; **I-94 number from the most recent I-797A** (same number if status was extended in the U.S.) |
| Current status | H-1B |
| Status valid until | **I-94 expiry on the most recent I-797A** (`beneficiary.status_valid_until`) |
| U.S. address | current residence |
| Foreign address | permanent address abroad |
| Prior periods in H or L status | one row per I-797 period. For the current period: "To" = I-94 expiry or **mark Present** — leaving the current period's end blank is the single most common gap in the draft review. |
| Education | each degree, highest first; field of study = the full name on the transcript |
| Employment history | employers the user allows, newest first; the founder role at the petitioning company as the newest row with the officer title; former employer rows with real from/to dates |
| Present occupation (500 chars) | A capitalised sentence. Template: `Software engineer specializing in <specialty>; founder, President and CEO of <Company>, developing <one-line product>.` Keep the specialty first — it shows the beneficiary already works in the field. |

## 4. Employment and position information

| Field | Source |
|---|---|
| Job title | `lca.job_title` exactly |
| SOC code and title | `lca.soc_code`, `lca.soc_title` |
| Wage rate, unit, level | `lca.wage_rate` per hour, `lca.wage_level` |
| Full-time? | No if part-time; hours per week = `lca.hours_per_week` |
| Worksite address | `lca.worksite` exactly, unit number included |
| Work at other locations / itinerary / third-party placement | No |
| LCA number, certification date, validity | `lca.number`, `lca.certified_on`, `lca.valid_from`–`valid_to` |
| Duties (500 chars) | Four or five specialty duties, then the owner-duty share. Template: `<Duty 1>; <duty 2>; <duty 3>; <duty 4>. About <specialty_hours_pct>% of weekly hours on these specialty duties; the remainder on founder/officer duties (customer discovery, fundraising, administration). All hours paid at the LCA wage.` |
| Minimum requirements | `petition.degree_requirement`; experience years `petition.experience_years`; license: No |
| Is the beneficiary a member of the petitioner's board / owner? | Yes — see section 5 |

## 5. H-1B data collection and numerical limitation

| Field | Answer |
|---|---|
| Highest level of education | from `beneficiary.education[0]` |
| Major / field | full name |
| Rate of pay per year | `petition.annualized_pay` (part-time annualised). Explain in Additional Information. |
| LCA case number | `lca.number` |
| H-1B dependent / willful violator | No / No |
| Exemption from DOL attestation because of education or pay | Yes if master's or higher **or** annual pay ≥ $60,000 (either basis is true). It is harmless for a non-dependent employer; answer literally. |
| Beneficiary has a controlling interest in the petitioner | Yes |
| Explain the controlling interest (≈400 chars) | `The beneficiary owns <ownership_pct>% of the petitioner's issued stock, is its <sole director / a director> and serves as <officer titles>. The petition is filed under 8 CFR 214.2(h)(9)(iii)(E). The beneficiary will spend the majority of working time (<specialty_hours_pct>%) on specialty occupation duties and the remainder on duties directly related to owning and directing the business. The requested validity period is within the 18-month limit.` |
| Previously counted against the cap | Yes; receipt numbers |
| Basis for cap exemption | "Beneficiary was previously counted" |
| Numerical limitation exemption — nonprofit/research/government | No |

## 6. Evidence

Upload PDFs under the category the page shows. See `evidence-map.md`. Upload **every** document the
support letter's exhibit index lists; the review step found the job description missing after it
had been drafted and signed — check the uploads against the index before the review page.

## 7. Additional information

The form has a free-text "Additional Information" area keyed to page/section. Add at least:

1. **Rate of pay.** `Part 5 / H-1B data collection, rate of pay per year: the position is part-time at <hours> hours per week at $<rate> per hour under certified LCA <number>; the annual figure entered ($<annualized>) is that hourly wage annualised (<rate> × <hours> × 52).`
2. **Cap exemption.** `Part 2, numerical limitation: the beneficiary was previously counted against the H-1B cap (receipt <IOE…>, approved <date>); this petition is exempt under INA 214(g)(7).`
3. **Controlling interest**, if the 400-character field truncated it.
4. **Current status period.** `Part 3, prior H status: the beneficiary's current H-1B period under receipt <IOE…> runs to <I-94 expiry>; the petition requests an extension of stay to <petition.end>.`
5. Anything the user asked to clarify (e.g. why the start date is later than the LCA start).

Templates for all of these are in `templates/additional-information.md`.

## 8. Declarations and signature

Signer name and title = `petitioner.signer`. The petitioner's statement, contact information and
e-signature are applied by the user at submission. If the page offers "Interpreter" or "Preparer"
sections, answer No — the founder prepared the petition.

## 9. I-907 premium processing

Reached only through **"Finish and continue to I-907"** on the I-129 review page.

| Field | Answer |
|---|---|
| Who is filing | The petitioner (the company) |
| Company A-Number / USCIS Online Account Number | "I do not have one" |
| Related case | Form I-129; classification H-1B; beneficiary name; **name of the company in the related case** = legal name; EIN |
| Requested processing | 15 business days |
| Contact | signer name, title, phone, email; mailing address = company address |
| Declarations | petitioner |

Both fees are paid in one payment after the I-907 review page. Stop there.

## 10. Draft review

Download "Draft I-129 PDF" and the "Petition summary". Compare with `case.json` field by field.
Known quirks: the draft PDF renders numeric zeros, NAICS and the I-94 number as blanks even when the
summary shows them saved. Real gaps seen in practice, in order of frequency:

1. Current H-status period "To" not marked Present / blank
2. A-Number blank
3. Job description not uploaded
4. Present-occupation sentence lost its first clause or starts lowercase
5. Additional Information empty
6. Field of study shortened to two words
7. Controlling-interest explanation only one line
8. Former employer location typed as a city when the form asked for city **and** state

Fix each in the form, re-download, re-check, then go to the Drafts list.
