# R8 論文追加候補ストック
# R8 Paper Addition Candidates Stock

作成: 2026-05-04
方針: ラベリング・分析作業中に気づいた追加候補を記録する。
     最終的に整合性・リスク・重複をスクリーニングして採否を決定する。
     論文への実際の追記はラベリング完了後に改めて判断する。

【重要な方法論的注記】
本ファイルへの記録はラベリング基準（v0.7）の変更を意味しない。
ここで観察された構造概念は将来の独立検証を経るまで
現在のCMI計算・ラベリング判定の根拠として使用しない。
観察と記録は継続するが、判定の際に新たな知見を付け加えてはならない。

---

## スクリーニング基準（最終判定時）

1. 論文の主張と整合するか
2. 固有名詞・名誉毀損リスクがないか
3. 査読者が「蛇足」と判断しないか
4. 既存の記述と重複しないか
5. スコープ拡大により論文の焦点が曖昧になるリスクがないか（002以降で特に注意）
6. 現在のコーパスで観察した構造を同じコーパスで検証していないか（循環検証チェック）

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
- Zimbardo（2007）p27「バレルを作る人間」
- R8 Limitation「CMIスコアは意図を示さない」の具体的裏付け事例
- v2 Layer2設計の必要性の論拠

**リスク:**
- 固有名詞不使用 → 名誉毀損リスク低

---

### [002] 強制なき誘導構造（Non-coercive Influence）の検出スコープ

**発見日:** 2026-05-05
**着想の起点:** 「チャンネル登録よろしくお願いします」等の定型句の観察
**配置候補:** Future Work 7.2末尾 または 7.4内
**スクリーニング判定:** 未判定

**概念の整理:**

```
Level 0: 誘導なし（中立的情報提供）
Level 1: 強制なき誘導（社会的証明・互恵・登録依頼）← CMI未検出
Level 2: 損失回避・緊急性を伴う誘導（R8の現在の射程）
Level 3: 認知操作を伴う高リスク誘導（HIGHゾーン）
```

**追加候補文（英語）:**

> A further design consideration concerns the operationalization of influence without coercion. Texts that employ structurally equivalent persuasion mechanisms —social proof, reciprocity, and commitment induction (Cialdini, 1984) —without explicit urgency or fear signals represent a systematic gap in the current detection scope. Phase 2 will investigate whether a non-coercive influence dimension, distinct from the CMI's manipulation risk orientation, can be operationalized as a supplementary indicator for deployment contexts requiring broader persuasion-signal coverage.

**追加候補文（日本語）:**

> さらなる設計上の考慮事項として、強制を伴わない影響力の操作化がある。明示的な緊急性・恐怖シグナルを用いず、社会的証明・互恵・コミットメント誘導（Cialdini, 1984）等の構造的に等価な説得メカニズムを使用するテキストは、現在の検出スコープの系統的な空白を形成している。Phase 2では、CMIの操作的リスク志向とは区別される非強制的影響力次元を補助指標として操作化可能かどうかを検討する。

**理論的根拠:**
- Cialdini（1984）：社会的証明・互恵・コミットメント
- Kahneman（2011）：System 1は強制の有無に関わらず誘導可能

**スコープリスクの注記:**
- Future Workに留め、現在のR8の定義を変更しない形を厳守する
- ラベリング完了後に採否を決定する

---

### [003] エリート主義フレーミング（Elitism Framing）— 敵意なき内外分断構造

**発見日:** 2026-05-05
**着想の起点:** SN_24（PostPrimeプラットフォーム）のラベリング中に観察
**配置候補:** Future Work 7.2内（Layer2構造検出の設計根拠）
            または Limitations（EnemyFrameとの境界事例）
**スクリーニング判定:** 未判定

**概念の整理:**

「世間の多くが知らないが、自分と貴方は特別である」という誘導構造：

