# Research plan draft, University of Helsinki university-funded doctoral position
# Call 24 Aug - 7 Sep 2026 · Doctoral Programme in Social Sciences · start Jan 2027
# Proposed supervisor: Dr Matti Nelimarkka (Social Computing Group)
#
# >>> SUPERSEDED 26 Aug 2026 as the lead pitch by
# >>> PROPOSAL_Calibrating_the_Observatory.md (LLM instruments: equivalence,
# >>> drift, standpoint; adversarially novelty-checked against the 2023-2026
# >>> literature and aligned to Matti's Observatory, MarxistLLM and validity
# >>> credo; PDF live on asadfix.github.io/helsinki_proposal). This file stays
# >>> as the fallback classifier-era plan and the template-notes archive.
#
# Status: DRAFT for joint preparation with the supervisor; conform to the DPSS
# template (section order, page limit) once Matti engages. Roughly 5 pages when
# formatted. British English, no dashes, plain prose throughout.

---

## Title

Is the Platform Part of the Measurement? Establishing, Testing and Correcting
Cross-Platform Equivalence of Machine-Labelled Public Opinion

## 1. Motivation and objectives

Computational social science now compares machine-labelled text across
platforms as a matter of course, and pooled multi-platform indices are treated
as measures of public opinion by researchers and by the institutions that buy
their outputs. These comparisons rest on an untested assumption: that a
classifier measures the same construct, on the same scale, on every platform it
reads. Survey methodology solved the structurally identical problem decades ago
by treating the mode of administration as part of the instrument and testing
measurement equivalence before comparing across modes. No such discipline
exists yet for machine-labelled platform data.

The doctoral project develops that discipline. Its core claim, set out in the
applicant's paper with Dr Ella Haig (arXiv, 2026), is that a platform is a
survey mode: affordances stand to posts as interview settings stand to answers,
and the psychometric equivalence toolkit, generalizability theory, measurement
invariance and differential item functioning, and score linking, transfers to
machine-labelled constructs with the platforms as the groups. The paper
specifies a six-step protocol and demonstrates, in a 500-replication simulation
with known ground truth, what assuming equivalence costs: a pooled index that
takes platform scores at face value misstates a known event shift by roughly an
eighth and reports the wrong sign of aggregate sentiment on nearly a quarter of
days, while a measurement-adjusted index avoids both errors. The doctoral
project executes and extends the empirical programme the paper pre-specifies.

Objectives. (O1) Execute the full four-platform application of the equivalence
protocol on freshly collected, event-window-scoped UK policy data. (O2) Extend
the protocol causally: decompose detected non-equivalence into affordance,
algorithmic and population components using within-user cross-posting and
event-based identification. (O3) Validate externally: benchmark platform-level
and adjusted estimates against probability-sample survey measures of the same
policy attitudes. (O4) Deliver an open protocol and software so that any
cross-platform study can test, rather than assume, comparability.

## 2. State of the art and the contribution

The position of this project relative to prior work was established by an
adversarial literature review conducted for the arXiv paper, and it is
deliberately narrow. That platforms differ is not the claim; that has been
shown repeatedly, including by Nelimarkka, Laaksonen, Tuokko and Valkonen
(2020), whose account of platformed interactions during the Finnish 2015
campaign demonstrates that the same actors and the same electoral moment take
structurally different communicative forms across platforms. Sen and colleagues
(2021) name the corresponding error class, platform affordance error, in their
total error framework for digital traces, but provide no formal test for it.
The measurement literature for machine-labelled text audits classifiers
(Jacobs and Wallach 2021; Atreja et al. 2025; Baumann et al. 2025) and corrects
label error against gold standards (Egami et al. 2023), while leaving the
platform an unmodelled stratum. The psychometric toolkit has reached survey
self-reports across platforms (Boyd et al. 2024), annotator facets (Kennedy et
al. 2020; Sachdeva et al. 2022), survey-versus-trace comparisons (Cernat et al.
2025), and time-grouped text scales within one platform (Pokropek 2026), and
generalizability designs have reached LLM annotation with prompt and model as
facets (Camuffo et al. 2026). None of these applies the equivalence toolkit to
machine-classified constructs with platform as the grouping facet. That
combination, formalising the affordance error Sen names and Nelimarkka's work
motivates, is the contribution, and it converts a documented qualitative
insight of the supervisor's own research programme into a quantitative
measurement discipline.

