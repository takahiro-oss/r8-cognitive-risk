# R8 Cognitive Risk Analyzer

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19306871.svg)](https://doi.org/10.5281/zenodo.19306871)

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
r8_strategy/
├── r8.py                  # メインスキャナ（v17）
├── mass_audit.py          # バッチスキャン
├── ailabel/               # AIlabel 3モデル比較ツール
├── scripts/               # 補助スクリプト群
├── docs/                  # 論文・設計文書
├── data/results/          # スキャン結果 CSV
└── corpus/                # テキストコーパス（非公開）
```

---

## Initial Calibration Results / 初期較正結果（v17・標準モード HIGH≥41）

| Metric | Value |
|---|---|
| Corpus | 225 documents |
| Precision | 93.3% |
| Recall | 39.6% |
| F1 | 55.6 |
| Exact match | 33.3% |
| Within-one | 80.4% |

Single-rater annotation (Phase 1). Inter-rater reliability (κ) to be established in Phase 2.

---

## Developer / 開発者

M.S. Clinical Psychology (Aichi Gakuin University, 2012) / Independent Researcher
臨床心理学修士（愛知学院大学2012）/ 独立研究者

ORCID: 0009-0005-9464-6264

---

## Status / ステータス

- **v17** (2026-05-01) — Variable threshold design, 225-document corpus
- Preprint: [Zenodo DOI: 10.5281/zenodo.19306871](https://doi.org/10.5281/zenodo.19306871)
- Annotation criteria: v0.6
- Phase 2 in preparation: inter-rater reliability, corpus expansion, structural detection layer
