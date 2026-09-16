# PhD Quest handoff: state on 16 September 2026

This file hands the PhD campaign over to another assistant (ChatGPT). Read all of it before writing anything for Asad. It covers who he is, the rules, every live application, the verified facts, and the next job (ELLIS Institute Finland, due 21 Sep).

Repository: `/Users/asad/git_projects/asad_phd/phd_quest`
Live tracker: https://asad-ikram-mc.github.io/phd_quest (single file `index.html`, auto-deploys on push to `main`)
Deeper fact base: `MASTER_RECORD.md` in the repo. If anything here conflicts with it, check the original document.

---

## 1. Hard rules. Break none of these.

1. **No em-dashes anywhere.** Not in letters, emails, CVs or the tracker. Use commas, full stops, colons or a plain hyphen. Write plain first-person English, not flowery AI prose.
2. **Never send an email.** Only prepare a draft and show it. Asad sends. Even "send it" means "prepare the draft".
3. **Never claim a publication.** He has none. The Ikram and Haig manuscript is complete, unpublished and not submitted.
4. **Never claim he fine-tuned a generative LLM.** He fine-tunes encoder classifiers (XLM-R, DistilBERT, DeBERTa-v3, Detoxify) and uses Claude and DeepSeek through APIs. Safe wording: "The models I fine-tune are encoder classifiers; I have not fine-tuned a generative model."
5. Also never claim: conversational or multi-turn dialogue systems, agent architectures, controlled experiments on LLMs, Node2Vec, Pinecone, XGBoost, GPT-4 or LLaMA fine-tunes.
6. **No HEC, no DAAD.** He opted out on 20 Aug 2026. Do not suggest either. (The Commonwealth route via HEC nomination is separate and still live.)
7. **Dr Ella Haig and Dr Fahad Ahmad are handled by Asad on his university Outlook.** Do not draft emails to them. Their absence from Gmail proves nothing.
8. **The proposal brief at asadfix.github.io/publish_proposal is private (for Dr Haig only).** Never link it.
9. **ArtemisAI launches 8 Dec 2026 and is not yet launched.** Say "running in production ahead of launch", never "served to clients".
10. When checking whether someone replied, open the whole Gmail thread. Search listings sometimes cut off the newest messages.

---

## 2. Who Asad is (verified)

| Item | Fact |
|---|---|
| Name | Asad Ikram, Pakistani, based in Lahore. Born 20 Jan 1998 |
| Contact | asad.ikram53@gmail.com · +44 7482 376417 · linkedin.com/in/asad-ikram98 · asad-ikram-mc.github.io/portfolio |
| MSc | Data Analytics, **Distinction**, University of Portsmouth, awarded 8 Dec 2025. Project mark 78, credit-weighted average 70.5. 180 UK credits = 90 ECTS. Supervisor Dr Ella Haig |
| BSc | Computer Science, FAST-NUCES Pakistan, 2017 to 2022, 130 credit hours, **CGPA 2.75/4.00** (the weak point; lead with the MSc) |
| English | IELTS Academic 28 Mar 2024: L7.0 R6.5 W6.0 S7.0, overall 6.5 (B2) |
| Award | Chevening Scholar 2024/25 (70,000+ applicants, 160 countries) |

**Research record**
- MSc dissertation: *Cross-Platform Sentiment Analysis of Public Reaction to UK Economic Policies*. About 279,000 posts from Twitter/X, Reddit, YouTube and Quora via official APIs and licensed feeds, ethics approval TETHIC-2025-111094, GDPR-compliant. Fine-tuned BERT macro-F1 0.878 against BiLSTM and lexicon baselines; human validation Cohen's kappa about 0.78; temperature-scaling calibration; McNemar and bootstrap tests; NRC emotion analysis; LIME; Prophet forecasting (MAE about 0.02). Key finding: the same policy event produced structurally different sentiment and emotion profiles on different platforms.
- Manuscript with Dr Haig: *"Is the Platform Part of the Measurement? A Protocol and Simulation Study for Cross-Platform Equivalence of Machine-Labelled Policy Sentiment."* Treats each platform as a survey mode; applies generalizability theory, measurement invariance and DIF, and score linking to machine-labelled text. In a 500-replication simulation with known ground truth, a pooled index reports the wrong sign of the aggregate on roughly a quarter of days. PDF: `Paper with Ella/Ikram_Haig_Is_the_Platform_Part_of_the_Measurement.pdf`. Known weakness (reviewer feedback): small human-labelled validation set, 279k is small by ICWSM standards. Target: ICWSM 2027 Round 3, 15 Jan 2027.

