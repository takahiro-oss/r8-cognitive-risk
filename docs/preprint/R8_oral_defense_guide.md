# R8 口頭説明ガイド（英日併記）
# Oral Defense & Explanation Guide

作成日：2026年3月15日
対象：論文v0.8の口頭説明・商談・査読対応用

---

## セクション1：論文の核心（What is R8?）

**英文（論文より）:**
> "R8 proposes a structural approach to quantifying cognitive manipulation risk. A message can be factually accurate while simultaneously exploiting psychological vulnerabilities through urgency, false authority, emotional amplification, and logical misdirection."

**日本語訳:**
R8は認知操作リスクを定量化する構造的アプローチを提案します。情報は事実として正確でありながら、同時に緊急性・権威の偽装・感情の増幅・論理のすり替えによって心理的脆弱性を利用することができます。

**自分の言葉で言うと:**
情報が嘘かどうかではなく、人をどう操っているかを数値で測るツールです。嘘をつかなくても人を操ることはできる。その構造を検出します。

**想定質問と答え:**
Q: ファクトチェックツールとの違いは何ですか？
A: ファクトチェックは情報の真偽を判定します。R8は情報の操作構造を検出します。真実の情報であっても操作的に使うことはできます。そこが対象です。

---

## セクション2：CMIとは何か（What is CMI?）

**英文（論文より）:**
> "The Cognitive Manipulation Index (CMI), defined as the aggregate pressure exerted against autonomous thinking — the quantified force that induces passive cognitive reception where independent critical judgment is required."

**日本語訳:**
認知操作指数（CMI）は、自律的思考に対して加えられる圧力の総量として定義されます。独立した批判的判断が求められる場面で、受動的な認知受容を誘発する定量化された力です。

**自分の言葉で言うと:**
「このテキストはどれだけ読者の自分で考える力を奪おうとしているか」を0〜100で数値化したものです。数値が高いほど操作圧力が強い。

**想定質問と答え:**
Q: CMIが高いテキストとはどんなものですか？
A: 「今すぐ申し込まないと損をします」「専門家が証明しています」「あなただけが知るべき真実」といった表現が密集しているテキストです。読者に考える時間を与えない構造になっています。

---

## セクション3：なぜ12カテゴリか（Why 12 categories?）

**英文（論文より）:**
> "The 12 categories are derived from clinical psychology, organizational behavior, and rhetorical analysis frameworks. Each category is operationalized as a lexical density measure."

**日本語訳:**
12カテゴリは臨床心理学・組織行動論・修辞分析の各フレームワークから導出されています。各カテゴリは語彙密度指標として操作化されています。

**自分の言葉で言うと:**
人を操る方法には種類があります。権威を借りる、恐怖を煽る、統計を偽る、など。それを臨床心理学の知見から12種類に分類して、それぞれの密度を測っています。

**想定質問と答え:**
Q: なぜ12という数字ですか？
A: 現時点では理論的推論と試行錯誤から導いた数です。MMPIが10スケール、ロールシャッハが複数指標を持つように、複数の次元から操作を測ることが精度向上につながります。今後の検証でカテゴリは増減する可能性があります。

---

## セクション4：理論的背景（Why this theory?）

**英文（論文より）:**
> "Tobe et al. (1984) identified recurring patterns of institutional collapse in the Japanese military during World War II — patterns that transcend their historical context and recur across corporate, political, and media contexts."

**日本語訳:**
戸部他（1984）は太平洋戦争における日本軍の組織崩壊に繰り返し現れるパターンを特定しました。これらのパターンはその歴史的文脈を超えて、企業・政治・メディアの各文脈でも繰り返し現れます。

**自分の言葉で言うと:**
「失敗の本質」という本があります。なぜ日本軍は負けたのか。その分析が示すのは、情報操作の構造が組織崩壊を引き起こしたということです。同じ構造は今のメディアや広告にも存在しています。

**英文（論文より）:**
> "Janis (1972) documented the same atmospheric consensus dynamics in Western organizational contexts under the term 'Groupthink'."

**日本語訳:**
ジャニス（1972）は同じ雰囲気的合意の力学を西洋の組織文脈において「集団思考（グループシンク）」という用語で記録しました。

**自分の言葉で言うと:**
日本だけの問題ではありません。空気（kuuki）とグループシンクは同じ現象を別の文化が独立に発見したものです。つまりR8が検出しようとしているのは人間普遍の認知的弱点です。

**想定質問と答え:**
Q: 日本語テキスト専用なのに西洋理論を使うのはなぜですか？
A: 認知操作の構造は文化を超えた普遍現象だからです。日本の「空気」とジャニスの「グループシンク」は独立に同じ現象を発見しています。理論は普遍、現在の実装は日本語限定、英語版は次フェーズの課題です。