```
① 一般大衆との差別化（「知らない人 vs 知っている人」）
② 読者を「知る側・気づいた側」に位置づける
③ 帰属感・優越感の生成
④ コミュニティへの参加コスト低下・離脱コスト上昇
```

**既存カテゴリとの対応:**

| 構造要素 | 既存カテゴリ | 対応度 |
|---|---|---|
| 専門家集団への帰属誘導 | NormativeInduction（6） | △ |
| プロ・専門家の権威提示 | AuthorityHalo（7） | ○ |
| 排他性シグナル | ClickbaitRisk | △ |
| 「貴方は特別」個別化 | **未対応** | ✕ |

**EnemyFrameとの境界:**
EnemyFrame：敵意ある外集団を明示する
ElitismFraming：敵意なく「知らない多数」対「知っている少数」の対比構造のみ

**出現ジャンル（観察）:**
投資系SNS・自己啓発・陰謀論（EnemyFrameと複合）・カルト

**追加候補文（英語）:**

> A structurally distinct framing pattern was identified in Phase 1 calibration that does not map cleanly onto the existing EnemyFrame category: Elitism Framing, defined as the construction of a cognitive boundary between "those who know" and "the uninformed majority," without explicit adversarial attribution to the out-group. This pattern positions the reader as a specially selected member of an informed minority, generating belonging and superiority signals that function as low-friction commitment induction (Cialdini, 1984) and exploit the fundamental need to belong (Baumeister & Leary, 1995). Unlike EnemyFrame, which requires hostile out-group designation, Elitism Framing operates through positive in-group construction alone. Current R8 lexical architecture detects partial signals through NormativeInduction and AuthorityHalo categories but lacks a unified detection mechanism for the individualization component ("you, specifically, are capable of understanding this"). This structural gap is identified as a Phase 2 Layer 2 detection target.

**追加候補文（日本語）:**

> Phase 1較正において、既存のEnemyFrameカテゴリに明確に対応しない構造的に独自のフレーミングパターンが確認された：エリート主義フレーミング（Elitism Framing）。これは外集団への明示的な敵対的帰属を伴わず、「知っている人」と「知らない多数」の間に認知的境界を構築するパターンとして定義される。このパターンは読者を情報を持つ少数派の特別に選ばれたメンバーとして位置づけ、低摩擦のコミットメント誘導（Cialdini, 1984）として機能し、帰属欲求（Baumeister & Leary, 1995）を利用する帰属感・優越感シグナルを生成する。現在のR8語彙アーキテクチャはNormativeInductionおよびAuthorityHaloカテゴリを通じて部分的なシグナルを検出するが、個別化コンポーネント（「特に貴方は、これを理解できる」）に対する統一された検出メカニズムを欠いている。この構造的空白はPhase 2 Layer 2検出ターゲットとして特定される。

**理論的根拠:**
- Cialdini（1984）：コミットメントと一貫性、社会的証明
- Baumeister & Leary（1995）：帰属欲求（論文2.8で既引用）
- Janis（1972）：invulnerabilityの幻想との接続可能性
- 002との関係：ElitismFramingは非強制的誘導（Level 1）の具体的実装形態

**判断メモ（2026-05-05）:**
- 001・002・003は理論的に連結しており、ラベリング完了後に一括スクリーニング
- v2設計文書への先行記録も検討
- EnemyFrameのサブタイプ化か独立カテゴリ化かはPhase 2設計文書で先に検討

---

### [004] AIlabelへのriskfactor次元追加

**発見日:** 2026-05-06
**着想の起点:** human_label再ラベリング（riskfactor9分類）の作業中
**配置候補:** Future Work — AIlabel設計の拡張候補
**スクリーニング判定:** 未判定・実装はv1.7提出後

**概念の整理:**

現在のAIlabelはHML3値のみを出力する。human_labelと同様に、9分類のriskfactorコードを1〜3枚付与する設計に拡張することで以下が得られる：

