# R8 論文追加候補ストック
# R8 Paper Addition Candidates Stock

作成: 2026-05-04
方針: ラベリング・分析作業中に気づいた追加候補を記録する。
     最終的に整合性・リスク・重複をスクリーニングして採否を決定する。

---

## スクリーニング基準（最終判定時）

1. 論文の主張と整合するか
2. 固有名詞・名誉毀損リスクがないか
3. 査読者が「蛇足」と判断しないか
4. 既存の記述と重複しないか

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
