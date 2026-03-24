# R8: A Lexical Framework for Approximating Cognitive Manipulation Risk in Text

**Author:** Takahiro Saito, M.S. in Clinical Psychology
**Affiliation:** Independent Researcher
**GitHub:** https://github.com/takahiro-oss/r8-cognitive-risk
**License:** CC BY 4.0
**Status:** Preprint (not peer-reviewed)
**Date:** March 2026
**Version:** v1.0 (preprint)

---

## Abstract

R8 proposes a structural approach to approximating cognitive manipulation risk in Japanese-language text across 12 theoretically grounded categories, drawing conceptual inspiration from factor-based psychometric models including the MMPI and Rorschach Comprehensive System. This is an exploratory framework at an early stage of empirical development; the claims made in this paper are limited to what the current implementation can support.

R8 proposes a lexical approximation framework informed by the qualitative analysis of organizational cognitive failure — as documented in studies of military and institutional collapse (Tobe et al., 1984). The theoretical framework integrates Japanese organizational sociology (Yamamoto, 1977; Nakane, 1967) with Western social psychology (Janis, 1972; Milgram, 1963; Kahneman, 2011) and clinical psychology of manipulation (Symington, 1993).

The system produces a single composite score, the Cognitive Manipulation Index (CMI), defined as an approximation of the aggregate linguistic signals associated with manipulation pressure against autonomous thinking. Initial calibration against a 62-document corpus (51 with valid CMI scores) yields an exact match rate of 61% and within-one-level agreement of 92%, with discrepancies attributable primarily to JavaScript-rendered content limitations, corpus scope, and single-rater annotation bias. The complete corpus and scoring data are publicly available at https://github.com/takahiro-oss/r8-cognitive-risk under CC BY 4.0.

---

## 1. Introduction

The proliferation of digital information has intensified the challenge of distinguishing legitimate communication from cognitive manipulation. Existing approaches to this problem — including fact-checking systems, hate speech detection, and misinformation classifiers — focus primarily on the veracity of content. However, cognitive manipulation operates at a structural level that precedes factual falsity. A message can be factually accurate while simultaneously exploiting psychological vulnerabilities through urgency, false authority, emotional amplification, and logical misdirection.

This structural dimension of manipulation has been examined qualitatively in organizational research. Notably, Tobe et al. (1984) identified the cognitive patterns that preceded Japan's institutional collapse in World War II — including the suppression of disconfirming information, over-reliance on authority, and emotionally-driven decision-making. These patterns were not unique to military organizations; they recur across corporate, political, and media contexts.

R8 (Cognitive Risk Analyzer) proposes a lexical extension of this qualitative tradition. The system operates across 12 risk categories derived from psychometric and clinical psychology frameworks, producing a single composite score: the Cognitive Manipulation Index (CMI). The present paper positions R8 explicitly as an exploratory baseline instrument rather than a validated measurement tool.

A parallel problem emerges from computational linguistics research on machine reading comprehension. Arai (2018) demonstrated that AI systems process text through statistical pattern matching without achieving genuine semantic understanding. This finding is cautionary rather than validating for R8: it highlights the risk that surface-level pattern matching — whether by AI or by lexical tools — may systematically fail to capture meaning. R8 operates within this same constraint. The decision to use surface-level lexical analysis is not presented as a principled methodological choice but as a practical starting point whose limitations are documented throughout this paper.

The present paper describes the theoretical foundation, implementation, and initial calibration of R8 as an open-source lexical auditing framework. Surface-level lexical analysis, while limited in contextual sensitivity, provides a reproducible and transparent baseline for cognitive risk approximation — one that complements rather than replaces deeper semantic analysis.

---

## 2. Theoretical Background

### 2.1 From Institutional Failure to Cognitive Manipulation: The "Essence of Failure" Framework

The structural analysis of cognitive failure in organizations has been examined qualitatively in Japanese organizational research. Tobe et al. (1984) identified recurring patterns of institutional collapse in the Japanese military during World War II — patterns that transcend their historical context and recur across corporate, political, and media environments.

Four structural patterns identified by Tobe et al. are directly relevant to R8's design. First, decision-making was dominated by subjective, wishful thinking rather than objective situational assessment — a pattern R8 operationalizes as Emotional Risk. Second, logical argumentation was systematically displaced by hierarchical authority and face-saving behavior — corresponding to R8's Authority Risk and Logical Risk categories. Third, organizations demonstrated a consistent refusal to incorporate disconfirming information, suppressing data that contradicted prevailing assumptions — a pattern detectable through R8's Disclaimer Exploit and Anonymous Authority scores. Fourth, and most critically, organizational decisions were governed not by explicit rules but by an implicit atmospheric consensus.

### 2.2 "Kuuki" and the Vertical Society: Structural Foundations of Cognitive Coercion

This implicit atmospheric consensus was theorized by Yamamoto (1977) as "kuuki" (空気, literally "air") — a form of social pressure that operates below the level of explicit argument, yet determines collective outcomes with greater force than formal reasoning. Kuuki functions as an extra-logical coercive force that paralyzes rational dissent without requiring explicit justification.

The structural foundation that sustains kuuki is identified by Nakane (1967) in her analysis of Japanese vertical society (tate-shakai). In this framework, the credibility of information is determined not by its content but by the hierarchical position of its source. Truth, in effect, is assigned by rank rather than derived through reasoning. R8 operationalizes a proxy for this structural dynamic through its False Authority and Logical Misdirection categories: the CMI approximates the density of linguistic markers associated with bypassing critical thinking through hierarchical status and situational mood rather than logical demonstration.

