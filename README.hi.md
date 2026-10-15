# h1b-founder-self-petition

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · **हिन्दी**

स्टार्टअप संस्थापकों के लिए एक AI skill, जो **beneficiary-owner** के रूप में अपनी H-1B petition खुद file करते हैं: जिस कंपनी में आपकी बहुमत हिस्सेदारी है वह petitioner है, आप beneficiary हैं, और आप बिना वकील के कंपनी के USCIS online account से file करते हैं।

यह एक असली filing से निकली है: कुछ हफ़्ते पुरानी Delaware C-corp की 100% मालिक और एकमात्र director एक solo founder ने part-time specialty position के लिए change of employer + extension petition file की, premium processing लिया, और 11 कार्यदिवसों में बिना RFE के approval मिला। हर वह फ़ैसला जिस पर बहस हुई, हर वह field जो पहली बार गलत भरी गई, और package का हर document यहाँ है।

## Quick start (तकनीकी जानकारी ज़रूरी नहीं)

**Claude के साथ**
1. इस repository के Releases से `h1b-founder-self-petition.skill` (एक file) download करें।
2. Claude → Settings → Capabilities → Skills → Upload खोलें और वह file चुनें।
3. नई chat शुरू करें और लिखें: **मैं चाहता/चाहती हूँ कि मेरी अपनी कंपनी मेरा H-1B sponsor करे। शुरू से guide करो।**

यह पहले आपकी स्थिति के बारे में आठ सवाल पूछेगा, फिर कंपनी के कागज़ात और immigration documents chat में डालने को कहेगा। जब form भरने का समय आए, Chrome Web Store से **Claude in Chrome** extension install करें, कंपनी के USCIS account में login करें और कहें "I-129 भर दो"। यह form भरता है, evidence upload करता है और रुक जाता है; payment और Submit आप करते हैं।

**ChatGPT के साथ**
maintainer द्वारा publish किया गया Custom GPT link खोलें (Release notes देखें)। ChatGPT आपका browser नहीं चला सकता, इसलिए वह page-by-page बताता है कि क्या लिखना है।

`scripts/` के scripts AI के चलाने के लिए हैं। आपको कुछ भी run नहीं करना है।

## यह क्या करता है

1. **Screening** — आठ multiple-choice सवाल: status, company, ownership, LCA, cap history, schedule, premium processing, USCIS account। कुछ कमी हो तो रास्ता बताता है।
2. **Intake** — incorporation papers, EIN letter, cap table, bank page, lease, passport, I-797, I-94, pay stubs, degrees, certified LCA पढ़कर एक `case.json` बनाता है।
3. **सवाल** — केवल वह जो documents से पता नहीं चलता (dates, hours split, degree wording, signer title, क्या छोड़ना है, funding story)।
4. **Drafting** — templates से support letter, job description, offer letter, employment agreement, board consent और I-129 के free-text fields बनाता है; business-plan outline देता है।
5. **Consistency pass** — documents और form के बीच जो कुछ match होना चाहिए, उसकी checklist।
6. **Form filling** — Claude in Chrome से online I-129 और I-907 भरता है, evidence upload करता है, draft PDF को `case.json` से मिलाता है।
7. **Payment से पहले रुकता है।** आप कंपनी के account से pay करते हैं और Submit दबाते हैं।
8. **बाद में** — receipt, portability, payroll start, public access file, approval email का मतलब, I-797A की जाँच।

## Install

| Host | कैसे |
|---|---|
| Claude.ai / Claude desktop | Settings → Skills में `.skill` file upload करें, या chat में भेजकर *Save skill* दबाएँ |
| Claude Code | folder को `~/.claude/skills/h1b-founder-self-petition/` में copy करें |
| Codex CLI | folder को `~/.codex/skills/h1b-founder-self-petition/` में copy करें (वही SKILL.md format) |
| ChatGPT | Custom GPT बनाएँ, `adapters/chatgpt-custom-gpt.md` को Instructions में paste करें, `references/*` और `templates/*` को Knowledge में upload करें |

Form filling के लिए `my.uscis.gov` की permission वाला **Claude in Chrome** extension चाहिए। बाकी सब बिना browser के चलता है। हर host क्या कर सकता है, `adapters/README.md` में देखें।

## Layout

```
SKILL.md                      वह workflow जो AI follow करता है
references/                   I-129 answer key, evidence map, consistency checklist, Chrome automation, fees, LCA prep, post-filing, legal basis, असली filing के सबक
templates/                    case.json schema और example, support letter, job description, offer letter, employment agreement, board consent, business-plan outline, form texts
adapters/                     ChatGPT Custom GPT के लिए Instructions, host तुलना
scripts/                      validate_case.py (जाँच), render_templates.py (templates)
```

## Scripts आज़माएँ

```bash
python scripts/validate_case.py templates/case.example.json
python scripts/render_templates.py templates/case.example.json --out drafts/ --docx
```

## दायरा

ऐसे founder के लिए change of employer / extension / cap-exempt transfer जो पहले से U.S. में H-1B status में है और जिसके पास certified LCA है। Cap-subject registration, consular processing और L-1/O-1 दायरे से बाहर हैं। Fees और form का layout बदलते रहते हैं; skill AI को uscis.gov पर verify करने को कहती है।

यह अपनी filing तैयार करने का tool है, कानूनी सलाह नहीं।

## License

MIT
