# VU Amsterdam - PhD Position in Social Data Science
# Deadline: Monday 14 September 2026, 23:59 · Interviews 21-30 Sep · Start 4 Jan 2027
# Verified from workingat.vu.nl 2 Sep 2026

## THE POST, VERIFIED
- **Title:** PhD Position in Social Data Science. Faculty of Social Sciences and Humanities, **Department of Communication Science**.
- **Supervisors:** Assoc. Prof. **Jon Roozenbeek** (PI, splits time between Cambridge and Amsterdam; Director of the Influence and Technology Lab at Cambridge) and Assoc. Prof. **Ivar Vermeulen** (Head of Department, persuasion researcher, co-director of the Digital Media & Behaviour Lab).
- **Project:** "The economy of digital influence operations", NWO **Vidi**-funded. Maps the **online manipulation economy**: the market where fake accounts, fake engagement and bot services are bought and sold. Identify buyers and sellers, interview key players, analyse social media and financial data, and find policy and regulatory interventions. VU's own headline for the grant was "Banning Bad Bots".
- **Documents:** "Curriculum Vitae and short application letter (in Dutch or English; **maximum 2 pages**)". Online portal only, email applications not accepted.
- **Terms:** EUR 3,204 to 4,051 gross/month, 1 year then extended to 4 on satisfactory evaluation.
- **Methods named:** experimental design, quantitative analysis, **time series analysis**, social media data collection, qualitative interviews, open science.

## REQUIREMENTS vs ASAD, HONESTLY
| They ask for | Position |
| --- | --- |
| Completed **research master's** in Social Data Science, Communication Science, Psychology or Economics | **GAP.** MSc Data Analytics (Portsmouth, Distinction) is a UK one-year taught MSc, not a Dutch two-year onderzoeksmaster, and the field is data analytics rather than one of the four named. **Ask Roozenbeek before the deadline.** |
| Strong quantitative empirical research design | Strong. Dissertation with a pre-registered-style protocol, human validation, significance testing; the Haig methods paper. |
| Advanced statistics **including time series** | Strong. Prophet forecasting of a daily sentiment index (MAE ~0.02); KL-divergence drift detection on production time series; McNemar and bootstrap CIs. |
| **Python and R essential** | Python daily for seven years. **R: check your own honest level before sending.** The psychometric protocol in the paper is lavaan-shaped work; if your R is reading-and-adapting rather than fluent, say "Python daily, R for the psychometric work" and do not overclaim. |
| Excellent English academic writing | Yes. 23-page methods paper, a 24-section public technical reference. |
| Russian and/or Mandarin **preferred** | No. Urdu native, and production collection in Arabic, Urdu and Hindi. Preferred, not required. |
| Works independently (supervisor is part-time in Amsterdam) | Strong. Founded and runs a company, leads distributed teams, seven years of remote delivery. |

## THE ASYMMETRY, WHICH IS THE WHOLE CASE
The project cannot be done without collecting data from people who do not want to be collected from: bot vendors, engagement farms, resale marketplaces, and the sites that broker them. That is adversarial data collection, and it is a specialist engineering skill that almost no Communication Science or Psychology graduate has. It is what Asad has done for seven years across 500+ production scrapers, and he has published the public reference on it. Everything else in the application supports that one sentence.

---

# 1. PRE-EMAIL TO ROOZENBEEK (send this first, it does double duty)

**To:** j.roozenbeek@vu.nl (VERIFY on vu.nl/en/research/scientists/jon-roozenbeek before sending)
**Subject:** Eligibility question, PhD in Social Data Science (economy of digital influence operations)

Dear Dr Roozenbeek,

I am preparing an application for the PhD position on the economy of digital influence operations, and I have one eligibility question I would rather ask than guess at.

The advert asks for a completed research master's in Social Data Science, Communication Science, Psychology or Economics. Mine is an MSc in Data Analytics from the University of Portsmouth, taken with Distinction as a Chevening Scholar, which is a one-year UK taught master's rather than a Dutch two-year research master. Would that rule me out, or is it something the committee would consider alongside the rest of a profile?

I ask because the part of your project I am strongest on is the part that is hardest to staff. Mapping a market where fake accounts and engagement are sold means collecting data from vendors who actively resist collection, and that is what I have done for seven years: over 500 production scrapers across fifteen countries at Dubizzle Labs, a self-healing crawler fleet at M+C Saatchi Fluency, and a public 24-section engineering reference on the subject at web-scraping-guide.com. On the analysis side, my MSc dissertation applied fine-tuned BERT and Prophet time-series forecasting to 279,000 posts across four platforms, and I have a methods paper with my supervisor on whether machine-labelled measures of online behaviour mean the same thing across platforms, which bears on how a market of this kind gets measured at all.

I will submit before the 14 September deadline either way. I would simply rather know whether the master's requirement is firm.

Best wishes,
Asad Ikram

Chevening Scholar 2024/25 | MSc Data Analytics (Distinction), University of Portsmouth
asad.ikram53@gmail.com
https://linkedin.com/in/asad-ikram98
https://asad-ikram-mc.github.io/portfolio/

---

# 2. THE APPLICATION LETTER (max 2 pages)

Dear Dr Roozenbeek and Dr Vermeulen,