### 2.3 The "Glider" Problem: Approximating Cognitive Dependency

The susceptibility of individuals to such manipulation is illuminated by Toyama's (1983) "glider" metaphor, describing cognitive subjects who lack independent reasoning propulsion and rely instead on external information flow for directional guidance. Manipulative texts exploit this dependency through urgency signals and disclaimer exploitation — keeping the subject in a state of passive reception that may prevent the activation of autonomous critical judgment.

R8 functions as a "Cognitive Breakwater" (認知的防波堤): it identifies linguistic patterns in text that may incline a reader toward cognitive dependency rather than deliberation. The CMI is defined not as a direct measure of manipulation, but as an approximation of the density of linguistic signals associated with such pressure.

### 2.4 From "Kuuki" to CMI: A Lexical Approximation of Implicit Coercion

The phenomena described by Tobe et al. (1984), Yamamoto (1977), and Nakane (1967) have resisted quantification precisely because they operate through implicit linguistic signals rather than explicit propositional content. Qualitative identification has been possible; measurement has not.

R8's Cognitive Manipulation Index (CMI) proposes a first approximation of this quantification. By measuring the density of lexical markers across 12 risk categories — including urgency signals, false authority claims, emotional amplifiers, and disclaimer exploitation — CMI approximates the aggregate linguistic environment within which cognitive coercion may operate. We do not claim that CMI captures the kuuki phenomenon; rather, we propose it as a measurable proxy for the linguistic conditions under which implicit coercion becomes structurally probable. Whether CMI scores correspond to actual manipulation effects on readers is an empirical question that the current study cannot answer.

### 2.4.1 Cross-Cultural Convergence

The structural dynamics described by Tobe et al. (1984), Yamamoto (1977), and Nakane (1967) are not culturally unique to Japan. Western social psychology has independently identified structurally similar phenomena, providing theoretical convergence for R8's foundations.

Janis (1972) documented similar atmospheric consensus dynamics in Western organizational contexts under the term "Groupthink" — a process whereby cohesive groups suppress critical thinking and converge on decisions through social pressure rather than logical deliberation. The structural parallels between kuuki and Groupthink suggest that R8's detection framework may address features of collective cognition that extend beyond Japan-specific phenomena, though cross-cultural empirical validation is deferred to future work.

Milgram's (1963) obedience experiments demonstrated the cross-cultural tendency toward authority submission: individuals systematically reduce autonomous judgment in the presence of authority markers — titles, institutional affiliation — regardless of the content of the instruction. This finding provides theoretical grounding for R8's Authority Risk and Anonymous Authority categories.

Kahneman (2011) provided the cognitive architecture underlying Toyama's (1983) "glider" metaphor. System 1 thinking — fast, automatic, and effortless — is the cognitive default that manipulative texts may exploit. Urgency signals, naked numbers, and emotional amplification may be designed to prevent the activation of System 2 — slow, deliberate, and analytically demanding. R8's CMI can be interpreted as an approximation of aggregate System 1 pressure signals in a text, with the important caveat that lexical density does not demonstrate actual cognitive effects on readers.

### 2.5 Psychometric Foundations

R8's multi-category scoring structure draws conceptual inspiration from established psychometric instruments that share a common architectural logic: qualitatively observed psychological phenomena are operationalized as multiple discrete indicators, which are then aggregated into a composite score through weighted combination.

The Minnesota Multiphasic Personality Inventory (MMPI; Hathaway & McKinley, 1943) exemplifies this structure: ten clinical scales, each measuring a distinct dimension of psychopathology, are combined into a profile that enables multi-dimensional assessment from a single administration. Similarly, Exner's Comprehensive System for the Rorschach (Exner, 1993) transformed a projective technique of inherently qualitative responses into a standardized numerical coding system.

R8 applies this architectural logic to textual cognitive risk: 12 risk categories function analogously to clinical scales, each capturing a distinct linguistic dimension; the CMI represents the weighted composite. This inspiration is acknowledged explicitly as conceptual only. R8's categories have not undergone the large-scale normative validation that characterizes established psychometric instruments (DeVellis, 2016), and the comparison to MMPI or Rorschach reflects architectural analogy, not equivalence of validation status. The present framework is positioned as an exploratory first-generation instrument.

### 2.6 Narcissistic Manipulation and Clinical Lexical Patterns

Clinical psychology offers a further theoretical grounding for R8's lexical approach. Symington (1993) identified the structural features of narcissistic communication — including the systematic denial of the other's autonomous perspective, the exploitation of emotional dependency, and the use of authority claims to pre-empt critical evaluation. These clinical patterns manifest in language through identifiable lexical signatures: absolutist framing, urgency induction, false authority appeals, and the simultaneous deployment of disclaimers and amplification.

R8's dictionary construction draws on this clinical tradition. The categories of Emotional Risk, Authority Risk, Disclaimer Exploit, and Naked Number reflect patterns recognizable in the clinical literature on manipulative communication. The connection between clinical theory and dictionary items is the author's interpretive construction and requires independent empirical validation.

### 2.7 Information Integrity Context

