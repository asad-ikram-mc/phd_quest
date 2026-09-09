# WRITING BRIEF — the PoliMi research project report
# Everything you need before you write. No sentences to paste; that is the point.
# 9 September 2026. Deadline 18 September 14:00 Rome (17:00 Pakistan).

**How to use this.** Read Part 1 and Part 2 first, they set the shape. Parts 3 to 5 are the three
sections you write, each with its budget and the questions it must answer. Parts 6 to 10 are the
research and the facts you draw on. Part 11 is the order to write in.

**What I will not do.** Art. 3 permits AI only for correcting text you have written entirely.
So there are no example sentences, no openers, no "you could say" anywhere in this file. What is
here is: what each section must accomplish, how long it can be, what is already published so you do
not propose it, what you can truthfully claim, and what the committee will ask. That is a supervisor's
briefing, not a draft. When you have written a section in full, I can correct it, and we declare that.

---

# PART 1 — THE CHARACTER BUDGET, AND THE TRAP IN IT

## The ambiguity

The **template** assigns the range to one field:

| Field | Template limit |
|---|---|
| Summary | max 500 |
| Project description | **4,000–8,000** |
| Motivations | max 2,000 |

But **Art. 3 of the call** states "minimum 4,000, maximum 8,000 characters" for **the report**.
The template's fields sum to 10,500. Both cannot be right, and no PoliMi document resolves it.
It is question 4 in the email to PhD-INF@polimi.it.

## The budget that is safe under BOTH readings

You do not have to wait for their answer. There is an intersection.

If the 8,000 cap is the whole report, then Description ≤ 8,000 − 500 − 2,000 = **5,500**.
If the range applies to Description alone, Description must be **≥ 4,000**.
**So anything between 4,000 and 5,500 characters of Description satisfies both readings at once.**

**Write to this:**

| Section | Target | Hard ceiling |
|---|---|---|
| Summary | **480** | 500 |
| **Project description** | **5,200–5,400** | 5,500 |
| Motivations | **1,900** | 2,000 |
| **Total** | **~7,780** | 8,000 |

That is roughly **1,150 words of description**, plus 80 for the summary and 320 for the motivations.
About **1,550 words in total.** It is short. Every sentence has to carry weight.

If PoliMi answers that the range governs the Description alone, you can expand toward 8,000 in the
last two days. Do not build a 7,500-character Description first and try to cut it; write to 5,400
and expand only if permitted.

**Count with:** `python3 count_chars.py proposal.txt` — characters including spaces, bibliography
excluded, which is what the call actually measures.

**File limit: 3 MB PDF.** The portal widget says 10 MB. The widget is wrong.

---

# PART 2 — WHAT YOU ARE ACTUALLY BEING SCORED ON

**55 of 100 points.** The CV is 45. You need ≥60/100 **and** a separate judgement that the research
topic fit is suitable. Both, cumulatively. There may be an informal interview; it carries no points.

**One position. One scholarship.** The group already has 5 PhD students, 1 full professor,
1 associate, 2 assistant professors.

## The two readers want different things

**Francesco Pierri** wrote this call. He is an empirical auditor of deployed information systems who
ships artefacts: multi-platform datasets, sockpuppet audits, cross-system comparisons, and since 2026
Prolific experiments with IRB approval. His signature is LLM-as-annotator at scale, always validated
against a small human reference set with a reported agreement coefficient. He does **not** do
mechanistic interpretability, activation steering, generative fine-tuning, formal causal inference,
or **any psychometrics**. He co-authored GUIDE-LLM in *Nature Human Behaviour*, which demands
psychometric validation of LLM measurement, and has never performed any.

**Marco Brambilla** is a different audience entirely. Full professor, head of the Data Science Lab.
His listed interests include **Data Extraction and Scraping**, streaming data management, crowdsourcing,
explainable AI, and LLMs inside graph-based RAG architectures. He is infrastructure and architecture,
not misinformation sociology.

**The consequence for your document.** A proposal that is all social-science framing with no
architecture loses Brambilla. A proposal that is all pipeline engineering loses Pierri. **The middle
of your Description has to contain a real, nameable architecture** — how a corpus is built, indexed
and served to an agent — and that is the part Brambilla will read closely. It is also the part
where your seven years stop being a curiosity and become core competence.

---

# PART 3 — THE SUMMARY (480 characters, about 80 words)

500 characters is three or four sentences. The template asks for three things and you must hit all
three in that space:

1. **Problem statement**
2. **Main expected results**
3. **Originality**

**Questions it must answer:**
- What is the failure being measured, in one clause?
- What is built or produced that does not currently exist?
- What is the one sentence that says why nobody has done this?

