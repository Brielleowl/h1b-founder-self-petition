# h1b-founder-self-petition

**English** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [हिन्दी](README.hi.md)

An AI skill for startup founders who file their own H-1B petition as a **beneficiary-owner**: the
company you majority-own is the petitioner, you are the beneficiary, and you do the filing in the
company's USCIS online account without a lawyer.

It was distilled from a real filing: a solo founder, 100% owner and sole director of a weeks-old
Delaware C-corp, filed a change-of-employer + extension petition for a part-time specialty position,
paid for premium processing, and was approved in 11 business days with no RFE. Every step that was
debated, every field that was filled wrong on the first pass, and every document in the package is
in here.

## Quick start (no technical skills needed)

**With Claude**
1. Download `h1b-founder-self-petition.skill` from this repository's Releases (one file).
2. Open Claude → Settings → Capabilities → Skills → Upload, and pick that file.
3. Start a new chat and type: **I want my own company to sponsor my H-1B. Walk me through it from the start.**

It first asks eight questions about your situation, then asks you to drop your company papers and
immigration documents into the chat. When it is time to fill the form, install the **Claude in
Chrome** extension from the Chrome Web Store, log in to the company's USCIS account, and say
"fill in the I-129". It fills the form, uploads the evidence, and stops; you pay and click Submit.

**With ChatGPT**
Open the Custom GPT link published by the maintainer (see the Release notes). ChatGPT cannot drive
your browser, so it tells you page by page what to type.

The scripts in `scripts/` are for the AI to run. You never need to run anything.

## What it does

1. **Screening** — eight multiple-choice questions: status, company, ownership, LCA, cap history,
   schedule, premium processing, USCIS account. Routes you if something is missing.
2. **Intake** — reads incorporation papers, EIN letter, cap table, bank page, lease, passport,
   I-797s, I-94, pay stubs, diplomas, the certified LCA, and builds one `case.json`.
3. **Questions** — asks only what the documents can't answer (dates, hours split, degree wording,
   signer title, what to omit, funding story).
4. **Drafting** — renders the support letter, job description, offer letter, employment agreement,
   board consent and I-129 free-text fields from templates; gives you a business-plan outline.
5. **Consistency pass** — a checklist of everything that has to match across documents and the form.
6. **Form filling** — drives Claude in Chrome through the online I-129 and I-907, uploads evidence,
   reviews the draft PDF against `case.json`.
7. **Stops** before payment. You pay from the company account and click Submit.
8. **After** — receipt, portability, payroll start, public access file, what the approval email
   means, checking the I-797A.

## Install

| Host | How |
|---|---|
| Claude.ai / Claude desktop | Settings → Skills → upload the `.skill` file, or send it in a chat and click *Save skill* |
| Claude Code | copy the folder to `~/.claude/skills/h1b-founder-self-petition/` |
| Codex CLI | copy the folder to `~/.codex/skills/h1b-founder-self-petition/` (same SKILL.md format) |
| ChatGPT | create a Custom GPT, paste `adapters/chatgpt-custom-gpt.md` into Instructions, upload `references/*` and `templates/*` as Knowledge |

Form filling needs the **Claude in Chrome** extension with permission for `my.uscis.gov`. Everything
else works without a browser. `adapters/README.md` compares what each host can do.

## Layout

```
SKILL.md                      the workflow the AI follows
references/
  i129-answer-key.md          every I-129 / I-907 section, field by field
  evidence-map.md             what to collect, upload categories, exhibit index
  consistency-checklist.md    the cross-document review
  chrome-automation.md        driving my.uscis.gov; what may and may not be clicked
  fees.md                     fee table and how to verify it
  lca-prep.md                 before the LCA is certified
  post-filing.md              receipt → approval → first payroll
  legal-basis.md              regulations and official links
  lessons-learned.md          decisions from the real filing
templates/
  case.schema.json            the case file, every field explained
  case.example.json           a complete fictional example
  support-letter.md  job-description.md  offer-letter.md
  employment-agreement.md  board-consent.md  business-plan-outline.md
  additional-information.md   the 500-character form texts
adapters/
  chatgpt-custom-gpt.md       Instructions text for a Custom GPT; README.md compares hosts
scripts/
  validate_case.py            date / wage / fee / filename checks, --fix fills derivable fields
  render_templates.py         case.json → drafts/*.md (+ .docx with pandoc)
```

## Try the scripts

```bash
python scripts/validate_case.py templates/case.example.json
python scripts/render_templates.py templates/case.example.json --out drafts/ --docx
```

## Scope

Change of employer / extension / cap-exempt transfer for a founder already in the U.S. in H-1B
status, with a certified LCA. Cap-subject registrations, consular processing and L-1/O-1 are out of
scope. Fee amounts and form layouts change; the skill tells the AI to verify them on uscis.gov.

This is a tool for preparing your own filing, not legal advice.

## Contributing

Translations, corrections to the answer key when USCIS changes the form, and lessons from your own
filing are welcome as pull requests. Keep personal data out of every file.

## License

MIT
