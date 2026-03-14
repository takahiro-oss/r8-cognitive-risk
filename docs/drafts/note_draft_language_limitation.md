# R8言語処理の限界と将来対応

## 現在できること
- 日本語の文字列一致ベースの単語マッチング
- 正規表現による数値パターン検出
- 複数カテゴリの共起による構造的欺瞞検出（例：権威語×煽り語）
- 免責文と煽り語の同時出現による逆用構造の検出

## 現在できないこと・限界事項

### 言語の揺れ
「絶対」「絶対に」「ゼッタイ」「ぜったい」を同一視できない
表記ゆれへの対応は正規表現で部分的に吸収可能

### 多義性
「支配」は政治操作文脈では高リスク
「市場を支配する」という客観的記述では低リスク
現在は文脈を区別できない
文脈判定にはBERT等のtransformerベース言語モデルが必要

### 多言語対応
現在は日本語専用辞書
英語圏市場を狙うなら英語辞書が必要
英語の操作的表現は日本語と構造が異なる

## 将来対応ロードマップ
Phase 1（現在）: 日本語単語マッチング・割り切って進める
Phase 2（将来）: transformer-basedモデルによる文脈判定導入
Phase 3（構想）: 多言語対応・言語の成り立ちと多義性への対応

## プレプリントへの記載方針
限界事項として正直に記載する
Current Limitations セクションに以下を含める

The current implementation relies on surface-level lexical matching
and does not account for contextual disambiguation, linguistic variation,
or cross-linguistic semantic equivalence. Future versions will incorporate
transformer-based contextual language models to address these limitations.

These limitations may result in false positives for formal documents
containing legitimate authority references, and false negatives for
manipulative content that employs non-standard orthography.

## 各国言語の成り立ちへの留意
日本語: 重層的意味構造・文脈依存度が高い・省略が多い
英語: 統語構造が明示的・省略が少ない（文脈依存度は日本語より低い傾向）
アラビア語・中国語: 語根・文字の多義性が大きい
多言語対応はPhase3以降で設計が必要