```
現在: AIlabel = HIGH / MEDIUM / LOW
拡張後: AIlabel = HIGH + [No academic/empirical support, Desire Activation, ...]
```

**意義:**
- kappa計算の多次元化（HMLの一致率だけでなくriskfactor一致率も算出可能）
- AIlabelの説明責任の構造化（ailabel_reasonの自由記述 → コード化）
- v2 Layer2設計の根拠データ（riskfactorパターン分布）の獲得

**実装上の注意:**
- human_label側のriskfactor入力が完了・安定してから設計すること
- 人間側基準が固まる前にAI側を設計すると基準ずれが生じる
- プロンプト設計はv0.7基準をそのままAIに渡す形を基本とする

**優先度:** 低（v1.7提出後のAIlabel再設計フェーズで実装）

---

### [005] ジャンル別CMI分析（genre_label活用）

**発見日:** 2026-05-06
**着想の起点:** ラベリング作業中（識別子がweb/note/SNS等で、ジャンルも投資・恋愛・自己啓発等と多様）
**配置候補:** Methods 3.x（コーパス構成の説明）または Future Work（Phase2以降の分析計画）
**スクリーニング判定:** 未判定

**概念の整理:**

corpus_masterにはgenre_labelカラムが既存（一部入力済み）。
Phase2以降のLayer2設計では、ジャンル別に操作構造が異なるため分析単位としてのジャンル分類が必要。

```
想定ジャンル分類例:
  1: 投資・金融
  2: 恋愛・出会い
  3: 宗教・カルト
  4: 教育・自己啓発
  5: 政治・陰謀論
  6: 美容・健康・ダイエット
  7: 採用・就労
  8: その他
```

**意義:**
- ジャンル別CMIスコア分布の比較（論文のFigure候補）
- riskfactorのジャンル別頻度分析（どのジャンルで何が支配的か）
- Phase2 Layer2のジャンル別構造パターン設計の根拠
- 商業化（cocoanala）における検査対象の分類UIへの接続

**現時点での対応:**
- genre_labelカラムは既存。タクソノミー定義と全件入力はラベリング完了後に実施
- 現ラベリング作業中はgenre_labelに触らない（スコープ管理）

**優先度:** 中（ラベリング完了後、kappa計算と並行して実施）

---

### [006] 陰謀系テキストのHIGH集中：辞書バイアスか構造的必然か

**発見日:** 2026-05-06
**着想の起点:** ラベリング作業中の雑感（陰謀系テキストがHIGHに計測されやすい傾向の観察）
**配置候補:** Limitations — 辞書構築バイアスと検出精度の限界
**スクリーニング判定:** 未判定

**4仮説の整理:**

```
① 事実だから        → R8の射程外（内容真実性はCMIに無関係）
② 文章構造が強い    → 最有力。EnemyFrame＋Fear＋Propagandaの同時出現が
                       HIGHを引き起こす構造的必然
③ 辞書バイアス      → 否定不可。EnemyFrame・Propaganda辞書語彙が
                       陰謀論語彙と重複して設計されていれば循環的にHIGHが出る
④ 偶然（サンプル偏り）→ genre_label完成後にジャンル別件数を確認して検証可能
```

**論文上の扱い:**
②は「政治・陰謀論テキストのみが確実にHIGHに到達する」という既存のhandout記録と整合。
③は辞書構築バイアスとしてLimitationsに記載すべき問題。
「R8の検出はr8辞書の設計に依存する」という根本的限界であり、独立検証の必要性の論拠になる。

**検証方法（ラベリング完了後）:**
- ジャンル別CMIスコア分布のKruskal-Wallis検定
- 陰謀論ジャンルのみ有意にHIGHが多い場合 → ②または③の可能性
- 辞書語彙と陰謀論語彙の重複率を手動で確認 → ③の定量的評価

**優先度:** 中（[005]ジャンル別分析と同時に実施）

---
