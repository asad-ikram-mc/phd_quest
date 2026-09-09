# ATTACK ON THE DRAFT — v1 of the research project report
# 9 September 2026. Six adversarial lenses, 76 objections raised, triaged to what actually matters.
# Every load-bearing claim below was verified by me against the primary source, not taken on trust.

## THE VERDICT FIRST

This is a real proposal. It has an architecture, a manipulated variable, a declared unit of analysis
with the clustering handled, an attempt at judge-error correction, a cost line, and a paragraph that
names what you cannot do. Nothing else in this repository is at that level, and the thesis sentence
is correct and survived every attack:

> **live-web audits cannot say why, because the auditor never knows what the agent could have retrieved**

Do not touch that sentence. What follows is what will lose you the scholarship if left alone.

## MECHANICAL

| Section | Chars | Limit | Note |
|---|---|---|---|
| Summary | **499** | 500 | **One character spare.** Any correction breaks it. |
| Description | 5,560 | 4,000–8,000 | |
| Motivations | 1,863 | 2,000 | |
| **Total** | **7,922** | **8,000 under the strict reading** | **78 spare** |

Legal under both readings of the ambiguity, but you have almost no headroom. Every fix below names
what to cut to pay for it. **3 MB PDF limit** — you are at 11.5 KB, no issue.

---

# THE FOUR THAT WOULD COST YOU THE PLACE

## 1. FATAL — the GUIDE-LLM sentence is factually wrong, and your own citation disproves it

> "the TikTok audit ships on a kappa of 0.42 with a censored annotator, and GUIDE-LLM, which he
> co-signed in Nature Human Behaviour, asks for psychometric validation that nobody in the group
> has yet performed"

**I verified all three parts. Two are wrong.**

- **κ = 0.42 is real** — Saffari & Pierri report "aggregate kappa = 0.42" for Gemini 2.5 Flash,
  best of four multimodal LLMs. **But it is the agreement of the LLM annotator against native-speaker
  labels on a 300-video reference set.** It is a validation figure they report in their own abstract,
  not a quality floor they overlooked. "Ships on" accuses them of missing what they foreground.
- **"Censored annotator" is accurate** — their limitation section says the provider safety layer
  refuses ~1.1% of inputs non-randomly by harm category, so prevalences are under-estimates. But
  again: **they say it themselves.**
- **GUIDE-LLM does not ask for psychometric validation.** I pulled the checklist. Item **E.1 is
  "Human validation of LLM outputs"**, asking for inter-rater reliability, Cohen's κ or
  Krippendorff's α. There is no psychometric item. You have told a co-author what his own checklist
  says, incorrectly.
- **"Nobody in the group has yet performed it" is falsified by the paper you cite two clauses
  earlier.** Saffari & Pierri validated four models against human labels and reported the κ. That
  *is* E.1, performed. Nogara et al., also in your bibliography, is a second counter-example.

So the sentence grades three of the deciding supervisor's papers and gets two of the three wrong,
and one of those papers is first-authored by a PhD student in the group you are applying to join.
Pierri's reply is one sentence long and it is a quotation of his own abstract.

**What must change.** Cut to one target: the Chinese-web "circular noise" concession. It is the only
one of the three that quotes the paper's own limitation section, and it is the only one your
ArtemisAI moving-reference story actually answers. Delete the κ figure, "censored", and the
"nobody has yet performed" assertion. Do not soften them — remove them.

**This releases characters rather than spending them.**

## 2. FATAL — the central novelty claim is false, and I verified the counterexamples

> "Nobody varies the retrieved evidence set under experimental control"

**Two real papers, both checked by me directly on arXiv:**

