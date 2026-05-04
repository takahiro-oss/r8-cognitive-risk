# corpus_archive — 分析済みコーパス格納フォルダ
最終更新：2026-04-26

## 概要
R8スキャン済みのテキストファイルを保管するフォルダ。
再スキャン・再処理は不要。参照専用。

## ファイル命名規則

### 旧命名形式（手作業期：〜2026-04初旬）
  例：AD_001_20260326.txt、WEB_016_20260326.txt
  形式：[種別]_[連番]_[収集日].txt
  対象：phase1〜phase2手作業期のコーパス

### 新命名形式（自動パイプライン以降：2026-04中旬〜）
  例：note111.txt、web201.txt、sn231.txt
  形式：[種別][連番].txt
  対象：url_batch.py / rename_corpus.py / ocr_batch.py 経由のコーパス

## 種別一覧
  note  : noteプラットフォーム記事
  web   : 一般Webサイト
  sn    : SNS（X等）スクリーンショット
  ad    : 広告・LP
  bl    : ブログ
  phish : フィッシング・詐欺系サイト
  ch    : 書籍章（与沢翼等）

## ラベリング情報
  human_label・riskfactor等はaudit_results.xlsmで管理。
  このフォルダのファイル名をキーにxlsmを参照すること。

## 注意
  このフォルダはrename_corpus.py・ocr_batch.pyの連番走査から除外済み。
  新規コーパスはcorpus/phase2/inbox/ → scan/ のパイプラインを使うこと。