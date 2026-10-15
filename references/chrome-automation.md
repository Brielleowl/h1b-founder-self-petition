# Driving my.uscis.gov with Claude in Chrome

The online petition lives in the user's own Chrome session, logged into the **company** USCIS
account (the "legal representative / petitioner" account type, not the beneficiary's personal
account). You fill; the user pays.

## Load the tools once

Read the `claude-in-chrome` skill, then load everything in one ToolSearch call:

```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__file_upload
```

Call `tabs_context_mcp` first; then open a **new tab** at `https://my.uscis.gov` rather than reusing
whatever the user has open.

## Session rules

- If the login or two-factor page appears, stop and ask the user to log in; never type their
  password or codes. The site logs out after ~15 idle minutes — expect this a few times.
- Navigate: My Company → company name → Cases → **Drafts**. Open an existing I-129 draft if one
  exists (don't start a second one); otherwise File a form → I-129 → H-1B.
- Per page: `get_page_text` (or `read_page` for the form structure) → fill with `form_input` →
  screenshot → click Next / Save. Saving after every section is what makes a logout harmless.
- Radio buttons and dropdowns sometimes don't take `form_input`; use `find` + click, then re-read
  the page to confirm the value stuck before moving on.
- Never trigger a browser dialog. The site uses in-page modals, which are fine.
- Evidence files must be on the user's computer. Ask for the folder path once, then use
  `file_upload` per document. After each upload, re-read the page to confirm the filename appears
  under the right category. Filenames with commas are rejected with a generic error.
- If a tool call fails twice on the same element, screenshot, tell the user what you tried, and ask
  them to do that one click; then continue.

## What you may and may not click

Allowed: Save, Next, Back, Continue, Review, Edit, Upload, Remove (your own upload), Download draft
PDF, "Finish and continue to I-907".

Not allowed, ever: "Pay and submit", "Submit", any button on pay.gov /
public.payment.uscis.dhs.gov, "Delete draft", anything in the beneficiary's personal account.

The stop line: the Drafts table shows **I-129 + I-907 · Ready to pay and submit**. Screenshot it,
hand off.

## Payment, for the user

When the user pays: credit/debit card on the government payment page. A card with a per-transaction
or monthly limit below the fee total fails silently — the payment page returns **HTTP 500** and the
bank shows a *Failed* authorisation. The case stays in Drafts, nothing is lost; raise the card limit
and pay again. If the bank shows the charge *Completed* but the case still shows Drafts after a few
minutes, do not pay again; refresh and check email.

## After submission (user's screenshots)

Confirm: Submitted (1); receipt number `IOE…`; status "Case Was Received and A Receipt Notice Was
Sent"; "Download I-129 PDF" link (save it — it is the as-filed copy); Notices tab for the I-797C.