**ArtemisAI Ltd (trading as ViralData), Founder and CTO, Feb 2025 to present**
- Meta Graph API ingestion of 30+ public pages daily into a lakehouse and Redshift; 111,000+ posts and 3.39M comments processed.
- Six fine-tuned encoder classifiers (sentiment, emotion, toxicity, topic, language, intent) on six SageMaker endpoints.
- Labelling pipeline: Claude labels about 6,000 posts with reasoning, decision rules are mined into a DeepSeek prompt, DeepSeek labels about 12,000 more, low-confidence cases route back. About 20K weighted dataset; loss weighted by label confidence, class balance and label source. Deploy gate: macro-F1 above 0.85 on a human holdout and a 4K test set. Weekly retraining with three-tier confidence routing.
- Multimodal: CLIP embeddings into a trained PyTorch fusion classifier (macro-F1 0.93 on a hand-built gold set), OCR pipeline (token-F1 0.928), Whisper transcription. networkx affinity graph (network theory for a collaboration feature).
- Products: underperforming-post prediction, best posting times, post drafting, crisis alerts, collaboration graph.
- **The measurement insight he tells in letters:** the two annotation tiers agree on 82.9% of sentiment labels and 74.4% of emotion labels while the toxicity model reports 96.7% average confidence, and the dashboard's "accuracy" figure turned out to be inter-model agreement with no criterion behind it. Model versions v1 to v3 were scored against a human holdout, v4 onward against Claude labels, so part of the jump is the reference moving. This is what moved him from building instruments to asking what their outputs mean.

**Employment**
| Role | Dates | Facts |
|---|---|---|
| M+C Saatchi Fluency, Data Engineer (consultant) | Dec 2024 to present | Social listening pipeline for UK Government departments, Amazon, Ford, Nike, Reckitt. Sprinklr and Brandwatch plus custom collectors into AWS (ECS Fargate, Step Functions, Glue, Athena), SageMaker NLP. 68 collectors, 10 platforms daily, governed 156-column master table, 6.7M items in six weeks, self-healing repair agent as a named CI workflow, 99%+ uptime, weekly KL-divergence drift alarms |
| Dubizzle Labs (Dubizzle, Bayut, Zameen, OLX), Senior Data Engineer | Feb 2022 to Aug 2024 | Led 3 engineers, 500+ collectors across 15 MENA countries on Kubernetes/EKS, English, Arabic, Urdu, Hindi. Redesigned RDL/ODL/ADL warehouse, ETL throughput +60%. Promoted twice |
| Fix.com, consultant | May 2023 to present, part time | Scrapy pipelines, 50M+ data points from 200+ sources, Great Expectations validation, bad production data -70% |
| VendueTech, Lead Data Engineer | Jun to Jul 2025 | Led 3 engineers, real-time auction ingestion, Azure to AWS |
| Prefe, consultant | Sep to Dec 2024 | Rebuilt collectors, failure rate -60%, mentored two juniors |
| CXG, freelance | Dec 2025 to Jan 2026 | Luxury retail collectors, 99%+ completeness against anti-bot |
| Freelance data engineer | Dec 2018 to Feb 2026 | 300+ five-star projects, 400+ websites, 50+ clients |

Public work: author of web-scraping-guide.com (free engineering reference).
**Career story he wants told (STAR, chronological):** freelance with 300+ clients worldwide, then Dubizzle (multilingual data, how people talk on forums versus social platforms), Fix.com, then Chevening (argument: public decisions deserve better evidence about what people think), then MSc alongside Prefe, Fluency, VendueTech, CXG, then founding ArtemisAI as CTO. Throughline: social media data and the problem of what a number made from it actually means.

