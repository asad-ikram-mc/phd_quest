# Edinburgh UKRI CDT in Designing Responsible NLP: Stage 1 form answers (2027 entry)

Form: https://app.onlinesurveys.jisc.ac.uk/s/edinburgh/drnlp-cdt-2026 (save and return is allowed; once submitted it cannot be edited)
Deadline: 30 November 2026, midnight UK time. Target: submit by 10 November.
No attachments at Stage 1. Everything is typed into the form. Text boxes allow up to 32,000 characters; the answers below are deliberately much shorter.

Rules applied: no em dashes; research and analysis first, infrastructure in one line; the CDT's own vocabulary (Skills Domains, in-the-world, measurement bias, field book); no promises of future dates.

---

## Page 2: Personal details (fill yourself)
- Last name: Ikram
- First name(s): Asad
- Nationality: Pakistani
- Current address: (your Lahore address), Pakistan
- Email: asad.ikram53@gmail.com

## Degrees (fill yourself; check the exact fields on the form)
- MSc Data Analytics, University of Portsmouth, UK, 2025, Distinction. Chevening Scholar 2024/25. Dissertation supervised by Dr Ella Haig.
- BS Computer Science, FAST National University of Computer and Emerging Sciences (FAST-NUCES), Pakistan, awarded January 2022.

---

## 1. Research experience (within and beyond academia)
*(about 430 words)*

My research experience has one thread: measuring public opinion from social media text, and finding out when that measurement can be trusted.

**MSc dissertation (University of Portsmouth, 2025, supervisor Dr Ella Haig).** I studied how public reaction to UK economic policy (tax, prices, welfare, energy, housing) differed across X, Reddit, YouTube and Quora. The project was mine from question to write-up. I obtained ethics approval, collected 255,446 public comments through official APIs and licensed feeds, and built the analysis in Python: VADER and BiLSTM baselines, a fine-tuned BERT classifier (macro-F1 0.878), temperature-scaling calibration, McNemar and bootstrap tests, Prophet forecasts, NRC emotion scores, and LIME and integrated gradients to see what the model relied on. Public mood fell sharply around the 2022 mini-budget, and the platforms told different stories.

**What did not go as expected, and what it taught me.** After submission I realised the validation was circular. BERT had been trained on labels seeded by the VADER lexicon and evaluated against the same kind of labels, and my 200 hand-labelled posts were a review of VADER's output, so the Cohen's kappa of about 0.78 measured agreement with VADER rather than with independent human judgement. I had also assumed, without testing it, that a "negative" label means the same thing on Reddit as on YouTube. And because the pipeline was English-only, posts in other languages about the same policy events were simply dropped: the measure was silent about anyone not writing in English. The lesson was that a high agreement score describes the reference as much as the model, and that comparisons across groups need evidence that the instrument behaves alike in each group.

**Methods paper (arXiv:2610.16757, October 2026, with Dr Ella Haig).** We turned that lesson into *Is the Platform Part of the Measurement?* The paper treats each platform as a survey mode and sets out a six-step protocol from survey methodology: anchor events fixed in advance, a generalizability study against human labels, measurement invariance and differential item functioning (DIF), a multilevel model for who posts, score linking onto one scale, and a known-truth simulation. I wrote the simulation (Python, 500 replications, public code on GitHub): pooling platform scores at face value reports the wrong direction of daily sentiment on 13.8 of 60 days on average, against 0.8 days for a measurement-adjusted index. Every test is repeated with a second model family (RoBERTa), and the fifteen policy anchor events were fixed and recorded before any counts were computed.

**Research beyond academia.** At M+C Saatchi Fluency I ran a year-long discourse study of 100,845 posts: BERTopic for theme discovery, LLM tagging with a prompt-version hash on every label, three pilot runs on the same 500 posts to check stability, and Twitter and Reddit reported as two separate publics rather than added together. At Artemis AI, the company I co-founded, I audited our own labelling pipeline and found that a dashboard "accuracy" figure was really agreement between two models, with no human reference behind it. We are now designing evaluation around human-labelled sets.

---

## 2. Publications, outputs and links (optional)
- Ikram, A. and Haig, E. (2026). *Is the Platform Part of the Measurement? A Protocol and Simulation Study for Cross-Platform Equivalence of Machine-Labelled Policy Sentiment.* arXiv:2610.16757. https://arxiv.org/abs/2610.16757
- Simulation and protocol code: https://github.com/asadfix/platform-measurement (Zenodo DOI 10.5281/zenodo.23105129)
- MSc dissertation (Distinction), University of Portsmouth, 2025: available on request.
- Web Scraping Guide, a free public guide to responsible web data collection that I write and maintain: https://web-scraping-guide.com
- Portfolio: https://asad-ikram-mc.github.io/portfolio/


