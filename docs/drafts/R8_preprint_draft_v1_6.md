# R8 v1.6 論文草稿 - Markdown版（Claudeが直接更新可能）
# 最終更新：2026-04-20
# 注意：このファイルはdocxの正式版と並走する作業用ファイルです
# Claudeが直接更新できます（docxはダウンロードが必要なためこちらを正とする）
# 2026-04-20更新：Section 1末尾追加・Section 2.9拡張（Baumeister&Leary/Brehm/Brock/Cialdini）・Discussion 6.1スクリーニング概念・Future Work 7.2ScarcityRisk・7.4非線形モデル新設・References 6件追加

---

R8: A Lexical Framework for Approximating Cognitive Manipulation Risk in Text

Author: Takahiro Saito, M.S. in Clinical Psychology
Affiliation: Independent Researcher
GitHub: https://github.com/takahiro-oss/r8-cognitive-risk
License: CC BY 4.0
Status: Preprint (not peer-reviewed)
Date: March 2026
Version: v1.6 (preprint draft)

---

## Abstract

R8 proposes a structural approach to approximating cognitive manipulation risk in Japanese-language text across 12 theoretically grounded categories. This is an exploratory framework at an early stage of empirical development; the claims made in this paper are limited to what the current implementation can support. The multi-category scoring architecture draws conceptual inspiration — not methodological equivalence — from factor-based psychometric models such as the MMPI and Rorschach Comprehensive System.

R8 proposes a lexical approximation framework informed by the qualitative analysis of organizational cognitive failure — as documented in studies of military and institutional collapse (Tobe et al., 1984). The theoretical framework integrates Japanese organizational sociology (Yamamoto, 1977; Nakane, 1967) with Western social psychology (Janis, 1972; Milgram, 1963; Kahneman, 2011) and clinical psychology of manipulation (Symington, 1993).

The system produces a single composite score, the Cognitive Manipulation Index (CMI), defined as an approximation of the aggregate linguistic signals associated with manipulation pressure against autonomous thinking. Initial calibration against a 224-document corpus yields an exact match rate of 61% and within-one-level agreement of 92%. These figures reflect author-initiated reclassification of 5 documents; without this intervention, the exact match rate was 51%. Discrepancies are attributable primarily to JavaScript-rendered content limitations, corpus scope, and single-rater annotation bias. The complete corpus and scoring data are publicly available at https://github.com/takahiro-oss/r8-cognitive-risk under CC BY 4.0.

---

## 1. Introduction

The proliferation of digital information has intensified the challenge of distinguishing legitimate communication from cognitive manipulation. Existing approaches to this problem — including fact-checking systems, hate speech detection, and misinformation classifiers — focus primarily on the veracity of content. However, cognitive manipulation operates at a structural level that precedes factual falsity. A message can be factually accurate while simultaneously exploiting psychological vulnerabilities through urgency, false authority, emotional amplification, and logical misdirection.

This structural dimension of manipulation has been examined qualitatively in organizational research. Notably, Tobe et al. (1984) identified the cognitive patterns that preceded Japan's institutional collapse in World War II — including the suppression of disconfirming information, over-reliance on authority, and emotionally-driven decision-making. These patterns were not unique to military organizations; they recur across corporate, political, and media contexts.

R8 (Cognitive Risk Analyzer) proposes a lexical extension of this qualitative tradition. The system operates across 12 risk categories derived from psychometric and clinical psychology frameworks, producing a single composite score: the Cognitive Manipulation Index (CMI). The present paper positions R8 explicitly as an exploratory baseline instrument rather than a validated measurement tool.

A parallel problem emerges from computational linguistics research on machine reading comprehension. Arai (2018) demonstrated that AI systems process text through statistical pattern matching without achieving genuine semantic understanding. This finding is cautionary rather than validating for R8: it highlights the risk that surface-level pattern matching — whether by AI or by lexical tools — may systematically fail to capture meaning. R8 operates within this same constraint.

The present paper describes the theoretical foundation, implementation, and initial calibration of R8 as an open-source lexical auditing framework. Surface-level lexical analysis, while limited in contextual sensitivity, provides a reproducible and transparent baseline for cognitive risk approximation — one that complements rather than replaces deeper semantic analysis.

R8 is designed as a screening tool that approximates the lexical density of manipulation-compatible signals in text. At the current stage of development, the system cannot determine authorial intent, nor does it empirically demonstrate the cognitive effects of detected vocabulary on readers. These constraints arise from the structural limitations of surface-level lexical analysis, detailed in Section 5. Accordingly, the CMI score functions not as a definitive judgment of manipulative intent, but as an initial flag identifying texts that warrant closer scrutiny.

Within these acknowledged limitations, the utility of R8 rests on three properties. First, transparency and reproducibility: the rule-based, dictionary-matching architecture makes the basis for every score fully explicable and manually verifiable. Second, scalability: large volumes of text can be processed consistently against a fixed set of criteria. Third, complementary function: when combined with human judgment and contextual information, R8 serves as a diagnostic aid rather than a replacement for critical evaluation.

Future development directions include the implementation of structural pattern detection (Phase 2 second-layer architecture), false-negative detection through contrastive corpus construction, and extension to multimodal analysis — including audio and video content, made technically feasible by placing a speech-to-text conversion stage (e.g., Whisper) prior to the R8 pipeline. These developments are positioned as research priorities aimed at approximating intent-level assessment, and are detailed in Section 7.

The cognitive difficulty of individual-level defense against manipulation signals is well documented. Cialdini (1984) proposed a two-question verification procedure for authority signals — "Is this person truly an expert?" and "How trustworthy is this expert?" — while simultaneously acknowledging that applying these checks in real time is "nearly impossible" for most individuals (p. 371). Similarly, regarding scarcity-based pressure, Cialdini notes that the emotional arousal generated by scarcity signals actively impairs the deliberative capacity required for self-protection (p. 425). These observations generalize to the broader class of manipulation-compatible signals that R8 targets: the cognitive conditions that make manipulation effective are precisely those that make individual defense unreliable. R8 is designed to address this structural gap by providing pre-interaction text screening — a function that does not depend on the reader's real-time deliberative capacity.

---

## 2. Theoretical Background

### 2.1 From Institutional Failure to Cognitive Manipulation: The "Essence of Failure" Framework

The structural analysis of cognitive failure in organizations has been examined qualitatively in Japanese organizational research. Tobe et al. (1984) identified recurring patterns of institutional collapse in the Japanese military during World War II — patterns that transcend their historical context and recur across corporate, political, and media environments.

Four structural patterns identified by Tobe et al. are directly relevant to R8's design. First, decision-making was dominated by subjective, wishful thinking rather than objective situational assessment — a pattern R8 operationalizes as Emotional Risk. Second, logical argumentation was systematically displaced by hierarchical authority and face-saving behavior — corresponding to R8's Authority Risk and Logical Risk categories. Third, organizations demonstrated a consistent refusal to incorporate disconfirming information, suppressing data that contradicted prevailing assumptions — a pattern detectable through R8's Disclaimer Exploit and Anonymous Authority scores. Fourth, and most critically, organizational decisions were governed not by explicit rules but by an implicit atmospheric consensus.

### 2.2 "Kuuki" and the Vertical Society: Structural Foundations of Cognitive Coercion