**Referees:** Dr Ella Haig (Associate Professor in AI, School of Computing, University of Portsmouth, Ella.Haig@port.ac.uk; dissertation supervisor and co-author) and Dr Fahad Ahmad (Senior Lecturer, Centre for Cybercrime and Economic Crime, University of Portsmouth, Fahad.Ahmad@port.ac.uk). Ready PDF: `Application Assets/Asad_Ikram_Referees.pdf`.

---

## 3. NEXT JOB: ELLIS Institute Finland doctoral positions

**Deadline: Monday 21 Sep 2026, 23:59 EEST (UTC+3) = 20:59 UTC = 01:59 Pakistan time on 22 Sep.** Submit on the 21st.
Call: https://www.ellisinstitute.fi/postdoc-and-phd-recruit-autumn-2026
Apply (DOCTORAL link, Aalto Workday, requisition R47606): https://aalto.wd3.myworkdayjobs.com/PrivateJobPosting/job/Otaniemi-Espoo-Finland/Doctoral-student-positions-at-ELLIS-Institute-Finland_R47606
Asad creates the Workday account himself. Questions: contact@ellisinstitute.fi

**What the call says (read in full 15 Sep)**
- Fully funded, Finnish university pay scale, doctoral contracts four years, start date negotiable. Positions hosted at the institute or a partner university (Aalto, Helsinki, Turku, Tampere, Oulu and others). Dozens of positions.
- Requirements: master's in CS, statistics, EE, maths or related; experience in ML, statistics or AI "preferably demonstrated by strong performance in relevant studies"; "other merits demonstrating suitability" count. Excellent written and spoken English, **no test score required**. No Finnish.
- Assessment (FAQ Q12): academic merits (publications, study record, teaching) **and other relevant experience, e.g. working in or with industry, or software development.** This favours Asad.
- Timeline: eligibility review end of September; supervisor review and interviews end of September to end of October; finalised November.
- One application can name several supervisors (FAQ Q11); matching happens in review; multiple offers possible.

**Required documents (English, PDF)**
| Document | Status |
|---|---|
| Cover letter, 1 to 2 pages | **TO WRITE.** FAQ Q7: (a) research interests at the Institute and how background and current interests align; (b) supervisors you want; (c) plans or ideas for future research direction |
| CV | **TO ADAPT.** Start from `SDU Application/cv_source.html` (two pages). Re-order to lead with ML: six fine-tuned classifiers, labelling pipeline, fusion classifier, BERT 0.878 |
| MSc and BSc transcripts + latest degree certificate | **READY:** `Application Assets/Asad_Ikram_Certificates_and_Transcripts.pdf` (MSc certificate, Portsmouth transcript, BSc degree, BSc transcript, IELTS) |
| Publications list | Only "if applicable". Skip, or one line: manuscript complete, unpublished, not submitted |
| 2 to 3 referees (typed into the form) | Haig and Ahmad. At least one must be lecturer level or above (both qualify). Contacted only if shortlisted |

**Supervisors to name (researched 15 Sep)**
1. **Eric Malmi**: Aalto adjunct professor and ELLIS Institute faculty; Staff Research Scientist at Google DeepMind leading a Gemini post-training team (user signals, distillation). At Aalto he focuses on LLMs in interdisciplinary applications in the social sciences and humanities. PhD Aalto 2018 on linking historical records. eric.malmi@aalto.fi. **Primary fit**: LLM labelling and distillation (his ArtemisAI Claude-to-DeepSeek pipeline is a distillation chain) plus computational social science.
2. **Filip Ginter**: University of Turku, NLP and language technology, large web corpora and web-register classification. Fit: web data collection at scale and what automated labels of web text measure.
3. **Corinna Coupette**: Aalto assistant professor, Telos Lab; networks, responsible AI, data-centric AI; aim to "model, measure, and manage complex systems"; ERC Starting Grant CompLex. Fit: measurement and responsible data-centric ML.
4. Optional mentions: **Shaoxiong Ji** (ML, NLP, multilingual LLMs), **Indre Zliobaite** (concept drift, which matches the instrument-drift argument).

