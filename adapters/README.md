# Using this skill outside Claude

The knowledge in `references/`, `templates/` and `scripts/` is plain markdown, JSON and Python.
Only the entry point differs per host.

| Host | Entry point | Browser filling |
|---|---|---|
| Claude.ai / Claude desktop / Claude Code | `SKILL.md` (install the `.skill` or copy the folder to `~/.claude/skills/`) | Claude in Chrome drives the user's own Chrome; local PDFs upload |
| OpenAI Codex CLI | same `SKILL.md` — copy the folder to `~/.codex/skills/h1b-founder-self-petition/` (Agent Skills format) | no browser; the skill falls back to page-by-page values the user pastes |
| ChatGPT (Custom GPT or Project) | paste `chatgpt-custom-gpt.md` into Instructions; upload every file in `references/` and `templates/` as Knowledge | Agent mode runs in a cloud browser — logging into USCIS there and uploading local files is impractical; use the paste-by-page fallback |
| Any other agent | treat `SKILL.md` as the system prompt and the folder as retrievable docs | paste-by-page fallback |

The scripts run anywhere with Python 3.9+; `render_templates.py --docx` needs pandoc.