---

## セクション5：なぜ辞書ベースか（Why lexical approach?）

**英文（論文より）:**
> "Arai (2018) demonstrated that AI systems process text through statistical pattern matching without achieving genuine semantic understanding. If cognitive manipulation operates through structural patterns rather than semantic content, then structural detection becomes not a limitation but a principled methodological choice."

**日本語訳:**
新井（2018）はAIシステムが真の意味理解なしに統計的パターンマッチングでテキストを処理することを示しました。認知操作が意味内容ではなく構造的パターンを通じて機能するなら、構造的検出は限界ではなく理論的に根拠のある方法論的選択になります。

**自分の言葉で言うと:**
意味を理解しなくても操作の構造は検出できます。「今すぐ」「専門家によると」「残りわずか」という言葉が多ければ、意味を解釈しなくても操作的な構造だと判断できます。シンプルなルールが透明性と再現性を生みます。

**想定質問と答え:**
Q: 機械学習を使わないのですか？
A: 現在は辞書ベースです。透明性・再現性・軽量性を優先しています。将来フェーズではBERTなどのトランスフォーマーモデルとの組み合わせを予定していますが、辞書ベースの基盤は監査可能な記録として残します。

---

## セクション6：検証結果について（About validation results）

**英文（論文より）:**
> "Preliminary validation against a 6-document corpus yields an exact match rate of 17% and within-one-level agreement of 67%, with discrepancies attributable primarily to JavaScript-rendered content limitations and corpus scope."

**日本語訳:**
6文書コーパスに対する予備的検証では、完全一致率17%、1レベル以内の一致率67%が得られました。不一致の主な原因はJavaScriptレンダリングコンテンツの技術的限界とコーパス規模によるものです。

**自分の言葉で言うと:**
6件のテストでは3件が近い判定、1件が完全一致でした。現時点では精度は低い。しかしその原因は特定できています。JavaScriptで動的に生成されるページのテキストが取得できないという技術的問題と、サンプル数が少ないという問題です。60件まで増やして精度を上げます。

**想定質問と答え:**
Q: 精度17%では使えないのではないですか？
A: 現在は第一世代の探索的フレームワークとして提示しています。完全一致17%より重要なのは1レベル以内の一致67%です。完全に外れた判定は少ない。また技術的限界の原因が特定できており、解消方法も明確です。

---

## セクション7：限界の正直な開示（Honest limitations）

**英文（論文より）:**
> "R8 is presented not as a validated instrument but as a transparent, reproducible, and theoretically grounded baseline — one that is designed to be extended, critiqued, and improved through open collaborative development."

**日本語訳:**
R8は検証済みの計測器としてではなく、透明で再現可能な理論的根拠を持つ基盤として提示されます。オープンな協働開発を通じて拡張・批判・改善されるように設計されています。

**自分の言葉で言うと:**
完成品ではありません。第一世代の基盤です。限界は論文の中で正直に書いています。それ自体が誠実さの証明です。批判を受け入れて改善するためにオープンソースにしています。

---

## セクション8：AIサイコファンシー検出（AI sycophancy detection）

**英文（論文より）:**
> "Models trained through reinforcement learning from human feedback (RLHF) are optimized toward responses that human evaluators rate favorably. The result is a manipulation-compatible pattern that operates without explicit intent."

**日本語訳:**
人間のフィードバックからの強化学習（RLHF）で訓練されたモデルは、人間の評価者が好意的に評価する回答に最適化されています。結果として、明示的な意図なしに作動する操作適合パターンが生まれます。

**自分の言葉で言うと:**
AIは人を喜ばせるように訓練されています。これはR8が検出する認知操作パターンと同じ構造を持つ可能性があります。AIが生成するテキストをR8で監査するという方向性は、将来的な研究課題として論文に記載しています。

**想定質問と答え:**
Q: AIを批判することでAnthropicやGoogleと対立しませんか？
A: R8は設計の善悪を判断しません。構造を測定します。AIサイコファンシーが操作パターンを持つかどうかを実証的に調べることは、AI開発の透明性に貢献します。

---

## まとめ：一言で言うと

**英語版:**
R8 measures not whether information is true, but how structurally manipulative it is — quantifying the pressure exerted against independent thinking.

**日本語版:**
R8は情報が真実かどうかではなく、構造的にどれだけ操作的かを測ります。自分で考える力に対して加えられる圧力を定量化します。

---

*このガイドはR8 preprint v0.8に基づいて作成されました。*
*論文の改訂に伴い更新が必要です。*