This implicit atmospheric consensus was theorized by Yamamoto (1977) as "kuuki" (空気, literally "air") — a form of social pressure that operates below the level of explicit argument, yet determines collective outcomes with greater force than formal reasoning. Kuuki functions as an extra-logical coercive force that paralyzes rational dissent without requiring explicit justification.

The structural foundation that sustains kuuki is identified by Nakane (1967) in her analysis of Japanese vertical society (tate-shakai). In this framework, the credibility of information is determined not by its content but by the hierarchical position of its source. Truth, in effect, is assigned by rank rather than derived through reasoning. R8 operationalizes a proxy for this structural dynamic through its False Authority and Logical Misdirection categories.

### 2.3 The "Glider" Problem: Approximating Cognitive Dependency

The susceptibility of individuals to such manipulation is illuminated by Toyama's (1983) "glider" metaphor, describing cognitive subjects who lack independent reasoning propulsion and rely instead on external information flow for directional guidance. Manipulative texts exploit this dependency through urgency signals and disclaimer exploitation — keeping the subject in a state of passive reception that may prevent the activation of autonomous critical judgment.

R8 is described metaphorically as a "Cognitive Breakwater" (認知的防波堤): the intent is to identify linguistic patterns that may incline a reader toward cognitive dependency rather than deliberation. The CMI is defined not as a direct measure of manipulation, but as an approximation of the density of linguistic signals associated with such pressure.

### 2.4 From "Kuuki" to CMI: A Lexical Approximation of Implicit Coercion

#### 2.4.1 Cross-Cultural Convergence

The structural dynamics described by Tobe et al. (1984), Yamamoto (1977), and Nakane (1967) are not culturally unique to Japan. Western social psychology has independently identified structurally similar phenomena.

Janis (1972) documented similar atmospheric consensus dynamics in Western organizational contexts under the term "Groupthink." Milgram's (1963) obedience experiments demonstrated the cross-cultural tendency toward authority submission. Kahneman (2011) provided the cognitive architecture underlying Toyama's (1983) "glider" metaphor. System 1 thinking — fast, automatic, and effortless — is the cognitive default that manipulative texts may exploit. R8's CMI can be interpreted as an approximation of aggregate System 1 pressure signals in a text.

### 2.5 Psychometric Foundations

R8's multi-category scoring structure draws conceptual inspiration from established psychometric instruments that share a common architectural logic: qualitatively observed psychological phenomena are operationalized as multiple discrete indicators, which are then aggregated into a composite score through weighted combination.

The Minnesota Multiphasic Personality Inventory (MMPI; Hathaway & McKinley, 1943) exemplifies this structure. R8 applies this architectural logic to textual cognitive risk: 12 risk categories function analogously to clinical scales, each capturing a distinct linguistic dimension; the CMI represents the weighted composite. This inspiration is acknowledged explicitly as conceptual only.

### 2.6 Narcissistic Manipulation and Clinical Lexical Patterns

Symington (1993) identified the structural features of narcissistic communication — including the systematic denial of the other's autonomous perspective, the exploitation of emotional dependency, and the use of authority claims to pre-empt critical evaluation. R8's dictionary construction draws on this clinical tradition. The categories of Emotional Risk, Authority Risk, Disclaimer Exploit, and Naked Number reflect patterns recognizable in the clinical literature on manipulative communication.

### 2.7 Information Integrity Context

R8 is positioned as an open-source, transparent instrument for approximating the density of manipulation-compatible linguistic signatures, with the explicit acknowledgment that surface-level lexical patterns do not establish manipulative intent or effect. The relationship between this theoretical framing and the implemented method is examined critically in Section 5.7.

### 2.8 Relationship to Computational Linguistics Approaches

The computational detection of cognitive manipulation and propaganda in text has been addressed through several complementary research traditions.

Da San Martino et al. (2019) proposed a fine-grained propaganda detection framework identifying 18 rhetorical techniques at the fragment level in news articles. Their classification system shares conceptual overlap with R8's 12-category architecture, though the implementation approaches differ substantially: their neural sequence-labeling model achieves fragment-level annotation, while R8 operates through dictionary-based lexical density at the document level. The interpretability trade-off is explicit: R8 sacrifices coverage for auditability.

The MentalManip dataset (Xu et al., ACL 2024) provides a benchmark for manipulation detection in conversational text, reporting that large language models achieve approximately 65% classification accuracy on manipulation judgment tasks. This figure is notable for R8's positioning: if state-of-the-art LLM-based approaches achieve 65% on conversational manipulation, the interpretability and domain-specificity advantages of a rule-based system may justify its lower coverage in specialized deployment contexts where stakeholders require explainable outputs.

Pennebaker et al.'s (2015) LIWC framework established that lexical selection patterns carry measurable psychological signals, providing psycholinguistic grounding for density-based scoring approaches. R8 shares this architectural logic while applying it to manipulation-specific categories derived from clinical psychology and organizational behavior rather than general psychological dimensions.

R8 differs from these approaches in three respects. First, domain specificity: Japanese-language organizational and commercial texts, with theoretical grounding in Japanese organizational sociology. Second, architectural choice: dictionary-based rather than neural, prioritizing interpretability over predictive coverage. Third, theoretical integration: explicit derivation from cross-cultural convergence between Japanese organizational psychology (Tobe et al., 1984; Yamamoto, 1977; Nakane, 1967) and Western social psychology (Janis, 1972; Milgram, 1963; Kahneman, 2011).

