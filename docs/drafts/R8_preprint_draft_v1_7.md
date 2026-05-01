# R8 v1.7 論文草稿 - Markdown版（Claudeが直接更新可能）
# 最終更新：2026-05-01 | 注意：このファイルはdocxの正式版と並走する作業用ファイル。Claudeが直接更新できます。

---

R8: A Lexical Framework for Approximating Cognitive Manipulation Risk in Text

Author: Takahiro Saito, M.S. in Clinical Psychology
Affiliation: Independent Researcher
GitHub: https://github.com/takahiro-oss/r8-cognitive-risk
License: CC BY 4.0
Status: Preprint (not peer-reviewed)
Date: March 2026
Version: v1.7 (preprint draft)

---

## Abstract

R8 proposes a structural approach to approximating cognitive manipulation risk in Japanese-language text across 12 theoretically grounded categories. This is an exploratory framework at an early stage of empirical development; the claims made in this paper are limited to what the current implementation can support. The multi-category scoring architecture draws conceptual inspiration  Enot methodological equivalence  Efrom factor-based psychometric models such as the MMPI.

R8 proposes a lexical approximation framework informed by the qualitative analysis of organizational cognitive failure  Eas documented in studies of military and institutional collapse (Tobe et al., 1984). The theoretical framework integrates Japanese organizational sociology (Yamamoto, 1977; Nakane, 1967) with Western social psychology (Janis, 1972; Milgram, 1963; Kahneman, 2011) and clinical psychology of manipulation (Symington, 1993).

