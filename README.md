# R8 Cognitive Risk Analyzer

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20428127.svg)](https://doi.org/10.5281/zenodo.20428127)

情報の「真偽」ではなく「認知操作の構造」を定量化するテキスト監査システム。

A text analysis system that quantifies the **structure of cognitive manipulation**, not the truth or falsity of information.

---

## Concept / 概念

Fact-checking tools detect lies.
R8 detects the manipulative structure of information that deceives without lying.

ファクトチェックツールは嘘を検出する。
R8は、嘘をつかずに人を操る情報構造を検出する。

R8 proposes a structural approach to approximating cognitive manipulation risk across 12 theoretically grounded categories, drawing conceptual inspiration from factor-based psychometric models (MMPI). This is an exploratory framework at an early stage of empirical development.

---

## Why R8 / なぜR8か

Modern cognitive manipulation rarely relies on outright falsehoods.
It operates through emotional amplification, false authority, fear framing, and structural deception — none of which fact-checkers are designed to detect.

現代の認知操作は、嘘に頼らない。
感情的増幅、偽の権威、恐怖フレーミング、構造的欺瞞によって機能する。
ファクトチェッカーはこれらを検出するように設計されていない。

R8 was built to address this gap.

---

## Audit Categories / 監査カテゴリ（12）

| English | 日本語 |
|---|---|
| Authority Risk | 権威リスク |
| Emotional Risk | 感情誘導リスク |
| Logical Risk | 論理飛躍リスク |
| Statistical Risk | 統計操作リスク |
| Hype Risk | 責任回避型煽りリスク |
| Clickbait Risk | クリックベイト |
| Propaganda Risk | プロパガンダ |
| Fear Risk | 恐怖煽動リスク |
| Enemy Frame | 敵/味方フレーム |
| Disclaimer Exploit | 免責文逆利用 |
| Anonymous Authority | 匿名権威 |
| Naked Number | 根拠なき具体数値 |

---

## Supported Formats / 対応フォーマット

- Text file / テキストファイル（.txt）
- PDF file / PDFファイル（.pdf）
- Web page URL / ウェブページURL

---

## Repository Structure / リポジトリ構成

```
r8-cognitive-risk/
├── r8.py                  # メインスキャナ（v17）
├── mass_audit.py          # バッチスキャン
├── preprocess.py          # 前処理パイプライン
├── clean_corpus.py        # テキストクリーニング
├── quality_check.py       # 品質チェック
├── mask_corpus.py         # 個人情報マスク
├── translate_corpus.py    # 翻訳処理
├── remove_duplicate.py    # 重複除去
├── scripts/               # 補助スクリプト群
└── docs/
    ├── preprint/          # Zenodo公開論文（v1.5, v1.7, v1.8）
    └── drafts/            # アノテーション基準（v0.8）
```

---

## Calibration Results / 較正結果（v17・標準モード HIGH≥41）

| Metric | Value |
|---|---|
| Corpus | 216 documents |
| Precision | 97.7% |
| Recall | 35.2% |
| F1 | 51.8 |
| Cohen's κ (Claude Sonnet) | 0.231 |
| Cohen's κ (Gemini 2.5 Flash) | 0.103 |

Single-rater expert annotation (Phase 1). Human inter-rater reliability (κ) to be established in Phase 2.

---

## Developer / 開発者

M.S. Clinical Psychology (Aichi Gakuin University, 2012) / Independent Researcher
臨床心理学修士（愛知学院大学2012）/ 独立研究者

ORCID: 0009-0005-9464-6260

---

## Status / ステータス

- **v17** (2026-05-31) — Section 5.4 corrected (v1.7/v1.8); repository restructured (whitelist-only public release)
- Preprint: [Zenodo DOI: 10.5281/zenodo.20428127](https://doi.org/10.5281/zenodo.20428127)
- Annotation criteria: v0.8
- Phase 2 in preparation: human inter-rater reliability, corpus expansion, structural detection layer
