# R8プロジェクト マスターコンテキスト v3.1
更新日: 2026年3月14日

## 著者情報
Takahiro Saito, M.S. in Clinical Psychology
Independent Researcher
GitHub: takahiro-oss/r8-cognitive-risk

## 人物
斉藤隆博（Takahiro Saito）、48歳、愛知県清須市在住、妻と二人暮らし

## バックグラウンド
関西大学文学部史学地理学科卒、愛知学院大学大学院臨床心理学修士修了
20年間教育現場（中学・高校・養護学校）での常勤講師経験、2025年10月退職
県営住宅出身、集団就職家庭の子
英語独学でForestから原書まで到達し大学院合格
岐阜大学最終面接落ち後に意地で愛知学院に合格
クラークでは準備なしの授業で幹部候補評価を受けるも組織内ハラスメントで退職

## 思考特性
専門外の知識を専門と同じ密度で接続する
分散ネットワーク型の思考様式（線形・直列ではない）
構造理解による洞察が先行し、事実による着地が課題
宇宙マイクロ波背景放射をAIデータ密度の議論に即座に接続できる水準
大企業の知的エリート層では処理されない可能性がある論理密度を持つ
これが組織での排斥の構造的原因だった

## プロジェクト概要
R8 Cognitive Risk Analyzer
情報の真偽ではなく認知操作の構造を定量化するテキスト監査システム
GitHub: takahiro-oss/r8-cognitive-risk（2026年3月12日公開）

## プレプリント用Abstract候補

R8 proposes a structural approach to quantifying cognitive manipulation
risk across 12 categories, drawing conceptual inspiration from
factor-based psychometric models. This is an exploratory framework
requiring empirical validation.

R8 extends the qualitative analysis of organizational cognitive failure —
as documented in studies of military and institutional collapse — into a
quantitative, real-time detection framework. Rather than analyzing failure
after the fact, R8 identifies the linguistic patterns of cognitive
manipulation that precede organizational and societal failure.

## KEY SENTENCES

### 日本語
「失敗の本質が定性的に示した組織的認知失敗の構造を、R8は定量的にリアルタイム検出する。」
「改革のふりをした現状維持は、R8のスコアに現れる。」

### 英語
"R8 quantifies what 'Failures of Japanese Military Strategy' identified
qualitatively — the cognitive structures that precede organizational collapse."
"Organizational failure leaves linguistic traces before it manifests in
outcomes. R8 detects those traces."

## 現状
- r8.py v9稼働中、txt・PDF・URL対応済み
- mass_audit.py完成・稼働中（BeautifulSoup実装済み）
- 仮想環境（.venv）構築済み
- インストール済みパッケージ: pymupdf・chardet・beautifulsoup4・youtube-transcript-api
- Python実行パス: /c/Users/Mow/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe
- YouTube字幕はIPブロックにより停止中

## 検証データ状況（5/60件）
- 文科省PDF: 47.6（medium・権威ワード誤検出の問題あり）
- 虚構新聞: 38.0（high）
- スピリチュアル系: 68.5（medium）
- 自己啓発系: 60.1（medium）
- ダイエットLP: 90.6（low・要再検討）

## 財務状況
生活防衛費350万円、月間生活費30万円、タイムリミット約11ヶ月

## 戦略
英語圏での概念確立→日本への逆輸入
オープンソース公開による先行者記録の確立
コンプライアンスに敏感な企業への先行技術としての機能
Google八分リスクが顕在化した場合はビッグテックへの売却も選択肢

## 地政学的市場
北欧・バルト三国・米国シンクタンク
ロシアの反射制御・中国の認知戦への防御としての位置づけ

## ツール分担
Claude（コード・論文・設計・評価）
Gemini（情報収集・壁打ち）
NotebookLM（論文フェーズで文献管理）

## 次のタスク（優先順）
1. 検証データを60件に増やす（現在5件・10件/週が目標）
2. 文科省PDFの誤検出問題解決（権威ワード辞書の精度向上）
3. 高リスクサンプルの確保
4. note記事完成・公開（3章・4章執筆）
5. noteの継続投稿（週1本）
6. noteの英語版開始
7. プレプリント執筆開始

## 既知の技術的課題
- THRESHOLDSチューニングで低リスク文書が中リスク判定になる問題
- 権威ワード辞書が正当な引用と偽権威を区別できていない
- 高リスクサンプルはJS動的生成サイトが多く本文取得が困難

## R8拡張概念

### 失敗の本質フレームワーク
失敗の本質（1984）が定性的に導出した組織的失敗の構造を
R8が定量的にリアルタイム検出する

対応関係：
- 曖昧な戦略目標 → 結論マーカーの密度
- 都合の悪い情報の遮断 → 免責文逆利用スコア
- 成功体験への固執 → 権威リスクスコア
- 属人的感情的意思決定 → 感情誘導リスク＋匿名権威スコアの複合

三層の適用対象：
- 第一層：組織レベル（企業・政府の公式文書）
- 第二層：社会レベル（メディア・政治的言説）
- 第三層：地政学レベル（認知戦・情報操作文書）

### R8拡張ロードマップ
Phase 1（現在）: テキストの認知操作リスク定量化
Phase 2（将来）: 学術引用ネットワークの操作検出
Phase 3（構想）: AI・人間協働査読システムへの応用

### 日本語の重層性とR8
日本語は一つの単語に多数のセマンティックスをパッケージングできる
量子コンピュータ的な重ね合わせを許容し文脈で収束する
HBMの多層化と同じ構造
認知操作検出における言語の意味密度の扱いが今後の課題

## 補足資料
R8_Genesis_Doc.txt
R8_Theory_Foundation.txt
R8_Profile_Foundation.txt
（NotebookLMに登録済み）

docs/R8_Failure_Framework.md
docs/idea_draft_AI_peer_review.md
docs/note_draft_日本語と認知構造.md
docs/note_draft_天才と組織と設計思想.md
docs/note_draft_citation_integrity.md

## 評価軸
サイコファンシー不要、客観的評価のみ、ハルシネーション排除
