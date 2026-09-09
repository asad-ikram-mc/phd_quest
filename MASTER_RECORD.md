# MASTER RECORD — every fact, every claim, every version that went out
# Built 9 September 2026 by reading the whole repository, the extracted PDFs and the Gmail sent folder.
# This is the single source of truth. If a new document contradicts this file, one of them is wrong; find out which.

---

## 0. THE TWO CORRECTIONS THIS READ-THROUGH PRODUCED

**0.1 — Our own PoliMi pack contains a false statement. "Asad has no IELTS" is wrong.**
He sat IELTS Academic on **28 March 2024**: Listening 7.0, Reading 6.5, Writing 6.0, Speaking 7.0,
**Overall 6.5**, CEFR B2, TRF number 23PK507881IKRA011A. That clears PoliMi's threshold of ≥6.

**Whether it survives is genuinely unresolved, and I overstated this on 9 Sep.** Art. 2 of this call
says the certification "must be **valid upon enrolment**", and enrolment closes **31 October 2026**.
IELTS itself prints a recommendation that ability be re-assessed after two years, which from
28 March 2024 ran out in March 2026. That is IELTS's wording, not PoliMi's: **the call sets no shelf
life of its own.**

Against that, **PoliMi's own FAQ v1.9 and its application Quickstart both state that "The English
language certifications are valid regardless of the date when they were awarded"**, and the 41st
cycle said so in the call itself ("a prescindere dalla data di conseguimento"). The 42nd cycle
changed the wording to "in corso di validità" without explaining what that means for a fixed-date
test. So the sources contradict each other and only PhD-INF@polimi.it can settle it.

**Pursue both routes in parallel and rely on neither alone.**

**The Portsmouth English-medium letter is the safe route, and it is now due EARLIER than we thought.**
The Italian call says candidates using this exemption "devono allegare alla domanda documenti
ufficiali" — must attach official documents **to the application**, i.e. by **18 September**, not at
enrolment. It is the same letter already sitting unresolved on the Edinburgh checklist. Two wording
traps: the English call calls it a "certification", but the Italian and the PoliMi website both say
a **declaration** from the institution stating the language of delivery, so asking for the wrong
artefact wastes days we do not have; and the Italian scopes it more narrowly than the English, as
"tutti gli insegnamenti... per la maggior parte del percorso", so ask Portsmouth to confirm the
programme was **taught and assessed entirely in English**. Art. 2 exemption:
> "applicants who have been awarded ... academic qualifications by an institute in which all teaching
> activities have been carried out in English are not required to certify their knowledge of English.
> In this latter case, candidates are required to submit an official language certification from the
> corresponding academic institute."

Send the IELTS **as well**. It costs nothing and it may be accepted. There is also a third argument
in reserve: English is an official language of Pakistan under Article 251 of its Constitution, and
the call exempts "citizens of Countries in which English is an official language". Do not lead with
that one; it is an argument, not a document.

**0.2 — The "seven years" / "6+ years" inconsistency, and the comment count.**
- The academic CV profile says "**6+ years**". Agder, VU and Edinburgh all say "**seven years**".
  Freelancing started Dec 2018, so seven is defensible and is what has gone to professors. **Use seven.**
- ArtemisAI comments: the CV says "**3.2M+ comments**", Agder and Edinburgh say "**3.39 million**".
  3.39M is the figure that went to professors. Pick one and make the CV match.

---

## 1. THE VERIFIED FACT BASE

Everything below is checkable against a document in this repository. Numbers that go into any
application come from here.