**Do not** spend characters on context, on the importance of AI, or on yourself. At 480 characters
there is room for the claim and nothing else. Write this **last**, after the Description exists.

---

# PART 4 — THE PROJECT DESCRIPTION (5,200–5,400 characters, about 1,150 words)

The template asks for "detailed description of the research project, emphasizing original and
innovative aspects and scientific relevance."

## A working allocation

This is a suggestion of proportion, not a template to fill. Adjust it, but know what you are trading.

| Part | Characters | Roughly |
|---|---|---|
| The problem and the gap | 900 | 200 words |
| **The architecture: how the environment is built and served** | **1,400** | **300 words** |
| The studies / work packages | 1,600 | 350 words |
| The safeguard (objective 4) | 700 | 150 words |
| Feasibility, risks, what you do not bring | 500 | 110 words |
| Contribution | 300 | 65 words |

**The architecture section is the one most applicants will not have.** Give it the space.

## The questions this section must answer

**On the gap:**
- Everyone varies the model, the judge, the prompt, the persona and the harness, because those are
  free. What is the variable nobody varies, and why is it expensive to vary?
- Why does the expense of it *cause* the gap, rather than the gap being an oversight?

**On the architecture — this is the technical heart and the committee will press here:**
- How do you serve a provenance-controlled corpus to an agent that browses live, **without the whole
  thing collapsing into an offline replay?** Proxy interception, index substitution, seeded domains
  registered and populated, or a hybrid? Name one and say why.
- What exactly do you control about each document: source identity, provenance chain, factual
  status, quality signals, contamination, recency?
- How many documents, over how many domains, and what does it cost to build and hold for three years?
- **What is the harness, and is it declared as a controlled factor?** The literature says the
  scaffold dominates the result. If this is not named early you look unread.
- Which agent stack: open-weight models pinned locally, frontier models by API, or both? If the
  models you anchor on are deprecated in year two, what survives? (Pinned open weights are the only
  clean answer.)

**On the studies:**
- Which of the six named failure modes do you actually take? *Evidence laundering, source omission,
  overconfident synthesis, bias amplification, sycophancy, susceptibility to adversarial or
  manipulated content.* Taking two properly beats gesturing at six.
- What is the manipulation in each study, and what is measured in response?
- What is the **unit of analysis**? Items inside one agent trajectory share retrieved context and
  memory, so local independence fails. What is your answer: trajectory-level units, or explicit
  dependence modelling?
- What is your **ground truth for evidence quality, and who validated it?** If the answer is an LLM,
  the REFLECT benchmark says the best judges are under 55% accurate and worst precisely on evidence
  verification. Name a human reference set, its size, and a target agreement coefficient. Pierri
  reports one in every paper; its absence will be noticed.

**On the safeguard — do not skip this:**
- **What is the one measurable intervention, and how would you know it worked?** Objective 4 asks for
  source verification, provenance-aware generation, weak-model oversight, model steering or
  interaction-design interventions, "while preserving usefulness, personalisation and user agency."
- Against what is it evaluated: robustness, computational cost, usability, preserved usefulness?
- A thesis that only reports that measurement is hard will lose this scholarship to someone who
  builds something. The verdict on one of the rejected angles put it plainly: **there is no safeguard
  for Cloudflare.** Make sure yours has one.

**On feasibility and honesty:**
- Why can *you* stand this environment up and keep it alive for three years?
- What do you not bring? Name it before they find it. The Agder proposal's Section 9 is the model:
  it named no extremism background, no Norwegian, no qualitative interviewing, R functional rather
  than fluent — and sized the studies accordingly. That paragraph is why that document reads as
  honest rather than promotional.

---

# PART 5 — THE MOTIVATIONS (1,900 characters, about 320 words)

"Reasons that led to wanting to carry out research at the Polytechnic of Milan."

This is not a personal statement and not a CV summary. It is: **why here, and why not anywhere else.**

**Questions it must answer:**
- What specifically about **this group** — not this university, not Italy?
- Pierri's DSA work and Brambilla's data-extraction and RAG work sit either side of your project.
  What does each of them supply that you cannot supply yourself?
- What can you do here that you could not do in industry, or alone?
- Why a PhD now, after seven years of building the instruments?

**Concrete PoliMi facts you can use, all verified:**
- The scholarship carries **€750/month for up to 6 months abroad**, which is a real research plan
  item, not a perk.
- The group is **1 full professor, 1 associate, 2 assistant professors, 5 PhD students** — a group
  with existing students working on exactly this material.
