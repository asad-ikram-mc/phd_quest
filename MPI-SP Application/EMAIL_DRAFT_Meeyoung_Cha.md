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

## THE EMAIL

**To:** mia.cha@mpi-sp.org
**Subject:** PhD Enquiry, 2027 - Construct Validity, LLM Annotation Drift and Whether a Seven-Year Denial Trend Is Real

Dear Professor Cha,

I am writing to enquire about PhD opportunities in your Data Science for Humanity group at MPI-SP for 2027 entry, through the CS@max planck December deadline.

Your argument in the Million Follower Fallacy is the one that put me on this path. Follower count was the obvious measure of influence, everyone used it, and it turned out not to measure the thing people thought it measured. You only discover that by testing the metric against criteria instead of trusting it. I have spent seven years building systems that produce exactly that kind of untested metric at scale, and I want to work on the 2010 problem in the form it takes now.

Your FAccT paper on climate misinformation playbooks in Brazil is where I think that form is clearest. The central result is temporal, a shift from old denial to new denial across 2019 to 2025, and the labels come from GPT-4.1-mini applied across that whole window. The validation is careful, 702 human-annotated videos and a kappa of 0.89, and the paper is honest that old versus new denial is the harder call at 0.77 accuracy. What no protocol currently covers, in your work or anyone else's, is whether a proprietary annotator applied over seven years is measuring the same construct in 2025 as in 2019. A silent model update inside that window and a genuine change in the discourse leave the same trace in the data.

That gap is what my research addresses. With my MSc supervisor Dr Ella Haig I have written a methods paper, on arXiv shortly, that treats each platform as a survey mode and specifies a psychometric protocol for machine-labelled text: generalizability theory, measurement invariance and DIF testing, and score linking. Its simulation result is that across 500 replications, a pooled index taking platform scores at face value reports the wrong sign of aggregate sentiment on roughly a quarter of days, purely from measurement differences. The doctoral work I want to do extends that to the instrument itself: a shadow-anchored bridging design that keeps a series like your Brazil one comparable when the annotating model changes underneath it.

I also see this from inside production rather than only from the literature. At ArtemisAI, the company I co-founded, 3.39 million comments have gone through a multi-model annotation cascade I designed. Our two model tiers agree on 82.9 per cent of sentiment labels and 0.0 per cent of toxicity labels, while the toxicity model reports 96.7 per cent average confidence. The dashboard's accuracy number is, when you read the code, inter-model agreement with no criterion behind it. I built that system, and it is why I stopped trusting instruments I had not calibrated.

Two things I would bring to a group working on the Global South. At Dubizzle Labs I led the team running over 500 scrapers across fifteen countries in Arabic, Urdu and Hindi, so multilingual collection at scale is routine work for me rather than a project risk. And I am Pakistani and based in Lahore, so the information environments your group studies are not ones I would be visiting.

I am applying through CS@max planck for the 15 December deadline and would like to name your group. Before I do, may I ask whether you expect to take a doctoral student in this direction for 2027, and whether calibration of LLM annotation is something you would want pursued inside Data Science for Humanity? I have attached my CV and would be glad to send the paper or a fuller research proposal.

Best wishes,
Asad Ikram

Chevening Scholar 2024/25 | MSc Data Analytics (Distinction), University of Portsmouth
asad.ikram53@gmail.com
https://linkedin.com/in/asad-ikram98
https://asad-ikram-mc.github.io/portfolio/

---

## BEFORE SENDING
- [ ] Verify mia.cha@mpi-sp.org on mpi-sp.org/cha
- [ ] Attach Asad_Ikram_Full_Resume_2026.pdf
- [ ] If the arXiv paper is live by then, replace "on arXiv shortly" with the actual link. It is a materially stronger email with the link in it, so send it AFTER the paper posts if that is days away rather than weeks.
- [ ] Read it aloud once for the AI test
