# R8 論文追加候補ストック
# R8 Paper Addition Candidates Stock

作成: 2026-05-04
方針: ラベリング・分析作業中に気づいた追加候補を記録する。
     最終的に整合性・リスク・重複をスクリーニングして採否を決定する。
     論文への実際の追記はラベリング完了後に改めて判断する。

---

## スクリーニング基準（最終判定時）

1. 論文の主張と整合するか
2. 固有名詞・名誉毀損リスクがないか
3. 査読者が「蛇足」と判断しないか
4. 既存の記述と重複しないか
5. スコープ拡大により論文の焦点が曖昧になるリスクがないか（002以降で特に注意）

---

## 候補一覧

---

### [001] カリスマ起業家型テキストにおけるAuthorityHalo+NormativeInduction

**発見日:** 2026-05-04
**根拠コーパス事例:** AD_019（著名公人によるオンラインサロン記事、MEDIUM評定）
**配置候補:** Limitations — CMIスコアの解釈上の留意点
**スクリーニング判定:** 未判定

**追加候補文（英語）:**

> A notable structural finding is that AuthorityHalo and NormativeInduction signals are not limited to texts from unknown or fraudulent actors. Texts authored by publicly recognized entrepreneurs and creators with established social credibility also exhibit these patterns (e.g., membership community communications from prominent public figures, MEDIUM-rated in this corpus). This suggests that R8 detects linguistic structures functioning as cognitive manipulation signals, rather than proxies for sender credibility or intent. High CMI scores therefore neither confirm nor deny fraudulent intent; they indicate the presence of System 1-targeting linguistic patterns regardless of sender status.

**追加候補文（日本語）:**

> 注目すべき構造的知見として、AuthorityHaloおよびNormativeInductionシグナルは、未知の発信者や詐欺的行為者のテキストに限定されない。社会的信頼性が確立された著名な起業家・クリエイターによるテキスト（本コーパスにおいてMEDIUM評定を受けた著名公人によるコミュニティ向けコミュニケーション等）においても同様のパターンが検出された。これはR8が発信者の信頼性や意図の代理指標ではなく、認知操作シグナルとして機能する言語構造を検出することを示唆する。すなわち高CMIスコアは詐欺的意図を確認も否定もせず、発信者の社会的地位に依存しない形でSystem 1を標的とする言語パターンの存在を示すものである。

**理論的根拠:**
- Zimbardo（2007）p27「バレルを作る人間」：洗練された操作者は個別語彙ではなく権威と構造で操作する
- R8 Limitation「CMIスコアは意図を示さない」の具体的裏付け事例
- v2 Layer2設計の必要性の論拠にもなり得る

**リスク:**
- 存命公人への言及なし（固有名詞不使用）→ 名誉毀損リスク低
- 「著名公人」の匿名記述で対応済み

---

### [002] 強制なき誘導構造（Non-coercive Influence）の検出スコープ

**発見日:** 2026-05-05
**着想の起点:** ラベリング中に「チャンネル登録よろしくお願いします」等の定型句が
              悪意なく誘導構造を持つことに気づいた。
**配置候補:** Future Work 7.2末尾 または 7.4内
**スクリーニング判定:** 未判定

**概念の整理:**

現在のR8は「認知操作リスク（損害可能性あり）」を検出することを前提としている。
しかし誘導構造は「強制の強度」によって連続体をなしている：

```
Level 0: 誘導なし（中立的情報提供）
Level 1: 強制なき誘導（社会的証明・互恵・登録依頼）← CMI未検出
Level 2: 損失回避・緊急性を伴う誘導（R8の現在の射程）
Level 3: 認知操作を伴う高リスク誘導（HIGHゾーン）
```

Level 1はCialdini（1984）の社会的証明・互恵・コミットメント誘導に対応する。
受信者への強制はゼロだが、構造的には同一のSystem 1標的メカニズムが機能している。

**追加候補文（英語）:**

> A further design consideration concerns the operationalization of influence without coercion. Texts that employ structurally equivalent persuasion mechanisms —social proof, reciprocity, and commitment induction (Cialdini, 1984) —without explicit urgency or fear signals represent a systematic gap in the current detection scope. Phase 2 will investigate whether a non-coercive influence dimension, distinct from the CMI's manipulation risk orientation, can be operationalized as a supplementary indicator for deployment contexts requiring broader persuasion-signal coverage.

**追加候補文（日本語）:**

> さらなる設計上の考慮事項として、強制を伴わない影響力の操作化がある。明示的な緊急性・恐怖シグナルを用いず、社会的証明・互恵・コミットメント誘導（Cialdini, 1984）等の構造的に等価な説得メカニズムを使用するテキストは、現在の検出スコープの系統的な空白を形成している。Phase 2では、CMIの操作的リスク志向とは区別される非強制的影響力次元を補助指標として操作化可能かどうかを検討する。

**理論的根拠:**
- Cialdini（1984）：社会的証明・互恵・コミットメントはSystem 1を標的とするが強制を含まない
- Kahneman（2011）：System 1は強制の有無に関わらず誘導可能
- 7.4の非線形検出モデルとの接続：誘導強度のスペクトラムは閾値モデルの拡張として位置づけ可能

**スコープリスクの注記（要注意）:**
- 「認知操作リスク検出」から「説得シグナル検出全般」へのスコープ拡大を示唆する
- 査読者から「R8の定義が曖昧」と見なされる可能性がある
- 追記する場合はFuture Workに留め、現在のR8の定義を変更しない形を厳守する
- 既存の7.2・7.4との重複チェックが必要（ScarcityRisk・EVT変数操作との境界整理）