- Pierri's *Communications of the ACM* article (Sept 2026, with Araujo, Kruikemeier, Lorenz-Spreen
  and others) argues that LLMs *"meet all the criteria of the DSA"* and that their integration into
  search and social platforms is a **"regulatory blind spot"** that "should be urgently addressed."
  That sentence is the intellectual charter of the call you are applying to.
- The same paper names the **"circular problem of resources"**: you need data to win grants and
  funding to survive the data-access process.
- Brambilla's lab lists **Data Extraction and Scraping** as a stated research interest.

**Do not**: flatter the university, list rankings, or say Milan is a wonderful city.
**Do not** repeat the Description. Every character here should be unavailable to any other applicant.

---

# PART 6 — THE RESEARCH: WHAT IS ALREADY DONE, SO YOU DO NOT PROPOSE IT

Eleven agents researched this. Four angles were tested adversarially. **All four were refuted as the
spine of a thesis.** Every one was the same move — port psychometrics to LLM evaluation — and between
April and August 2026 at least six groups made that move and published it.

## The four dead angles, and who killed them

| Angle | Killed by |
|---|---|
| Live-web vs fixed-corpus retrieval auditing | Gundelach, Mühlhäuser & Herrmann, **arXiv 2606.14525**, Jun 2026 — 10,000 sites × 4 browser configs. Personalisation and geography solved by Hannak (WWW 2013), Kliman-Silver (IMC 2015), Urman/Makhortykh/Ulloa (2022). Also: **there is no safeguard for Cloudflare**, so it cannot reach objective 4 |
| LLM-as-ground-truth error propagation | **Solved and packaged**: Prediction-Powered Inference (Angelopoulos et al., *Science* 2023), control variates (Chaganty, ACL 2018), DSL (Egami). Domain half owned by **REFLECT** (Yale/IBM, arXiv 2605.19196) |
| Measurement invariance on benchmark scores | **Cacioli, arXiv 2604.27405** (Apr 2026), reliable-change across versions. **Zheng & Yang, arXiv 2609.00482** — DIF across model families, posted **31 August 2026** |
| Shadow-anchored bridging for silent updates | **Habba et al., arXiv 2604.12843** (Apr 2026), fixed-parameter IRT with locked anchors, explicitly for cross-time comparability. Plus arXiv 2606.15474 (drift attribution), Wiese *PLOS ONE* Feb 2026 |

**Verify these against the PDFs before citing any of them.** Several were read through a summarising
fetch and the numbers should be confirmed.

## The angle that survived, found independently by three of the four attack agents

> **Build controlled, provenance-labelled information environments. Manipulate the evidence
> distribution while holding the model, harness and prompt fixed. Measure how the agent's epistemic
> failures respond.**

Why it survives where the others died:

1. It is **objective 3 of the call verbatim** — "controlled experiments with open models and modular
   agent architectures."
2. It is **the one grouping variable in objective 2 nobody has occupied.** Everyone varies what is
   free. Nobody varies the retrieved evidence set under experimental control, because that requires
   building and holding a corpus with known provenance and serving it as if it were live.
3. **Planted documents make evidence laundering and source omission directly measurable** rather than
   inferred. If you planted it, you know what the agent should have said about it.
4. It **reaches objective 4**. Every rejected angle failed here.
5. It **needs no DSA Article 40 access.** Pierri's own CACM paper says that process is slow and
   adversarial, with first decisions expected only in late February 2026. Do not build on it.
6. It is **the one capability a psychometrician does not have and Pierri's audit work needs.**

**The inversion that makes your background load-bearing rather than decorative.** Objective 4 names
**weak-model oversight** — build a system where a weaker model checks a stronger one. That is the
reference-standard problem with the sign flipped. Everything you know about judge error stops being
a discovery you are claiming and becomes the reason your safeguard is designed correctly.

## Where psychometrics belongs now

**Inside the design, as an instrument. Not as the thesis.** Use it to show that a failure metric does
not survive an environment swap. Do not build the proposal on it: Pierri has no psychometrics
publications and neither does anyone in his department, so there is nobody there to defend a naive
design to a committee — and the systematic review at arXiv 2505.08245 has already installed the
vocabulary in the field anyway.

## Papers to read before you write

1. **Pierri et al., "Research Opportunities and Challenges of the EU's Digital Services Act,"
   *Communications of the ACM*, Sept 2026** (preprint arXiv:2512.14223). Read recommendation 3 twice.