The system produces a single composite score, the Cognitive Manipulation Index (CMI), defined as an approximation of the aggregate density of linguistic signals associated with manipulation pressure against autonomous thinking. Initial calibration against a 225-document corpus yields, under the standard detection mode (HIGH ≥ 41), a Precision of 93.3%, Recall of 39.6%, and F1 of 55.6 for HIGH-risk binary classification, with an exact match rate of 33.3% and within-one-level agreement of 80.4% across all three levels. Under the high-precision mode (HIGH ≥ 60), Precision reaches 100% with Recall of 4.3%. These figures reflect single-rater annotation prior to full corpus re-labeling; inter-rater reliability (Cohen's κ) will be established in Phase 2. The complete corpus and scoring data are publicly available at https://github.com/takahiro-oss/r8-cognitive-risk under CC BY 4.0.

---

## 1. Introduction

The proliferation of digital information has intensified the challenge of distinguishing legitimate communication from cognitive manipulation. Existing approaches to this problem  Eincluding fact-checking systems, hate speech detection, and misinformation classifiers  Efocus primarily on the veracity of content. However, cognitive manipulation operates at a structural level that precedes factual falsity. A message can be factually accurate while simultaneously exploiting psychological vulnerabilities through urgency, false authority, emotional amplification, and logical misdirection.

This structural dimension of manipulation has been examined qualitatively in organizational research. Notably, Tobe et al. (1984) identified the cognitive patterns that preceded Japan's institutional collapse in World War II  Eincluding the suppression of disconfirming information, over-reliance on authority, and emotionally-driven decision-making. These patterns were not unique to military organizations; they recur across corporate, political, and media contexts.

R8 (Cognitive Risk Analyzer) proposes a lexical extension of this qualitative tradition. The system operates across 12 risk categories derived from psychometric and clinical psychology frameworks, producing a single composite score: the Cognitive Manipulation Index (CMI). The present paper positions R8 explicitly as an exploratory baseline instrument rather than a validated measurement tool.

A parallel problem emerges from computational linguistics research on machine reading comprehension. Arai (2018) demonstrated that AI systems process text through statistical pattern matching without achieving genuine semantic understanding. This finding is cautionary rather than validating for R8: it highlights the risk that surface-level pattern matching  Ewhether by AI or by lexical tools  Emay systematically fail to capture meaning. R8 operates within this same constraint.

The present paper describes the theoretical foundation, implementation, and initial calibration of R8 as an open-source lexical auditing framework. Surface-level lexical analysis, while limited in contextual sensitivity, provides a reproducible and transparent baseline for cognitive risk approximation  Eone that complements rather than replaces deeper semantic analysis.

R8 is designed as a screening tool that approximates the lexical density of manipulation-compatible signals in text. At the current stage of development, the system cannot determine authorial intent, nor does it empirically demonstrate the cognitive effects of detected vocabulary on readers. These constraints arise from the structural limitations of surface-level lexical analysis, detailed in Section 5. Accordingly, the CMI score functions not as a definitive judgment of manipulative intent, but as an initial flag identifying texts that warrant closer scrutiny.

Within these acknowledged limitations, the utility of R8 rests on three properties. First, transparency and reproducibility: the rule-based, dictionary-matching architecture makes the basis for every score fully explicable and manually verifiable. Second, scalability: large volumes of text can be processed consistently against a fixed set of criteria. Third, complementary function: when combined with human judgment and contextual information, R8 serves as a diagnostic aid rather than a replacement for critical evaluation.

Future development directions include the implementation of structural pattern detection (Phase 2 second-layer architecture), false-negative detection through contrastive corpus construction, and extension to multimodal analysis  Eincluding audio and video content, made technically feasible by placing a speech-to-text conversion stage (e.g., Whisper) prior to the R8 pipeline. These developments are positioned as research priorities aimed at approximating intent-level assessment, and are detailed in Section 7.

The cognitive difficulty of individual-level defense against manipulation signals is well documented. Cialdini (1984) proposed a two-question verification procedure for authority signals  E"Is this person truly an expert?" and "How trustworthy is this expert?"  Ewhile noting that experts may strategically disclose minor unfavorable information to manufacture an appearance of credibility, after which all subsequent information is accepted uncritically (pp. 371 E72). Similarly, regarding scarcity-based pressure, Cialdini notes that the emotional arousal generated by scarcity signals actively impairs the deliberative capacity required for self-protection (p. 425). These observations generalize to the broader class of manipulation-compatible signals that R8 targets: the cognitive conditions that make manipulation effective are precisely those that make individual defense unreliable. R8 is designed to address this structural gap by providing pre-interaction text screening  Ea function that does not depend on the reader's real-time deliberative capacity.

---

## 2. Theoretical Background


The theoretical framework of R8 integrates previously disconnected research traditions under a unified construct: linguistic signals that target System 1 cognitive processing (Kahneman, 2011). This framing positions R8 not merely as a text analysis tool, but as an operationalization of cross-disciplinary convergence in the study of cognitive manipulation.

The framework draws on six bodies of work. Japanese organizational sociology and cultural psychology (Yamamoto, 1977; Nakane, 1967; Tobe et al., 1984) establish the structural conditions under which implicit cognitive coercion operates. Western social psychology (Janis, 1972; Milgram, 1963, 1974; Cialdini, 1984) independently identifies structurally equivalent phenomena, providing cross-cultural grounding. Cognitive psychology (Kahneman, 2011) provides the processing architecture that unifies these observations: manipulation-compatible linguistic signals function by activating System 1 responses—fast, automatic, and effortless—before deliberative System 2 evaluation can engage. Clinical psychology of manipulation (Symington, 1993) grounds the lexical detection strategy in documented patterns of narcissistic communication. Psychometric methodology (Hathaway & McKinley, 1943) provides the architectural model for multi-category composite scoring. Computational linguistics (Da San Martino et al., 2019; Pennebaker et al., 2015) situates R8 within existing detection approaches.

The novel contribution of this integration is the identification of a shared functional mechanism across these traditions: each documents a distinct pathway through which linguistic structure bypasses deliberative evaluation. R8 operationalizes this mechanism as a lexical density approximation. The following sections develop each component of this theoretical foundation in turn.

### 2.1 From Institutional Failure to Cognitive Manipulation: The "Essence of Failure" Framework

The structural analysis of cognitive failure in organizations has been examined qualitatively in Japanese organizational research. Tobe et al. (1984) identified recurring patterns of institutional collapse in the Japanese military during World War II  Epatterns that transcend their historical context and recur across corporate, political, and media environments.

Four structural patterns identified by Tobe et al. are directly relevant to R8's design. First, decision-making was dominated by subjective, wishful thinking rather than objective situational assessment  Ea pattern R8 operationalizes as Emotional Risk. Second, logical argumentation was systematically displaced by hierarchical authority and face-saving behavior  Ecorresponding to R8's Authority Risk and Logical Risk categories. Third, organizations demonstrated a consistent refusal to incorporate disconfirming information, suppressing data that contradicted prevailing assumptions  Ea pattern detectable through R8's Disclaimer Exploit and Anonymous Authority scores. Fourth, and most critically, organizational decisions were governed not by explicit rules but by an implicit atmospheric consensus.

### 2.2 "Kuuki" and the Vertical Society: Structural Foundations of Cognitive Coercion

This implicit atmospheric consensus was theorized by Yamamoto (1977) as "kuuki" (空氁E literally "air")  Ea form of social pressure that operates below the level of explicit argument, yet determines collective outcomes with greater force than formal reasoning. Kuuki functions as an extra-logical coercive force that paralyzes rational dissent without requiring explicit justification.

The structural foundation that sustains kuuki is identified by Nakane (1967) in her analysis of Japanese vertical society (tate-shakai). In this framework, the credibility of information is determined not by its content but by the hierarchical position of its source. Truth, in effect, is assigned by rank rather than derived through reasoning. R8 operationalizes a proxy for this structural dynamic through its False Authority and Logical Misdirection categories. This vertical structure further generates a sharp cognitive boundary between insider (*uchi*) and outsider (*yoso*) groups, constituting the social substrate from which EnemyFrame linguistic signals emerge in Japanese organizational text (Nakane, 1967, pp. 46–47).

Yamamoto illustrates the potency of this force through the case of Japan's wartime naval leadership: experts in possession of statistical data, analytical reports, and formal logical argumentation nonetheless executed operations they collectively recognized as indefensible—and subsequently found themselves unable to articulate any rational account of why they had done so (Yamamoto, 1977, pp. 19–20). This account is significant for R8's theoretical grounding: it is not the absence of evidence or reasoning capacity that produces cognitive failure, but the displacement of both by atmospheric coercion. Statistical analysis, documentary evidence, and logical argument are not merely ignored—they are rendered functionally inert.

Yamamoto further identifies the mechanism through which kuuki is generated: not as a spontaneous cultural phenomenon, but as a product of deliberate textual construction. In his analysis of Meiji-era press coverage of the Satsuma Rebellion, Yamamoto documents a reproducible operational pattern—the systematic publication of articles depicting the opposing force as a collective of savage aggressors, juxtaposed against the sacralized representation of the legitimate authority as the embodiment of benevolent order (pp. 49). This binary construction—demonized enemy versus sanctified authority—functions to anchor the reader's emotional orientation before rational evaluation can engage. Yamamoto observes that the fabricated nature of such reporting was detectable to any careful reader, yet the atmospheric effect was achieved regardless (pp. 24, 49).

### 2.3 The "Glider" Problem: Approximating Cognitive Dependency

The susceptibility of individuals to such manipulation is illuminated by Toyama's (1983) "glider" metaphor, describing cognitive subjects who lack independent reasoning propulsion and rely instead on external information flow for directional guidance. Manipulative texts exploit this dependency through urgency signals and disclaimer exploitation  Ekeeping the subject in a state of passive reception that may prevent the activation of autonomous critical judgment.

R8 is described metaphorically as a "Cognitive Breakwater" (認知的防波堤): the intent is to identify linguistic patterns that may incline a reader toward cognitive dependency rather than deliberation. The CMI is defined not as a direct measure of manipulation, but as an approximation of the density of linguistic signals associated with such pressure.

### 2.4 From "Kuuki" to CMI: A Lexical Approximation of Implicit Coercion

#### 2.4.1 Cross-Cultural Convergence

The structural dynamics described by Tobe et al. (1984), Yamamoto (1977), and Nakane (1967) are not culturally unique to Japan. Western social psychology has independently identified structurally similar phenomena.

Janis (1972) documented similar atmospheric consensus dynamics in Western organizational contexts under the term "Groupthink." Milgram's (1963) obedience experiments demonstrated the cross-cultural tendency toward authority submission. Kahneman (2011) provided the cognitive architecture underlying Toyama's (1983) "glider" metaphor. System 1 thinking  Efast, automatic, and effortless  Eis the cognitive default that manipulative texts may exploit. R8's CMI can be interpreted as an approximation of aggregate System 1 pressure signals in a text.

### 2.5 Psychometric Foundations

R8's multi-category scoring structure draws conceptual inspiration from established psychometric instruments that share a common architectural logic: qualitatively observed psychological phenomena are operationalized as multiple discrete indicators, which are then aggregated into a composite score through weighted combination.

The Minnesota Multiphasic Personality Inventory (MMPI; Hathaway & McKinley, 1943) exemplifies this structure. R8 applies this architectural logic to textual cognitive risk: 12 risk categories function analogously to clinical scales, each capturing a distinct linguistic dimension; the CMI represents the weighted composite. This inspiration is acknowledged explicitly as conceptual only.

### 2.6 Narcissistic Manipulation and Clinical Lexical Patterns

Symington (1993) identified the structural features of narcissistic communication  Eincluding the systematic denial of the other's autonomous perspective, the exploitation of emotional dependency, and the use of authority claims to pre-empt critical evaluation. R8's dictionary construction draws on this clinical tradition. The categories of Emotional Risk, Authority Risk, Disclaimer Exploit, and Naked Number reflect patterns recognizable in the clinical literature on manipulative communication.



Symington's clinical observations provide a more specific mechanistic account of how this dependency operates. He describes a reciprocal contract structure in which the communicator offers continuous emotional soothing in exchange for the reader's reciprocal soothing, forming a closed affective loop that progressively raises the psychological cost of disengagement (p. 84). A further clinical observation illuminates the reinforcement dynamic: the act of providing soothing continuously functions not to resolve the recipient's distress but to intensify it, deepening reliance on the communicator as the sole source of relief (p. 80). Critically, Symington locates these processes at the sub-threshold level of consciousness (p. 86)—operating below explicit reasoning in a manner structurally analogous to Kahneman's (2011) System 1 activation. This clinical account grounds R8's EmotionalRisk, FearRisk, and EnemyFrame categories as approximations of the lexical surface through which such sub-threshold dependency-induction operates in text.

### 2.7 Relationship to Computational Linguistics Approaches

The computational detection of cognitive manipulation and propaganda in text has been addressed through several complementary research traditions.

Da San Martino et al. (2019) proposed a fine-grained propaganda detection framework identifying 18 rhetorical techniques at the fragment level in news articles. Their classification system shares conceptual overlap with R8's 12-category architecture, though the implementation approaches differ substantially: their neural sequence-labeling model achieves fragment-level annotation, while R8 operates through dictionary-based lexical density at the document level. The interpretability trade-off is explicit: R8 sacrifices coverage for auditability.

The MentalManip dataset (Wang et al., ACL 2024) provides a benchmark for manipulation detection in conversational text, reporting that large language models achieve approximately 65% classification accuracy on manipulation judgment tasks. This figure is notable for R8's positioning: if state-of-the-art LLM-based approaches achieve 65% on conversational manipulation, the interpretability and domain-specificity advantages of a rule-based system may justify its lower coverage in specialized deployment contexts where stakeholders require explainable outputs.

Pennebaker et al.'s (2015) LIWC framework established that lexical selection patterns carry measurable psychological signals, providing psycholinguistic grounding for density-based scoring approaches. R8 shares this architectural logic while applying it to manipulation-specific categories derived from clinical psychology and organizational behavior rather than general psychological dimensions.

R8 differs from these approaches in three respects. First, domain specificity: Japanese-language organizational and commercial texts, with theoretical grounding in Japanese organizational sociology. Second, architectural choice: dictionary-based rather than neural, prioritizing interpretability over predictive coverage. Third, theoretical integration: explicit derivation from cross-cultural convergence between Japanese organizational psychology (Tobe et al., 1984; Yamamoto, 1977; Nakane, 1967) and Western social psychology (Janis, 1972; Milgram, 1963; Kahneman, 2011).

Two additional bodies of work provide direct empirical grounding for the manipulation patterns that R8 targets. Ross (2014) identified three structural criteria for cult characterization  Eabsolute authority, coercive persuasion techniques, and exploitative harm  Eand documented the emergence of online cult dynamics in which manipulation operates exclusively through text, without physical co-presence. This observation grounds R8's focus on digital text as a self-contained manipulation medium. Ben-Ghiat (2020) analyzed the rhetorical strategies of authoritarian political leaders across historical and contemporary contexts, identifying a recurring operational playbook: sustained disinformation campaigns that overwhelm the audience's capacity for factual adjudication (corresponding to R8's PropagandaRisk and EnemyFrame categories), authority signals that bypass deliberative evaluation (AuthorityRisk), and fear-based mobilization that activates threat responses prior to rational processing (FearRisk and AbsolutistWords). The parallel operationalization of cult communication (Ross, 2014) and authoritarian political rhetoric (Ben-Ghiat, 2020) within the same detection framework supports R8's claim to cross-domain applicability  Espanning the organizational, commercial, spiritual, and political genres represented in the calibration corpus.

While research on echo chambers and filter bubbles (Sunstein, 2017) addresses the information environment architecture through which manipulative content reaches audiences, these frameworks operate at a different unit of analysis than R8. R8 targets linguistic signals embedded within individual texts, independently of the distributional context in which those texts are encountered. This distinction defines the boundary of the present study's claims.

### 2.8 Expectancy-Value Theory and the Functional Manipulation of Reader Goals

Eccles and Wigfield (2002) proposed Expectancy-Value Theory (EVT) as a framework for explaining achievement behavior through two psychological constructs: the individual's expectation of success, and the subjective value assigned to a given task. Subjective value is further decomposed into attainment value (personal importance of succeeding), utility value (instrumental relevance to future goals), intrinsic value (enjoyment derived from the task itself), and cost (psychological and material sacrifice required).

EVT was developed in educational psychology to describe how individuals autonomously form motivational beliefs. The present study identifies a structural inversion of this framework in manipulative text: rather than emerging from autonomous appraisal, EVT variables are externally inflated, concealed, or fabricated through lexical means. Utility value is amplified through fear and urgency signals; attainment value is elevated through authority and exclusivity framing; expectancy for success is manufactured through unverifiable statistical claims; and cost is systematically concealed or redefined as evidence of growth.

R8's 12 risk categories can be interpreted as theoretically motivated proxies for EVT variable manipulation. EmotionalRisk and FearRisk are theoretically aligned with utility value inflation; AuthorityRisk and PropagandaRisk with attainment value targeting; LogicalRisk and NakedNumber with expectancy fabrication; and DisclaimerExploit and AbsolutistWords with cost concealment. The category vector profiles observed in Phase 1 calibration  Eparticularly the simultaneous EnemyFrame, PropagandaRisk, and FearRisk activation in HIGH-classified texts, and the LogicalRisk 1.0 pattern in charismatic entrepreneur texts  Eare directionally consistent with this theoretical mapping, though formal validation against EVT constructs requires independent measurement instruments beyond the scope of the current study. This mapping is proposed as a theoretical foundation for Phase 2 operationalization rather than a claim that current CMI scores measure EVT constructs directly. Critically, intrinsic value manipulation  Ethe use of affirmatively valenced vocabulary (compassion, gratitude, light) to simulate authentic engagement  Efalls systematically outside the detection scope of the current lexical architecture, constituting the primary source of false negatives documented in Section 5.8.

This mapping does not imply that EVT variable manipulation reflects deliberate authorial design. As documented in Section 5.7, R8 detects lexical patterns that function as EVT variable manipulation  Einflating utility value, concealing cost, or fabricating expectancy  Eindependent of whether such manipulation reflects intentional strategy or habitual communication pattern. The distinction between the two cannot be resolved through lexical evidence alone.

The convergence between EVT's motivational architecture and R8's empirically derived category structure was reached through independent analytical paths, providing conceptual support for the theoretical coherence of R8's design. The relationship is presented here as structural correspondence, not as a claim that R8 operationalizes EVT constructs directly.

The motivational foundation underlying EVT variable manipulation is further illuminated by need-to-belong theory. Baumeister and Leary (1995) proposed that the need to belong  Eto form and maintain stable, positive interpersonal relationships  Econstitutes a fundamental human motivation with pervasive effects on cognition, emotion, and behavior. Manipulative texts systematically exploit this need through the sequential construction of in-group inclusion and out-group exclusion: establishing similarity and shared identity before introducing enemy framing and exclusivity signals (see Section 3.3, EnemyFrame and PropagandaRisk). This sequential exploitation corresponds structurally to the EVT category of attainment value manipulation  Ethe manufactured sense that belonging to a specific community is personally essential. R8's AuthorityRisk, EnemyFrame, and EmotionalRisk categories function as partial detection proxies for this motivational targeting, though the sequential structure of the exploitation pattern falls outside the scope of lexical density scoring and is identified as a Phase 2 design target (Section 7.2).

A related mechanism operates through psychological reactance. Brehm (1966) demonstrated that perceived threats to behavioral freedom generate motivational pressure to restore that freedom  Ea response that can be exploited by scarcity signals that frame inaction as loss of opportunity. In manipulative text, scarcity signals (time-limited offers, quantity restrictions, exclusive access framing) trigger reactance-based approach motivation, overriding deliberative evaluation. Brock's (1968) commodity theory formalizes this dynamic: objects become more desirable as their availability decreases, and this effect extends from material goods to information and ideas. Brock further demonstrated that the persuasive power of information increases when access to that information is itself restricted  Ean effect amplified when both the content and the source are framed as exclusive. These mechanisms underlie the FearRisk and ClickbaitRisk categories in R8's architecture, and provide theoretical grounding for the ScarcityRisk category proposed for Phase 2 development (Section 7.4).

Cialdini (1984) synthesizes these mechanisms in a behavioral framework. Authority signals  Etitles, credentials, institutional affiliations  Etrigger automatic compliance responses through the same System 1 pathway that Kahneman (2011) identifies as the default cognitive mode. Critically, Cialdini demonstrates that it is not the actual authority of the source that triggers this response, but the perceived authority conveyed by symbols  Etitles, attire, and automobiles  Ethat have been shown experimentally to elicit compliance even without any legitimate underlying credentials (p. 371). An actor playing a president in a television drama was treated as a genuine political authority and questioned about real presidential policy  Ea compliance response identical to that generated by actual expertise (p. 349). This finding is directly relevant to R8's design rationale: R8's AnonymousAuthority and AuthorityRisk categories detect the linguistic symbols of authority  Etitles, endorsements, institutional references  Erather than the actual authority of the source, because it is these symbols, not the underlying reality, that function as System 1 activation triggers in readers.

---

## 3. Methodology

### 3.1 System Architecture

R8 operates as a pipeline of three sequential processes: text acquisition, lexical analysis, and score aggregation. Input sources include plain text files, PDF documents, and web URLs. All acquired text is passed to a unified analysis function regardless of source type.

### 3.2 Text Normalization (Phase 1)

Prior to analysis, all input text undergoes normalization to reduce orthographic variation. The normalization pipeline applies Unicode NFKC normalization, followed by katakana-to-hiragana conversion via Unicode codepoint mapping (U+30A1–U+30F3, offset -96).

### 3.3 Operational Definitions of 12 Risk Categories

The 12 categories are derived from clinical psychology, organizational behavior, and rhetorical analysis frameworks. Each category is operationalized as a lexical density measure: the count of matched dictionary terms divided by text length per 100 characters.

**Note on implementation scope:** The implemented system includes 14 scoring dimensions. Two dimensions  ESexual Induction Risk and Beauty/Diet Hype Risk  Efunction as peripheral risk indicators. Sexual Induction Risk carries a weight of 0.04 and is included as a primary scoring dimension. Beauty/Diet Hype Risk carries a weight of 0.00 and functions as a reference-only indicator excluded from CMI calculation. These peripheral dimensions are not included in the theoretical 12-category framework presented in this paper; they represent implementation extensions for applied deployment contexts.

### 3.4 Two-Layer Authority Detection

Authority Risk employs a two-layer detection architecture distinguishing pseudo-authority from legitimate authority reference. Pseudo-authority markers are scored directly as risk indicators. Legitimate authority markers are scored conditionally: their risk contribution is modulated by the concurrent Hype Risk density.

### 3.5 Scoring Algorithm

The Cognitive Manipulation Index (CMI) is computed as a weighted sum of normalized category scores. Category weights reflect the relative contribution of each manipulation dimension to overall cognitive risk, derived through theoretical reasoning and iterative empirical calibration on a small pilot corpus. Statistical Risk carries the highest weight (0.16), reflecting the theoretical manipulative potency of false quantification. CMI ranges from 0 to 100.

Threshold levels for risk classification operate in two modes. The standard mode (default) sets HIGH: CMI ≥ 41, MEDIUM: 35 ≤ CMI < 41, LOW: CMI < 35, optimizing for screening sensitivity (Precision = 93.3%, Recall = 39.6%, F1 = 55.6). The high-precision mode sets HIGH: CMI ≥ 60, MEDIUM: 35 ≤ CMI < 60, LOW: CMI < 35, optimizing for specificity (Precision = 100%, Recall = 4.3%). The threshold is treated as a tunable parameter analogous to temperature in language model inference: the appropriate setting depends on the deployment context and the relative cost of false positives versus false negatives. All corpus statistics reported in this paper use the standard mode (HIGH ≥ 41).

### 3.6 Implementation and AI Disclosure

R8 is implemented in Python 3.x as two modules: r8.py (single-document analysis) and mass_audit.py (batch processing). The system requires no machine learning infrastructure, operating entirely through dictionary lookup and regular expression matching. All source code is publicly available under CC BY 4.0 at https://github.com/takahiro-oss/r8-cognitive-risk.

R8's development was conducted with support from large language models (Claude, Anthropic; Gemini, Google). AI support was provided for: code development and optimization, translation between Japanese and English, drafting assistance for sections of this manuscript, and literature summarization and synthesis.

The following decisions and analyses were performed solely by the author: theoretical framework design, selection and operationalization of the 12 risk categories, construction of the Japanese-language lexical dictionaries, calibration of category weights, all substantive research direction and interpretive choices, manual annotation of the calibration corpus, and critical assessment of limitations and implications.

The author holds an M.S. in Clinical Psychology (Aichi Gakuin University, 2012) and brings approximately 20 years of direct experience in Japanese educational settings.

---

## 4. Initial Calibration and Exploratory Testing

### 4.1 Study Design

The present calibration exercise is explicitly preliminary in scope. The calibration corpus comprises 225 documents collected through automated URL-based scraping using the mass_audit.py pipeline, supplemented by manual collection via OCR-based screenshot processing for social media content. Of the 225 documents, 9 returned CMI scores of 0.0 due to JavaScript-rendered content inaccessibility, yielding 216 documents with valid CMI scores (CMI > 0)  Ea structural limitation documented in Section 5.4.

Ground truth classification was determined through single-rater expert judgment by the author, drawing on clinical psychology training and 20 years of educational practice. A structured rubric was applied on a provisional basis, drawing on two theoretical frameworks already established in the literature: Ross's (2014) three-criterion model of coercive communication (absolute authority, coercive persuasion techniques, and exploitative framing) and Janis's (1972) groupthink symptom profile. Expert judgment was applied at the document level, integrating these theoretical criteria with the author's clinical psychology training (M.S., Aichi Gakuin University, 2012). The provisional nature of this rubric reflects the preliminary scope of Phase 1; the consolidated annotation criteria (v0.6) were finalized subsequent to the initial scanning phase.

### 4.2 Corpus Description

The 225-document corpus spans the following distribution under the standard mode (HIGH ≥ 41): HIGH-risk documents (n=45, CMI ≥ 41), MEDIUM-risk documents (n=41, 35 ≤ CMI < 41), and LOW-risk documents (n=130, CMI < 35), with 9 documents returning CMI = 0.0 excluded from classification. This distribution reflects the structural finding that the current lexical architecture achieves HIGH classification across a broader range than the high-precision mode (HIGH ≥ 60, n=8), with the standard mode optimized for screening sensitivity.

Genre distribution includes: governmental and institutional documents (LOW baseline), commercial manipulation content (investment schemes, MLM, diet/health products), spiritual and pseudoscientific content, political party media (domestic and international state-affiliated outlets), cult and religious organization content, legal information accounts, financial advisory content, and book-format texts (22 chapters across 4 titles; charismatic entrepreneur and educational critique genres). The book-format subset is analyzed separately in Section 5.8 as a cross-genre replication site for the surface-positive vocabulary false-negative pattern.

### 4.3 Results

CMI scores were obtained across the full 225-document corpus. Of these, 9 documents returned CMI = 0.0 and are excluded from the following summary statistics; all 9 are retained in the corpus as documented cases (false-negative records or English-language acquisition failures). Summary statistics are reported for the 216 documents with valid CMI scores (CMI > 0).

**Table 1. CMI Summary Statistics by Automated Classification Level**

| Level | n | Mean | SD | Min | Max |
|---|---|---|---|---|---|
| HIGH | 45 | 48.9 | 6.6 | 41.3 | 67.6 |
| MEDIUM | 41 | 37.5 | 1.8 | 35.0 | 40.9 |
| LOW | 130 | 21.8 | 8.4 | 2.6 | 34.9 |
| **Overall** | **216** | **30.4** | **13.3** | **2.6** | **67.6** |

Median CMI across valid documents: 31.5.

Exact match rate (automated vs. expert label): 33.3% (75/225) across the Phase 1 corpus. Agreement within one risk level: 80.4% (181/225). For HIGH-risk binary classification under the standard mode (HIGH ≥ 41): Precision = 93.3% (TP=42, FP=3), Recall = 39.6% (FN=64), F1 = 55.6. These figures reflect single-rater annotation prior to full corpus re-labeling under the consolidated annotation criteria (v0.6); inter-rater reliability (Cohen's κ) will be established in Phase 2. The low exact match rate of 33.3% reflects the preliminary state of human annotation prior to full corpus re-labeling under the consolidated annotation criteria (v0.6), which was finalized subsequent to the initial scanning phase. Full re-labeling of all 225 documents under v0.6 criteria is scheduled prior to Phase 2 inter-rater reliability assessment; updated agreement statistics will be reported at that stage. A blind evaluation conducted on three representative documents (corpus ID: web203, note164, web193) revealed divergence in two of three cases (66.7%), confirming systematic limitations documented in Sections 5.8 and 5.9.

### 4.4 Analysis of Discrepancies

Three categories of discrepancy were identified.

The first concerns text acquisition limitations. Documents returned CMI=0.0 due to JavaScript-rendered dynamic content that BeautifulSoup-based scraping cannot access.

The second concerns scalar underdetection of politically framed content. State-affiliated international outlets and domestic political party media exhibited Enemy Frame and Fear Risk activation at maximum density while returning LOW scalar CMI scores. This reflects a systematic limitation of the current scalar aggregation architecture.

The third concerns satirical mimicry. Satirical content (虚構新聁E that intentionally mimics manipulative news structure registers elevated CMI scores relative to expert LOW classification.

### 4.5 Implications for Dictionary Calibration

The preliminary results indicate that R8's current lexical dictionary is sensitive to commercially framed manipulation but requires expansion to capture anecdotal manipulation, spiritually framed authority, and satirical mimicry.

---

## 5. Current Limitations

### 5.1 Surface-Level Lexical Matching

The current implementation relies exclusively on surface-level lexical matching and does not account for contextual disambiguation, linguistic variation, or discourse-level manipulation structures. Three specific consequences follow from this design choice. First, the system cannot distinguish between identical surface forms that carry different semantic functions depending on context. Second, paraphrase and lexical substitution allow manipulation-compatible content to evade detection entirely. Third, the scoring architecture measures lexical density across the entire document, which means locally concentrated high-severity signals are systematically diluted in long-form texts (see Section 5.10 for empirical demonstration).

The false-positive and false-negative implications of these constraints have been empirically observed in the calibration corpus. The author's own analytical essays (corpus ID: note219–note228) provide a documented case of false-positive risk. Category-level analysis reveals that LogicalRisk (9/10 documents, density 0.95 E.0) and EmotionalRisk (10/10 documents, density 0.46 E.99) were the dominant activation sources across all ten documents  Epatterns structurally attributable to the argumentative and critical register of analytical prose rather than manipulative intent. This demonstrates that the system cannot distinguish between logical argumentation as a rhetorical structure and logical misdirection as a manipulation technique.

These limitations are not resolvable through dictionary expansion alone. The ceiling of lexical-only detection has been empirically mapped through iterative dictionary development from version 10 to version 16.

### 5.2 Language Scope

The current implementation is Japanese-language specific. All dictionaries, normalization procedures, and validation corpora are constructed for Japanese text, and the theoretical framework draws substantially on Japanese organizational sociology and cultural psychology.

This constraint reflects a deliberate scoping decision rather than a technical limitation. Extension to other languages  Eincluding English and other East Asian languages  Eis a longer-term research direction, contingent on the establishment of validated annotation protocols and comparable theoretical grounding in the target language context.

### 5.3 Calibration Corpus Limitations

The present calibration corpus is insufficient for definitive statistical inference. The use of the system's author as the sole annotator constitutes a significant source of bias. To partially assess the validity of the annotation process, a blind evaluation was conducted on three representative documents: web203 (HIGH, confirmed), note164 (divergence: automated MEDIUM / expert HIGH), and web193 (divergence: automated LOW / expert MEDIUM). Of these three, two (66.7%) showed divergence between automated and expert classification.

Furthermore, the corpus includes documents authored by the present author (corpus ID: note219–note228), a series of critical essays examining AI sycophancy. These documents produced CMI scores in the LOW–MEDIUM range (22.4 E0.5) despite the absence of manipulative intent on the author's part. These documents are retained in the corpus as documented instances of intent-unresolved classification, with human_label recorded as MEDIUM and riskfactor noted as intent-unresolved.

Phase 2 will prioritize annotation standard consolidation before expanding the annotator pool to a minimum of two independent raters with Cohen's kappa as the reliability metric. Inter-rater reliability will be reported using Cohen's kappa (κ), calculated as:

κ = (P_o ∁EP_e) / (1 ∁EP_e)

where P_o denotes the observed proportion of agreement and P_e denotes the proportion of agreement expected by chance. A minimum threshold of κ ≥ 0.60 is adopted as the criterion for acceptable reliability, consistent with the benchmark established by Landis and Koch (1977), who characterized κ values of 0.41 E.60 as moderate, 0.61 E.80 as substantial, and 0.81 E.00 as almost perfect. The current Phase 1 corpus provides no inter-rater κ estimate, as all annotations were performed by the single author; this absence is disclosed as a limitation rather than concealed.

### 5.4 Digital Media Application Constraints

The application of URL-based lexical analysis to digital media faces a hierarchy of structural constraints. At the technical level, a significant proportion of high-risk web content employs JavaScript rendering that prevents direct HTML extraction. Direct URL scanning consistently underperforms text-converted scanning by a substantial margin (CMI 10.0 vs 44.7 confirmed on identical pages).

Beyond the JavaScript problem, a more fundamental constraint emerges from the structural characteristics of social media content. Short-form posts on platforms such as X (formerly Twitter) present a categorically different challenge. During calibration, five posts (corpus ID: sn229–sn233) were scanned via OCR pipeline. All produced CMI LOW despite containing vocabulary consistent with EnemyFrame and Propaganda categories. Two failure modes were identified: density calculation failure for 140 E80 character texts, and OCR-induced character-level misreads breaking dictionary matching.

The most fundamental limitation is epistemological. Fact-based disinformation  Eclaims such as "the suspect's father holds Chinese citizenship"  Ecannot be evaluated through lexical analysis alone. This reflects a categorical boundary between lexical pattern detection and factual verification.

Phase 2 design priorities include dynamic threshold adjustment based on text length (short-text mode) and thread-level aggregation enabling multi-post integration before scoring.

### 5.5 Dictionary Construction Methodology

The current lexical dictionaries were constructed through theoretical reasoning and expert judgment rather than corpus-based induction. The iterative development process from version 10 to version 17 of the R8 dictionary expanded detection coverage for specific genres (spiritual/pseudoscience content in v11 E3, political conspiracy content in v14 E5, deletion-threat urgency patterns in v16). However, this expansion process has a structural ceiling: the most sophisticated manipulation content remained in the MEDIUM range regardless of dictionary expansion, because the manipulation operates through vocabulary that does not appear in any risk category.

This iterative expansion process introduces the risk of circular validation. Dictionary expansion is therefore reframed not as a precision improvement strategy but as documentation of the lexical detection ceiling before transition to transformer-based contextual analysis. Version 17 represents the current boundary of what surface-level lexical matching can achieve for the genres represented in the calibration corpus.

### 5.6 The Gap Between Theoretical Framing and Implemented Method

R8 is an open-source, transparent instrument for approximating the density of manipulation-compatible linguistic signatures; surface-level lexical patterns do not establish manipulative intent or effect. A structural limitation that underlies all others in this paper deserves explicit statement. The theoretical framework presented in Section 2 draws on cognitive psychology (Kahneman, 2011), social psychology (Janis, 1972; Milgram, 1974; Zimbardo, 2007), and Japanese organizational sociology (Nakane, 1967; Yamamoto, 1977) to characterize cognitive manipulation as a multi-level phenomenon. R8 is theoretically positioned as a detection system for linguistic signals targeting System 1 cognitive processing (Kahneman, 2011).

The implemented method  Esurface-level lexical density analysis  Eoperates at a categorically different level of description. No amount of dictionary expansion will bridge the gap between counting words and measuring cognitive effects.

What the gap does require is explicit restraint in theoretical claims. The paper presents R8 as a lexical screening tool that approximates manipulation-compatible signal density, not as a direct measure of cognitive manipulation. The theoretical framing in Section 2 should be read as motivating the category design and providing interpretive context, not as a claim that CMI scores measure the theoretical constructs directly. This distinction is particularly salient for the limitations documented in Sections 5.7 through 5.10.

### 5.7 Authorial Intent and the Limits of Lexical Inference

The present system analyzes the linguistic structure of texts but cannot determine the intentional state of the author reflected in that structure. The high-density occurrence of manipulation-compatible vocabulary may reflect deliberate cognitive manipulation design, the author's own sincere beliefs expressed through habitual language, or any combination of the two.

Symington (1993) describes cases in which narcissistically structured communicators are themselves unaware of the manipulative architecture of their speech. Festinger's (1957) cognitive dissonance theory suggests a parallel mechanism: communicators who experience tension between their stated framing and their underlying intent may resolve this dissonance by elaborating the framing itself  Einadvertently intensifying the manipulation-compatible signal density of their text. The present study has no means of empirically distinguishing these three types (intentional, unconscious, and mixed), and CMI scores therefore carry no implication about the author's cognitive state or ethical status.

In the calibration corpus, a legal information note account (corpus ID: note164–note179, 15 valid documents) reproduced the stereotyped sequence of fear induction, authority presentation, logical justification, and action induction across all articles  Einstantiating what the present study terms a two-stage cognitive induction architecture. This structure may represent intentional design or habitual communication pattern; text analysis alone cannot resolve the distinction.

### 5.8 Surface-Positive Vocabulary and Systematic False Negatives

The most structurally significant detection limitation identified in Phase 1 calibration is the systematic underdetection of texts employing affirmatively valenced vocabulary as a manipulation medium.

Cult-affiliated and spiritual texts in the calibration corpus (corpus ID: web138–web197, relevant subset) were classified as MEDIUM-equivalent by the expert evaluator but produced CMI scores consistently in the LOW range. These texts share a characteristic vocabulary profile: high-density use of terms such as "compassion," "love," "light," "walking together," and "gratitude"  Esurface-positive expressions that appear in none of R8's 12 risk categories.

The author's own analytical essays (corpus ID: note219–note228) provide a particularly clear illustration. Critical analyses of AI sycophancy produced CMI scores between 22.4 and 50.5 despite explicit analytic intent. The author cannot themselves determine with certainty whether implicit rhetorical intent is entirely absent, instantiating Section 5.8's fundamental problem.

Distinguishing authentic positive communication from manipulation-mediated positive vocabulary requires three analytical layers: statistical extraction of co-occurrence patterns between positive vocabulary and action-induction language (PMI analysis); inductive sequence analysis reconstructing the communicative destination from the final paragraph backward; and contrastive corpus comparison against authentic positive text baselines. These constitute Phase 2 research priorities.

A cross-genre replication of this false-negative pattern was identified in the book-format corpus. Seven chapters of a charismatic entrepreneur text (Yozawa, T., 2013, *Byousoku de ichioku-en kasegu jouken* [The conditions for earning 100 million yen per second], Forest Publishing; corpus ID: book001_ch01–ch07) were analyzed using the same pipeline. All seven chapters received HIGH human_label assignment; automated CMI scores ranged from 18.6 to 45.5, with five of seven chapters classified as LOW. LogicalRisk reached saturation (0.74 E.0) across all chapters, and AbsolutistWords reached ceiling (1.0) in two chapters (ch03, ch07), yet EmotionalRisk remained near zero (0.0 E.139) throughout. This profile is structurally identical to the charismatic entrepreneur texts identified in Phase 1 web corpus calibration (Watanabe corpus, 2010 E011): LogicalRisk saturation co-occurring with near-zero EmotionalRisk, producing systematic underdetection despite expert HIGH classification. The cross-corpus replication across a publication span spanning the early 2010s suggests that this false-negative pattern reflects a stable structural feature of charismatic entrepreneur discourse rather than an artifact of individual authorial style. This pattern constitutes a transhistorical reproduction of surface-non-negative vocabulary manipulation  Ea systematic false-negative class for which lexical dictionary expansion offers no structural remedy.

A structurally distinct false-negative pattern concerns the visual and multimodal dimensions of authority construction. Cialdini (1984) demonstrated that authority compliance is triggered not by the genuine credentials of a source but by the perceived authority conveyed by symbols  Etitles, attire, institutional affiliations, and the visual presentation of expertise (p. 371). In digital text environments, these authority symbols are instantiated not through vocabulary but through visual elements: profile photographs conveying professional appearance, display of academic credentials or certifications as images, institutional logos, and the visual design language of high-production-value websites. R8 operates exclusively on extracted text and therefore cannot detect any of these visual authority signals. A text that functions as high-risk authority-based manipulation through visual cues may register near-zero AuthorityRisk and AnonymousAuthority scores if the verbal content is stripped of explicit authority vocabulary. This represents a categorical detection boundary rather than a calibration limitation: no expansion of the lexical dictionary can address signals that are not encoded in text. Phase 2 corpus design will include human annotation of visual authority signal presence as a supplementary dimension to enable systematic documentation of this false-negative class.

### 5.9 Lexical Density and Qualitative Severity: An Empirical Demonstration

The density-based scoring architecture measures the quantitative distribution of manipulation-compatible signals but does not reflect the qualitative severity of individual lexical items.

A legal information note account (corpus ID: note164) contains explicit threatening expressions including references to criminal extortion law. Despite expert classification as HIGH-equivalent in blind evaluation, the system returned CMI 52.1, MEDIUM classification. Threatening vocabulary was concentrated in the first 2,000 characters, producing a local density of 1.81 per 100 characters. Calculated across the full text of 8,500 characters, density fell to 0.094 per 100 characters  Ebelow the FearRisk activation threshold.

In contrast, web203 (CMI 61.4, HIGH) distributed fear-relevant vocabulary across its full 6,043-character text, yielding a global density of 0.149 per 100 characters sufficient to activate the HIGH threshold. The comparison demonstrates that the scoring architecture systematically underestimates locally concentrated high-severity signals in long-form texts.

This dilution effect may correspond to a structural property of certain manipulation architectures  Econsistent with Kahneman's (2011) System 1 activation followed by System 2 rationalization. Whether this sequential structure reflects deliberate design or habitual communication pattern cannot be determined from textual evidence alone (see Section 5.7).

Possible architectural responses include maximum-value scoring or severity-weighted threshold calibration for specific categories. Both approaches introduce increased false-positive risk whose magnitude remains unquantified. These are documented as Phase 2 architectural investigation priorities.

### 5.10 Short-Form Text Application Constraints

The density-based scoring architecture was designed for medium-to-long-form texts and exhibits structural detection failure for short-form social media content.

During Phase 1 calibration, five posts related to a child homicide case on X (formerly Twitter) (corpus ID: sn229–sn233) were scanned via an OCR-based pipeline. All five produced CMI LOW despite containing vocabulary consistent with EnemyFrame and Propaganda categories. Two failure modes were identified: density calculation failure for 140 E80 character texts, and OCR-induced character-level misreads breaking dictionary matching.

The most fundamental limitation is epistemological. Fact-based disinformation  Especific factual claims whose falsity cannot be assessed through lexical analysis  Efalls categorically outside the detection scope of the current system. This marks a categorical boundary between lexical pattern detection and factual verification, not resolvable through dictionary expansion.

Phase 2 architectural responses include dynamic threshold adjustment calibrated to text length (short-text mode), thread-level aggregation processing multiple posts as a unified document before scoring, and hashtag pattern analysis as a supplementary signal channel.

A further failure mode was identified during Phase 1 corpus construction: two documents (corpus ID: sn234, sn235) were acquired via OCR-based screenshot processing but returned CMI = 0.0 due to capture of non-target content — a NAS management interface and a Claude session window respectively. These documents are retained in the corpus as documented cases of acquisition failure and flagged for deletion prior to Phase 2 re-labeling. This failure mode illustrates a categorical limitation of screenshot-based corpus construction: OCR cannot distinguish between the target text and surrounding interface elements, and acquisition validity cannot be confirmed without manual inspection of each document. Phase 2 corpus design will require a mandatory content-validity check prior to annotation.

---

## 6. Discussion

### 6.1 R8 as a Screening Tool: Utility and Acknowledged Limitations

R8 is explicitly positioned not as a definitive classifier of manipulative intent, but as an initial flag that complements rather than replaces human judgment. The system's utility rests on three properties: transparency and reproducibility, scalability, and complementary function.

This positioning is analogous to medical blood testing: blood tests do not definitively diagnose disease but identify abnormal values requiring closer examination. R8 detects "signs requiring scrutiny" in text; it does not determine manipulative intent. Explicit disclosure of this limitation is essential for preventing misuse of the instrument.

The corpus distribution observed in Phase 1 calibration  ELOW: 64.3%, MEDIUM/HIGH: 35.7%  Eshould be interpreted within this screening framework rather than as evidence of low detection power. A first-stage screening instrument is designed to efficiently exclude low-risk documents from further analysis while directing resources toward documents requiring closer scrutiny. Of the 225 documents, 9 returned CMI = 0.0 and are excluded from scalar screening analysis, yielding 216 valid cases. R8 identifies 39.8% of documents (86/216 valid cases) as requiring attention  Ea proportion that, within a screening framework, functions as a first-stage filter directing analytic resources toward a tractable subset. Specifically, documents classified as MEDIUM or HIGH are flagged for closer examination of category vector profiles, co-occurrence patterns, and contextual factors that fall outside the scope of lexical density scoring. The false-positive rate within this flagged subset is low: 3 of 45 HIGH-classified documents received non-HIGH human_label assignment (6.7%), indicating that the first-stage filter produces few spurious escalations. However, the complementary figure demands equal transparency: 126 of 139 LOW-classified documents received MEDIUM or HIGH human_label assignment (90.6%), indicating that the majority of documents cleared by the first-stage filter may warrant re-examination under a second detection layer. The LOW classification does not assert absence of manipulation; it asserts that the lexical signal density does not reach the threshold justifying escalation. The magnitude of the false-negative rate  Eempirically documented here for the first time  Eprovides direct quantitative motivation for the Phase 2 structural detection architecture described in Section 7.2. These figures reflect single-rater annotation and are subject to revision upon establishment of inter-rater reliability in Phase 2.

### 6.2 CMI Scores and Category Vector Profiles

A key finding of Phase 1 calibration is that the 12-category vector profile is diagnostically superior to the scalar CMI value. Political and conspiracy-theory texts reached HIGH classification through simultaneous elevation of EnemyFrame, Propaganda, and FearRisk  Ea pattern that, based on Phase 1 calibration data, shows directional convergence with elements of Janis's (1972) groupthink symptom profile, though the analogy is subject to the structural limitations described below. An empirical observation from Phase 1 calibration provides a partial point of contact: under the high-precision mode (HIGH ≥ 60), all eight HIGH-classified documents exhibited simultaneous activation of EnemyFrame, FearRisk, and PropagandaRisk—the three categories directionally corresponding to Janis's stereotyped out-group framing, vulnerability illusion, and pressure toward uniformity. Conversely, charismatic entrepreneur texts that plateaued at MEDIUM showed near-zero EnemyFrame activation, consistent with Janis's observation that out-group designation accelerates groupthink dynamics. This co-occurrence pattern is interpreted as directional convergence rather than empirical validation: the sample of four HIGH documents is insufficient for statistical inference, and the correspondence between R8 lexical categories and Janis's group-process symptoms operates across categorically different levels of analysis. Three structural differences further limit the analogy. First, Janis described closed-group face-to-face decision-making processes, whereas R8 targets one-directional text addressed to an unspecified audience. Second, Janis's unit of analysis is the group; R8's unit is the relationship between an individual reader and a text. Third, Janis documented decision-making processes observable by external researchers; R8 detects lexical surface features that may or may not reflect the group-level dynamics Janis theorized. No systematic empirical mapping between R8 categories and Janis's eight symptoms has been conducted in this study.

Category vector profile analysis can visualize differences invisible to scalar scores. FearRisk elevation in isolation suggests fear-induction manipulation; Authority combined with Hype suggests pseudo-authority exploitation.

### 6.3 Surface-Positive Vocabulary and the False-Negative Problem

The most important structural finding of Phase 1 calibration is the systematic false-negative pattern for texts using affirmatively valenced vocabulary as a manipulation medium (Section 5.8). The finding is not resolvable through dictionary expansion.

The author's own analytical essays (corpus ID: note219–note228) illustrate this problem. Critical writing about AI sycophancy produced CMI MEDIUM scores, with the author unable to determine with certainty whether implicit rhetorical intent is entirely absent. Phase 2 priority: construction of a contrastive corpus pairing authentic positive texts with manipulation-mediated positive texts to enable false-negative detection.

### 6.4 Short-Form Social Media Content

Phase 1 calibration confirmed that X (formerly Twitter) posts present a structurally distinct challenge for density-based scoring (Section 5.10). The scoring architecture is not suited for texts of 140 E80 characters, and fact-based disinformation falls categorically outside lexical detection scope. Phase 2 architectural design priorities: dynamic threshold adjustment (short-text mode) and thread-level aggregation.

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

Additionally, EVT variables not currently covered by R8's lexical architecture  Especifically Self-schema manipulation ("discover your true self") and Personal goal targeting ("what is your dream?")  Erepresent structural targets for the second detection layer. These patterns correspond to the paragraph-level sequencing identified in Section 2.8 and align with Cialdini's (1984) commitment and consistency mechanisms. Detecting Self-schema and Personal goal manipulation requires structural pattern recognition beyond the scope of surface lexical density, and is positioned as a Phase 2 design priority.

Phase 2 will also investigate the independent operationalization of scarcity signals as a dedicated detection category (ScarcityRisk). In the current implementation, scarcity-compatible vocabulary is distributed across FearRisk, AbsolutistWords, and ClickbaitRisk without a unified detection architecture. Brock's (1968) commodity theory and Brehm's (1966) psychological reactance theory provide the theoretical basis for treating scarcity signaling as a structurally distinct manipulation mechanism warranting independent detection. Five lexical sub-types are proposed for ScarcityRisk operationalization: temporal scarcity ("today only," "deadline"), quantitative scarcity ("only 3 remaining," "limited to 50"), informational scarcity ("what only a few know," "not publicly available"), relational scarcity ("exclusively for you," "specially selected"), and opportunity scarcity ("this chance will never come again"). Critically, Phase 1 calibration observations indicate that these sub-types rarely appear in isolation in high-risk texts; rather, they co-occur in combination patterns that produce amplified persuasive effects beyond what linear score aggregation captures (Fromkin & Brock, 1971). Phase 2 will investigate weighted co-occurrence scoring for ScarcityRisk sub-type combinations as an approach to approximating these interaction effects within the current lexical architecture.

### 7.3 Phase 2: Transformer-Based Contextual Analysis

Following corpus expansion and reliability establishment, integration of transformer-based language models for contextual disambiguation is identified as a significant development direction. This development is framed as complementary rather than replacement.

### 7.4 Phase 2 E: Toward a Non-Linear Detection Model and Multi-Stage Architecture

The current CMI is computed as a linear weighted sum of lexical category scores. This architecture assumes that the persuasive risk contribution of each signal type is additive and independent  Ean assumption that Phase 1 observations suggest is empirically incomplete.

Two non-linear effects are identified as Phase 2 E research priorities. The first is the interaction effect between positive and negative valence signals. It is theoretically hypothesized that texts combining high-density affirmatively valenced vocabulary (EmotionalRisk) with high-density negatively valenced vocabulary (FearRisk) may produce persuasive effects exceeding the prediction of linear score aggregation, consistent with Kahneman's (2011) negativity dominance finding: negative signals are processed with higher priority than positive signals of equivalent magnitude, so sequential positive-then-negative structures do not cancel but amplify. A preliminary examination of Phase 1 corpus data provides limited directional support for this hypothesis. When documents are partitioned by EmotionalRisk and FearRisk density (threshold ≥ 0.5), the group exhibiting simultaneous high density in both categories (n=16, excluding intent-unresolved documents) shows a human HIGH-label rate of 87.5%, compared to a linear additive prediction of 69.6% derived from the single-category groups (EmotionalRisk-only high: 57.1%, n=49; FearRisk-only high: 82.1%, n=28). The 17.9 percentage-point gap is directionally consistent with an interaction effect. However, three constraints preclude stronger inference: the sample of 16 documents is insufficient for statistical testing; the exclusion of 7 intent-unresolved documents (corpus ID: note219–note228) materially affects the result (inclusion reduces the gap to ∁E.2 percentage points); and the observed pattern may reflect confounding variables rather than a true interaction between EmotionalRisk and FearRisk. Both figures are reported in the interest of transparency. This interaction hypothesis is proposed as a priority target for Phase 2 empirical investigation with an expanded, independently annotated corpus.

The second is the threshold effect in multi-signal combinations. Phase 1 calibration observations are consistent with the hypothesis that manipulation-compatible signals do not produce proportional effects across their full range, but rather exhibit threshold behavior: below a signal density threshold, effects are sub-linear (weak or absent); above the threshold, effects become supra-linear (rapidly amplifying). This structure is theoretically grounded in Granovetter's (1978) threshold model of collective behavior, which demonstrates that individual response thresholds determine when and whether cascades of behavior propagate through a population. Applied to text-based manipulation, the threshold model predicts that: (1) individual readers have personal response thresholds determined by cognitive vulnerability; (2) CMI scores below a reader's threshold produce minimal compliance effects regardless of absolute score magnitude; and (3) CMI scores that cross the threshold trigger disproportionately amplified responses, consistent with the phase-transition structure of collective behavior cascades.

A candidate mathematical formalization of this threshold structure is the sigmoidal transformation:

CMI_nonlinear = 1 / (1 + e^(−k(CMI_linear ∁Eθ)))

where θ represents the individual response threshold and k represents the slope parameter governing the steepness of the transition. This formalization is proposed as a theoretical framework for Phase 3 empirical investigation. The current corpus of 225 documents with single-rater annotation is insufficient to estimate the parameters θ and k, and the absence of behavioral outcome measures (compliance rates, financial losses, recruitment success) makes empirical validation of the threshold model impossible at this stage. The proposal is presented as a research direction rather than an implemented component.

The multi-stage detection architecture that follows from this theoretical framework is structured as follows. Phase 1 lexical screening (current implementation) functions as a first-stage filter, efficiently excluding documents with CMI below 35 from further processing while directing MEDIUM and HIGH documents  Eand LOW documents with specific co-occurrence patterns  Eto second-stage analysis. Phase 2 structural detection applies co-occurrence pattern weighting, paragraph-sequence analysis, and ScarcityRisk combination scoring to the non-cleared subset. Phase 3 contextual and behavioral modeling integrates transformer-based disambiguation, reader vulnerability profiling, and empirical threshold estimation where behavioral outcome data become available. This staged architecture is designed to maximize detection utility at each phase while maintaining transparency about the limitations of each analytical layer.

The threshold model introduced above also provides the conceptual foundation for a complementary construct: the Cognitive Vulnerability Index (CVI). While CMI quantifies the manipulation-compatible signal density of a text  Ea property of the sender  ECVI would quantify the cognitive vulnerability of the reader as the threshold parameter θ that determines when CMI signals produce behavioral effects. The theoretical basis for CVI derives directly from Cialdini's (1984) empirical observation that susceptibility to consistency-based persuasion increases with age (p. 177), Milgram's (1974) documentation of authority submission as an individual-difference variable, and Altemeyer's (1981) Right-Wing Authoritarianism scale, which identifies dispositional tendencies toward authority deference, conventionalism, and out-group hostility as measurable individual differences that correspond structurally to R8's AuthorityRisk, AbsolutistWords, and EnemyFrame categories. A full CVI operationalization is beyond the scope of the current research; it is proposed here as a Phase 3 theoretical target whose development depends on Phase 2 empirical foundations.

A further theoretical extension concerns the directionality of manipulation vectors. The current R8 architecture treats texts as directed at an external audience  Ewhat may be termed an outward manipulation vector. However, organizational and institutional texts often function simultaneously across multiple audience dimensions: externally toward the public or media, internally toward organizational members, and reflexively toward the text's author as a mechanism of self-justification. Festinger's (1957) cognitive dissonance theory predicts that inward-directed manipulation  Ethe rhetorical reinforcement of an organization's own normative framework in the face of contradictory evidence  Eintensifies rather than resolves when external pressure increases. Empirical candidates for this inward-vector pattern include government crisis-response texts, corporate incident communications, and institutional denial statements, which Phase 1 calibration identified as a systematic false-negative category: high human-label risk but low automated CMI, attributed to the absence of cult- or commercial-genre vocabulary in bureaucratic register. Operationalizing vector directionality  Edistinguishing outward persuasion from inward self-legitimation  Eis identified as a Phase 2 corpus design priority and a Phase 3 modeling target.

### 7.5 Phase 3: Multilingual Extension

Extension to English-language analysis is a potential direction pending Phase 2 validation outcomes.

### 7.6 Phase 3: AI-Generated Text Analysis

A longer-term research direction extends R8's framework to the analysis of AI-generated communication. Whether R8's lexical categories are sensitive to sycophantic bias patterns in AI-generated text is an open empirical question that cannot be meaningfully investigated until the framework's validity on human-authored text has been established in Phase 2.

### 7.7 Phase 3: Multimodal Extension

Extension to audio and video content is technically feasible by placing a speech-to-text conversion stage (e.g., Whisper) prior to the R8 pipeline. Theoretical grounding: Janis (1972) documented that defective decision-making patterns manifest in leaders' public statements, providing a basis for extending manipulation signal detection to spoken discourse.

---

## 8. Conclusion

R8 presents a first-generation lexical framework for approximating cognitive manipulation risk in Japanese-language text. By operationalizing 12 theoretically grounded risk categories into a single composite index  Ethe Cognitive Manipulation Index (CMI)  Ethe system provides a transparent, reproducible, and scalable screening tool for identifying texts that warrant closer scrutiny. The system is explicitly positioned not as a definitive classifier of manipulative intent, but as an initial flag that complements rather than replaces human judgment.

The theoretical framing of R8 integrates cognitive psychology (Kahneman, 2011), social psychology (Janis, 1972; Milgram, 1974; Zimbardo, 2007), Japanese organizational sociology (Tobe et al., 1984; Yamamoto, 1977; Nakane, 1967), and clinical psychology of manipulation (Symington, 1993). The novel contribution of this research lies in integrating these previously disconnected theoretical domains under the unified lens of "linguistic signals targeting System 1 cognitive processing," and operationalizing this integration as a quantifiable lexical instrument for Japanese text.

Phase 1 calibration identified three principal findings. First, CMI achieves its highest detection performance for politically framed content combining EnemyFrame, Propaganda, and FearRisk simultaneously. Second, commercial manipulation content systematically evades HIGH classification through surface-positive vocabulary, establishing the central diagnostic finding of Phase 1. Third, calibration confirmed that lexical density scoring produces systematic false negatives for sophisticated manipulation and systematic false positives for argumentative analytical prose, establishing the empirical ceiling of the lexical-only approach.

The limitations of the current implementation are substantial and explicitly acknowledged. These limitations define the Phase 2 research agenda: validated corpus expansion with independent inter-rater annotation; development of a second detection layer targeting structural manipulation patterns; and construction of a contrastive corpus enabling false-negative detection.

R8 is released as open-source software with the explicit acknowledgment that it is a first approximation. The value of this release lies in establishing a transparent, reproducible baseline  Eone that documents the ceiling of lexical detection before the transition to structural and semantic analysis, and that positions Japanese-language cognitive manipulation research within the broader international conversation on computational detection of persuasive and deceptive text.

---

## References

Altemeyer, B. (1981). Right-wing authoritarianism. University of Manitoba Press.

Arai, N. (2018). Robotto wa toudai ni haireruka [Can a robot get into Tokyo University?] (Rev. ed.). Shin-yo-sha.

Baumeister, R. F., & Leary, M. R. (1995). The need to belong: Desire for interpersonal attachments as a fundamental human motivation. Psychological Bulletin, 117(3), 497 E29.

Brehm, J. W. (1966). A theory of psychological reactance. Academic Press.

Brock, T. C. (1968). Implications of commodity theory for value change. In A. G. Greenwald, T. C. Brock, & T. M. Ostrom (Eds.), Psychological foundations of attitudes (pp. 243 E75). Academic Press.

Cialdini, R. B. (1984). Influence: The psychology of persuasion. Harper Business.

Eccles, J. S., & Wigfield, A. (2002). Motivational beliefs, values, and goals. Annual Review of Psychology, 53, 109 E32.

Festinger, L. (1957). A theory of cognitive dissonance. Stanford University Press.

Fromkin, H. L., & Brock, T. C. (1971). A commodity theory analysis of persuasion. Public Opinion Quarterly, 35(3), 367 E77.

Granovetter, M. (1978). Threshold models of collective behavior. American Journal of Sociology, 83(6), 1420 E443.

Granovetter, M., & Soong, R. (1983). Threshold models of diffusion and collective behavior. Journal of Mathematical Sociology, 9(3), 165 E79.

Hathaway, S. R., & McKinley, J. C. (1943). The Minnesota Multiphasic Personality Inventory. University of Minnesota Press.

Janis, I. L. (1972). Victims of groupthink: A psychological study of foreign-policy decisions and fiascoes. Houghton Mifflin.

Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus and Giroux.

Milgram, S. (1963). Behavioral study of obedience. Journal of Abnormal and Social Psychology, 67(4), 371 E78.

Milgram, S. (1974). Obedience to authority: An experimental view. Harper & Row.

Nakane, C. (1967). Tate-shakai no ningen kankei [Human relations in a vertical society]. Kodansha.

Ross, R. A. (2014). Cults inside out: How people get in and can get out. CreateSpace.

Sunstein, C. R. (2017). #Republic: Divided democracy in the age of social media. Princeton University Press.

Symington, N. (1993). Narcissism: A new theory. Karnac Books.

Tobe, R., Teramoto, Y., Kamata, S., Suginoo, Y., Murai, T., & Nonaka, I. (1984). Shippai no honshitsu [The essence of failure]. Diamond.

Toyama, S. (1983). Shikou no seirigaku. Chikuma Shobo.

Yamamoto, S. (1977). Kuuki no kenkyuu [A study of "air"]. Bungeishunju.

Zimbardo, P. G. (2007). The Lucifer effect: Understanding how good people turn evil. Random House.

Ben-Ghiat, R. (2020). Strongmen: Mussolini to the present. W. W. Norton.

Da San Martino, G., Yu, S., Barrón-Cedeño, A., Petrov, R., & Nakov, P. (2019). Fine-grained analysis of propaganda in news articles. EMNLP 2019, 5636 E646.

Da San Martino, G., Barrón-Cedeño, A., Wachsmuth, H., Petrov, R., & Nakov, P. (2020). SemEval-2020 task 11: Detection of propaganda techniques in news articles. SemEval 2020, 1377 E414.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33(1), 159 E74.

Pennebaker, J. W., Boyd, R. L., Jordan, K., & Blackburn, K. (2015). The development and psychometric properties of LIWC2015. University of Texas at Austin.

Wang, Y., Yang, I., Hassanpour, S., & Vosoughi, S. (2024). MentalManip: A dataset for fine-grained analysis of mental manipulation in conversations. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 3747 E764). Association for Computational Linguistics.

---

## AI Disclosure

This paper was developed with AI assistance (Claude, Anthropic; Gemini, Google). The conceptual framework, theoretical integration, and research direction are the original work of the author. AI tools were used for drafting, translation, and code implementation support.

本論文はClaude（Anthropic）およびGemini（Google）のAI支援のもとで執筆された。概念的枠組み、理論統合、研究方向性は著者のオリジナルである。AIツールは草稿作成、翻訳、コード実装支援に使用された。
---