**判断メモ（2026-05-05）:**
- ラベリング完了後に改めてスコープ整合性を確認してから採否を決定する
- 採用する場合は7.2末尾への1〜2文追記が最小侵襲的

---

### [003] エリート主義フレーミング（Elitism Framing）— 敵意なき内外分断構造

**発見日:** 2026-05-05
**着想の起点:** SN_24（PostPrimeプラットフォームトップページ、投資系SNS）の
              ラベリング中に「知らない多数 vs 知っている少数」という
              敵意を伴わない内外分断構造を観察した。
**配置候補:** Future Work 7.2内（Layer2構造検出の設計根拠として）
            または Limitations 5.x（EnemyFrameとの境界事例として）
**スクリーニング判定:** 未判定

**概念の整理:**

「世間の多くが知らないが、自分と（それを読んで理解できる）貴方は特別である」
という認知誘導構造。分解すると：

```
① 一般大衆との差別化（「知らない人 vs 知っている人」）
② 読者を「知る側・気づいた側」に位置づける
③ その位置づけ自体が帰属感・優越感を生成する
④ コミュニティへの参加コスト低下・離脱コスト上昇
```

**既存カテゴリとの対応関係:**

| 構造要素 | 既存カテゴリ | 対応度 |
|---|---|---|
| 専門家集団への帰属誘導 | NormativeInduction（6） | △ 部分的 |
| プロ・専門家の権威提示 | AuthorityHalo（7） | ○ 対応 |
| 「知る者だけが得をする」排他性 | ClickbaitRisk | △ 部分的 |
| 「貴方は特別・理解できる」個別化 | **未対応** | ✕ |

**EnemyFrameとの境界:**
EnemyFrameは「敵の存在」と「敵意」を前提とする。
ElitismFramingは敵意なく「気づいていない多数」対「気づいている少数」という
対比構造を使う点で構造的に異なる。
→ EnemyFrameのサブタイプとして位置づけるか、独立カテゴリとするかは要検討。

**出現ジャンル（Phase 1コーパスでの観察）:**
- 投資系SNS・プラットフォーム（SN_24: PostPrime）
- 自己啓発系（「成功者だけが知っている」）
- 陰謀論系（「真実に気づいた者だけが」）→ EnemyFrameと複合
- カルト・宗教系（「選ばれた者・覚醒した者」）

**追加候補文（英語）:**

> A structurally distinct framing pattern was identified in Phase 1 calibration that does not map cleanly onto the existing EnemyFrame category: Elitism Framing, defined as the construction of a cognitive boundary between "those who know" and "the uninformed majority," without explicit adversarial attribution to the out-group. This pattern —observed in investment platform communications, self-development content, and spiritual texts in the calibration corpus —positions the reader as a specially selected member of an informed minority, generating belonging and superiority signals that function as low-friction commitment induction (Cialdini, 1984) and exploit the fundamental need to belong (Baumeister & Leary, 1995). Unlike EnemyFrame, which requires hostile out-group designation, Elitism Framing operates through positive in-group construction alone. Current R8 lexical architecture detects partial signals through NormativeInduction and AuthorityHalo categories but lacks a unified detection mechanism for the individualization component ("you, specifically, are capable of understanding this"). This structural gap is identified as a Phase 2 Layer 2 detection target.

**追加候補文（日本語）:**

> Phase 1較正において、既存のEnemyFrameカテゴリに明確に対応しない構造的に独自のフレーミングパターンが確認された：エリート主義フレーミング（Elitism Framing）。これは「知っている人」と「知らない多数」の間に認知的境界を構築するが、外集団への明示的な敵対的帰属を伴わないパターンとして定義される。投資プラットフォームのコミュニケーション・自己啓発コンテンツ・スピリチュアルテキスト等において観察されたこのパターンは、読者を情報を持つ少数派の特別に選ばれたメンバーとして位置づけ、低摩擦のコミットメント誘導（Cialdini, 1984）として機能し、帰属欲求（Baumeister & Leary, 1995）を利用する帰属感・優越感シグナルを生成する。敵対的外集団の指定を必要とするEnemyFrameとは異なり、ElitismFramingは肯定的内集団構築のみによって機能する。現在のR8語彙アーキテクチャはNormativeInductionおよびAuthorityHaloカテゴリを通じて部分的なシグナルを検出するが、個別化コンポーネント（「特に貴方は、これを理解できる」）に対する統一された検出メカニズムを欠いている。この構造的空白はPhase 2 Layer 2検出ターゲットとして特定される。

**理論的根拠:**
- Cialdini（1984）：コミットメントと一貫性、社会的証明
- Baumeister & Leary（1995）：帰属欲求の操作（論文2.8で既に引用済み）
- Janis（1972）：invulnerabilityの幻想（グループシンク症状）との接続可能性
- 002（非強制的誘導）との関係：ElitismFramingはLevel 1誘導の具体的実装形態の一つ

**スコープリスクの注記:**
- EnemyFrameの拡張として位置づければ既存カテゴリ体系を壊さない
- 独立カテゴリ化するとv2設計に影響する → Phase 2設計文書で先に検討すべき
- 論文への追記はFuture Workの1文に留めるのが最小侵襲的

**判断メモ（2026-05-05）:**
- 003は002と理論的に接続している（ElitismFramingは非強制的誘導の具体的形態）
- ラベリング完了後に001・002・003を一括してスクリーニングする
- v2設計文書（D:\r8_strategy\docs\design\R8_v2_design.md）への先行記録も検討

---
