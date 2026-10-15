# h1b-founder-self-petition

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · **한국어** · [Español](README.es.md) · [हिन्दी](README.hi.md)

스타트업 창업자가 **자기 회사를 스폰서로 자신의 H-1B를 직접 신청**하기 위한 AI 스킬입니다 (beneficiary-owner 규정, 8 CFR 214.2(h)(9)(iii)(E)). 과반 지분을 가진 회사가 청원인, 본인이 수혜자가 되어 변호사 없이 회사의 USCIS 온라인 계정에서 제출합니다.

실제 사례에서 추출했습니다: 설립 몇 주 된 델라웨어 C-corp의 100% 소유주이자 단독 이사인 1인 창업자가 파트타임 전문직으로 change of employer + extension을 신청하고, 프리미엄 처리로 11 영업일 만에 RFE 없이 승인받았습니다. 논의된 모든 결정, 처음에 잘못 채운 모든 항목, 서류 패키지의 모든 문서가 여기 있습니다.

## 빠른 시작 (기술 지식 불필요)

**Claude로**
1. 이 저장소의 Releases에서 `h1b-founder-self-petition.skill` (파일 하나) 다운로드
2. Claude → Settings → Capabilities → Skills → Upload에서 그 파일 선택
3. 새 대화를 열고 입력: **내 회사로 내 H-1B를 신청하고 싶어. 처음부터 안내해 줘.**

먼저 상황에 대한 8가지 질문을 한 뒤, 회사 서류와 이민 서류를 대화창에 넣으라고 합니다. 양식 작성 단계가 되면 Chrome 웹 스토어에서 **Claude in Chrome** 확장 프로그램을 설치하고, 회사 USCIS 계정에 로그인한 뒤 "I-129 작성해 줘"라고 말하세요. 양식을 채우고 증빙을 업로드한 후 멈춥니다. 결제와 제출은 본인이 합니다.

**ChatGPT로**
관리자가 공개한 Custom GPT 링크를 여세요 (Release 노트 참조). ChatGPT는 브라우저를 조작할 수 없으므로 페이지마다 무엇을 입력할지 알려줍니다.

`scripts/`의 스크립트는 AI가 실행하는 것입니다. 직접 실행할 필요가 없습니다.

## 하는 일

1. **스크리닝** — 8개 객관식 질문: 체류 신분, 회사, 지분, LCA, cap 이력, 근무 형태, 프리미엄 처리, USCIS 계정. 빠진 것이 있으면 안내합니다.
2. **서류 읽기** — 설립 증명서, EIN, 주주 명부, 은행 잔고, 임대 계약, 여권, I-797, I-94, 급여 명세서, 학위, 승인된 LCA를 읽어 `case.json` 하나로 만듭니다.
3. **질문** — 서류로 알 수 없는 것만 (날짜, 전문 업무/오너 업무 시간 비율, 학위 요건 문구, 서명자 직함, 제외할 사항, 자금 계획).
4. **초안 작성** — 서포트 레터, 직무 기술서, 오퍼 레터, 고용 계약서, 이사회 결의, I-129 자유 기술란을 템플릿으로 생성. 사업 계획서 개요 제공.
5. **일관성 검토** — 서류와 양식 사이에 일치해야 하는 모든 항목의 체크리스트.
6. **양식 작성** — Claude in Chrome으로 온라인 I-129와 I-907을 채우고, 증빙을 업로드하고, 초안 PDF를 `case.json`과 대조.
7. **결제 전 정지** — 회사 계좌로 결제하고 Submit을 누르는 것은 본인입니다.
8. **제출 후** — 접수증, 포터빌리티, 급여 시작, Public Access File, 승인 이메일 읽는 법, I-797A 확인.

## 설치

| 호스트 | 방법 |
|---|---|
| Claude.ai / Claude 데스크톱 | Settings → Skills에서 `.skill` 업로드, 또는 대화에 보내고 *Save skill* 클릭 |
| Claude Code | 폴더를 `~/.claude/skills/h1b-founder-self-petition/`에 복사 |
| Codex CLI | 폴더를 `~/.codex/skills/h1b-founder-self-petition/`에 복사 (같은 SKILL.md 형식) |
| ChatGPT | Custom GPT 생성, `adapters/chatgpt-custom-gpt.md`를 Instructions에 붙여넣고 `references/*`와 `templates/*`를 Knowledge로 업로드 |

양식 작성에는 `my.uscis.gov` 접근을 허용한 **Claude in Chrome** 확장 프로그램이 필요합니다. 나머지는 브라우저 없이 동작합니다. 호스트별 가능 범위는 `adapters/README.md` 참조.

## 구성

```
SKILL.md                      AI가 따르는 워크플로
references/                   I-129 답안표, 증빙 맵, 일관성 체크리스트, Chrome 자동화, 수수료, LCA 준비, 제출 후, 법적 근거, 실제 사례의 교훈
templates/                    case.json 스키마와 예시, 서포트 레터, 직무 기술서, 오퍼 레터, 고용 계약서, 이사회 결의, 사업 계획 개요, 양식용 텍스트
adapters/                     ChatGPT Custom GPT용 Instructions, 호스트 비교
scripts/                      validate_case.py (검증), render_templates.py (템플릿 렌더링)
```

## 스크립트 실행해 보기

```bash
python scripts/validate_case.py templates/case.example.json
python scripts/render_templates.py templates/case.example.json --out drafts/ --docx
```

## 적용 범위

이미 미국에서 H-1B 신분이고 승인된 LCA가 있는 창업자의 change of employer / extension / cap-exempt transfer. 추첨 등록, 영사 처리, L-1/O-1은 범위 밖입니다. 수수료와 양식 구성은 바뀌므로 스킬은 AI에게 uscis.gov에서 확인하도록 지시합니다.

이것은 본인의 신청을 준비하는 도구이며 법률 자문이 아닙니다.

## 라이선스

MIT
