# h1b-founder-self-petition

[English](README.md) · **简体中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [हिन्दी](README.hi.md)

一个给创业者用的 AI skill：**用自己的公司给自己办 H-1B**（beneficiary-owner 规则，8 CFR 214.2(h)(9)(iii)(E)）。你持股过半的公司是申请方，你是受益人，在公司的 USCIS 在线账号里自己提交，不用律师。

它来自一次真实申请：一位独立创始人，100% 持股、唯一董事，公司注册才几周，为一个兼职专业岗位提交了 change of employer + extension，加急处理，11 个工作日批准，没有 RFE。所有讨论过的决定、第一遍填错的每个字段、材料包里的每份文件，都在这个仓库里。

## 快速开始（不需要懂技术）

**用 Claude**
1. 在本仓库 Releases 下载 `h1b-founder-self-petition.skill`（一个文件）
2. 打开 Claude → Settings → Capabilities → Skills → Upload，选中它
3. 新开对话，发一句：**我想让自己的公司给我办 H-1B，帮我从头开始**

它会先问你 8 个基本情况问题，再让你把公司文件和移民材料拖进对话。到填表那一步，去 Chrome 应用商店装 **Claude in Chrome** 插件、登录 USCIS 公司账号，然后说「帮我填 I-129」。它填好表、传好证据就停下来，付款和提交你自己点。

**用 ChatGPT**
点维护者发布的 Custom GPT 链接（见 Release 说明）。ChatGPT 不能操作你的浏览器，填表时它会逐页告诉你每个框填什么。

`scripts/` 里的脚本是给 AI 自己跑的，你不需要运行任何东西。

## 它做什么

1. **筛查** — 8 个选择题：身份、公司、持股、LCA、是否被 cap 算过、全职/兼职、是否加急、有没有 USCIS 公司账号。缺什么就先指路。
2. **读材料** — 注册证书、EIN、股权表、银行余额、租约、护照、所有 I-797、I-94、工资单、学位、认证 LCA，汇成一份 `case.json`。
3. **提问** — 只问文件里没有的：起止日期、专业/owner 时间比例、学历要求措辞、签字人头衔、要回避什么、资金口径。
4. **起草** — 按模板生成 support letter、JD、offer letter、employment agreement、董事决议和 I-129 的自由文本；给出商业计划书大纲。
5. **一致性检查** — 所有文件和表格之间必须对得上的项，一张清单。
6. **填表** — 用 Claude in Chrome 逐页填 I-129 和 I-907，上传证据，用草稿 PDF 对照 `case.json` 复核。
7. **停在付款前** — 你用公司账户付款并点提交。
8. **提交后** — 收据、portability、payroll 起始、Public Access File、批准邮件怎么看、核对 I-797A。

## 安装

| 平台 | 方法 |
|---|---|
| Claude.ai / Claude 桌面版 | Settings → Skills 上传 `.skill` 文件，或在对话里发送文件点 *Save skill* |
| Claude Code | 把文件夹复制到 `~/.claude/skills/h1b-founder-self-petition/` |
| Codex CLI | 把文件夹复制到 `~/.codex/skills/h1b-founder-self-petition/`（同一 SKILL.md 格式） |
| ChatGPT | 新建 Custom GPT，把 `adapters/chatgpt-custom-gpt.md` 贴进 Instructions，把 `references/*` 和 `templates/*` 作为 Knowledge 上传 |

填表需要 **Claude in Chrome** 插件并允许访问 `my.uscis.gov`；其他步骤不需要浏览器。各平台能做到哪一步见 `adapters/README.md`。

## 目录

```
SKILL.md                      AI 遵循的主流程
references/
  i129-answer-key.md          I-129 / I-907 每个 section 逐字段答案
  evidence-map.md             要收集的文件、上传分类、Exhibit 索引
  consistency-checklist.md    跨文件一致性清单
  chrome-automation.md        操作 my.uscis.gov；哪些按钮能点、哪些不能
  fees.md                     费用表及如何核实
  lca-prep.md                 LCA 认证之前要做的事
  post-filing.md              收据 → 批准 → 第一次发薪
  legal-basis.md              法规与官方链接
  lessons-learned.md          真实申请中的决定
templates/
  case.schema.json            案件文件，每个字段有说明
  case.example.json           完整的虚构示例
  support-letter.md  job-description.md  offer-letter.md
  employment-agreement.md  board-consent.md  business-plan-outline.md
  additional-information.md   表格里 500 字符的文本
adapters/
  chatgpt-custom-gpt.md       Custom GPT 的 Instructions；README.md 对比各平台
scripts/
  validate_case.py            日期 / 工资 / 费用 / 文件名检查，--fix 自动补可推导字段
  render_templates.py         case.json → drafts/*.md（pandoc 可输出 .docx）
```

## 试跑脚本

```bash
python scripts/validate_case.py templates/case.example.json
python scripts/render_templates.py templates/case.example.json --out drafts/ --docx
```

## 适用范围

已在美国持 H-1B、有认证 LCA 的创始人的 change of employer / extension / cap-exempt transfer。抽签注册、领馆处理、L-1/O-1 不在范围内。费用和表格布局会变，skill 会让 AI 去 uscis.gov 核实。

这是帮你准备自己申请的工具，不是法律意见。

## 贡献

欢迎 PR：翻译、USCIS 改表后的答案表修正、你自己申请的经验。所有文件不要包含个人数据。

## 许可

MIT