2. **Møller, Bassignana, Pierri, Aiello, "Overreliance on AI in Information-seeking from Video
   Content," EMNLP 2026** (arXiv:2603.19843). 1,026 recruited on Prolific, 917 analysed, 2×3
   between-subjects, deceiving-AI arm. **Self-reported confidence stayed flat at ~4.5/5 across all
   three conditions.** Read the Limitations as a to-do list: one proprietary model, three topics,
   US/UK sample, no longitudinal or memory dimension, no personalisation.
3. **Liu, Mu, Feng, Zhu, Pierri, "Misinformation Exposure in the Chinese Web,"** arXiv:2602.22221.
   12,161 questions. Baidu 63.7%, Qwen 68.5%, LLaMA 45.0%, Baidu AI Overview 69.8%. Bing 98.5%
   correct on "No" questions and **5.6% on "Yes."** Find the Limitations sentence conceding that
   LLM-assisted labelling "may introduce (circular) noise."
4. **Feuerriegel et al. (incl. Pierri), "A reporting checklist for large language models in
   behavioural science," *Nature Human Behaviour* 2026**, DOI 10.1038/s41562-026-02492-7. GUIDE-LLM,
   14 items. Get the actual items.
5. **Saffari & Pierri, "Auditing Exposure to Harmful Content on TikTok using Multimodal Language
   Models," Findings of EMNLP 2026.** Cross-national, age-stratified. Note they published a **$50 API
   cost line** — they will expect you to have one.

---

# PART 7 — WHAT YOU CAN TRUTHFULLY CLAIM

Every number here is verified. Full detail in `MASTER_RECORD.md`.

## The strongest thing you own for motivation

**The ArtemisAI benchmark switch.** v1–v3 were scored against a 97-post human holdout (64.7, 66.4,
71.6). From v4 the reference became Claude's labels (81.8, 85.8). The benchmark moved at the same
time as the models, and there is no principled separation.

*Supports:* a first-hand production instance of a reference standard moving underneath a reported
gain — the thing REFLECT and the PPI literature model statistically, happening in a real deployment.
*Does not support:* any quantified split of the 21-point gain. You have no counterfactual; v4 and v5
were never scored against the holdout.
**Use it as motivation, one or two sentences, then move on.** Two independent verdicts said the same
thing: it is not a contribution.
**Worth doing if the endpoints are still live:** run v4/v5 against the 97-post holdout before you
submit. That converts an anecdote into a measured discrepancy.

## The infrastructure — your only uncontested advantage

68 collectors over 10 platforms daily with an automated repair layer running as a named CI workflow
(M+C Saatchi Fluency, clients including UK Government departments, Amazon and Ford); 6.7M items in
six weeks; 500+ collectors across 15 countries in four languages (Dubizzle Labs);
**web-scraping-guide.com** covering anti-bot systems, detection anatomy and agentic browsers.

*Supports:* that you can build and **maintain** controlled environments at scale, against adversarial
defences, for three years. Nobody else in the applicant pool can make that feasibility argument.
*Does not support:* research design competence or statistical inference. A committee will suspect an
engineer of proposing an engineering project.
*Overreach to avoid:* implying platform **data access**. You have collection capability, not
privileged APIs.

## The models

Six fine-tuned encoder classifiers on six SageMaker endpoints (XLM-R, DistilBERT, DeBERTa-v3,
Detoxify bases), ~20K weighted set, custom loss, weekly loop with three-tier confidence routing.
Claude→DeepSeek distillation: 6,000 posts labelled with reasoning, rules mined into a DeepSeek prompt,
12,000 more labelled, confidence below 0.80 routed back to Claude.

*Supports:* **a weak-model-oversight system running in production**, which objective 4 names directly.
*Does not support:* generative fine-tuning, RLHF, conversational or multi-turn systems, agent engineering.
*Overreach to avoid:* **the word "agents."** ArtemisAI is a labelling pipeline. Calling it agentic is
the kind of stretch that poisons everything else if caught.

## The paper

*"Is the Platform Part of the Measurement?"* with Dr Ella Haig. 500-replication simulation: a pooled
index reports the **wrong sign** of aggregate sentiment on roughly a quarter of days.

*Supports:* that mode-level non-invariance can invert a directional conclusion, and that you have run
a simulation with known ground truth.
*Does not support:* anything about agents, retrieval or the web.
**It is not on arXiv.** A committee cannot check it and cannot count it. **Do not describe it as
published.** Do not let it carry the novelty claim — Messing (arXiv 2604.11581) already ran the
G-theory move on LLM evaluation.
*Overreach to avoid:* "therefore agent benchmark scores are wrong 25% of the time." Different
population, instrument and design.

## The dissertation