- **"The Synthetic Web: Adversarially-Curated Mini-Internets for Diagnosing Epistemic Weaknesses of
  Language Agents"** — Shah & Ozgur, arXiv **2603.00801**, 28 Feb 2026, revised 16 Aug 2026. A
  procedurally generated environment of thousands of hyperlinked articles **with ground-truth labels
  for credibility and factuality**, served to agents through search and read tools, with a
  high-plausibility misinformation article **injected at a controllable search rank** to measure
  causal effects across six frontier models, with elicited confidence. Its title contains
  "Epistemic Weaknesses of Language Agents." It is not in your bibliography.
- **"Retrieval Collapses When AI Pollutes the Web"** — Yu, Kim & Kim, **The Web Conference 2026**,
  arXiv **2602.16136**, 18 Feb 2026. Dose-response contamination of a retrieval pool by
  AI-generated documents with per-document provenance in separately labelled pools; 67% pool
  contamination produces over 80% exposure contamination. **That is Study A's manipulation, at a
  top venue, six months before your deadline.**

An absolute-priority claim in a literature moving this fast needs only one counterexample to fail,
and the reviewer's conclusion is not "derivative" but "does not know his own field." That is
unrecoverable in a 55-point document.

**What must change.** You do not need the whole territory, and the good news is that **your genuinely
unoccupied axis is already in your own provenance record.** Everyone above controls *credibility* or
*factuality* of a source. Nobody manipulates **derivation depth of a true claim** — original,
syndicated copy, paraphrase, AI rewrite — which is exactly what evidence laundering is and exactly
what your schema encodes. Narrow the claim to that axis, cite both papers, and position against them.
The Synthetic Web has no derivation relation. "Retrieval Collapses" has no agent, no browsing, no
multi-turn. Those two gaps are yours and they are defensible.

## 3. FATAL — the only cost line states the small cost precisely and omits the dominant one

> "about 2,000 euros a year, plus roughly 500 euros of API spend per study"

Then, uncosted: **500 double-annotated agent trajectories at κ ≥ 0.75**, human usefulness ratings on
held-out tasks, and the same again in Italian and Urdu. Agent trajectories are long multi-step
documents. That is hundreds of person-hours and five figures of euros, against a PoliMi PhD research
allowance of roughly €1,600 a year. There is no annotator source, no compensation, no pilot, no
codebook, no adjudication rule, no ethics route, and no fallback if κ lands below 0.75 — promised by
someone who states in the same paragraph that he has never run a human-subjects study.

Pierri publishes cost lines. Saffari's TikTok audit has one. The omission is conspicuous precisely
*because* you costed the GPU.

**What must change.** Two things. Give the annotation its own line: unit, source, cost, ethics route
and lead time. And **change the unit from the whole trajectory to the claim-citation pair** — κ is
computable on a claim-citation pair and barely meaningful on a whole trajectory, and it changes the
arithmetic in your favour.

**Pay for it by deleting the euro figures you already have.**

## 4. FATAL — count the workstreams on your own page

Environment, corpus, human-validated claim set, Study A, Study B, human reference set, validated LLM
judge, trained gate, adversarial robustness arm, usefulness study, two scaffolds, open-weight arm,
frontier arm, Italian, Urdu, an annual dataset release, and an environment-swap demonstration that is
promised in the last paragraph and never designed. **Sixteen workstreams in 36 months**, three of them
things you have just said you have never done, plus coursework and a six-month secondment.

**What must change.** Name a core and label the rest contingent: environment + Study A + the gate is
the core; Study B, the adversarial arm and any non-English replication are extensions conditional on
the first result. Add a compressed three-year progression. **There is currently no timeline anywhere
in the document.**

---

# THE SHARP ONES

## 5. Study A's primary outcome is not identifiable as designed

The original is in the retrievable set at every dose. So "the agent read the original and cited the
original" produces **exactly the same observable record** as laundering. Telling them apart requires
attributing answer text to a specific retrieved document, and your derivatives are by construction
near-duplicates of their originals, so lexical and embedding similarity have their *lowest*
discriminative power precisely where the outcome is decided.