Most other faculty are health, vision, robotics or probabilistic ML. Do not name people whose work does not connect.

**Suggested angle for the letter (not yet written)**
Open with a concrete hook from his own production system: when an LLM labels data and a cheaper model is distilled from it, the benchmark quietly becomes the teacher, so reported accuracy measures agreement, not validity (the 82.9% / 74.4% / 96.7% numbers and the v3 to v4 reference switch). Then the research question: how to validate LLM-based and distilled annotators when they are used as measurement instruments for social data, including across platforms, languages and model versions. Connect to Malmi (post-training, distillation, LLMs for social science), Ginter (web text at scale), Coupette (measurement, data-centric responsible AI). Show the career throughline briefly. Name gaps honestly: no publications, BSc grade; state how they close (manuscript, MSc Distinction, industry ML record). Keep to two pages, no em-dashes.

**Weak point to manage:** BSc CGPA 2.75. Lead with MSc Distinction, dissertation 78 and production ML.

---

## 4. Every application and where it stands (16 Sep 2026)

### Submitted, waiting
| Target | Submitted | Next |
|---|---|---|
| **PoliMi** PhD, 42nd cycle, "Auditing and Mitigating Epistemic Failures in Web-Connected AI Agents" (Pierri and Brambilla) | 9 to 10 Sep, fee EUR 25.82 paid | Rankings from about 15 Oct. Start 1 Nov |
| **SDU Odense**, "Navigating Negativity" SP1 (Kim Andersen) | 11 Sep | Kim Andersen replied 11 Sep "sounds interesting". **Do not reply to him.** Careja ECTS email not needed (closed by Asad). Start 1 Nov |
| **VU Amsterdam**, Social Data Science (Roozenbeek) | 8 Sep | Interviews 21 to 30 Sep; watch for an invite |
| **University of Vienna**, PhD in Responsible AI, job 6159 | 10 Sep (portal acknowledged) | Nothing before October; status query only if silent by 9 Oct |
| **Utrecht** "What Moves Us?" | 20 Aug | **Rejected 7 Sep.** Closed |

### Emails sent, waiting
| Who | Sent | Next |
|---|---|---|
| Meeyoung Cha (MPI-SP) | 2 Sep | **Nudge due 16 Sep** (one short note, one new fact). CS@max planck closes 15 Dec regardless |
| Fengran Mo (RIT) | 9 Sep | Nudge if silent by 24 Sep |
| Casas (Royal Holloway / LSMO) | 8 Sep | Check 29 Sep; do not nudge; close if silent |
| Gligoric (JHU), Pierri, Hovy (Bocconi), Ashton Anderson (Toronto) | 8 Sep | Check 22 Sep |