I am applying for the PhD position in Social Data Science on the economy of digital influence operations.

Your project has a bottleneck that is not psychological or theoretical. It is collection. To map a market where fake accounts, fake engagement and bot services are bought and sold, someone has to get reliable data out of vendors, resellers and brokers who actively resist being measured, and keep getting it as they change their defences. That is the part of the project I can do on day one, and it is the part that is hardest to staff from within communication science.

I have spent seven years doing exactly this work. At Dubizzle Labs I led a three-engineer team running over 500 production scrapers across fifteen countries, collecting in English, Arabic, Urdu and Hindi. At M+C Saatchi Fluency I built and run a self-healing crawler fleet of 68 collectors with an agentic repair layer, so that when a source changes its structure the fleet diagnoses the break and repairs itself rather than going quietly empty. I wrote the public engineering reference on this subject, web-scraping-guide.com, a 24-section guide covering fingerprinting, anti-bot systems, the legal landscape from hiQ v. LinkedIn to Meta v. Bright Data, and the failure modes where a collector returns a valid-looking response containing nothing. Those failure modes matter here: a market study that silently loses a vendor for six weeks does not report an error, it reports a smaller market.

The analysis side is where my research sits. My MSc dissertation at Portsmouth, completed with Distinction as a Chevening Scholar, built a cross-platform framework over 279,000 posts from Twitter, Reddit, YouTube and Quora on UK economic policy, using fine-tuned BERT at macro-F1 0.878 against BiLSTM and lexicon baselines, with human validation, calibration, McNemar and bootstrap testing, and Prophet forecasting of the daily sentiment index. The finding that mattered was that the same event produced structurally different profiles on different platforms, which meant the pooled measure rested on an assumption nobody had tested.

That question became a methods paper with my supervisor Dr Ella Haig, "Is the Platform Part of the Measurement?", which treats each platform as a survey mode and applies psychometric tools, generalizability theory, measurement invariance and DIF testing, and score linking, to machine-labelled text. In a 500-replication simulation with known ground truth, an index that takes platform scores at face value reports the wrong sign of aggregate sentiment on roughly a quarter of days, purely from measurement differences. The paper is complete and goes to arXiv shortly.

I think that question is directly load-bearing for your project. Estimating the size and structure of a manipulation market means classifying accounts and engagement as authentic or inauthentic, and the estimate inherits whatever that classifier gets wrong. If the detector behaves differently across platforms, or drifts as the vendors adapt, the resulting market trend is partly a measurement artefact. I would want to build the calibration into the design rather than bolt it on, so that when the project reports how the market moved, that claim is defensible.

I also know this problem from inside a production system rather than only from the literature. I am the founder and CTO of ArtemisAI, where 3.39 million comments have gone through a multi-model annotation cascade I designed. Our two model tiers agree on 82.9 per cent of sentiment labels and 0.0 per cent of toxicity labels, while the toxicity model reports 96.7 per cent average confidence. The dashboard's accuracy figure turned out, on reading the code, to be inter-model agreement with nothing behind it. I built that system and I built the honesty controls that now make it say "not comparable" instead of inventing a number, and that experience is why I care about this rather than finding it abstract.

On the practical requirements: Python is my daily working language and has been for seven years; my statistical work includes time series, and the drift detection running in my production fleets is a time-series problem I solve weekly. I work independently by necessity, having built and run a company alongside consulting engagements across five countries, so a supervisor splitting time between Cambridge and Amsterdam is a working arrangement I am comfortable with. English is my academic working language. I do not have Russian or Mandarin.

One thing I should state plainly rather than let you discover it. My master's is a one-year UK taught MSc in Data Analytics, not a two-year Dutch research master in one of the four fields you name. I have written to Dr Roozenbeek separately to ask whether that is firm. If it is, I would rather you spend the time on candidates who qualify. If there is discretion, I would ask you to weigh it against seven years of building the collection infrastructure this project depends on, a completed methods paper on measuring exactly the kind of construct this project has to measure, and a dissertation that did the quantitative work end to end.

I would be glad to discuss any of it.

Best wishes,
Asad Ikram

Chevening Scholar 2024/25 | MSc Data Analytics (Distinction), University of Portsmouth
asad.ikram53@gmail.com | https://linkedin.com/in/asad-ikram98 | https://asad-ikram-mc.github.io/portfolio/

---

## BEFORE SUBMITTING
- [ ] **Verify your honest R level** and adjust the "Python is my daily working language" sentence if you want R named. Do not overclaim; they list R as essential and will test it at interview.
- [ ] Send the pre-email to Roozenbeek first (verify the address on vu.nl). It resolves the eligibility question and puts your name in front of the PI before the pile lands.
- [ ] Attach the academic CV: MPI-SP Application/Asad_Ikram_CV_Academic_MPI.pdf works as-is (Research = paper + dissertation, nothing claimed as published).
- [ ] Check the letter fits 2 pages once formatted. If it runs over, cut the ArtemisAI paragraph to two sentences; it is the most compressible.
- [ ] Submit through the VU portal only. Email applications are not accepted.
- [ ] If the arXiv paper posts before 14 Sep, replace "goes to arXiv shortly" with the link in both documents.