The practical context for R8 extends into the domain of information integrity — the challenge of identifying communication that may exploit structural psychological vulnerabilities rather than relying on verifiable evidence. Automated lexical tools capable of flagging manipulation-compatible patterns at the surface level represent one possible complement to existing approaches focused on source credibility and network propagation analysis.

R8 is positioned as an open-source, transparent instrument for detecting manipulation-compatible linguistic signatures, with the explicit acknowledgment that surface-level detection does not establish manipulative intent or effect.

---

## 3. Methodology

### 3.1 System Architecture

R8 operates as a pipeline of three sequential processes: text acquisition, lexical analysis, and score aggregation. Input sources include plain text files, PDF documents, and web URLs. Text acquisition from web sources employs HTTP request with BeautifulSoup-based HTML parsing, with removal of non-content elements (navigation, scripts, footers). PDF extraction is implemented via PyMuPDF. All acquired text is passed to a unified analysis function regardless of source type.

### 3.2 Text Normalization (Phase 1)

Prior to analysis, all input text undergoes normalization to reduce orthographic variation. The normalization pipeline applies Unicode NFKC normalization (converting full-width alphanumerics to half-width, decomposing ligatures), followed by katakana-to-hiragana conversion via Unicode codepoint mapping (U+30A1–U+30F3, offset -96). Consecutive whitespace and redundant line breaks are compressed.

This Phase 1 normalization addresses surface-level orthographic variation while explicitly acknowledging its limitations: kanji-kana equivalence, contextual disambiguation, and cross-linguistic semantic mapping require morphological analysis and are deferred to Phase 2 development.

### 3.3 Operational Definitions of 12 Risk Categories

The 12 categories are derived from clinical psychology, organizational behavior, and rhetorical analysis frameworks. Each category is operationalized as a lexical density measure: the count of matched dictionary terms divided by text length per 100 characters.

| Category | Operational Definition | Theoretical Basis |
|---|---|---|
| Authority Risk | Density of pseudo-authority markers (e.g., "scientifically proven," "independent research") excluding legitimate academic citation | Tobe et al. (1984): over-reliance on authority |
| Emotional Risk | Mean density of urgency, absolutist, and emotional amplification markers | Yamamoto (1977): kuuki as emotional coercion |
| Logical Risk | Density of anecdotal evidence markers and unwarranted conclusion markers | Nakane (1967): rank over reasoning |
| Statistical Risk | Density of statistical claim markers plus frequency of percentage expressions | False quantification patterns |
| Hype Risk | Density of responsibility-evasion amplification markers | Disclaimer exploitation |
| Clickbait Risk | Density of attention-hijacking markers | Engagement manipulation |
| Propaganda Risk | Density of institutional distrust and conspiracy markers | Information environment degradation |
| Fear Risk | Density of threat and catastrophe markers | Fear-based compliance induction |
| Enemy Frame | Density of in-group/out-group polarization markers | Us-vs-them cognitive framing |
| Disclaimer Exploit | Binary: high when disclaimer density and hype density co-occur above threshold | Simultaneous deniability and amplification |
| Anonymous Authority | Density of unattributed authority claims (e.g., "analysts say," "sources indicate") | Yamamoto (1977): kuuki through unverifiable consensus |
| Naked Number | Binary: high when specific numerical claims appear without cited sources | False precision as manipulation |

### 3.4 Two-Layer Authority Detection

Authority Risk employs a two-layer detection architecture distinguishing pseudo-authority from legitimate authority reference. Pseudo-authority markers (e.g., "scientifically proven," "proprietary research," "as research shows") are scored directly as risk indicators, as these expressions appear with negligible frequency in formal academic or governmental documents. Legitimate authority markers (e.g., "researcher," "professor," "clinical") are scored conditionally: their risk contribution is modulated by the concurrent Hype Risk density, operationalizing the pattern of exploiting legitimate authority frames within manipulative rhetorical contexts.

This architecture was introduced to resolve systematic false positives observed when analyzing formal governmental documents, which contain high densities of legitimate authority language without manipulative intent.

### 3.5 Scoring Algorithm

The Cognitive Manipulation Index (CMI) is computed as a weighted sum of normalized category scores:

$$CMI = 100 \times \sum_{i=1}^{12} w_i \cdot \min\left(\frac{raw_i}{threshold_i}, 1.0\right)$$

where $w_i$ is the category weight ($\sum w_i = 1.0$), $raw_i$ is the raw lexical density for category $i$, and $threshold_i$ is the calibrated normalization threshold. The $\min(\cdot, 1.0)$ ceiling prevents any single category from dominating the composite score.

Category weights reflect the relative contribution of each manipulation dimension to overall cognitive risk, derived through theoretical reasoning and iterative empirical calibration on a small pilot corpus. These weights have not been validated against an independent held-out dataset and should be treated as provisional. Statistical Risk carries the highest weight (0.16), reflecting the theoretical manipulative potency of false quantification. CMI ranges from 0 (no detected manipulation signals) to 100 (maximum signal density across all categories).

Threshold levels for risk classification:

- LOW: CMI < 35
- MEDIUM: 35 ≤ CMI < 60
- HIGH: CMI ≥ 60

A key limitation of the scalar CMI is that it aggregates across all 12 categories, which may obscure structurally distinct manipulation profiles. The per-category vector — showing which specific dimensions are activated — is often more diagnostically informative than the scalar composite, particularly for politically framed content (see Section 4.4).

### 3.6 Implementation