### Closed contacts
- **Theocharis (TUM):** 14 Sep, his PhD funding bid failed, next post is a postdoc. Asad replied 14 Sep. Send only the arXiv link later.
- **Saarland SOUNDS (Weber, Martin Ulrich):** call for applications aimed for autumn 2026; Asad is on the mailing list; replied 14 Sep. Note: address him "Dr Ulrich" (Martin is his first name). The Graduate School requires an entrepreneurship strand, which ArtemisAI answers.
- **Nelimarkka (Helsinki):** moving institutions, cannot supervise; closing note sent 2 Sep. Send arXiv link later only.
- **Agder:** not applying (Asad's choice 7 Sep); HR replied warmly 14 Sep.
- **Hasselt, Aarhus:** closed.

### To apply, by deadline (P1 top, P2 strong, P3 optional)
| Deadline | Pri | Target | Notes |
|---|---|---|---|
| 16 Sep | P1 | Oxford OII DPhil: register for the 2027-28 email | Applications open 16 Sep |
| **21 Sep** | **P1** | **ELLIS Institute Finland** | Section 3 |
| 30 Sep 21:59 UTC | P1 | UvA Amsterdam PhD, emotion-sensitive AI in politics and policymaking (A.I. Feels) | Salaried, strong fit |
| 2 Oct | P2 | NTNU Trondheim, efficient search engines (Jobbnorge 307690) | Weaker fit (search, not social measurement) |
| 15 Oct midnight Vienna | P1 | Complexity Science Hub Vienna Graduate Program | Email Garcia and Lasser first |
| 15 Oct 23:59 | P3 | Stockholm University DSV, MSCA SoCRISP, government crisis communication | Start Feb 2027; gap is agent-based simulation |
| 20 Oct 16:00 BST | P1 | Commonwealth PhD Scholarship 2027/28 | Portal ref 33095524-PHD-PK-27, started not submitted; via HEC nomination; UK supervisor statement needed |
| 1 Dec | P2 | EPFL EDIC round 1 | |
| 15 Dec | P1 | MBZUAI Abu Dhabi PhD in NLP (Nakov) | Best fit; GRE optional |
| 15 Dec | P3 | US December block (CMU, UW HCDE, NYU, JHU) | |
| 7 Jan 2027 | P1 | Edinburgh CDT in Responsible NLP (Magdy, Ross) | Parked until the 2027 page posts (about Oct). Drafts in `Edinburgh Application/` |
| **7 Jan 2027 12:00 UK** | P2 | **Oxford OII DPhil Social Data Science** | Same day as Edinburgh. Statement 500 words, proposal 2,500 words, 2,000-word written work, **three** referees. English HIGHER level (IELTS 7.5); request the test waiver on the MSc (gap of exactly two academic years, discretionary) |
| 15 Jan 2027 | P1 | ICWSM 2027 Round 3: the Haig paper | |

**Open decision:** PoliMi and SDU both start 1 Nov 2026, which collides with the ArtemisAI 8 Dec launch sprint. Unresolved; do not raise the "step down" idea in letters (Asad said no).

**Discovery status:** broad sweeps on 10, 11, 14 and 15 Sep found nothing else open and fitting. Hertie School advertises most stipends November to January; re-check then. Do not spend time on more searching before October.

---

## 5. Where things are in the repo

| Path | What |
|---|---|
| `index.html` | The tracker. JS arrays: `PRIORITIES` (rows with id, tier, due, time, name, why, req, link), `EVENTS` (calendar), `TODAY_ACTIONS` (top panel), `PRIO_RANK` (P1 to P3), `ACTION_META`, `ACTION_RETIRED`, `PRIO_DEFAULT_ST`, `LAST_REFRESHED`. Rows sort by due date then priority. After editing, check the script parses, commit, push to `main` |
| `MASTER_RECORD.md` | Full verified fact base and what went to whom |
| `SDU Application/` | Best recent examples: `letter_source.html` (motivated letter, STAR narrative), `proposal_source.html`, `cv_source.html`, and the PDFs. PDFs are built with headless Chrome `--print-to-pdf` |
| `PoliMi Application/` | Proposal, CV with photo, requirements, attack notes |
| `Application Assets/` | Certificates and transcripts PDF, referees PDF |
| `Paper with Ella/` | The manuscript PDF |
| `Edinburgh Application/`, `Agder Application/`, `Helsinki Application/` | Reusable proposals and statements |
| `Previous Applications/` | Older letters. **Do not reuse their claims**: they contain false statements ("trained custom LLMs", "GPT for Facebook", "300 scrapers nine countries", "five years") |
| `ielts_result.pdf`, `Asad_Ikram_MSc_Certificate.pdf`, `Asad_Ikram_Portsmouth_Transcript.pdf`, `degree_bscs_asad.pdf`, `Asad bscs transcript.pdf` | Originals |

---

## 6. How Asad likes to work

- He wants documents that tell his real journey (STAR, chronological, specific clients and numbers), not generic academic filler. He rejected a letter once for "talking about useless stuff".
- Hook-first openings. No "I will step down from" statements.
- Attack drafts adversarially before calling them final, then verify each criticism before acting on it (several "fatal" criticisms turned out wrong).
- Honest gap statements work in his letters: name the gap, then show how it closes.
- Short direct answers; tables for status; always give dates and days left.