279,000 posts across four platforms, fine-tuned BERT at macro-F1 0.878, Cohen's κ ≈ 0.78, Prophet
MAE ≈ 0.02. MSc Distinction, project mark 78, awarded 8 December 2025.

---

# PART 8 — HARD DO-NOT-CLAIM LIST

- **No publications.** Zero. Never imply otherwise, and do not call the manuscript "submitted."
- **No agent architectures built.** No multi-turn or conversational systems.
- **No controlled experiments on LLMs.** No human-subjects study, no IRB, no Prolific.
- **No generative LLM fine-tuning.** Correct phrasing: *the models I fine-tune are encoder
  classifiers, XLM-R, DistilBERT and DeBERTa; I have not fine-tuned a generative model, and I use
  Claude and DeepSeek through APIs.*
- **No privileged platform data access.** No Article 40 status.
- **Do not call ArtemisAI agentic.**
- **Do not present a known estimator as a discovery.** If PPI or DSL appear, cite them and position
  against them. A DEIB committee will include someone quantitative.
- **Do not explain the 2.75 CGPA in the proposal.** That is the CV's problem, not this document's.
- **No em-dashes**, per your standing rule.

---

# PART 9 — THE QUESTIONS THEY WILL ASK

Have an answer to all of these before you submit. The last five are the real exposures.

1. **"Zheng and Yang posted family-DIF benchmark recomposition on 31 August. Cacioli posted
   reliable-change detection in April. What is left?"** You need two sentences that concede the
   method and claim the object. If you cannot say this cleanly, the proposal is in trouble.
2. **"What is your harness, and is it a controlled factor?"**
3. **"How do you serve a provenance-controlled corpus to a live-browsing agent without it becoming
   an offline replay?"** Concrete architecture, not a gesture.
4. **"Local independence fails inside a trajectory. What is your model?"**
5. **"What is your ground truth for evidence quality, and who validated it?"**
6. **"You have no publications. In a group where students publish from year one, what is the
   evidence you can produce them?"** The Haig paper is your only answer and it is not on arXiv.
   **Post it before 18 September if Ella agrees.** An arXiv ID converts "claims to have a paper"
   into "has a preprint."
7. "What does the artefact cost?" Have a corpus size, a rollout count and a dollar figure.
8. "What is your target venue and when is paper one?"
9. "What happens when the models you anchor on are deprecated in year two?"
10. "What is your safeguard, concretely, and how would you know it worked?"

**And one for you, not for them.** The programme starts **1 November 2026**, five weeks before the
ArtemisAI launch, on the first day of the Hardening sprint you personally own, with the launch board
at 14% and behind pace. That is a decision to make before you spend a week writing, not after.

---

# PART 10 — STYLE

- **1,550 words total.** There is no room for throat-clearing. The Royal Holloway proposal from
  November 2025 is the anti-model: five research questions, four numbered "contributions", bulleted
  methods, high buzzword density. Against Art. 3 that register is exactly what draws suspicion.
- **The VU letter and the Agder proposal are the models.** VU opens on one sentence from the group's
  own methodology page and turns it into two open problems. Agder names what it does not bring.
- Specific beats general. A number a committee can check beats an adjective.
- Name the gap before they find it.
- Plain first-person prose. No em-dashes.

---

# PART 11 — THE ORDER TO WRITE IN

**Do not start at the Summary.** Write it last, when you know what you are summarising.

| When | What |
|---|---|
| **Today, 9 Sep** | Read Parts 6 and 7. Read the five papers in Part 6. Decide **which architecture** answers question 3 in Part 9, and **which two failure modes** you take. Write nothing yet. |
| **10–11 Sep** | Draft the **architecture** paragraphs, 1,400 characters. This is the hardest part and the part that wins Brambilla. |
| **11–12 Sep** | Draft the **studies** and the **safeguard**, 2,300 characters. |
| **13 Sep** | Draft the **problem and gap** (900) and **feasibility and contribution** (800). Description now complete at ~5,400. Run the counter. |
| **14 Sep** | Draft the **Motivations**, 1,900. |
| **15 Sep** | Draft the **Summary**, 480. Run the counter on everything. |
| **15–16 Sep** | I check it for factual errors and correct text you have written in full, which Art. 3 permits, and we declare that use. |
| **16 Sep** | Typeset onto the RTF template, export PDF under 3 MB, upload, questionnaire, close, pay. |
| 17 Sep | Buffer. |
| **18 Sep 14:00 Rome** | Hard stop. |

**Write into `proposal.txt`.** Check with:

```bash
python3 "PoliMi Application/count_chars.py" "PoliMi Application/proposal.txt"
```