Two additional bodies of work provide direct empirical grounding for the manipulation patterns that R8 targets. Ross (2014) identified three structural criteria for cult characterization — absolute authority, coercive persuasion techniques, and exploitative harm — and documented the emergence of online cult dynamics in which manipulation operates exclusively through text, without physical co-presence. This observation grounds R8's focus on digital text as a self-contained manipulation medium. Ben-Ghiat (2020) analyzed the rhetorical strategies of authoritarian political leaders across historical and contemporary contexts, identifying a recurring operational playbook: sustained disinformation campaigns that overwhelm the audience's capacity for factual adjudication (corresponding to R8's PropagandaRisk and EnemyFrame categories), authority signals that bypass deliberative evaluation (AuthorityRisk), and fear-based mobilization that activates threat responses prior to rational processing (FearRisk and AbsolutistWords). The parallel operationalization of cult communication (Ross, 2014) and authoritarian political rhetoric (Ben-Ghiat, 2020) within the same detection framework supports R8's claim to cross-domain applicability — spanning the organizational, commercial, spiritual, and political genres represented in the calibration corpus.

### 2.9 Expectancy-Value Theory and the Functional Manipulation of Reader Goals

Eccles and Wigfield (2002) proposed Expectancy-Value Theory (EVT) as a framework for explaining achievement behavior through two psychological constructs: the individual's expectation of success, and the subjective value assigned to a given task. Subjective value is further decomposed into attainment value (personal importance of succeeding), utility value (instrumental relevance to future goals), intrinsic value (enjoyment derived from the task itself), and cost (psychological and material sacrifice required).

EVT was developed in educational psychology to describe how individuals autonomously form motivational beliefs. The present study identifies a structural inversion of this framework in manipulative text: rather than emerging from autonomous appraisal, EVT variables are externally inflated, concealed, or fabricated through lexical means. Utility value is amplified through fear and urgency signals; attainment value is elevated through authority and exclusivity framing; expectancy for success is manufactured through unverifiable statistical claims; and cost is systematically concealed or redefined as evidence of growth.

R8's 12 risk categories can be mapped onto this functional manipulation structure. EmotionalRisk and FearRisk operate primarily on utility value inflation. AuthorityRisk and PropagandaRisk target attainment value. LogicalRisk and NakedNumber fabricate expectancy. DisclaimerExploit and AbsolutistWords function as cost concealment mechanisms. Critically, intrinsic value manipulation — the use of affirmatively valenced vocabulary (compassion, gratitude, light) to simulate authentic engagement — falls systematically outside the detection scope of the current lexical architecture, constituting the primary source of false negatives documented in Section 5.9.

This mapping does not imply that EVT variable manipulation reflects deliberate authorial design. As documented in Section 5.8, R8 detects lexical patterns that function as EVT variable manipulation — inflating utility value, concealing cost, or fabricating expectancy — independent of whether such manipulation reflects intentional strategy or habitual communication pattern. The distinction between the two cannot be resolved through lexical evidence alone.

The convergence between EVT's motivational architecture and R8's empirically derived category structure was reached through independent analytical paths, providing conceptual support for the theoretical coherence of R8's design. The relationship is presented here as structural correspondence, not as a claim that R8 operationalizes EVT constructs directly.

The motivational foundation underlying EVT variable manipulation is further illuminated by need-to-belong theory. Baumeister and Leary (1995) proposed that the need to belong — to form and maintain stable, positive interpersonal relationships — constitutes a fundamental human motivation with pervasive effects on cognition, emotion, and behavior. Manipulative texts systematically exploit this need through the sequential construction of in-group inclusion and out-group exclusion: establishing similarity and shared identity before introducing enemy framing and exclusivity signals (see Section 3.3, EnemyFrame and PropagandaRisk). This sequential exploitation corresponds structurally to the EVT category of attainment value manipulation — the manufactured sense that belonging to a specific community is personally essential. R8's AuthorityRisk, EnemyFrame, and EmotionalRisk categories function as partial detection proxies for this motivational targeting, though the sequential structure of the exploitation pattern falls outside the scope of lexical density scoring and is identified as a Phase 2 design target (Section 7.2).

A related mechanism operates through psychological reactance. Brehm (1966) demonstrated that perceived threats to behavioral freedom generate motivational pressure to restore that freedom — a response that can be exploited by scarcity signals that frame inaction as loss of opportunity. In manipulative text, scarcity signals (time-limited offers, quantity restrictions, exclusive access framing) trigger reactance-based approach motivation, overriding deliberative evaluation. Brock's (1968) commodity theory formalizes this dynamic: objects become more desirable as their availability decreases, and this effect extends from material goods to information and ideas. Brock further demonstrated that the persuasive power of information increases when access to that information is itself restricted — an effect amplified when both the content and the source are framed as exclusive. These mechanisms underlie the FearRisk and ClickbaitRisk categories in R8's architecture, and provide theoretical grounding for the ScarcityRisk category proposed for Phase 2 development (Section 7.4).

Cialdini (1984) synthesizes these mechanisms in a behavioral framework. Authority signals — titles, credentials, institutional affiliations — trigger automatic compliance responses through the same System 1 pathway that Kahneman (2011) identifies as the default cognitive mode. Critically, Cialdini demonstrates that it is not the actual authority of the source that triggers this response, but the perceived authority conveyed by symbols (p. 349). A fictional television character with a medical role generated the same compliance response as a genuine physician. This finding is directly relevant to R8's design rationale: R8's AnonymousAuthority and AuthorityRisk categories detect the linguistic symbols of authority — titles, endorsements, institutional references — rather than the actual authority of the source, because it is these symbols, not the underlying reality, that function as System 1 activation triggers in readers.

---

## 3. Methodology

### 3.1 System Architecture

R8 operates as a pipeline of three sequential processes: text acquisition, lexical analysis, and score aggregation. Input sources include plain text files, PDF documents, and web URLs. All acquired text is passed to a unified analysis function regardless of source type.

### 3.2 Text Normalization (Phase 1)

Prior to analysis, all input text undergoes normalization to reduce orthographic variation. The normalization pipeline applies Unicode NFKC normalization, followed by katakana-to-hiragana conversion via Unicode codepoint mapping (U+30A1–U+30F3, offset -96).

### 3.3 Operational Definitions of 12 Risk Categories

The 12 categories are derived from clinical psychology, organizational behavior, and rhetorical analysis frameworks. Each category is operationalized as a lexical density measure: the count of matched dictionary terms divided by text length per 100 characters.

**Note on implementation scope:** The implemented system includes 14 scoring dimensions. Two dimensions — Sexual Induction Risk and Beauty/Diet Hype Risk — function as peripheral risk indicators. Sexual Induction Risk carries a weight of 0.04 and is included as a primary scoring dimension. Beauty/Diet Hype Risk carries a weight of 0.00 and functions as a reference-only indicator excluded from CMI calculation. These peripheral dimensions are not included in the theoretical 12-category framework presented in this paper; they represent implementation extensions for applied deployment contexts.

### 3.4 Two-Layer Authority Detection

Authority Risk employs a two-layer detection architecture distinguishing pseudo-authority from legitimate authority reference. Pseudo-authority markers are scored directly as risk indicators. Legitimate authority markers are scored conditionally: their risk contribution is modulated by the concurrent Hype Risk density.

### 3.5 Scoring Algorithm

The Cognitive Manipulation Index (CMI) is computed as a weighted sum of normalized category scores. Category weights reflect the relative contribution of each manipulation dimension to overall cognitive risk, derived through theoretical reasoning and iterative empirical calibration on a small pilot corpus. Statistical Risk carries the highest weight (0.16), reflecting the theoretical manipulative potency of false quantification. CMI ranges from 0 to 100.

Threshold levels for risk classification:
- LOW: CMI < 35
- MEDIUM: 35 ≤ CMI < 60
- HIGH: CMI ≥ 60

### 3.6 Implementation and AI Disclosure

R8 is implemented in Python 3.x as two modules: r8.py (single-document analysis) and mass_audit.py (batch processing). The system requires no machine learning infrastructure, operating entirely through dictionary lookup and regular expression matching. All source code is publicly available under CC BY 4.0 at https://github.com/takahiro-oss/r8-cognitive-risk.

R8's development was conducted with support from large language models (Claude, Anthropic; Gemini, Google). AI support was provided for: code development and optimization, translation between Japanese and English, drafting assistance for sections of this manuscript, and literature summarization and synthesis.

The following decisions and analyses were performed solely by the author: theoretical framework design, selection and operationalization of the 12 risk categories, construction of the Japanese-language lexical dictionaries, calibration of category weights, all substantive research direction and interpretive choices, manual annotation of the calibration corpus, and critical assessment of limitations and implications.

The author holds an M.S. in Clinical Psychology (Aichi Gakuin University, 2012) and brings approximately 20 years of direct experience in Japanese educational settings.

---

## 4. Initial Calibration and Exploratory Testing

### 4.1 Study Design

The present calibration exercise is explicitly preliminary in scope. The calibration corpus comprises 224 documents collected through automated URL-based scraping using the mass_audit.py pipeline, supplemented by manual collection via OCR-based screenshot processing for social media content. Of the 224 documents, a subset returned CMI scores of 0.0 due to JavaScript-rendered content inaccessibility — a structural limitation documented in Section 5.4.

Ground truth classification was determined through single-rater expert judgment by the author, drawing on clinical psychology training and 20 years of educational practice. A structured rubric was applied (see Appendix A). The use of the system's author as the sole annotator constitutes a significant source of bias that cannot be quantified at this scale.

### 4.2 Corpus Description

The 224-document corpus spans the following distribution: HIGH-risk documents (n=4, CMI ≥ 60), MEDIUM-risk documents (n=75, 35 ≤ CMI < 60), and LOW-risk documents (n=145, CMI < 35). This distribution reflects the structural finding that the current lexical architecture achieves HIGH classification primarily for political and conspiracy-theory content combining simultaneous EnemyFrame, Propaganda, and FearRisk activation.

Genre distribution includes: governmental and institutional documents (LOW baseline), commercial manipulation content (investment schemes, MLM, diet/health products), spiritual and pseudoscientific content, political party media (domestic and international state-affiliated outlets), cult and religious organization content, legal information accounts, and financial advisory content.

### 4.3 Results

CMI scores were obtained across the full 224-document corpus. Summary statistics are reported for documents with valid CMI scores (CMI > 0).

Exact match rate (automated vs. expert label): 61% across the Phase 1 corpus. Agreement within one risk level: 92%. These figures reflect author-initiated reclassification of documents where structural evidence of manipulation-compatible patterns was present despite LOW automated scores; without this intervention the exact match rate was 51%. A blind evaluation conducted on three representative documents (corpus ID: web203, note164, web193) revealed divergence in two of three cases (66.7%), confirming systematic limitations documented in Sections 5.9 and 5.10.

### 4.4 Analysis of Discrepancies

Three categories of discrepancy were identified.

The first concerns text acquisition limitations. Documents returned CMI=0.0 due to JavaScript-rendered dynamic content that BeautifulSoup-based scraping cannot access.

The second concerns scalar underdetection of politically framed content. State-affiliated international outlets and domestic political party media exhibited Enemy Frame and Fear Risk activation at maximum density while returning LOW scalar CMI scores. This reflects a systematic limitation of the current scalar aggregation architecture.

The third concerns satirical mimicry. Satirical content (虚構新聞) that intentionally mimics manipulative news structure registers elevated CMI scores relative to expert LOW classification.

### 4.5 Implications for Dictionary Calibration

The preliminary results indicate that R8's current lexical dictionary is sensitive to commercially framed manipulation but requires expansion to capture anecdotal manipulation, spiritually framed authority, and satirical mimicry.

---

## 5. Current Limitations

### 5.1 Surface-Level Lexical Matching

The current implementation relies exclusively on surface-level lexical matching and does not account for contextual disambiguation, linguistic variation, or discourse-level manipulation structures. Three specific consequences follow from this design choice. First, the system cannot distinguish between identical surface forms that carry different semantic functions depending on context. Second, paraphrase and lexical substitution allow manipulation-compatible content to evade detection entirely. Third, the scoring architecture measures lexical density across the entire document, which means locally concentrated high-severity signals are systematically diluted in long-form texts (see Section 5.10 for empirical demonstration).

The false-positive and false-negative implications of these constraints have been empirically observed in the calibration corpus. The author's own analytical essays (corpus ID: note219–note228) provide a documented case of false-positive risk: critical writing about AI manipulation produced CMI scores in the MEDIUM range due to argumentative prose structures activating the same categorical signals as genuinely manipulative texts.

These limitations are not resolvable through dictionary expansion alone. The ceiling of lexical-only detection has been empirically mapped through iterative dictionary development from version 10 to version 16.

### 5.2 Language Scope

The current implementation is Japanese-language specific. All dictionaries, normalization procedures, and validation corpora are constructed for Japanese text, and the theoretical framework draws substantially on Japanese organizational sociology and cultural psychology.

This constraint reflects a deliberate scoping decision rather than a technical limitation. Japanese-language manipulation patterns exhibit structural features that differ systematically from English-language counterparts. Extension to other East Asian languages sharing Confucian organizational frameworks (Korean, Mandarin Chinese) represents a more proximate research direction than English extension.

### 5.3 Calibration Corpus Limitations

The present calibration corpus is insufficient for definitive statistical inference. The use of the system's author as the sole annotator constitutes a significant source of bias. To partially assess the validity of the annotation process, a blind evaluation was conducted on three representative documents: web203 (HIGH, confirmed), note164 (divergence: automated MEDIUM / expert HIGH), and web193 (divergence: automated LOW / expert MEDIUM). Of these three, two (66.7%) showed divergence between automated and expert classification.

Furthermore, the corpus includes documents authored by the present author (corpus ID: note219–note228), a series of critical essays examining AI sycophancy. These documents produced CMI scores in the LOW–MEDIUM range (22.4–50.5) despite the absence of manipulative intent on the author's part. These documents are retained in the corpus as documented instances of intent-unresolved classification, with human_label recorded as MEDIUM and riskfactor noted as intent-unresolved.

Phase 2 will prioritize annotation standard consolidation before expanding the annotator pool to a minimum of two independent raters with Cohen's kappa as the reliability metric. Inter-rater reliability will be reported using Cohen's kappa (κ), calculated as:

κ = (P_o − P_e) / (1 − P_e)

where P_o denotes the observed proportion of agreement and P_e denotes the proportion of agreement expected by chance. A minimum threshold of κ ≥ 0.60 is adopted as the criterion for acceptable reliability, consistent with the benchmark established by Landis and Koch (1977), who characterized κ values of 0.41–0.60 as moderate, 0.61–0.80 as substantial, and 0.81–1.00 as almost perfect. The current Phase 1 corpus provides no inter-rater κ estimate, as all annotations were performed by the single author; this absence is disclosed as a limitation rather than concealed.

### 5.4 Digital Media Application Constraints

The application of URL-based lexical analysis to digital media faces a hierarchy of structural constraints. At the technical level, a significant proportion of high-risk web content employs JavaScript rendering that prevents direct HTML extraction. Direct URL scanning consistently underperforms text-converted scanning by a substantial margin (CMI 10.0 vs 44.7 confirmed on identical pages).

Beyond the JavaScript problem, a more fundamental constraint emerges from the structural characteristics of social media content. Short-form posts on platforms such as X (formerly Twitter) present a categorically different challenge. During calibration, five posts (corpus ID: sn229–sn233) were scanned via OCR pipeline. All produced CMI LOW despite containing vocabulary consistent with EnemyFrame and Propaganda categories. Two failure modes were identified: density calculation failure for 140–280 character texts, and OCR-induced character-level misreads breaking dictionary matching.

The most fundamental limitation is epistemological. Fact-based disinformation — claims such as "the suspect's father holds Chinese citizenship" — cannot be evaluated through lexical analysis alone. This reflects a categorical boundary between lexical pattern detection and factual verification.

Phase 2 design priorities include dynamic threshold adjustment based on text length (short-text mode) and thread-level aggregation enabling multi-post integration before scoring.

### 5.5 Dictionary Construction Methodology

The current lexical dictionaries were constructed through theoretical reasoning and expert judgment rather than corpus-based induction. The iterative development process from version 10 to version 16 of the R8 dictionary expanded detection coverage for specific genres (spiritual/pseudoscience content in v11–13, political conspiracy content in v14–15, deletion-threat urgency patterns in v16). However, this expansion process has a structural ceiling: the most sophisticated manipulation content remained in the MEDIUM range regardless of dictionary expansion, because the manipulation operates through vocabulary that does not appear in any risk category.

This iterative expansion process introduces the risk of circular validation. Dictionary expansion is therefore reframed not as a precision improvement strategy but as documentation of the lexical detection ceiling before transition to transformer-based contextual analysis. Version 16 represents the current boundary of what surface-level lexical matching can achieve for the genres represented in the calibration corpus.

### 5.7 The Gap Between Theoretical Framing and Implemented Method

A structural limitation that underlies all others in this paper deserves explicit statement. The theoretical framework presented in Section 2 draws on cognitive psychology (Kahneman, 2011), social psychology (Janis, 1972; Milgram, 1974; Zimbardo, 2007), and Japanese organizational sociology (Nakane, 1967; Yamamoto, 1977) to characterize cognitive manipulation as a multi-level phenomenon. R8 is theoretically positioned as a detection system for linguistic signals targeting System 1 cognitive processing (Kahneman, 2011).

The implemented method — surface-level lexical density analysis — operates at a categorically different level of description. No amount of dictionary expansion will bridge the gap between counting words and measuring cognitive effects.

What the gap does require is explicit restraint in theoretical claims. The paper presents R8 as a lexical screening tool that approximates manipulation-compatible signal density, not as a direct measure of cognitive manipulation. The theoretical framing in Section 2 should be read as motivating the category design and providing interpretive context, not as a claim that CMI scores measure the theoretical constructs directly. This distinction is particularly salient for the limitations documented in Sections 5.8 through 5.11.

### 5.8 Authorial Intent and the Limits of Lexical Inference

The present system analyzes the linguistic structure of texts but cannot determine the intentional state of the author reflected in that structure. The high-density occurrence of manipulation-compatible vocabulary may reflect deliberate cognitive manipulation design, the author's own sincere beliefs expressed through habitual language, or any combination of the two.

Symington (1993) describes cases in which narcissistically structured communicators are themselves unaware of the manipulative architecture of their speech. Festinger's (1957) cognitive dissonance theory illuminates a parallel mechanism. The present study has no means of empirically distinguishing these three types (intentional, unconscious, and mixed), and CMI scores therefore carry no implication about the author's cognitive state or ethical status.

In the calibration corpus, a legal information note account (corpus ID: note164–note179, 15 valid documents) reproduced the stereotyped sequence of fear induction, authority presentation, logical justification, and action induction across all articles — instantiating what the present study terms a two-stage cognitive induction architecture. This structure may represent intentional design or habitual communication pattern; text analysis alone cannot resolve the distinction.

### 5.9 Surface-Positive Vocabulary and Systematic False Negatives

The most structurally significant detection limitation identified in Phase 1 calibration is the systematic underdetection of texts employing affirmatively valenced vocabulary as a manipulation medium.

Cult-affiliated and spiritual texts in the calibration corpus (corpus ID: web138–web197, relevant subset) were classified as MEDIUM-equivalent by the expert evaluator but produced CMI scores consistently in the LOW range. These texts share a characteristic vocabulary profile: high-density use of terms such as "compassion," "love," "light," "walking together," and "gratitude" — surface-positive expressions that appear in none of R8's 12 risk categories.

The author's own analytical essays (corpus ID: note219–note228) provide a particularly clear illustration. Critical analyses of AI sycophancy produced CMI scores between 22.4 and 50.5 despite explicit analytic intent. The author cannot themselves determine with certainty whether implicit rhetorical intent is entirely absent, instantiating Section 5.8's fundamental problem.

Distinguishing authentic positive communication from manipulation-mediated positive vocabulary requires three analytical layers: statistical extraction of co-occurrence patterns between positive vocabulary and action-induction language (PMI analysis); inductive sequence analysis reconstructing the communicative destination from the final paragraph backward; and contrastive corpus comparison against authentic positive text baselines. These constitute Phase 2 research priorities.

A structurally distinct false-negative pattern concerns the visual and multimodal dimensions of authority construction. Cialdini (1984) demonstrated that authority compliance is triggered not by the genuine credentials of a source but by the perceived authority conveyed by symbols — titles, attire, institutional affiliations, and the visual presentation of expertise (p. 349). In digital text environments, these authority symbols are instantiated not through vocabulary but through visual elements: profile photographs conveying professional appearance, display of academic credentials or certifications as images, institutional logos, and the visual design language of high-production-value websites. R8 operates exclusively on extracted text and therefore cannot detect any of these visual authority signals. A text that functions as high-risk authority-based manipulation through visual cues may register near-zero AuthorityRisk and AnonymousAuthority scores if the verbal content is stripped of explicit authority vocabulary. This represents a categorical detection boundary rather than a calibration limitation: no expansion of the lexical dictionary can address signals that are not encoded in text. Phase 2 corpus design will include human annotation of visual authority signal presence as a supplementary dimension to enable systematic documentation of this false-negative class.

### 5.10 Lexical Density and Qualitative Severity: An Empirical Demonstration

The density-based scoring architecture measures the quantitative distribution of manipulation-compatible signals but does not reflect the qualitative severity of individual lexical items.

A legal information note account (corpus ID: note164) contains explicit threatening expressions including references to criminal extortion law. Despite expert classification as HIGH-equivalent in blind evaluation, the system returned CMI 52.1, MEDIUM classification. Threatening vocabulary was concentrated in the first 2,000 characters, producing a local density of 1.81 per 100 characters. Calculated across the full text of 8,500 characters, density fell to 0.094 per 100 characters — below the FearRisk activation threshold.

In contrast, web203 (CMI 61.4, HIGH) distributed fear-relevant vocabulary across its full 6,043-character text, yielding a global density of 0.149 per 100 characters sufficient to activate the HIGH threshold. The comparison demonstrates that the scoring architecture systematically underestimates locally concentrated high-severity signals in long-form texts.

This dilution effect may correspond to a structural property of certain manipulation architectures — consistent with Kahneman's (2011) System 1 activation followed by System 2 rationalization. Whether this sequential structure reflects deliberate design or habitual communication pattern cannot be determined from textual evidence alone (see Section 5.8).

Possible architectural responses include maximum-value scoring or severity-weighted threshold calibration for specific categories. Both approaches introduce increased false-positive risk whose magnitude remains unquantified. These are documented as Phase 2 architectural investigation priorities.

### 5.11 Short-Form Text Application Constraints

The density-based scoring architecture was designed for medium-to-long-form texts and exhibits structural detection failure for short-form social media content.

During Phase 1 calibration, five posts related to a child homicide case on X (formerly Twitter) (corpus ID: sn229–sn233) were scanned via an OCR-based pipeline. All five produced CMI LOW despite containing vocabulary consistent with EnemyFrame and Propaganda categories. Two failure modes were identified: density calculation failure for 140–280 character texts, and OCR-induced character-level misreads breaking dictionary matching.

The most fundamental limitation is epistemological. Fact-based disinformation — specific factual claims whose falsity cannot be assessed through lexical analysis — falls categorically outside the detection scope of the current system. This marks a categorical boundary between lexical pattern detection and factual verification, not resolvable through dictionary expansion.

Phase 2 architectural responses include dynamic threshold adjustment calibrated to text length (short-text mode), thread-level aggregation processing multiple posts as a unified document before scoring, and hashtag pattern analysis as a supplementary signal channel.

---

## 6. Discussion

### 6.1 R8 as a Screening Tool: Utility and Acknowledged Limitations

R8 is explicitly positioned not as a definitive classifier of manipulative intent, but as an initial flag that complements rather than replaces human judgment. The system's utility rests on three properties: transparency and reproducibility, scalability, and complementary function.

This positioning is analogous to medical blood testing: blood tests do not definitively diagnose disease but identify abnormal values requiring closer examination. R8 detects "signs requiring scrutiny" in text; it does not determine manipulative intent. Explicit disclosure of this limitation is essential for preventing misuse of the instrument.

The corpus distribution observed in Phase 1 calibration — LOW: 64.7%, MEDIUM: 33.5%, HIGH: 1.8% — should be interpreted within this screening framework rather than as evidence of low detection power. A first-stage screening instrument is designed to efficiently exclude low-risk documents from further analysis while directing resources toward documents requiring closer scrutiny. The Phase 1 distribution indicates that R8 successfully identifies a manageable subset of documents (35.3%) as requiring attention, while clearing the majority (64.7%) as below the threshold for further investigation. The LOW classification does not assert absence of manipulation; it asserts that the lexical signal density does not reach the threshold justifying escalation. This distinction is central to the multi-stage detection architecture described in Section 7.4, in which Phase 1 lexical screening functions as a first filter, with subsequent analytical layers — co-occurrence pattern analysis, paragraph-sequence detection, and goal-convergence scoring — applied to the non-cleared subset.

### 6.2 CMI Scores and Category Vector Profiles

A key finding of Phase 1 calibration is that the 12-category vector profile is diagnostically superior to the scalar CMI value. Political and conspiracy-theory texts reached HIGH classification through simultaneous elevation of EnemyFrame, Propaganda, and FearRisk — a pattern structurally consistent with Janis's (1972) groupthink symptom profile. Charismatic entrepreneur texts produced LogicalRisk 1.0 while remaining below HIGH overall.

Category vector profile analysis can visualize differences invisible to scalar scores. FearRisk elevation in isolation suggests fear-induction manipulation; Authority combined with Hype suggests pseudo-authority exploitation.

### 6.3 Surface-Positive Vocabulary and the False-Negative Problem

The most important structural finding of Phase 1 calibration is the systematic false-negative pattern for texts using affirmatively valenced vocabulary as a manipulation medium (Section 5.9). The finding is not resolvable through dictionary expansion.

The author's own analytical essays (corpus ID: note219–note228) illustrate this problem. Critical writing about AI sycophancy produced CMI MEDIUM scores, with the author unable to determine with certainty whether implicit rhetorical intent is entirely absent. Phase 2 priority: construction of a contrastive corpus pairing authentic positive texts with manipulation-mediated positive texts to enable false-negative detection.

### 6.4 Short-Form Social Media Content

Phase 1 calibration confirmed that X (formerly Twitter) posts present a structurally distinct challenge for density-based scoring (Section 5.11). The scoring architecture is not suited for texts of 140–280 characters, and fact-based disinformation falls categorically outside lexical detection scope. Phase 2 architectural design priorities: dynamic threshold adjustment (short-text mode) and thread-level aggregation.

### 6.5 Circular Validity and the Need for Independent Validation

The most critical methodological constraint of this study is the circular structure in which the system designer serves as sole evaluator. Dictionary design, threshold calibration, and human_label assignment were all performed by the same individual, with no independent external validation.

Phase 2 establishes annotation standard consolidation and a minimum of two independent raters with Cohen's kappa reliability measurement as necessary conditions before corpus expansion.

---

## 7. Future Work

The development roadmap is structured in two phases. Phase 2 addresses the empirical foundations required before the current framework can support stronger claims. Phase 3 work is not planned to begin until Phase 2 has produced an independently annotated corpus of at least 200 documents with documented inter-rater reliability (Cohen's kappa ≥ 0.6) and a CMI-to-annotation agreement rate of at least 65% exact match on the independent corpus.

### 7.1 Phase 2: Validation Corpus Expansion and Inter-Rater Reliability

Expansion of the calibration corpus and establishment of inter-rater reliability are the immediate empirical priorities. The Phase 2 corpus design will address current limitations through: (1) manual collection of HIGH-risk documents where automated collection fails due to JavaScript rendering; (2) addition of a contrastive corpus of authentic positive texts (administrative documents, medical informed consent forms); (3) inclusion of social media content (SNS); (4) independent annotation by a minimum of two raters with Cohen's kappa measurement (κ ≥ 0.60; Landis & Koch, 1977). The κ threshold of 0.60 is adopted as the minimum criterion for acceptable reliability before corpus expansion proceeds. Inter-rater training and annotation protocols will be standardized in advance of the Phase 2 annotation cycle.

### 7.2 Phase 2: Vector Profile Development and Structural Pattern Detection

Phase 2 will investigate whether vector distance measures provide more discriminative power than scalar aggregation for politically framed content. The second-layer detection architecture will target structural manipulation patterns: self-achievement-to-recommendation induction, agreement-seeking sentence-final repetition, numerical chains, scarcity/urgency presentation, and problem-raising-to-self-as-solver. Theoretical basis: Cialdini (1984), Milgram (1974), Janis (1972).

Additionally, EVT variables not currently covered by R8's lexical architecture — specifically Self-schema manipulation ("discover your true self") and Personal goal targeting ("what is your dream?") — represent structural targets for the second detection layer. These patterns correspond to the paragraph-level sequencing identified in Section 2.9 and align with Cialdini's (1984) commitment and consistency mechanisms. Detecting Self-schema and Personal goal manipulation requires structural pattern recognition beyond the scope of surface lexical density, and is positioned as a Phase 2 design priority.

Phase 2 will also investigate the independent operationalization of scarcity signals as a dedicated detection category (ScarcityRisk). In the current implementation, scarcity-compatible vocabulary is distributed across FearRisk, AbsolutistWords, and ClickbaitRisk without a unified detection architecture. Brock's (1968) commodity theory and Brehm's (1966) psychological reactance theory provide the theoretical basis for treating scarcity signaling as a structurally distinct manipulation mechanism warranting independent detection. Five lexical sub-types are proposed for ScarcityRisk operationalization: temporal scarcity ("today only," "deadline"), quantitative scarcity ("only 3 remaining," "limited to 50"), informational scarcity ("what only a few know," "not publicly available"), relational scarcity ("exclusively for you," "specially selected"), and opportunity scarcity ("this chance will never come again"). Critically, Phase 1 calibration observations indicate that these sub-types rarely appear in isolation in high-risk texts; rather, they co-occur in combination patterns that produce amplified persuasive effects beyond what linear score aggregation captures (Fromkin & Brock, 1971). Phase 2 will investigate weighted co-occurrence scoring for ScarcityRisk sub-type combinations as an approach to approximating these interaction effects within the current lexical architecture.

### 7.3 Phase 2: Transformer-Based Contextual Analysis

Following corpus expansion and reliability establishment, integration of transformer-based language models for contextual disambiguation is identified as a significant development direction. This development is framed as complementary rather than replacement.

### 7.4 Phase 2–3: Toward a Non-Linear Detection Model and Multi-Stage Architecture

The current CMI is computed as a linear weighted sum of lexical category scores. This architecture assumes that the persuasive risk contribution of each signal type is additive and independent — an assumption that Phase 1 observations suggest is empirically incomplete.

Two non-linear effects are identified as Phase 2–3 research priorities. The first is the interaction effect between positive and negative valence signals. Phase 1 calibration observations suggest that texts combining high-density affirmatively valenced vocabulary (EmotionalRisk) with high-density negatively valenced vocabulary (FearRisk) in alternating or sandwich structures may produce persuasive effects that exceed the prediction of linear score aggregation. The cognitive mechanism is consistent with Kahneman's (2011) negativity dominance finding: negative signals are processed with higher priority than positive signals of equivalent magnitude, so sequential positive-then-negative structures do not cancel but amplify — the positive content elevates anticipated value while the subsequent negative content activates loss aversion at the elevated baseline. The linear model cannot capture this multiplicative structure.

The second is the threshold effect in multi-signal combinations. Phase 1 calibration observations are consistent with the hypothesis that manipulation-compatible signals do not produce proportional effects across their full range, but rather exhibit threshold behavior: below a signal density threshold, effects are sub-linear (weak or absent); above the threshold, effects become supra-linear (rapidly amplifying). This structure is theoretically grounded in Granovetter's (1978) threshold model of collective behavior, which demonstrates that individual response thresholds determine when and whether cascades of behavior propagate through a population. Applied to text-based manipulation, the threshold model predicts that: (1) individual readers have personal response thresholds determined by cognitive vulnerability; (2) CMI scores below a reader's threshold produce minimal compliance effects regardless of absolute score magnitude; and (3) CMI scores that cross the threshold trigger disproportionately amplified responses, consistent with the phase-transition structure of collective behavior cascades.

A candidate mathematical formalization of this threshold structure is the sigmoidal transformation:

CMI_nonlinear = 1 / (1 + e^(−k(CMI_linear − θ)))

where θ represents the individual response threshold and k represents the slope parameter governing the steepness of the transition. This formalization is proposed as a theoretical framework for Phase 3 empirical investigation. The current corpus of 224 documents with single-rater annotation is insufficient to estimate the parameters θ and k, and the absence of behavioral outcome measures (compliance rates, financial losses, recruitment success) makes empirical validation of the threshold model impossible at this stage. The proposal is presented as a research direction rather than an implemented component.

The multi-stage detection architecture that follows from this theoretical framework is structured as follows. Phase 1 lexical screening (current implementation) functions as a first-stage filter, efficiently excluding documents with CMI below 35 from further processing while directing MEDIUM and HIGH documents — and LOW documents with specific co-occurrence patterns — to second-stage analysis. Phase 2 structural detection applies co-occurrence pattern weighting, paragraph-sequence analysis, and ScarcityRisk combination scoring to the non-cleared subset. Phase 3 contextual and behavioral modeling integrates transformer-based disambiguation, reader vulnerability profiling, and empirical threshold estimation where behavioral outcome data become available. This staged architecture is designed to maximize detection utility at each phase while maintaining transparency about the limitations of each analytical layer.

The threshold model introduced above also provides the conceptual foundation for a complementary construct: the Cognitive Vulnerability Index (CVI). While CMI quantifies the manipulation-compatible signal density of a text — a property of the sender — CVI would quantify the cognitive vulnerability of the reader as the threshold parameter θ that determines when CMI signals produce behavioral effects. The theoretical basis for CVI derives directly from Cialdini's (1984) empirical observation that susceptibility to consistency-based persuasion increases with age (p. 177), Milgram's (1974) documentation of authority submission as an individual-difference variable, and Altemeyer's (1981) Right-Wing Authoritarianism scale, which identifies dispositional tendencies toward authority deference, conventionalism, and out-group hostility as measurable individual differences that correspond structurally to R8's AuthorityRisk, AbsolutistWords, and EnemyFrame categories. A full CVI operationalization is beyond the scope of the current research; it is proposed here as a Phase 3 theoretical target whose development depends on Phase 2 empirical foundations.

A further theoretical extension concerns the directionality of manipulation vectors. The current R8 architecture treats texts as directed at an external audience — what may be termed an outward manipulation vector. However, organizational and institutional texts often function simultaneously across multiple audience dimensions: externally toward the public or media, internally toward organizational members, and reflexively toward the text's author as a mechanism of self-justification. Festinger's (1957) cognitive dissonance theory predicts that inward-directed manipulation — the rhetorical reinforcement of an organization's own normative framework in the face of contradictory evidence — intensifies rather than resolves when external pressure increases. Empirical candidates for this inward-vector pattern include government crisis-response texts, corporate incident communications, and institutional denial statements, which Phase 1 calibration identified as a systematic false-negative category: high human-label risk but low automated CMI, attributed to the absence of cult- or commercial-genre vocabulary in bureaucratic register. Operationalizing vector directionality — distinguishing outward persuasion from inward self-legitimation — is identified as a Phase 2 corpus design priority and a Phase 3 modeling target.

### 7.5 Phase 3: Multilingual Extension

Extension to English-language analysis is a potential direction pending Phase 2 validation outcomes.

### 7.6 Phase 3: AI-Generated Text Analysis

A longer-term research direction extends R8's framework to the analysis of AI-generated communication. Whether R8's lexical categories are sensitive to sycophantic bias patterns in AI-generated text is an open empirical question that cannot be meaningfully investigated until the framework's validity on human-authored text has been established in Phase 2.

### 7.7 Phase 3: Multimodal Extension

Extension to audio and video content is technically feasible by placing a speech-to-text conversion stage (e.g., Whisper) prior to the R8 pipeline. Theoretical grounding: Janis (1972) p289-290, documenting that defective decision-making patterns manifest in leaders' public statements.

---

## 8. Conclusion

R8 presents a first-generation lexical framework for approximating cognitive manipulation risk in Japanese-language text. By operationalizing 12 theoretically grounded risk categories into a single composite index — the Cognitive Manipulation Index (CMI) — the system provides a transparent, reproducible, and scalable screening tool for identifying texts that warrant closer scrutiny. The system is explicitly positioned not as a definitive classifier of manipulative intent, but as an initial flag that complements rather than replaces human judgment.

The theoretical framing of R8 integrates cognitive psychology (Kahneman, 2011), social psychology (Janis, 1972; Milgram, 1974; Zimbardo, 2007), Japanese organizational sociology (Tobe et al., 1984; Yamamoto, 1977; Nakane, 1967), and clinical psychology of manipulation (Symington, 1993). The novel contribution of this research lies in integrating these previously disconnected theoretical domains under the unified lens of "linguistic signals targeting System 1 cognitive processing," and operationalizing this integration as a quantifiable lexical instrument for Japanese text.

Phase 1 calibration identified three principal findings. First, CMI achieves its highest detection performance for politically framed content combining EnemyFrame, Propaganda, and FearRisk simultaneously. Second, commercial manipulation content systematically evades HIGH classification through surface-positive vocabulary, establishing the central diagnostic finding of Phase 1. Third, calibration confirmed that lexical density scoring produces systematic false negatives for sophisticated manipulation and systematic false positives for argumentative analytical prose, establishing the empirical ceiling of the lexical-only approach.

The limitations of the current implementation are substantial and explicitly acknowledged. These limitations define the Phase 2 research agenda: validated corpus expansion with independent inter-rater annotation; development of a second detection layer targeting structural manipulation patterns; and construction of a contrastive corpus enabling false-negative detection.

R8 is released as open-source software with the explicit acknowledgment that it is a first approximation. The value of this release lies in establishing a transparent, reproducible baseline — one that documents the ceiling of lexical detection before the transition to structural and semantic analysis, and that positions Japanese-language cognitive manipulation research within the broader international conversation on computational detection of persuasive and deceptive text.

---

## References

Altemeyer, B. (1981). Right-wing authoritarianism. University of Manitoba Press.

Arai, N. (2018). Robotto wa toudai ni haireruka [Can a robot get into Tokyo University?]. Toyo Keizai.

Baumeister, R. F., & Leary, M. R. (1995). The need to belong: Desire for interpersonal attachments as a fundamental human motivation. Psychological Bulletin, 117(3), 497–529.

Brehm, J. W. (1966). A theory of psychological reactance. Academic Press.

Brock, T. C. (1968). Implications of commodity theory for value change. In A. G. Greenwald, T. C. Brock, & T. M. Ostrom (Eds.), Psychological foundations of attitudes (pp. 243–275). Academic Press.

Cialdini, R. B. (1984). Influence: The psychology of persuasion. Harper Business.

DeVellis, R. F. (2016). Scale development: Theory and applications (4th ed.). SAGE Publications.

Eccles, J. S., & Wigfield, A. (2002). Motivational beliefs, values, and goals. Annual Review of Psychology, 53, 109–132.

Exner, J. E. (1993). The Rorschach: A comprehensive system (3rd ed.). Wiley.

Festinger, L. (1957). A theory of cognitive dissonance. Stanford University Press.

Fromkin, H. L., & Brock, T. C. (1971). A commodity theory analysis of persuasion. Public Opinion Quarterly, 35(3), 367–377.

Granovetter, M. (1978). Threshold models of collective behavior. American Journal of Sociology, 83(6), 1420–1443.

Granovetter, M., & Soong, R. (1983). Threshold models of diffusion and collective behavior. Journal of Mathematical Sociology, 9(3), 165–179.

Hathaway, S. R., & McKinley, J. C. (1943). The Minnesota Multiphasic Personality Inventory. University of Minnesota Press.

Hobbs, R. (2010). Digital and media literacy: A plan of action. Aspen Institute.

Janis, I. L. (1972). Victims of groupthink: A psychological study of foreign-policy decisions and fiascoes. Houghton Mifflin.

Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus and Giroux.

Milgram, S. (1963). Behavioral study of obedience. Journal of Abnormal and Social Psychology, 67(4), 371–378.

Milgram, S. (1974). Obedience to authority: An experimental view. Harper & Row.

Nakane, C. (1967). Tate-shakai no ningen kankei [Human relations in a vertical society]. Kodansha.

National Police Agency. (2025). Tokushu sagi oyobi SNS-gata toshi/romance sagi no ninchi/kenkyo jokyo-to (Reiwa 6-nen, zantei-chi) ni tsuite. National Police Agency of Japan.

Ross, R. A. (2014). Cults inside out: How people get in and can get out. CreateSpace.

Symington, N. (1993). Narcissism: A new theory. Karnac Books.

Tobe, R., Teramoto, Y., Kamata, S., Suginoo, Y., Murai, T., & Nonaka, I. (1984). Shippai no honshitsu [The essence of failure]. Diamond.

Toyama, S. (1983). Shikou no seirigaku. Chikuma Shobo.

Yamamoto, S. (1977). Kuuki no kenkyuu [A study of "air"]. Bungeishunju.

Zimbardo, P. G. (2007). The Lucifer effect: Understanding how good people turn evil. Random House.

Baly, R., Karadzhov, G., Alexandrov, D., Glass, J., & Nakov, P. (2018). Predicting factuality of reporting and bias of news media sources. EMNLP 2018, 3528–3539.

Ben-Ghiat, R. (2020). Strongmen: Mussolini to the present. W. W. Norton.

Chakraborty, A., Paranjape, B., Kakarla, S., & Ganguly, N. (2016). Stop clickbait: Detecting and preventing clickbait in online news media. ASONAM 2016, 9–16.

Da San Martino, G., Yu, S., Barrón-Cedeño, A., Petrov, R., & Nakov, P. (2019). Fine-grained analysis of propaganda in news articles. EMNLP 2019, 5636–5646.

Da San Martino, G., Barrón-Cedeño, A., Wachsmuth, H., Petrov, R., & Nakov, P. (2020). SemEval-2020 task 11: Detection of propaganda techniques in news articles. SemEval 2020, 1377–1414.

Douglas, K. M., Sutton, R. M., & Cichocka, A. (2017). The psychology of conspiracy theories. Current Directions in Psychological Science, 26(6), 538–542.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33(1), 159–174.

Lazer, D. M. J., et al. (2018). The science of fake news. Science, 359(6380), 1094–1096.

Pennebaker, J. W., Boyd, R. L., Jordan, K., & Blackburn, K. (2015). The development and psychometric properties of LIWC2015. University of Texas at Austin.

Pennycook, G., & Rand, D. G. (2019). Fighting misinformation on social media using crowdsourced judgments of news source quality. PNAS, 116(7), 2521–2526.

Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. Science, 359(6380), 1146–1151.

Woolley, S. C., & Howard, P. N. (Eds.). (2018). Computational propaganda. Oxford University Press.

---

## AI Disclosure

This paper was developed with AI assistance (Claude, Anthropic; Gemini, Google). The conceptual framework, theoretical integration, and research direction are the original work of the author. AI tools were used for drafting, translation, and code implementation support.

本論文はClaude（Anthropic）およびGemini（Google）のAI支援のもとで執筆された。概念的枠組み、理論統合、研究方向性は著者のオリジナルである。AIツールは草稿作成、翻訳、コード実装支援に使用された。

---

## 更新履歴
- 2026-04-15: v1.6草稿開始。5.8〜5.11新規追加。Discussion・Conclusion全面改訂。
- 2026-04-16: Section 1追記。2.8英語化。投稿戦略確定（PLOS ONE第一候補）。
- 2026-04-17: Section 4数値更新（62件→224件）。2.8英語化完了。14カテゴリ問題の記述追加（3.3節）。mdファイル形式での管理開始。
- 2026-04-18: Section 2.9新規追加（EVT接続・Eccles & Wigfield 2002）。7.2末尾にSelf-schema・Personal goals追記。References追加。
- 2026-04-20: Section 2.8末尾にRoss(2014)・Ben-Ghiat(2020)追加。Limitation 5.3にκ計算式・基準値追加（Landis & Koch 1977）。Future Work 7.1にκ基準値追記。Future Work 7.4末尾にCVI・CMI×CVIモデル・内向きベクトル概念統合。Limitation 5.9末尾に視覚的権威シンボル検出不能（FalseNegative新類型）追加。References追加（Altemeyer 1981, Ben-Ghiat 2020, Ross 2014）。整合性修正：5.1プレースホルダー削除・Landis & Koch(1977)・Milgram(1974)をReferencesに追加・年号混在解消。

## 要更新箇所（最終確認時）
- Abstract: "62-document corpus" → "224-document corpus" ✅更新済み
- Section 4.1: 62件→224件 ✅更新済み
- Section 4.2: 分布数値 ✅更新済み（HIGH 4・MEDIUM 75・LOW 145）
- 「複数事例にわたり」の箇所→実数に置き換え（最終スキャン後）
- Festinger(1957)・Cialdini(1984)：引用前に原著確認が必要
