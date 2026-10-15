# h1b-founder-self-petition

[English](README.md) · [简体中文](README.zh-CN.md) · **日本語** · [한국어](README.ko.md) · [Español](README.es.md) · [हिन्दी](README.hi.md)

スタートアップ創業者が **自分の会社をスポンサーにして自分の H-1B を申請する**（beneficiary-owner ルール、8 CFR 214.2(h)(9)(iii)(E)）ための AI スキルです。過半数を所有する会社が申請者、あなたが受益者となり、弁護士なしで会社の USCIS オンラインアカウントから提出します。

実際の申請から抽出しました：設立数週間のデラウェア C-corp を 100% 所有し唯一の取締役である創業者が、パートタイムの専門職について change of employer + extension を申請し、プレミアム処理で 11 営業日後に RFE なしで承認されました。検討したすべての判断、最初に間違えたすべての項目、書類一式のすべてがここにあります。

## クイックスタート（技術知識は不要）

**Claude で使う**
1. このリポジトリの Releases から `h1b-founder-self-petition.skill`（1 ファイル）をダウンロード
2. Claude → Settings → Capabilities → Skills → Upload でそのファイルを選択
3. 新しいチャットで入力：**自分の会社で自分の H-1B を申請したい。最初から案内して。**

まず状況について 8 つの質問をし、次に会社の書類と移民書類をチャットにドロップするよう求めます。フォーム入力の段階になったら、Chrome ウェブストアから **Claude in Chrome** 拡張機能を入れ、会社の USCIS アカウントにログインして「I-129 を入力して」と言ってください。フォーム入力と証拠のアップロードが終わると停止します。支払いと送信はあなたが行います。

**ChatGPT で使う**
メンテナーが公開している Custom GPT のリンクを開いてください（Release ノート参照）。ChatGPT はブラウザを操作できないため、ページごとに入力内容を教えてくれます。

`scripts/` のスクリプトは AI が実行するものです。あなたが何かを実行する必要はありません。

## できること

1. **スクリーニング** — 8 つの選択式質問：ステータス、会社、持株比率、LCA、cap の履歴、勤務形態、プレミアム処理、USCIS アカウント。不足があれば案内します。
2. **書類の取り込み** — 設立証明書、EIN、株主名簿、銀行残高、賃貸契約、パスポート、I-797、I-94、給与明細、学位、認証済み LCA を読み、`case.json` を作成。
3. **質問** — 書類から分からないことだけ（日付、専門業務とオーナー業務の時間配分、学位要件の文言、署名者の肩書、除外事項、資金計画）。
4. **ドラフト作成** — サポートレター、職務記述書、オファーレター、雇用契約、取締役決議、I-129 の自由記述欄をテンプレートから生成。事業計画書のアウトラインも提供。
5. **整合性チェック** — 書類とフォームの間で一致していなければならない項目のチェックリスト。
6. **フォーム入力** — Claude in Chrome でオンラインの I-129 と I-907 を入力し、証拠をアップロードし、ドラフト PDF を `case.json` と照合。
7. **支払い前で停止** — 会社の口座から支払い、Submit を押すのはあなたです。
8. **提出後** — 受理通知、ポータビリティ、給与開始、Public Access File、承認メールの読み方、I-797A の確認。

## インストール

| ホスト | 方法 |
|---|---|
| Claude.ai / Claude デスクトップ | Settings → Skills で `.skill` をアップロード、またはチャットに送って *Save skill* |
| Claude Code | フォルダを `~/.claude/skills/h1b-founder-self-petition/` にコピー |
| Codex CLI | フォルダを `~/.codex/skills/h1b-founder-self-petition/` にコピー（同じ SKILL.md 形式） |
| ChatGPT | Custom GPT を作成し、`adapters/chatgpt-custom-gpt.md` を Instructions に貼り付け、`references/*` と `templates/*` を Knowledge にアップロード |

フォーム入力には `my.uscis.gov` へのアクセスを許可した **Claude in Chrome** 拡張機能が必要です。それ以外はブラウザなしで動作します。各ホストで可能なことは `adapters/README.md` を参照。

## 構成

```
SKILL.md                      AI が従うワークフロー
references/                   I-129 回答表、証拠マップ、整合性チェック、Chrome 操作、費用、LCA 準備、提出後、法的根拠、実例からの教訓
templates/                    case.json スキーマと例、サポートレター、職務記述書、オファーレター、雇用契約、取締役決議、事業計画アウトライン、フォーム用テキスト
adapters/                     ChatGPT Custom GPT 用の Instructions、ホスト比較
scripts/                      validate_case.py（検証）、render_templates.py（テンプレート展開）
```

## スクリプトを試す

```bash
python scripts/validate_case.py templates/case.example.json
python scripts/render_templates.py templates/case.example.json --out drafts/ --docx
```

## 対象範囲

すでに米国内で H-1B ステータスにあり、認証済み LCA を持つ創業者の change of employer / extension / cap-exempt transfer。抽選登録、領事手続き、L-1/O-1 は対象外。費用やフォームの構成は変わるため、スキルは AI に uscis.gov で確認するよう指示します。

これは自分の申請を準備するためのツールであり、法的助言ではありません。

## ライセンス

MIT