R8 is implemented in Python 3.x as two modules: `r8.py` (single-document analysis) and `mass_audit.py` (batch processing). The system requires no machine learning infrastructure, external APIs, or GPU resources, operating entirely through dictionary lookup and regular expression matching. This architectural decision prioritizes transparency, reproducibility, and deployability in resource-constrained environments over predictive accuracy. All source code is publicly available under CC BY 4.0 at https://github.com/takahiro-oss/r8-cognitive-risk.

### 3.7 AI-Assisted Development

The development of R8, including conceptual framework design, dictionary construction, code implementation, and the drafting of this manuscript, was conducted with AI assistance (Claude, Anthropic; Gemini, Google). The theoretical integration, research direction, and design decisions are the original work of the author. This disclosure is made in accordance with emerging norms of transparency in AI-assisted research, and is consistent with R8's own commitment to cognitive transparency as a research value.

---

## 4. Initial Calibration and Exploratory Testing

### 4.1 Study Design

The present calibration exercise is explicitly preliminary in scope. R8 is evaluated against a corpus of Japanese-language documents spanning three risk categories: high-risk (documents exhibiting known cognitive manipulation patterns), medium-risk (commercially oriented, editorially biased, or politically framed content), and low-risk (formal governmental and institutional documents). The term "validation" is avoided here because the study design does not meet the requirements for formal psychometric validation: the corpus is small, risk labels were assigned by a single rater (the system's author), and no independent ground-truth exists against which to evaluate the labels themselves.

The calibration corpus comprises 62 documents collected through automated URL-based scraping using the mass_audit.py pipeline. Of the 62 documents, 11 returned CMI scores of 0.0 due to JavaScript-rendered content inaccessibility — a structural limitation documented in Section 5.4 — yielding 51 documents with valid CMI scores. The corpus was assembled through stratified sampling targeting commercial manipulation (investment schemes, multi-level marketing, spiritual commercial content), political framing (domestic party media, international state-affiliated outlets), and institutional communication (governmental and academic sources).

Ground truth classification was determined through single-rater expert judgment by the author, drawing on clinical psychology training and 20 years of educational practice. A structured rubric was applied to ensure consistency and transparency of classification (see Appendix A). **The use of the system's author as the sole annotator constitutes a significant source of bias that cannot be quantified at this scale.** For 5 documents where CMI scores fell below the automated threshold despite structural evidence of manipulation-compatible patterns (particularly political framing content characterized by Enemy Frame and Fear Risk activation without commercial urgency markers), expert labels were assigned at MEDIUM rather than the automated LOW classification, with annotation recorded in the corpus metadata. Without this reclassification, the exact match rate would be 26/51 (51%) rather than 31/51 (61%); the effect of this author-initiated intervention on reported performance is therefore non-trivial and must be interpreted accordingly.

### 4.2 Corpus Description

The 62-document corpus spans the following distribution:

| Risk Label | Count | Proportion | Notes |
|---|---|---|---|
| HIGH | 3 | 5% | Spiritual commercial LP, investment scheme LP |
| MEDIUM | 19 | 31% | Commercial, political framing, spiritual content |
| LOW | 40 | 64% | Governmental, academic, news media |
| **Total** | **62** | **100%** | 11 CMI=0.0 (JS rendering failure) |

Genre distribution across the corpus includes: governmental and institutional documents (LOW baseline), commercial manipulation content (investment schemes, MLM, diet/health products), spiritual and pseudoscientific content, political party media (domestic and international state-affiliated outlets), and financial advisory content. Western media and geopolitical content were incorporated to provide initial cross-cultural testing of CMI behavior. The complete corpus URL list and per-document CMI scores are available in the project repository at https://github.com/takahiro-oss/r8-cognitive-risk.

The 11 documents returning CMI=0.0 are retained in the corpus as documented instances of JavaScript-rendered content inaccessibility, consistent with the structural limitation described in Section 5.4. Valid CMI scores were obtained for 51 of 62 documents (82.3%).

### 4.3 Results

CMI scores were obtained for 51 of 62 documents (82.3%). The remaining 11 documents returned CMI=0.0 due to JavaScript-rendered content inaccessibility and are excluded from quantitative analysis (see Section 5.4).

Summary statistics for valid documents (n=51):

| Metric | Value |
|---|---|
| Mean CMI | 28.7 |
| Maximum CMI | 65.2 |
| Minimum CMI (excluding 0.0) | 3.1 |
| HIGH label count (CMI ≥ 60) | 3 |
| MEDIUM label count (35–59) | 19 |
| LOW label count (CMI < 35) | 29 |

Representative samples by risk category:

| Risk | Source | CMI | Notable Category Profile |
|---|---|---|---|
| HIGH | Spiritual commercial LP (laviestella.co.jp) | 65.2 | Authority+Emotional+Propaganda 1.00 |
| HIGH | Business coaching LP (leaders-agency.com) | 63.1 | Authority+Emotional+Logical 1.00 |
| HIGH | Twin-ray spiritual LP (fortune-star.co.jp) | 63.6 | Fear+Propaganda+Naked Number 1.00 |
| MEDIUM | Akahata (jcp.or.jp) | 47.0 | Fear+EnemyFrame+Logical 1.00 |
| MEDIUM | Renmin Ribao JP (j.people.com.cn) | 17.3* | Fear+EnemyFrame (*scalar LOW, vector MEDIUM) |
| MEDIUM | Sputnik JP (sputniknews.jp) | 10.9* | EnemyFrame 1.00 (*scalar LOW, vector MEDIUM) |
| LOW | Ministry of Education PDF | 34.2 | Authority markers only |
| LOW | Governmental institutional docs | 0–15 | Minimal manipulation markers |

*These entries illustrate a key finding: scalar CMI underdetects politically framed content that operates primarily through Enemy Frame and Fear Risk activation without commercial urgency markers. Expert reclassification to MEDIUM reflects structural rather than scalar assessment, and highlights the diagnostic value of the per-category profile over the scalar composite.

Exact match rate (automated vs. expert label): 31/51 (61%). Agreement within one risk level: 47/51 (92%). These figures should be interpreted with caution given the single-rater annotation design.

### 4.4 Analysis of Discrepancies

Three categories of discrepancy were identified.

The first concerns text acquisition limitations. Eleven documents (17.7% of corpus) returned CMI=0.0 due to JavaScript-rendered dynamic content that BeautifulSoup-based scraping cannot access. These documents are retained in the corpus as documented instances of a structural sampling bias — high-risk commercial content disproportionately employs JS-rendered delivery — rather than excluded as invalid samples.

The second concerns scalar underdetection of politically framed content. State-affiliated international outlets (Sputnik JP, Renmin Ribao JP) and domestic political party media (Akahata) exhibited Enemy Frame and Fear Risk activation at maximum density while returning LOW scalar CMI scores. This pattern reflects a systematic limitation of the current scalar aggregation architecture: politically framed manipulation operates through structural framing rather than the commercial urgency and authority markers that dominate the current dictionary. Expert reclassification of five such documents to MEDIUM is annotated in corpus metadata.

The third concerns satirical mimicry. Satirical content (虚構新聞) that intentionally mimics manipulative news structure registers elevated CMI scores relative to expert LOW classification. This reflects R8's structural sensitivity: manipulation-compatible lexical patterns are detected regardless of authorial intent. This is a principled design characteristic of surface-level lexical analysis rather than an error, though it constitutes a source of false positives.

### 4.5 Implications for Dictionary Calibration

The preliminary results indicate that R8's current lexical dictionary is sensitive to commercially framed manipulation but requires expansion to capture anecdotal manipulation (personal testimony as proof), spiritually framed authority (appeal to non-verifiable experience), and satirical mimicry. The systematic underdetection of politically framed content indicates that the current scalar CMI is calibrated primarily to commercial manipulation patterns and should not be treated as a general-purpose manipulation detector in its current form.

---

## 5. Current Limitations

### 5.1 Surface-Level Lexical Matching

The current implementation relies exclusively on surface-level lexical matching and does not account for contextual disambiguation, linguistic variation, or cross-linguistic semantic equivalence. Integration of transformer-based contextual language models is identified as a future development direction, not a current capability.

Three specific consequences follow from this design choice. First, the system cannot distinguish between identical surface forms that carry different semantic functions across contexts. The term "支配" (domination/control), for instance, carries high risk weight in political manipulation contexts but is neutral in descriptive analyses of market dynamics. Second, orthographic variation beyond the scope of Phase 1 normalization — including non-standard kanji readings, dialectal expressions, and intentional obfuscation — may evade detection. Third, the binary and density-based scoring approach does not capture syntactic manipulation patterns such as presupposition, implicature, or pragmatic force.

These limitations may result in false positives for formal documents containing legitimate authority references, and false negatives for manipulative content that employs non-standard orthography or indirect rhetorical strategies.

### 5.2 Language Scope

The current implementation is Japanese-language specific. All dictionaries, normalization procedures, and validation corpora are constructed for Japanese text. Extension to other languages requires not only lexical translation but structural re-analysis, as manipulative rhetorical patterns differ systematically across linguistic and cultural contexts.

English-language manipulation, for instance, tends toward more syntactically explicit urgency framing, while Japanese manipulation more frequently operates through implicature and contextual pressure — precisely the kuuki dynamics described in Section 2.2. Cross-linguistic extension is deferred to future development phases.

### 5.3 Calibration Corpus Limitations

The present calibration corpus of 62 documents (51 with valid CMI scores) is insufficient for definitive statistical inference. Effect size estimation, inter-rater reliability assessment, and generalizability claims require a larger corpus with balanced risk categories and independent expert annotation by multiple raters. The current single-rater expert judgment — conducted by the system's author — introduces potential annotation bias that cannot be quantified at this scale and represents the most significant methodological limitation of the present study.

During corpus construction, a stratified sampling strategy targeting 60 documents across LOW, MEDIUM, and HIGH risk categories was designed with the following intended distribution: government and academic sources (LOW); advertising, health, and investment content (MEDIUM); and investment fraud, multi-level marketing recruitment, and spiritual commercial content (HIGH). The actual distribution deviated substantially from this design, skewing heavily toward LOW (40 of 51 valid documents), reflecting both the base-rate reality of web content and the systematic inaccessibility of high-risk JS-rendered material documented in Section 5.4.

Three structural findings emerged from this collection effort. First, HIGH-risk content disproportionately employs JavaScript-rendered dynamic content, creating a systematic sampling bias that underrepresents the most manipulative material. Second, spiritually framed commercial manipulation achieves HIGH CMI scores through dense deployment of emotional, authority, and propaganda markers, suggesting this genre is structurally well-captured by the current dictionary. Third, politically framed content consistently achieved LOW CMI scores despite structural evidence of manipulation-compatible patterns, indicating that the current dictionary is calibrated primarily to commercial rather than political manipulation.

### 5.4 Closed-Platform Migration: A Structural Limitation of URL-Based Analysis

A significant proportion of high-risk web content — including investment scheme promotions, multi-level marketing recruitment pages, and cult recruitment materials — employs JavaScript-rendered dynamic content that BeautifulSoup-based scraping cannot access. This creates a systematic sampling bias in which the most manipulative content is the least accessible to automated analysis. Headless browser integration (e.g., Playwright, Selenium) is identified as a priority technical development.

A structurally more fundamental limitation extends beyond the JavaScript rendering problem. Evidence gathered during corpus construction suggests that high-risk manipulative content has undergone systematic platform migration away from indexable open web pages toward closed-platform ecosystems that are inaccessible to URL-based analysis by design.

Japanese National Police Agency data for fiscal year 2024 indicate that the primary initial contact tool for SNS-type investment fraud and romance fraud was Facebook for male victims, with subsequent interaction systematically migrated to LINE — a closed messaging platform operating outside the indexable web (National Police Agency, 2025). Romance fraud incidents increased substantially year-over-year in 2024, reaching 3,784 reported cases with aggregate losses of 39.7 billion yen. This two-stage architecture — open platform for initial contact, closed platform for manipulation execution — renders URL-based corpus construction systematically incomplete for the most harmful manipulation categories.

The implication for R8's architecture is not merely technical but epistemological: URL-based lexical analysis captures the visible surface of the manipulation ecosystem while the highest-risk content has migrated below the indexable horizon. Future development will require either platform API access under appropriate ethical and legal frameworks, or corpus construction through controlled experimental methods such as synthetic text generation calibrated to documented manipulation patterns.

### 5.5 Dictionary Construction Methodology

The current lexical dictionaries were constructed through theoretical reasoning and expert judgment rather than corpus-based induction. While this approach ensures theoretical coherence, it may systematically underrepresent manipulation patterns that fall outside the author's domain expertise or cultural familiarity.

The iterative development process from version 10 to version 16 of the R8 dictionary illustrates both the potential and the limitation of this approach. Across six revision cycles, the dictionary was progressively expanded to include spiritual and pseudoscientific manipulation vocabulary, political conspiracy framing vocabulary, and international conspiracy terminology. Each expansion cycle produced measurable CMI increases for documents in the targeted genre.

However, this iterative expansion process introduces a methodological concern that must be explicitly acknowledged: the risk of circular validation. When dictionary expansion is guided by the observation that targeted content produces low CMI scores, the expansion process may be optimizing for a predetermined outcome rather than discovering a stable underlying construct. The current version of R8 cannot fully resolve this concern without independent corpus-based validation against an annotated ground-truth dataset constructed without reference to CMI scores. This limitation precisely characterizes the exploratory status of the current instrument.

### 5.7 The Gap Between Theoretical Framing and Implemented Method

A structural limitation that underlies all others in this paper deserves explicit statement. The theoretical framework presented in Section 2 draws heavily on phenomena that are by definition non-lexical: kuuki operates below the level of explicit argument; System 1 exploitation occurs through psychological priming that may be independent of specific vocabulary; narcissistic manipulation functions through relational dynamics and pragmatic implicature. These are context-dependent, cognitively mediated phenomena.

The implemented method — surface-level lexical density analysis — operates at a categorically different level of description. No amount of dictionary expansion or weight calibration can bridge this gap, because the phenomena the theory describes are not reducible to lexical frequency. What R8 detects is not manipulation as theorized in Section 2; it detects the presence of lexical patterns that have been associated with manipulation contexts by the author's judgment. Whether those lexical patterns are reliable surface correlates of the deeper phenomena remains entirely undemonstrated.

This does not invalidate the framework as an exploratory starting point. It does mean that the theoretical framing in Section 2 should be read as motivational context rather than as a validated theoretical foundation for the measurement model. Future work establishing empirical links between specific lexical patterns and documented manipulation outcomes would be required before the theoretical framing can be claimed as a genuine basis for the implemented method.



Category weights and normalization thresholds were set through iterative empirical observation on a small pilot corpus rather than through optimization against a held-out validation set. The current weight distribution (Statistical Risk: 0.16; Authority Risk, Emotional Risk: 0.12 each) reflects theoretical priors rather than empirically derived importance rankings. Systematic calibration using a larger annotated corpus is required before the weight structure can be considered validated.

---

## 6. Future Work

### 6.1 Phase 2: Transformer-Based Contextual Analysis

The most significant planned development is the integration of transformer-based language models for contextual disambiguation. Specifically, the distinction between legitimate authority citation and pseudo-authority exploitation — currently handled through the two-layer heuristic described in Section 3.4 — would benefit substantially from contextual encoding. A BERT-based or similar architecture fine-tuned on annotated Japanese manipulation corpora could provide sentence-level context sensitivity without sacrificing the transparency and reproducibility that characterize the current lexical approach.

This development is framed as complementary rather than replacement: the lexical baseline provides interpretable, auditable scores that transformer-based augmentation can refine without rendering opaque. Transformer integration is a planned direction, not a current capability.

### 6.2 Phase 2: Validation Corpus Expansion and Inter-Rater Reliability

Expansion of the calibration corpus and establishment of inter-rater reliability are the immediate empirical priorities. Independent annotation of the validation corpus by multiple raters with defined inter-rater reliability metrics (Cohen's kappa or Krippendorff's alpha) is required before calibration results can be presented as statistically defensible. The expanded corpus will include high-risk documents across three manipulation modalities currently underrepresented: cult recruitment and coercive control language, multi-level marketing and investment scheme promotions, and domestic violence and psychological abuse language patterns.

The Phase 2 corpus design will address current limitations through three modifications: (1) manual collection of HIGH-risk documents where automated collection fails due to JavaScript rendering; (2) genre-stratified sampling that separately targets commercial, political, and spiritual manipulation modalities; and (3) independent annotation by multiple raters to establish inter-rater reliability metrics prior to CMI calibration.

### 6.3 Phase 2: Vector Profile Development

A key finding of the initial calibration is that the scalar CMI fails to detect politically framed manipulation operating primarily through Enemy Frame and Fear Risk activation. A vector-based profiling approach — presenting the full 12-category score distribution rather than the scalar composite — would preserve this structural information. Phase 2 development will investigate whether vector distance measures (e.g., cosine similarity between category profiles) provide more discriminative power than scalar aggregation for politically framed content.

### 6.4 Phase 3: Multilingual Extension

Extension to English-language analysis is identified as a potential future direction pending resource availability. English dictionary construction would require structural re-analysis rather than direct translation, as manipulative rhetorical patterns differ systematically from their Japanese counterparts. Subsequent extension to other languages is deferred pending the outcomes of Phase 2 validation.

### 6.5 Phase 3: AI-Generated Text Analysis

A longer-term research direction extends R8's framework to the analysis of AI-generated communication. The proliferation of large language models (LLMs) as communication intermediaries introduces a potential vector of cognitive manipulation risk through sycophantic bias — the tendency of AI systems to affirm user preferences regardless of epistemic accuracy. Whether R8's lexical categories are sensitive to this pattern is an open empirical question.

A preliminary and insufficiently controlled probe applying R8 to responses generated by three LLMs under different framing conditions yielded CMI variation suggesting potential sensitivity. However, the prompt design was not adequately controlled for confounding variables, and these preliminary findings are not presented as results. Refined, controlled experimental designs are required before any claims about AI-generated text can be made. This application remains speculative.

### 6.6 Phase 3: Academic Integrity Application

An exploratory application of R8's framework to academic peer review processes has been identified as a longer-term research direction. The structural patterns of manipulative communication — false authority, logical misdirection, statistical manipulation — may appear in academic discourse, and a tool capable of flagging these patterns could contribute to research integrity infrastructure. This application is speculative and requires substantial theoretical and empirical development before implementation.

---

## 7. Conclusion

R8 presents a first-generation lexical framework for approximating cognitive manipulation risk in Japanese-language text. By operationalizing 12 theoretically grounded risk categories into a single composite index — the Cognitive Manipulation Index (CMI) — the system proposes a reproducible lexical approximation that may complement qualitative traditions of organizational failure analysis.

The theoretical framing of R8 draws on Japanese organizational sociology (Tobe et al., 1984; Yamamoto, 1977; Nakane, 1967), clinical psychology of manipulation (Symington, 1993), psychometric measurement methodology (MMPI, Rorschach Comprehensive System as conceptual inspiration only), and cognitive linguistics (Arai, 2018; Toyama, 1983) as a common reference frame. Whether this cross-disciplinary framing adequately maps onto the lexical detection implemented is itself an open question that future empirical work must address.

The empirical findings of this preprint are best understood as a problem map for second-generation development rather than a validation claim for the current instrument. Initial calibration identified three findings of methodological significance. First, spiritually framed commercial manipulation consistently produced HIGH CMI scores in this preliminary sample (n=3), suggesting the current dictionary may be sensitive to this genre — though the sample is too small to support generalization. Second, politically framed manipulation consistently falls below the HIGH threshold, indicating a systematic gap between the commercial manipulation dictionary and the rhetorical patterns characteristic of political content. Third, the iterative expansion from dictionary version 10 to version 16 — while producing measurable CMI improvements — introduces a circular validation risk that cannot be resolved without independent ground-truth annotation.

This asymmetry between commercial and political manipulation detection is a diagnostic finding that locates where second-generation development must focus.

The limitations of the current implementation are substantial and explicitly acknowledged: surface-level lexical matching without contextual disambiguation, a calibration corpus of insufficient scale, single-rater annotation, and dictionary construction without corpus-based induction. R8 is presented as a transparent, reproducible, and theoretically grounded exploratory baseline — one designed to be extended, critiqued, and improved through open collaborative development. All source code, corpus data, and this preprint are publicly available at https://github.com/takahiro-oss/r8-cognitive-risk under CC BY 4.0.

---

## Appendix A: Expert Judgment Rubric for Ground Truth Classification

### A.1 Rubric Design Rationale

Ground truth labels were assigned using a structured rubric derived from established frameworks in persuasion research, clinical psychology of manipulation, and media literacy assessment. The rubric operationalizes three dimensions of cognitive manipulation risk, each scored 0–2, yielding a composite expert score of 0–6. All labels were assigned by the author (single rater); inter-rater reliability has not been established and constitutes a priority for Phase 2.

The three dimensions are grounded in Cialdini's (1984) principles of influence. The clinical distinction between persuasion and manipulation proposed by Symington (1993) further informs the rubric: manipulation is defined by the systematic denial of the recipient's autonomous evaluative capacity — a criterion directly operationalized in Dimension 2. The verifiability dimension (Dimension 3) draws on media literacy frameworks (Hobbs, 2010).

### A.2 Scoring Dimensions

**Dimension 1: Evidence of Manipulative Intent in Language**

| Score | Criterion |
|---|---|
| 0 | No identifiable linguistic markers of persuasive intent beyond informational presentation |
| 1 | Presence of persuasive framing; some urgency, emotional, or authority markers present but contextualized |
| 2 | Systematic deployment of multiple manipulation categories; markers appear designed to bypass critical evaluation |

**Dimension 2: Impairment of Recipient Autonomy**

| Score | Criterion |
|---|---|
| 0 | Content invites independent verification; sources cited; conclusions presented as provisional |
| 1 | Partial inhibition of critical evaluation; some claims presented as settled without full evidentiary support |
| 2 | Systematic inhibition of independent judgment; urgency, authority, or emotional pressure forecloses evaluation |

**Dimension 3: Verifiability of Claims**

| Score | Criterion |
|---|---|
| 0 | All major claims are verifiable through cited sources or publicly accessible evidence |
| 1 | Some claims lack citation; numerical claims present without source attribution |
| 2 | Core claims are unverifiable by design; anonymous authority, naked numbers, or unfalsifiable assertions |

### A.3 Classification Thresholds

| Expert Score | Risk Label |
|---|---|
| 0–2 | LOW |
| 3–4 | MEDIUM |
| 5–6 | HIGH |

### A.4 Representative Corpus Samples with Rubric Scores

The table below provides rubric scores for six representative documents. Complete corpus labels (62 documents) are available in the project repository at https://github.com/takahiro-oss/r8-cognitive-risk.

| Source | D1 | D2 | D3 | Total | Label |
|---|---|---|---|---|---|
| Ministry of Education PDF | 0 | 0 | 0 | 0 | LOW |
| Kyoko Shimbun (satire) | 1 | 0 | 1 | 2 | LOW |
| Spiritual commercial content | 1 | 1 | 2 | 4 | MEDIUM |
| Micropreneur LP | 1 | 1 | 1 | 3 | MEDIUM |
| FX investment scheme | 2 | 1 | 2 | 5 | HIGH |
| Rakuten diet content | 1 | 1 | 1 | 3 | MEDIUM |

---

## References

Arai, N. (2018). *Robotto wa toudai ni haireruka* [Can a robot get into Tokyo University?]. Toyo Keizai.

Cialdini, R. B. (1984). *Influence: The psychology of persuasion*. Harper Business.

DeVellis, R. F. (2016). *Scale development: Theory and applications* (4th ed.). SAGE Publications.

Du Cluzel, F. (2021). *Cognitive warfare: A battle for the brain*. NATO ACT Innovation Hub. (STO-MP-HFM-334)

Exner, J. E. (1993). *The Rorschach: A comprehensive system* (3rd ed.). Wiley.

Ferrara, E., Varol, O., Davis, C., Menczer, F., & Flammini, A. (2016). The rise of social bots. *Communications of the ACM, 59*(7), 96–104.

Hathaway, S. R., & McKinley, J. C. (1943). *The Minnesota Multiphasic Personality Inventory*. University of Minnesota Press.

Hobbs, R. (2010). *Digital and media literacy: A plan of action*. Aspen Institute.

Janis, I. L. (1972). *Victims of groupthink: A psychological study of foreign-policy decisions and fiascoes*. Houghton Mifflin.

Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux.

Milgram, S. (1963). Behavioral study of obedience. *Journal of Abnormal and Social Psychology, 67*(4), 371–378.

Nakane, C. (1967). *Tate-shakai no ningen kankei* [Human relations in a vertical society]. Kodansha.

National Police Agency. (2025). *Tokushu sagi oyobi SNS-gata toshi/romance sagi no ninchi/kenkyo jokyo-to (Reiwa 6-nen, zantei-chi) ni tsuite* [Special fraud and SNS-type investment/romance fraud: Recognition and arrest statistics for fiscal year 2024 (provisional)]. National Police Agency of Japan.

Symington, N. (1993). *Narcissism: A new theory*. Karnac Books.

Tobe, R., Teramoto, Y., Kamata, S., Suginoo, Y., Murai, T., & Nonaka, I. (1984). *Shippai no honshitsu* [The essence of failure]. Diamond.

Toyama, S. (1983). *Shikou no seirigaku* [Lit. "Physiology of Thinking"; trans. as *The Art of Thought Organization*]. Chikuma Shobo.

United Nations Office on Drugs and Crime. (2023). *Transnational organized crime and the convergence of cyber-enabled fraud, underground banking and technological innovation: A call for collective action in South-East Asia*. UNODC.

Yamamoto, S. (1977). *Kuuki no kenkyuu* [A study of "air"]. Bungeishunju.

---

*This paper was developed with AI assistance (Claude, Anthropic; Gemini, Google). The conceptual framework, theoretical integration, and research direction are the original work of the author. AI tools were used for drafting, translation, and code implementation support.*

*AI使用開示: 本論文はClaude（Anthropic）およびGemini（Google）のAI支援のもとで執筆された。概念的枠組み、理論統合、研究方向性は著者のオリジナルである。AIツールは草稿作成、翻訳、コード実装支援に使用された。*
