# Outreach email: Prof. Meeyoung Cha (MPI-SP, Data Science for Humanity)
# Drafted 2 Sep 2026 · verified against her pages and papers the same day
# Route: CS@max planck doctoral programme, deadline 15 Dec 2026 for Fall 2027

## VERIFIED FACTS BEHIND THIS EMAIL (all checked 2 Sep 2026)
- **Her role:** Scientific Director, MPI-SP Bochum (since 2024); leads the **Data Science for Humanity** group (13 members listed); joint Professor at KAIST; previously IBS, Facebook (visiting 2015-16), postdoc at MPI-SWS.
- **Email:** mia.cha@mpi-sp.org (verify on mpi-sp.org/cha before sending).
- **Group agenda (their words):** harness data science for social impact; how digital technologies shape human behaviour, public discourse and societal trust; misinformation, privacy, algorithmic bias; collaborates with NGOs; deliberately interdisciplinary (geography, neuroscience, journalism, HCI, economics, physics, CS).
- **The hook paper:** Cha, Haddadi, Benevenuto, Gummadi, "Measuring User Influence in Twitter: The Million Follower Fallacy", ICWSM 2010. **ICWSM Test-of-Time Award 2020.** Compared indegree, retweets and mentions; showed follower count does not measure influence. It is a construct-validity paper, which is the entire through-line to Asad's work.
- **The live paper:** Locatelli, Dong, Alzamora, Dutenhefner, Meira, **Cha**, Almeida, "Mapping Emerging Climate Misinformation Playbooks in the Global South", **FAccT 2026** (arXiv 2604.24223). 226,775 climate YouTube videos, **Brazil, 2019-2025**. Finds a transition from "old denial" (disputes the science) to **"new denial"** (accepts climate change, attacks the solutions), which "often evades existing moderation policies".
- **Their method, which is the opening:** labels come from **GPT-4.1-mini with Chain-of-Thought prompting** over the whole seven-year window. Validated against **702 human-annotated videos** (351 random + 351 balanced), Cohen's kappa **0.89** for denial detection and **0.87** for narrative classification, overall accuracy **0.90** / F1 **0.86**, but **0.77 accuracy / 0.75 F1** on the old-versus-new distinction that carries the paper's central claim. The paper acknowledges annotation limits but **does not address label consistency over time**.
- **Why that matters:** the headline result is a TEMPORAL TRANSITION measured with a proprietary annotator across seven years. Instrument drift and a real discourse shift are not separable in that design. That is exactly Study 2 of the Calibrating the Observatory proposal, and it is a field-level gap, not a flaw peculiar to her team. Say it that way.
- **Programme:** CS@max planck, full financial support, Bachelor's or Master's in CS or a related field (Asad's BSc CS at FAST-NUCES qualifies), applications open 1 Sep, **close 15 Dec** for Fall admission. Admits to the programme rather than straight to an advisor, so students explore before committing. The MPI-SP positions page explicitly welcomes direct outreach to group leaders.

## SIX CHECKS
1. Names her own paper? YES, the Million Follower Fallacy by name plus the FAccT 2026 paper.
2. Finding lands inside her theory? YES, construct validity is her 2010 argument; the paper generalises it.
3. ArtemisAI gap = her research problem? YES, the 0.0% toxicity agreement is a silent annotation failure of the kind her Brazil pipeline could not detect.
4. Her vocabulary? YES: new denial, moderation policies, denial detection, Global South.
5. Nelimarkka test? YES. It does not say "platforms differ" or "LLM labels are noisy". It starts where her paper stops: a seven-year series labelled by a model that can change underneath it.
6. AI test? No em-dashes, no triads, contractions where natural.

---

## THE EMAIL (v2, 2 Sep - rebuilt to follow all eight parts of the master pattern)

**To:** mia.cha@mpi-sp.org
**Subject:** PhD Enquiry, 2027 - Construct Validity, LLM Annotation Drift and Cross-Platform Measurement Validity

Dear Professor Cha,

I am writing to enquire about PhD opportunities in your Data Science for Humanity group at MPI-SP for 2027 entry, through the CS@max planck December deadline. I wanted to ask whether my background connects to the measurement question you raised in the Million Follower Fallacy. Follower count was the obvious measure of influence, everyone used it, and it turned out not to measure what people assumed it measured. You only find that out by testing the metric against a criterion instead of trusting it. I have spent seven years building systems that produce exactly that kind of untested metric at scale, and I want to work on your 2010 problem in the form it takes now.

My Chevening Scholarship was built around a specific professional problem: social media analytics already inform government decisions, but the measurement systems underneath them cannot say whether a number means the same thing from one platform, or one year, to the next. At M+C Saatchi Fluency I built the infrastructure that processes social listening data daily for UK Government departments alongside Amazon, Ford and Nike. At Dubizzle Labs I led the team running over 500 scrapers across fifteen countries in Arabic, Urdu and Hindi, so multilingual collection at scale is routine work for me rather than a project risk. I am also Pakistani and based in Lahore, so the information environments your group studies are not ones I would be visiting.

Your FAccT paper on climate misinformation playbooks in Brazil is where I think that problem is clearest. The central result is temporal, a shift from old denial to new denial across 2019 to 2025, and the labels come from GPT-4.1-mini applied across that whole window. The validation is careful, 702 human-annotated videos and a kappa of 0.89, and the paper is honest that old versus new denial is the harder call at 0.77 accuracy. What no protocol currently covers, in your work or anyone else's, is whether a proprietary annotator applied over seven years measures the same construct in 2025 as it did in 2019. A silent model update inside that window and a genuine change in the discourse leave the same trace in the data.

That is the problem I have been working on. My MSc dissertation at Portsmouth built a cross-platform NLP framework analysing 279,000 posts across Twitter, Reddit, YouTube and Quora on UK economic policy, using fine-tuned BERT at macro-F1 0.878 against BiLSTM and lexicon baselines. The finding that mattered was not the accuracy. It was that the same policy event produced structurally different sentiment profiles on each platform, YouTube included, which means a cross-platform aggregate rests on an assumption nobody had tested.

That finding is now a methods paper with my MSc supervisor Dr Ella Haig, "Is the Platform Part of the Measurement?", which treats each platform as a survey mode and specifies a six-step psychometric protocol for machine-labelled text: generalizability theory, measurement invariance and DIF testing, and score linking. Across 500 replications of a known-truth simulation, a pooled index that takes platform scores at face value reports the wrong sign of aggregate sentiment on roughly a quarter of days, purely from measurement differences, while a measurement-adjusted index does not. It goes on arXiv shortly; the project page is https://asadfix.github.io/publish_proposal/#paper.

I also see this from inside production rather than only from the literature. I am CTO and co-founder of ArtemisAI (https://www.artemisai.co.uk), where 3.39 million comments have gone through a multi-model annotation cascade I designed. Our two model tiers agree on 82.9 per cent of sentiment labels and 0.0 per cent of toxicity labels, while the toxicity model reports 96.7 per cent average confidence. The dashboard's accuracy figure is, when you read the code, inter-model agreement with no criterion behind it. I built that system, and the failure it hides is the same one a labelling pipeline cannot see from the inside.

The question I want to pursue at doctoral level is whether a denial-detection series can be held comparable across model versions the way survey series are held comparable across instrument changes, and if so, what a shadow-anchored bridging design for LLM annotation would look like in practice.

I am looking for a fully funded position for 2027 entry and would apply through CS@max planck for the 15 December deadline, naming your group. Before I do, may I ask whether you expect to take a doctoral student in this direction, and whether calibration of LLM annotation is something you would want pursued inside Data Science for Humanity? I have attached my CV and would be glad to share the paper, my dissertation or a fuller research proposal.

Best wishes,
Asad Ikram

Chevening Scholar 2024/25 | MSc Data Analytics (Distinction), University of Portsmouth
asad.ikram53@gmail.com
https://linkedin.com/in/asad-ikram98
https://asad-ikram-mc.github.io/portfolio/

---

## PATTERN COMPLIANCE (audited 2 Sep, v1 failed four of these)
| Element | v1 | v2 |
|---|---|---|
| Rule 1, no em-dashes | pass | pass |
| Rule 2, exact opening line | pass | pass |
| Rule 3, hook on her named paper | pass (Million Follower Fallacy + FAccT 2026) | pass |
| Rule 6, project page link while arXiv pending | **FAIL, no link** | pass |
| Part 2, Chevening + government problem | **MISSING** | pass |
| Part 3, Fluency + Dubizzle + Fix.com | partial (Dubizzle only) | Fluency + Dubizzle (Fix.com dropped on purpose, no relevance to her) |
| Part 4a, dissertation 279k / 0.878 / four platforms | **MISSING** | pass, with YouTube named to meet her own platform |
| Part 4b, paper title + 500 / quarter of days | partial, no title | pass |
| Part 5, ArtemisAI as her problem | pass | pass, with CTO framing and site link |
| Part 6, explicit bridging question in her vocabulary | weak, folded into the ask | pass, stated separately |
| Part 7, funding note | **MISSING** | pass |
| Part 8, the ask | pass | pass |
| Signature exact | pass | pass |
| Subject line template | off-template third slot | pass |

**Alternative subject line**, off-pattern but sharper, if you want it: `PhD Enquiry, 2027 - Construct Validity, Annotation Drift and Whether a Seven-Year Denial Trend Is Real`. It is more arresting and it is the actual thesis of the email; the template version above keeps the campaign consistent. Your call.

## BEFORE SENDING
- [ ] Verify mia.cha@mpi-sp.org on mpi-sp.org/cha
- [ ] Attach **Asad_Ikram_CV_Academic_MPI.pdf** (in this folder), NOT the industry Full Resume. The master pattern's rule 4 says attach the full resume, but that file is the Full Stack Data Engineer version (anti-bot evasion, proxy rotation, DevOps) and it is the wrong artifact for a Max Planck director. The academic CV here leads with the paper, the doctoral proposal and the dissertation, names YouTube to meet her own platform, foregrounds the multilingual and Global South record for her group, and boxes the ArtemisAI 82.9/0.0/96.7 finding as the motivation. Source: cv_source.html in this folder. **HONESTY RULE APPLIED 2 Sep at Asad's instruction:** nothing is published yet, so the section is headed **Research**, not Publications; the Haig paper is labelled *Manuscript, 2026 ... to be posted to arXiv (cs.SI)* rather than implying it is live; the **Calibrating the Observatory proposal was REMOVED** from the CV entirely because an unposted proposal listed among research output reads as padding to a director; and web-scraping-guide.com moved to Awards and public work, where it belongs, since it is not a publication. The Research section is now the paper and the dissertation, and nothing else. Re-add the proposal only if a programme explicitly asks for a research plan, and add the arXiv ID to the paper line the moment it posts.
- [ ] If the arXiv paper is live by then, replace "on arXiv shortly" with the actual link. It is a materially stronger email with the link in it, so send it AFTER the paper posts if that is days away rather than weeks.
- [ ] Read it aloud once for the AI test