**The cheapest edit in the document relative to what it rescues:** plant a distinguishing marker — a
unique figure, name or phrasing — present only in the derivative and absent from the original.
Marker-in-answer plus citation-to-original is then unambiguous laundering, by construction, with no
judgement call. This makes your headline study identifiable.

## 6. The ranker is an uncontrolled confound that swallows the dose

Your manipulated variable is defined over the **corpus**, but the agent only ever sees the top-k
**BM25 returns**. AI-rewritten derivatives are cleaner, more keyword-dense and lexically closer to the
query than the originals they derive from, so they will systematically outrank them. Your "50 percent"
condition is therefore not *more derivatives*, it is *derivatives at the top of the list*. Share and
rank position are entangled and rank position dominates.

**Move the dose from the corpus to the served result list**, with planted documents stratified across
rank positions so share and position are orthogonal. Declare the retriever as a versioned factor with
its analyzer, field weights, k, and deduplication policy.

## 7. "Unmodified agent" is false, and the hostnames are a legal problem

Serving HTTPS for a **real** hostname needs your private root CA in the client trust store — that is
a modification of the execution environment, and it constrains which scaffolds you can intercept at
all, which is a feasibility problem for your replication arm. Separately, serving mirrored publisher
text **and AI-fabricated derivatives** under real outlets' identities is impersonation with copyright
and ToS exposure, and you propose to *release* it.

**Resolve the disjunction in the text: seeded hostnames only**, one registered domain with per-outlet
subdomains and a publicly trusted wildcard certificate, so no trust store is touched. Then state
precisely what is unmodified (weights, harness commit, prompt) and what is configured (proxy, DNS).

## 8. The DeepTRACE title in your bibliography is not the paper's title

You have: *"DeepTRACE: Auditing Citation and Evidence Reliability in Generative Search Engines and
Deep Research Agents."*

The real title is: **"DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across
Citations and Evidence"** (Venkit, Laban, Zhou, Huang, Mao, Wu). I checked it.

The ID and first author are right; the title is a plausible-sounding paraphrase. **That is the exact
signature of a machine-generated reference**, in a proposal whose thesis is provenance discipline,
against a call that prohibits AI-generated text and a portal tickbox about anti-plagiarism software.
It is also the paper a reviewer is most likely to open, because Study B is built on its dimensions.

**Highest return per hour of anything in the nine days, and it costs zero characters:** open all
fourteen arXiv pages and check title, authors, year and version character by character. One
paraphrased title implies the list was never checked.

## 9. PPI is misstated, in front of a group that uses it

> "its sensitivity and specificity correct the reported rates by prediction-powered inference"

PPI does not work through sensitivity and specificity. It computes the estimate on the
machine-labelled set and debiases it with a **rectifier**: the mean discrepancy between human and
predicted label on a **randomly sampled labelled subset**. Sensitivity-specificity prevalence
correction is a different estimator. Egami's DSL is a third, inverse-probability-weighted.
You have cited all three and described none of them.

The commitment is right and it is your methodological spine. The mechanism must be corrected.

## 10. The Haig manuscript is missing from the honesty paragraph

Your "what I do not bring" paragraph lists your deficits in full and omits your only research
artefact. The measurement-equivalence manuscript — 500-replication simulation, pooled index reports
the wrong sign on roughly a quarter of days — is the methodological ancestor of this entire proposal
and the only existing evidence that you can pose a measurement question, design a simulation and
write it up. Without it, "can he do research" rests on 68 collectors.

**State it as a number, described accurately as an unpublished manuscript written under supervision.**
No venue. Not "in submission" unless literally true. **And post it to arXiv before 18 September if
Ella agrees** — an arXiv ID converts "claims to have a paper" into "has a preprint."

---

# THE ONES I RAISED SEPARATELY, STILL STANDING