### 1.1 Identity and qualifications
| Item | Value | Source |
|---|---|---|
| Date of birth | 20 January 1998 | FAST-NUCES transcript |
| Nationality | Pakistani | — |
| Location | Lahore, Punjab, Pakistan | — |
| Email / phone | asad.ikram53@gmail.com · +44 7482 376417 | — |
| MSc | Data Analytics, **Distinction**, University of Portsmouth, **awarded 8 December 2025** | certificate + transcript |
| MSc project mark | **78** | transcript |
| MSc module spread | 78, 80, 70, 70, 67, 62, 56 → unweighted ≈ 69, **credit-weighted 70.5** (prefer 70.5) | transcript |
| MSc supervisor | Dr Ella Haig (ella.haig@port.ac.uk — verified, not e.haig@) | — |
| MSc ethics ref | Portsmouth **TETHIC-2025-111094** | Helsinki proposal |
| BSc | Computer Science, FAST-NUCES, 2017–2022 | degree + transcript |
| BSc CGPA | **2.75 / 4.00**, 130/130 credits | transcript, issued 1 Apr 2022 |
| BSc weak points | Two F grades (CL 103, CS 201); Fall 2018 GPA 1.23 | transcript |
| BSc roll number | 17K-3943 | transcript |
| IELTS | 28 Mar 2024 · L7.0 R6.5 W6.0 S7.0 · **Overall 6.5** · CEFR B2 | ielts_result.pdf |
| Chevening | Scholar **2024/25**, from 70,000+ applicants across 160 countries | — |

**The CGPA is the exposed flank.** 2.75/4.00 is below RIT's recommended 3.0 and is exactly why the
PoliMi Attachment 1 question matters. **CORRECTED 9 Sep 2026: Attachment 1 was never missing.** It
is page 8 of both call PDFs. It lists **PAKISTAN at 3,3/4,0**, above Asad's 2.75/4.00, and does not
list the United Kingdom, so the MSc is assessed directly by the Committee. Note also that the
95/110 and 86/100 figures belong to the *Italian* Laurea Magistrale bullet of Art. 2; foreign
qualifications are governed by the separate Attachment 1 bullet, and there is no published PoliMi
conversion from a UK Distinction. What still needs the email to PhD-INF@polimi.it is narrower:
whether the minimum binds only the qualification enabling admission, and how an unlisted UK
master's is treated. See `PoliMi Application/REQUIREMENTS.md` Part 0.1.

### 1.2 Research record
- **MSc dissertation**: *Cross-Platform Sentiment Analysis of Public Reaction to UK Economic Policies*.
  ~**279,000** posts, four platforms (Twitter/X, Reddit, YouTube, Quora), official APIs and licensed
  feeds, ethics-approved and GDPR-compliant. Fine-tuned **BERT macro-F1 0.878** against BiLSTM and
  lexicon baselines. Human validation **Cohen's κ ≈ 0.78**. Temperature-scaling calibration. McNemar
  and bootstrap tests. Chi-square topic tests. Prophet forecasting, **MAE ≈ 0.02**. NRC emotion
  analysis; LIME and integrated gradients.
- **Paper with Dr Ella Haig**: *"Is the Platform Part of the Measurement?"* Treats each platform as a
  survey mode; six-step psychometric protocol (generalizability theory, invariance and DIF, score
  linking) for machine-labelled sentiment. **500-replication simulation**: a pooled cross-platform
  index reports the **wrong sign** of aggregate sentiment on roughly **a quarter of days**.
  23 pages. **Not yet on arXiv.** Status has been "imminent" since August.
- **Reviewer feedback on the paper (Eni, ICWSM-experienced)** — record this honestly, it is the
  known weakness: the hand-labelled validation sample (~200 posts against 279k) is too small; 279k
  across four platforms is small by modern ICWSM standards; the anchor events were not pre-identified,
  which threatens the equating step. His recommendation was a **poster or short paper**, or expand
  both the corpus and the labelled set. The novelty claim itself he judged **sound**: nobody has
  treated the platform itself as the formal measurement instrument for machine-labelled text.

**Publication count is zero.** Never imply otherwise. The honest line that has worked in every
letter so far is to name the gap and say how it closes.

### 1.3 ArtemisAI Ltd (t/a ViralData) — Founder & CTO, Feb 2025–present
Verified against the `marvel` repo and the **live admin panel** (check the live panel, never the
local file — the local `nlp_accuracy_tracker.html` has an empty ENTRIES array and lies).
- Meta Graph API ingestion, 30+ brand pages daily → layered lakehouse + Redshift.
  **111,000+ posts, 3.2M–3.39M comments** processed.
- **Six fine-tuned transformer classifiers** on six SageMaker endpoints, <100ms in parallel:
  cardiffnlp XLM-R (sentiment), DistilBERT (emotion), DeBERTa-v3 (topic, intent), Detoxify (toxicity).
