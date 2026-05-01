# AIlabel Trial Design Document
Created: 2026-05-01
Branch: feature/ailabel-design
Status: Design phase (not yet implemented)

---

## 1. Purpose

Preliminary approximation of Phase 2 LLM integration.
Three LLMs (Claude, Gemini, GPT-4) independently apply annotation_criteria v0.6
to a subset of the Phase 1 corpus to generate AI-derived risk labels (AIlabel).

Inter-model agreement: Fleiss' kappa
AIlabel vs human_label agreement: Cohen's kappa (per model)

---

## 2. Corpus Subset Design

Target: 30 documents selected from 225-item corpus.
Stratified sampling:
- human=HIGH: 10 items (covering H-1, H-2, H-3, H-4 pattern types)
- human=MEDIUM: 10 items (covering M-1, M-2, M-3, M-4)
- human=LOW: 5 items
- Intent-Unresolved: 5 items

Selection criteria:
- Exclude sn234, sn235 (acquisition failure)
- Include sn236 (short-text FN case, Limitation 5.10 documentation)
- Include at least 1 book-genre item (charismatic entrepreneur, surface-positive FN)
- Include at least 1 political/conspiracy item (HIGH by EnemyFrame+FearRisk+Propaganda)

---

## 3. Prompt Template (to be applied identically across all 3 models)

```
あなたは認知的操作リスクのアノテーターです。
以下のアノテーション基準（annotation_criteria v0.6）に従い、
テキストにHIGH・MEDIUM・LOW・Intent-Unresolvedのいずれかのラベルを付けてください。

【判定基準の要約】
HIGH: H-1〜H-4のいずれか1つ以上を満たす
  H-1: 一人称体験談＋操作主体の不可視化＋外部誘導
  H-2: 並列累積エピソード＋規範収束＋反論余地の構造的不在
  H-3: 欲求喚起語彙（明示的）＋行動誘導の結合
  H-4: 恐怖・損失回避語彙＋即時外部行動誘導（2条件同時）

MEDIUM: H-1〜H-4を満たさず、M-1〜M-4のいずれかを満たす
  M-1: 間接的・漸進的行動誘導
  M-2: 検証不能な権威・統計の引用
  M-3: 商業的誘導意図（語彙密度低）
  M-4: 感情誘導語彙の近傍集中（同一段落3語以上）

LOW: HIGH・MEDIUMに該当しないと積極的に判断できる

Intent-Unresolved: 判定不能（保留）

【重要な注意事項】
- テキスト内の言語構造のみに基づいて判定する
- 発信者の属性・利益構造等テキスト外情報は使用しない
- CMIスコアは参考値。スコアに引きずられないこと
- 判定が定まらない場合はIntent-Unresolvedを使用する

【出力形式】
以下のJSON形式のみで回答してください。説明文は不要です。
{
  "label": "HIGH/MEDIUM/LOW/Intent-Unresolved",
  "primary_condition": "H-1/H-2/H-3/H-4/M-1/M-2/M-3/M-4/L-1/L-2/L-3/IU",
  "confidence": "high/medium/low",
  "reason": "判定根拠を1〜2文で"
}

【対象テキスト】
{TEXT}
```

---

## 4. Execution Protocol

1. Apply prompt to each of 30 documents x 3 models = 90 API calls total
2. Record output in ailabel_results.csv with columns:
   target, claude_label, gemini_label, gpt4_label, human_label, cmi, level
3. Calculate Fleiss' kappa across 3 models
4. Calculate Cohen's kappa per model vs human_label
5. Analyze divergence cases qualitatively

---

## 5. Known Biases to Document

- Claude: safety training may over-detect manipulation in ambiguous cases
- Gemini: Japanese language sensitivity may differ from Claude
- GPT-4: conservative tendency may under-detect subtle manipulation (H-1, H-2)
- All models: annotation_criteria v0.6 was developed in Claude sessions;
  Claude has implicit familiarity with the criteria that Gemini/GPT-4 lack

---

## 6. Success Criteria

- Fleiss' kappa among 3 LLMs >= 0.40 (moderate): criteria are operationalizable by LLMs
- Any model's kappa vs human_label >= 0.40: LLM can approximate human judgment
- If kappa < 0.40: document as evidence that H-2 and H-1 require human judgment

---

## 7. Placement in Paper

Section 7.3.1 (already drafted in develop branch):
"Three general-purpose large language models...Fleiss' kappa..."

Results will be added to Section 4 or new Section 4.5 after execution.
Limitation: Claude's implicit familiarity with criteria must be disclosed.

---

## 8. Next Steps

1. Select 30-document subset from corpus (stratified by human_label)
2. Extract text files for the 30 documents
3. Run prompt against Claude API (Sonnet 4)
4. Run same prompt against Gemini Pro and GPT-4
5. Compile ailabel_results.csv
6. Calculate Fleiss' kappa and Cohen's kappa per model
7. Evaluate against success criteria (Section 6)
8. Decide: merge to develop or purge feature branch