- **Training contamination.** Half your corpus is mirrored from Common Crawl; Llama, Qwen and Mistral
  trained on Common Crawl. If the model memorised the original, planting a derivative tests recall,
  not retrieval-based laundering. You need a closed-book baseline per item, or post-cutoff/synthetic
  content for the claim set.
- **No bridge to the real web.** 20,000 documents over 300 domains is a village. Your own closing
  line — that a failure rate does not survive an environment swap — is also the argument that your
  rates do not transfer outward. Nothing validates in-environment behaviour against live behaviour.
- **The gate may be circular.** It is trained and evaluated where derivation position and
  AI-generation flags are true by construction. You criticise circular labelling in Pierri's work
  three paragraphs later. Also note: FORGE (arXiv 2606.13610) already reports a credibility
  re-ranking defence that removes only 17% of fake recommendations — that is now the number to beat,
  and the credibility-filtering genre (CrAM, RA-RAG, ReliabilityRAG, TrustRAG) is absent from your
  bibliography.
- **No ethics statement**, despite human annotators and human raters. You have Portsmouth
  TETHIC-2025-111094 already; this is cheap.
- **Urdu is unjustified.** Italian is obvious. Urdu triples annotation in a language nobody on the
  panel can check. Nogara et al. — in your bibliography, never cited in the body — is the
  justification if you keep it. Otherwise cut it and recover the characters.
- **Uncited references read as padding.** REFLECT, Zhu, Fontana are in the bibliography and never
  appear in the text. REFLECT belongs exactly where you validate the LLM judge.
- **"Scaffold effects exceed model effects" is uncited and the closest source contradicts it.** The
  scaffold literature reports large differences in *tokens per solved task* with score differences
  of 0–8 points, mostly not distinguishable from zero. Cut the justification clause; declaring the
  harness as a pinned factor needs no magnitude claim. **This frees 61 characters** and is your
  cheapest source of budget.

---

# WHAT NOT TO TOUCH

The hostile supervisor lens respected these. Protect them in revision.

1. **The thesis sentence.** The auditor never knows what the agent could have retrieved.
2. **The provenance record with derivation position.** Original, syndicated copy, paraphrase, AI
   rewrite. This is your unoccupied axis and every fix should narrow onto it.
3. **The ArtemisAI moment.** 71.6 to 85.8 while the reference moved from a human holdout to a model's
   labels. The most credible sentence you have written.
4. **"What I do not bring, I name."** Add the manuscript to it. Never soften it.
5. **The collection credential, stated concretely.** The bridge from the 45-point CV to the 55-point
   report.
6. **The CACM line** — the regulatory blind spot, "this call is that sentence turned into a
   programme." Best line in Motivations. It should open the rebuilt paragraph.
7. **"In return it supplies what I cannot supply myself."** Correct direction of dependency.
8. **The gate framed as weak-model oversight, evaluated on preserved usefulness as well as harm.**
   Objective 4 answered on its own terms.
9. **Pinned weights and pinned harness commit.** Correct reproducibility instinct — now apply the
   same reasoning to the corpus generators.

---

# ORDER OF WORK

| Priority | What | Cost |
|---|---|---|
| 1 | Verify all 14 references character by character | 0 chars, ~1 hour |
| 2 | Rebuild the Motivations sentence: one target, the circular-noise concession | **frees** chars |
| 3 | Narrow the novelty claim to derivation depth; cite both 2026 papers | ~neutral |
| 4 | Plant the distinguishing marker so laundering is identifiable | small |
| 5 | Move the dose to the served result list | small |
| 6 | Seeded hostnames only; say what is unmodified | small |
| 7 | Annotation cost line, unit changed to claim-citation pair | pay by cutting euro figures |
| 8 | Core vs contingent, plus a three-year progression | pay by cutting Urdu + scaffold clause |
| 9 | Correct the PPI mechanism | small |
| 10 | Add the manuscript; add one ethics clause | small |

**The Summary must be rewritten last and re-counted.** It is at 499 of 500.