- **Distillation chain**: Claude labels 6,000 posts with reasoning (~$10) → rules mined into a
  DeepSeek prompt → DeepSeek labels 12,000 more (~$2.50) → confidence <0.80 routed back to Claude →
  18K real + ~2K synthetic = 20K weighted dataset, stratified 80/20.
- Custom weighted loss: `per_sample_loss × conf × class_wt × source_wt`.
- Gate: macro-F1 > 0.85 on **both** a 97-post human holdout and a 4K stratified test, then a human
  validates 200 random posts before deploy. Weekly Monday loop, three-tier confidence routing
  (auto-commit >0.85 ≈75%, agent review 0.60–0.85 ≈18%, <0.60 ≈7%). Quarterly retrain at 10K uncertain.
- **Versions v0→v5, average accuracy 64.7 → 66.4 → 71.6 → 81.8 → 85.8.** At v5: sentiment 87,
  emotion 84, topic 79, intent 82, toxicity 97.
- **Fusion classifier**: PyTorch MLP 1536→256→64→5 over three concatenated 512-dim CLIP vectors
  (image, OCR text, caption). Adam, dropout 0.3, balanced class weights, best-val checkpointing.
  Gold set **149** samples, ~680 with production data. **macro-F1 0.93 on the gold set.**
  Production labels come from **Claude Haiku 4.5 vision** — the classifier is partly trained to
  imitate an LLM annotator.
- Hybrid OCR pipeline **token-F1 0.928**. Whisper video transcription. networkx affinity graph.
- Weekly **KL-divergence drift alarms**, CI quality gates.

**The two observations worth more than any number, and both are his own:**
1. The two annotation tiers agree on **82.9%** of sentiment labels, **74.4%** of emotion labels and
   **0.0%** of toxicity labels, while the toxicity model reports **96.7%** average confidence. The
   zero was mismatched label taxonomies between tiers, not a model failure. The dashboard's
   "accuracy" was **inter-model agreement with no criterion behind it**.
2. **v1–v3 were scored against the 97-post human holdout (64.7, 66.4, 71.6). From v4 the reference
   became Claude's labels (81.8, 85.8).** The benchmark moved at the same time as the models, and
   there is no principled way to separate the two. That is his research argument happening inside
   his own production numbers.

**NEVER CLAIM** (this list exists because these errors have already been made once):
- ~~"He has not trained models"~~ — false, he has, end to end.
- ~~"He has not fine-tuned"~~ — false for encoder classifiers. **True only for generative LLMs.**
  Correct phrasing: *"The models I fine-tune are encoder classifiers, XLM-R, DistilBERT and
  DeBERTa; I have not fine-tuned a generative model, and I use Claude and DeepSeek through APIs."*
- ~~"The DeepSeek loop is planned"~~ — false, it runs; 18 DynamoDB entries on the live panel.
- No **conversational or multi-turn dialogue systems**. No **agent architectures**. No **controlled
  experiments on LLMs**. No **publications**. No Node2Vec, Pinecone, XGBoost, GPT-4 or LLaMA
  fine-tunes. LLaMA is ticket S19 and Pinecone S16, both tagged Later.

### 1.4 Employment, with the numbers that have gone out
| Role | Dates | The facts used in letters |
|---|---|---|
| **M+C Saatchi Fluency**, Data Engineer Consultant | Dec 2024–present | UK Gov depts, Amazon, Ford, Nike, Reckitt. Sprinklr + Brandwatch + custom crawlers into AWS (ECS Fargate, Step Functions, Glue, Athena) + SageMaker NLP. **68 crawlers, 62 active**, ingesting **10 platforms daily** into a governed **156-column** master table; **6.7M items in six weeks**. Self-healing repair agent as a **named CI workflow**; ~a third of repairs need no model call. CAPTCHA handling, proxy rotation, TLS fingerprinting. 99%+ uptime. Reports read by senior government communications teams. |
| **Dubizzle Labs** (Dubizzle, Bayut, Zameen, OLX), Senior Data Engineer | Feb 2022–Aug 2024 | Led **3 engineers**, **500+ scrapers across 15 MENA countries** on Kubernetes/EKS, English/Arabic/Urdu/Hindi. Redesigned RDL/ODL/ADL warehouse, **ETL throughput +60%**. **Promoted twice in two years.** |
| **Fix.com**, Data Engineer Consultant | May 2023–present (p/t) | Scrapy/Scrapyd, **50M+ data points from 200+ sources**, crawl time **−40%**. Great Expectations validation, bad production data **−70%**. |
| **VendueTech**, Lead Data Engineer | Jun–Jul 2025 | Led 3 engineers, real-time auction ingestion, Azure→AWS, latency **−40%**, PySpark on EMR Serverless. |
| **Prefe**, Consultant | Sep–Dec 2024 | Legacy → Scrapy, failure rate **−60%**, mentored two juniors. |
| **CXG**, Freelance | Dec 2025–Jan 2026 | Luxury fashion crawlers, **99%+ completeness** against advanced anti-bot. |
| **Freelance** (Level 2 seller) | Dec 2018–Feb 2026 | **300+ five-star projects, 400+ websites, 50+ clients.** |