## 3. Research questions

RQ1. Do machine classifiers measure the same sentiment construct, on the same
scale, across platforms discussing the same policy events? (Invariance and DIF
with platform as group; two classifier arms so lexicon artefacts cannot pass as
mode effects.)

RQ2. Where equivalence fails, what produces the failure? Decompose platform
non-equivalence into affordance, algorithmic curation and population
components. (Within-user cross-posted content as the measurement bridge;
event-window designs around pre-specified fiscal and electoral anchors.)

RQ3. Can non-equivalent platform signals be linked into a defensible aggregate,
and how do adjusted estimates compare with probability-sample surveys of the
same attitudes? (Score linking with ex ante anchor purification; external
validation against survey benchmarks such as the British Election Study
series, and Finnish equivalents where the design is replicated.)

RQ4. What do the answers imply for practice? An open protocol, reference
implementation and reporting standard for cross-platform measurement claims.

## 4. Data and methods

Work package 1 (months 1 to 12): collection and instrumentation. Purpose-built,
window-scoped collection for fifteen pre-specified UK fiscal events (list and
dates frozen in August 2026, published in the arXiv paper), across the
platforms whose retrospective access permits dense windows; a pre-registered
density audit decides retention per platform-event cell. Two classifier arms
are trained by the documented procedure from the applicant's prior pipeline:
one lexicon-seeded, one fine-tuned on independently human-labelled data with no
lexicon ancestry. A stratified probability sample of 1,000 to 1,500 items,
double-coded on a 25 to 30 per cent overlap, provides the human criterion; the
annotation codebook, including a relevance item measuring per-platform topical
precision, is drafted.

Work package 2 (months 10 to 24): equivalence testing. Fixed-facet
generalizability studies with the criterion sample; multiple-group categorical
invariance models and per-event DIF under effect-size criteria, with anchor-free
DIF and alignment as identification checks; multilevel models with comments
nested in posts and events, platform contrasts reported with and without
reaction latency. All pre-specified in the arXiv paper.

Work package 3 (months 20 to 36): causal decomposition. Within-user
cross-posted content across platform pairs as a bridge that holds the author
fixed; comparisons of algorithmically curated versus chronological or search
retrieval where platform interfaces permit; population adjustment from profile
and behavioural covariates. This work package operationalises RQ2 and is
developed jointly with the supervisor, whose platformed-interactions lens
defines the affordance component.

Work package 4 (months 30 to 46): linking, external validation, and the
protocol release. Score linking under the pre-specified purification rule;
comparison of naive, platform-specific and adjusted series against survey
benchmarks on matched policy questions; the open protocol, software and
reporting checklist; thesis compilation.

## 5. Ethics and data protection

Public content only; GDPR basis and minimisation practices as in the
applicant's ethics-approved MSc work (University of Portsmouth,
TETHIC-2025-111094), re-approved for this project under University of Helsinki
procedures before collection; hashed identifiers; aggregate reporting;
paraphrased quotations; annotator compensation stated. Platform terms of
service govern collection modes per platform; the density audit tolerates the
resulting asymmetries by design.

## 6. Timetable and outputs

Four years from January 2027. Outputs: the executed application paper (target:
ICWSM or CSCW full paper, year 2); the causal decomposition paper (year 3); the
validation and protocol paper plus software release (year 4); article-based
thesis. The foundation paper (protocol and simulation, with Dr Ella Haig) is on
arXiv from 2026 and the doctoral work cites and extends it; the applicant's
engineering background (six years of production-scale platform data systems
for UK Government analytics; 500-scraper fleets at Dubizzle Labs) removes the
usual collection risk from the timetable.