---

## 3. Professional or other relevant experience
*(about 400 words)*

I have worked with social media and web data for nearly eight years, and each role showed me a different way that NLP measurement can fail people who rely on it.

**Fiverr (2018 onwards, starting while I was studying).** As a Level 2 seller I completed more than 300 projects, mostly data collection and analysis tools for clients around the world. It taught me to scope a problem with non-technical people and deliver to a deadline.

**Dubizzle Labs, Lahore (2022 to 2024).** Promoted twice to Senior Data Engineer, I built the company's first web-scraping and data system for six products across nine countries in the Middle East, collecting online listings and discussion in English, Arabic, Urdu and Hindi, and led a team of three engineers. Working across four languages showed me early that models trained on English text do not travel cleanly to other languages and cultures.

**CXG, Dubai (Data Engineer, since December 2025).** I collect and analyse product data for global fashion and luxury brands such as Prada. The same attribute is recorded differently in every region and language, so the first job is always building one shared vocabulary before anything is compared.

**Chevening Scholarship (2024/25).** I was selected by the UK Government with a proposal for a cross-platform system to give governments early, honest evidence of public reaction to policy. That idea became my MSc dissertation and then my paper.

**M+C Saatchi Fluency, London (current).** I work on social listening and social media analytics for global brands and for UK government clients. I see first-hand how sentiment dashboards are read by decision-makers, and how rarely the numbers are checked against people. I also built self-repairing data pipelines in which every automated fix needs human approval and is logged, because a pipeline that breaks silently thins a time series and quietly biases any trend drawn from it.

**Artemis AI (co-founder and CTO, since February 2025).** We build analytics for creators and small businesses, including comment classification (sentiment, toxicity, intent), a detector for bursts of hostile comments, filters so that dialect and local banter are not misread as toxicity, and community detection on the network of pages. We have processed more than three million comments and are preparing a December beta. Running it has made the responsible-NLP questions concrete for me: who is misread by our models, how we explain a score to a small business owner, and what we owe the people whose comments we classify.

Across these roles I collect data through official APIs where they exist, with polite rate limits and licensed sources otherwise, and I have learned to treat data documentation as part of the product. I would bring this practical experience of NLP deployed in-the-world to the cohort, and I am looking for the research training to do it properly.

---

## 4. Statement of Alignment
*(about 950 words)*

### Primary Skills Domain: Responsible NLP data and models
I align most with Responsible NLP data and models, and specifically with the CDT's focus on locating measurement bias and on how NLP datasets and models translate, or fail to translate, across cultures and non-Anglo-centric contexts.

NLP is now routinely used as a measuring instrument. Researchers, companies, newsrooms and regulators ask LLMs and fine-tuned classifiers to read social media and report how the public feels about a policy, a product or a group. The resulting numbers are pooled across platforms, tracked over years and compared across countries. My own work shows how fragile this is. In my MSc, a classifier that looked 88 per cent accurate was only agreeing with the lexicon that produced its training labels. In our paper, a simulation shows that simply averaging platforms gets the direction of public mood wrong on about a quarter of days, even when every platform sees the same underlying opinion. Jacobs and Wallach (2021) argue that many fairness failures are measurement failures; I think the same is true of NLP used to measure society.

### Research directions I would like to pursue
1. **Equivalence across platforms and languages.** When is a machine-labelled construct (sentiment, stance, toxicity, a narrative frame) comparable across platforms and across languages? I want to test invariance and DIF with platform and language as groups and a human-coded criterion inside the measurement model, starting with English, Arabic and Urdu or Hindi communities where I can collect and read the data myself. This connects directly to Professor Walid Magdy's work on Arabic NLP, including sarcasm in Arabic sentiment (Abu Farha and Magdy, 2020), and on bias and culture in LLMs: a sarcastic or dialectal post that an English-trained model reads as positive is exactly the kind of measurement bias that distorts a cross-language comparison.
2. **LLM annotators that change under our feet.** Research increasingly uses LLMs as annotators (Gilardi et al., 2023), but model versions and prompts change, and a change in the model can look like a change in society. I want to develop designs that keep a measurement series comparable across model updates: a fixed human-labelled anchor set, version and prompt logging, and correction with a small human sample in the spirit of Egami et al. (2023).
3. **Who is represented in the measure.** Public comments over-represent certain voices; Chen, Kmetty, Iñiguez and Omodei (2025) show that people who comment are more polarised than people who only watch. Combined with automated and coordinated accounts, this means a "public opinion" index can systematically misrepresent groups. This joins Dr Björn Ross's and Dr Tj Elmas's work on social media, misinformation and bots.