- **web-scraping-guide.com** — free public engineering reference. **24 sections, 60+ libraries and
  tools, six anti-bot systems**, legal and ethical constraints, production architecture, data quality.
- Live sites: artemisai.co.uk · fluency-mcsaatchi.com (**NOT** mcsaatchifluency.com, that is a parked
  domain) · asad-ikram-mc.github.io/portfolio · linkedin.com/in/asad-ikram98

---

## 2. WHAT HAS GONE TO PROFESSORS — the final versions, verified in the Gmail sent folder

| Who | Where | Sent | What went, and what came back |
|---|---|---|---|
| **Dr Andreu Casas** | Royal Holloway / LSMO | 2 Nov 2025, then re-engagement **8 Sep 2026 12:51 UTC** | Full application Nov 2025. He replied within hours every time. Asked whether Asad was eligible; the studentship covered the **home fee only**. He had already asked the university about hiring an international candidate who could fund the difference. **This is the recurring UK blocker: the home/international fee gap, not the candidate.** The Sep 2026 re-engagement is v5, ~150 words, **capability only** — no numbers, no paper, no research argument. Asad edited before sending: softened the opening, added the artemisai.co.uk link, and cut the silent-failure paragraph. Check 29 Sep; if silent, close the row. |
| **Prof. Ingmar Weber** | Saarland, I2SC / SOUNDS | 17 Mar 2026, follow-ups 28 Mar, 15 Apr | **Replied warmly.** SOUNDS observatory positions expected by summer. Team Lead needs **C1 German** — blocked. Team-member positions to follow. |
| **Prof. Yannis Theocharis** | TUM | 16 Apr 2026, nudged 8 Sep | **Replied warmly**, found the platform-heterogeneity framing "very interesting". Said a PhD call was expected around September. Chair's vacancies page still empty on 8 Sep. |
| **Prof. Ashton Anderson** | Toronto CSSLab | 2 Apr 2026, follow-up 8 Sep | No reply. December application cycle. |
| **Prof. Dirk Hovy** | Bocconi MilaNLP | 2 Apr 2026, follow-up 8 Sep | No reply. |
| **Dr Matti Nelimarkka** | Helsinki | 6 Apr 2026, three exchanges, last 26 Aug 2026 | **The most useful rejection in the file.** "I am having a difficult time to identify what you'd like to work on in more concrete terms." Then, after a sharper reply: "I think this thesis requires a bit more work still." **He is the reason the work got specific.** The Helsinki proposal is the answer to him. |
| **Prof. Meeyoung Cha** | MPI-SP | 2 Sep 2026 | No reply. CS@max planck December deadline. Nudge 16 Sep. |
| **Dr Jiin Kim** | Utrecht | 20 Aug 2026 | Application submitted; introduction sent. |
| **Prof. Francesco Pierri** | **PoliMi** | **8 Sep 2026 13:35 UTC** | **No reply yet.** One question, correctly formed: does the project audit retrieval against the **live web** (anti-bot defences, personalisation, geographic variation) or against a **fixed corpus held constant**? Says he will submit before 18 Sep either way. |
| **Prof. Ksenia Gligorić** | Johns Hopkins | 8 Sep 2026 | No reply. Fall 2027. |
| **Dr Jon Roozenbeek / Dr Ivar Vermeulen** | VU Amsterdam | Application **submitted** | Interviews 21–30 Sep. |
| **Anna C. Færavaag (HR)** | Agder | 3 Sep 2026 | Conditional yes on eligibility. **Application then dropped by Asad's own decision, 7 Sep.** |
| **Prof. Walid Magdy / Dr Björn Ross** | Edinburgh | earlier | Magdy said in March: get a publication before applying. Both have seen the direction. |