## 7. Supervision and fit

The project sits squarely in the Social Computing Group's programme: it takes
the group's finding that platforms shape political communication (Platformed
Interactions, 2020) and builds the measurement theory that finding demands,
with the supervisor's computational-thinking-for-social-science framework as
its epistemological base. Requested supervision arrangement: Dr Matti
Nelimarkka (University of Helsinki) as principal supervisor; Dr Ella Haig
(University of Portsmouth) available as external co-supervisor or advisory
committee member, continuing the existing collaboration.

---

# Notes for Asad (not part of the plan)
- HARD CALL FACTS (verified 25 Aug on studies.helsinki.fi with the Social
  Sciences programme selected): single PDF max 5MB, Arial/Calibri 11, line
  spacing min 1.15; research plan MAX 5 PAGES incl. references ON THE MANDATORY
  TEMPLATE (PP26 Tutkimussuunnitelmamalli EN.docx) with per-section character
  caps: summary 1,000; theoretic rationale 3,000; objectives 1,500; methods and
  materials 4,000; data plan 1,000; ethics 1,000; timetable 3,000 (must include
  publication plan, funding plan for research costs, risk management, and "what
  makes it feasible in four years"). CV max 3 pages on template. SUPERVISION
  PLAN max 2 pages, SIGNED BY THE SUPERVISOR - Matti's signature is a hard
  prerequisite, not a courtesy. Evaluation: 50% plan quality / 30% feasibility
  / 20% CV, minimum 3/5 on every criterion. Form closes 7 Sep 23:59; questions
  answered only until 16:00 EEST that day. Interviews 2-4 Nov on Zoom; results
  end of Nov; contracts 4 years only, start 1 Jan 2027. Study right = separate
  application, autumn round 2-15 Sep.
- CRITICAL: the call REQUIRES an AI-use disclosure, and the admissions page
  states the application text "cannot be generated by AI". This draft is raw
  material: rewrite every section in your own words before it goes on the
  template, and disclose honestly whatever assistance you declare.
- Matti is a University Lecturer (Docent), not a professor; his process page
  asks for 2-3 months runway and a presentation to the group - the pitch page
  addresses the compression directly.
- Citation anchors that are actually IN Platformed Interactions: Alhabash and
  Ma 2017; Waterloo et al. 2018; Boczkowski, Matassi and Mitchelstein 2018;
  Tucker et al. 2018; Bucher and Helmond. Bossetta/Stier/Jungherr are NOT
  cited there. His own validity paper to echo: Berg and Nelimarkka 2023,
  JASIST (same images, different recognition services, divergent outputs).
- His live projects worth naming in conversation: Finnish Digital Observatory
  (2025-2030, PI), Maidem: Media AI and Democracy (2025-2028), Digital
  Ideologies, Lobbying in Social Media; book: Computational Thinking and
  Social Science (SAGE 2023), validity chapter is Ch. 12.

- The plan deliberately opens every section from Matti's own critique: novelty
  is positioned against HIS paper, and WP3 gives him ownership of the causal
  component. The three components from your 7 April email (invariance, causal
  decomposition, correction with survey validation) are all here, upgraded to
  the paper's machinery.
- Numbers quoted match the arXiv paper exactly (an eighth; a quarter of days;
  500 replications; 15 events; 1,000 to 1,500; 25 to 30 per cent overlap).
- Once Matti engages: conform to the DPSS template (fetch the
  programme-specific instructions from studies.helsinki.fi with him), agree
  the platform set for WP1, and let him reshape WP3.
- Two applications, remember: the position application (24 Aug - 7 Sep, this
  plan, jointly prepared) AND the separate study-right application to the
  Doctoral Programme in Social Sciences (its own call; confirm dates on the
  programme page).