These matter to the CDT because a biased instrument does not only produce a wrong number. It produces a wrong picture of specific communities, and that picture is then used to make decisions about them.

### Other Skills Domains I want to develop
**Governance and accountability.** Social media measurement is becoming a regulatory act. Researcher data access under Article 40 of the EU Digital Services Act, systemic-risk assessments, and the UK Online Safety Act all depend on measurements like the ones I study. I have built such systems from the engineering side, but I have no training in law or governance, and I want to learn how a measurement standard can hold up in-the-world and not just on paper. Dr Clare Llewellyn's work on AI, politics and NLP is a natural bridge here.

**Explainable NLP for users in-the-world.** The people who read sentiment dashboards, from small business owners at Artemis AI to policy teams, cannot see why a trend line moved. I would like to design a short, readable "instrument change log" for annotation pipelines, a model card for measurement, and test with real users whether it helps them decide when to trust a number.

### Working across disciplines and with partners
My work has always sat between people who build systems and people who use them. At Fluency I translate between engineers, analysts and clients; at Artemis AI I work with designers, product and legal advice; my paper borrows its core tools from survey methodology, a field outside my training. In the CDT I would like to pair with students from law, philosophy and design on shared projects. For example, a lawyer and I could test whether a measurement standard would satisfy a regulator, and a designer and I could co-create explanations with the people whose comments are being measured. With industry partners I can offer realistic test cases from social listening and creator analytics, and I would welcome a placement with a regulator or a public body that uses social media evidence. I would also like to contribute practical guidance on measurement documentation to the CDT's open-source field book.

### Why the CDT, rather than a traditional PhD
I do not want to arrive with a fixed proposal and execute it. My industrial path has given me data and engineering skills but left gaps in governance, explainability and participatory methods, and the CDT's integrated training is designed exactly to fill those gaps while the research question matures. My long-term aim is to translate this research into practice: open tools and standards that let researchers, companies and public bodies check when an NLP-based measure of public opinion can be trusted.

**References cited:** Abu Farha, I. and Magdy, W. (2020), From Arabic sentiment analysis to sarcasm detection: the ArSarcasm dataset, OSACT 2020. Jacobs, A. Z. and Wallach, H. (2021), Measurement and Fairness, ACM FAccT. Gilardi, F., Alizadeh, M. and Kubli, M. (2023), ChatGPT outperforms crowd workers for text-annotation tasks, PNAS. Egami, N. et al. (2023), Using imperfect surrogates for downstream inference, NeurIPS. Chen, Y., Kmetty, Z., Iñiguez, G. and Omodei, E. (2025), Communication Methods and Measures. Ikram, A. and Haig, E. (2026), arXiv:2610.16757.

---

## 5. Potential supervisors (optional)
1. **Prof. Walid Magdy** (primary): computational social science, Arabic NLP, low-resource languages, bias and culture in LLMs. He agreed on 3 April 2026 to be listed for this CDT and asked me to get a publication first; the paper now exists.
2. **Dr Björn Ross**: computational social science, social media, AI fairness. He replied in March 2026 that the project was a great fit and pointed me to this CDT.
3. **Dr Tj Elmas**: social media, misinformation, bots, political manipulation.
4. **Dr Clare Llewellyn** (Governance and accountability): AI, politics, data, NLP. Second-domain supervisor.
5. (Optional) **Dr Zee Talat**: critical machine learning, content moderation.

---

## Before submitting: checklist
- [ ] Email Magdy and Ross a two-line update with the arXiv link and say the Stage 1 form is going in this cycle (their earlier replies were March 2026).
- [ ] Request a letter from Portsmouth confirming the MSc was taught and assessed in English (needed at Stage 2; no IELTS).
- [x] arXiv title checked against the v1.1 PDF.
- [ ] Confirm that the Artemis "three million comments" and "December beta" lines are still accurate.
- [ ] Referees for Stage 2: Dr Ella Haig (academic) and Dr Fahad Ahmad (academic); Jareed Eve is an option as employer referee.
- [ ] Read every answer aloud once and change anything that does not sound like you.
- [ ] Submit by 10 November. The form cannot be edited after submission.