**One embarrassment, handled.** On 8 Sep a private brief link went into five of these emails and had
to be retracted the same day: *"The brief I linked was working material for my supervisor rather than
something meant to circulate, and that link is now closed."* Sent to Theocharis, Anderson, Hovy and
Gligorić at ~14:20 UTC. The proposal page is now AES-encrypted behind a passphrase and is **for Dr
Ella Haig only**. Never link it again.

**One process rule, learned the hard way.** Those six 8 Sep emails were substantially rewritten and
then sent without Asad reading the versions that went out. **Never send. Build the draft, show it,
stop.** "Send it" is an instruction to prepare a draft. Prior approval does not survive an edit.

**One formatting defect to fix before the next send.** In the Pierri email, Gmail wrapped every
signature URL in a `google.com/url?q=...` redirect, so the links render as long ugly Google URLs in
the plain-text part. Check how the signature renders before the next outreach.

---

## 3. THE PROPOSAL LINEAGE — four proposals, and how the argument got sharp

Read in order, this is the story of one idea being forced into focus. It matters because the PoliMi
proposal is the fifth, and it should not regress to the first.

**v1 — Royal Holloway, "Algorithmic Curation and Moderation Effects" (Nov 2025, ~1,881 words).**
Generic. Five research questions, four numbered "contributions", a bulleted methods list, buzzword
density high (explainable NLP, causal inference, policy relevance). It proposes to study whether
algorithms amplify. **It reads like a proposal assembled from a template**, and by the standard of
PoliMi's anti-AI article it is the version most likely to attract suspicion. Do not reuse its style.

**v2 — Helsinki, "Calibrating the Observatory" (Aug 2026).** The turn. Four contributions each
**stated against its nearest neighbour** in the literature, with the residual named. RQs on
Equivalence, Drift, Standpoint and Criterion. Identification actually specified: Wu–Estabrook
invariance sequence, WLSMV with theta parameterisation, dMACS effect sizes, DIF with anchor
purification, shadow-anchored bridging, multivariate G-study. Declared drop-order. **Has a
character-counted appendix mapping to the funder's template** — precisely the discipline PoliMi
needs.

**v3 — Agder, "Counting What the Classifier Sees" (Sep 2026).** The most complete document in the
repository. Same spine, dressed for Information Systems: affordances and institutional logics,
design science, four studies mapping to four papers, a named practitioner partner, a table of
planned progression with decision gates and pre-specified fallbacks. **Section 9 is the model to
copy: "Why I am the right person, and what I do not bring."** It names the gaps — no extremism
background, no Norwegian, no qualitative interviewing, R functional rather than fluent — and sizes
the studies accordingly. Not applying, but the document is reusable thinking.

**v4 — VU Amsterdam letter (submitted 3 Sep 2026).** The tightest piece of writing in the file. It
opens on **one sentence from their own methodology page** — that COTSI draws on five of seventeen
vendors, chosen because their data is reachable without a login — and turns it into two open
problems. Then the silent-failure paragraph: *"a collector that returns a valid-looking response
containing nothing, so the series does not break, it just goes thin. On a price index that does not
read as an outage. It reads as a cheaper market."* Then four papers. Then what he does not bring.
Then why four years.

**The spine, in one sentence, that all four share:**
> Every published claim about online phenomena is a ratio whose numerator is produced by a
> classifier; the classifiers disagree, do not generalise across datasets, and change under our
> feet; the field has no accepted way to carry that through to the final estimate; and I know this
> because it is happening in my own production system.

---

## 4. WHAT THIS MEANS FOR THE POLIMI PROPOSAL

**The rule, unchanged and not negotiable.** Art. 3: AI writing tools *"must be limited to the
correction of texts written entirely by the candidate"*, use *"must always be explicitly declared"*,
and the committee reserves the right to check. The submission form adds a **compulsory checkbox**
confirming awareness that originality is verified by **anti-plagiarism software**. Asad writes the
project description and the motivations. Claude corrects text already written in full, and the use
gets declared.

**Where the existing work maps onto the four objectives** (this is reading material, not text to reuse):
- *Objective 1, "operationalise" epistemic failure modes.* Operationalisation is a measurement act.
  The field's habit is to jump to a metric without asking whether it is valid. That is the argument
  he has already made in four documents.
- *Objective 2, "reproducible benchmarks and longitudinal audits ... across models".* This is a
  measurement-invariance problem in different clothes: does a benchmark score mean the same thing
  when the model changes? The Haig paper's machinery is built for it, with models as the grouping
  variable instead of platforms. **And he has the rarest thing here — a real longitudinal audit that
  went wrong: v1–v3 scored against humans, v4–v5 against Claude, benchmark and model moving together.**
- *Objective 3, mechanisms in retrieval, ranking, synthesis, memory.* **The retrieval layer is where
  his seven years live, and it is the part of the agent stack most AI-safety candidates treat as a
  black box.** This is his single largest differentiator against the field of applicants.
- *Objective 4, lightweight safeguards including weak-model oversight.* His distillation chain **is**
  weak-model oversight in production: Claude teaches, DeepSeek labels, low confidence routes back.

**What he must not overclaim:** no agent architectures, no controlled LLM experiments, no
publications, no multi-turn systems, no user studies. The Agder Section 9 pattern is how to say so.

**The Pierri question is still open** and it changes the proposal. If no answer arrives before the
17th, the proposal should acknowledge both readings and say which one it takes.

---

## 5. WHAT IS ACTUALLY BLOCKING THE POLIMI SUBMISSION

| # | Item | Status |
|---|---|---|
| 1 | **Portsmouth English-medium letter** | **NOT REQUESTED.** Gate 1. Registry turnaround is days and is not guaranteed. Send the IELTS alongside it. |
| 2 | **FAST-NUCES official transcript** | **HAVE IT** (`Asad bscs transcript.pdf`, issued 1 Apr 2022). Previously listed as missing. Resolved. |
| 3 | **Attachment 1 minimum grade** | **TABLE FOUND**, page 8 of both call PDFs; the earlier note that it was unpublished was false. Pakistan **3,3/4,0** vs Asad's **2.75/4.00**; UK unlisted so the MSc is judged directly. Still ask PhD-INF@polimi.it whether the minimum binds all degrees. |
| 4 | **Research proposal, 4,000–8,000 characters** | Asad writes. Not started. |
| 5 | **Motivations, max 2,000 characters** | Asad writes. Not started. |
| 6 | **Thesis summary, max 1,000 characters** | Asad writes. Placeholder in the CV. |
| 7 | **Social / organisational / other skills** | Asad writes. Placeholders in the CV. |
| 8 | **Two referees** — name, role, email, **telephone**, and Skype if any | **Ask both before naming them.** Dr Ella Haig plus one. |
| 9 | **Two attachments** | Haig manuscript + either the dissertation or the web-scraping guide. Asad's call. |
| 10 | **Signed passport copy** | Compulsory for non-EU. Must be signed. |
| 11 | **Questionnaire** | Required before the application can be closed. Seen on the portal. |
| 12 | **€25.82 via PagoPA** | **The link is generated only after the application is closed.** Do not leave this to the 18th. |
| 13 | Two compulsory confirmations | Undertaking to attend per the call, and awareness of anti-plagiarism verification. |

Photo: **done**, embedded 9 Sep. Address: **removed** at Asad's instruction.

---

## 6. STANDING DECISIONS AND RULES

- **No HEC, no DAAD.** Opted out 20 Aug 2026. Never re-add either. The Commonwealth CSC nomination
  is a separate route and is **not** blocked by this.
- **Drafts only.** Never send an email. Build the draft, show it, stop.
- **The proposal brief is private.** publish_proposal is passphrase-locked, for Dr Ella Haig only.
- **No em-dashes** in anything written for Asad. Plain first-person prose.
- **Check the live ArtemisAI admin panel**, never the local tracker file.
- **Agder is closed** by Asad's decision, 7 Sep 2026. Documents kept for reuse.
- **The 1 Nov 2026 PoliMi start collides with the 8 Dec 2026 ArtemisAI launch**, which is 14% built
  and behind pace, with Asad personally owning the stack decision, API contract and data model.
  Unresolved.
