# VU Amsterdam - PhD in Social Data Science (Roozenbeek, "The economy of digital influence operations")
# Closes Monday 14 September 2026, 23:59 · Interviews 21-30 Sep · Start 4 Jan 2027
# Pack v2, rewritten 3 Sep 2026 after a 33-agent research sweep. v1 was aimed at the wrong target.

## WHAT CHANGED FROM v1, AND WHY IT MATTERS
v1 built the application around an eligibility gap that **does not exist**, and never mentioned the thing the job actually is. Both errors are corrected here.

**1. There is no eligibility gap.** The advert, verified live on 3 Sep, reads:
> "holds a completed **(research)** master's degree in **(Social) Data Science**, Communication Science, Psychology, or Economics; **excellent grades, particularly for final-year dissertations, are preferred**."

Both brackets are load-bearing. "(research)" makes the Dutch two-year research master optional, not required. "(Social) Data Science" puts plain data science in-field. An MSc in Data Analytics at Distinction with a 78 dissertation mark meets the requirement and hits the stated preference. **Do not concede a disqualification the advert does not impose.** v1's closing paragraph did exactly that and has been deleted.

**2. There is no pre-email.** v1 drafted one whose only purpose was the eligibility question, which has now dissolved. The advert also says "Applications received by e-mail will not be considered" and "Acquisition in response to this advertisement is not appreciated". There is a contact route for genuine questions about the vacancy, but a question the advert answers in a bracket signals you did not read it. **Put everything into the letter and apply through the portal.**

**3. The job is COTSI.** The advert names one concrete deliverable: "You will also be responsible for building and maintaining public-facing outputs such as the **Cambridge Online Trust and Safety Index** (https://cotsi.org/)". v1 never mentioned it. It is now the opening line.

---

## THE PROJECT, VERIFIED
- **Post:** PhD Position in Social Data Science, Faculty of Social Sciences and Humanities, **Department of Communication Science**, VU Amsterdam. Published 17 Aug 2026, closes 14 Sep 2026 23:59.
- **Supervisors:** Assoc. Prof. **Jon Roozenbeek** (directs the **Influence and Technology Lab**, which sits between Cambridge Psychology and VU Communication Science; PhD in Slavonic Studies, Cambridge 2020, on propaganda in Russian-occupied Donbas) and Assoc. Prof. **Ivar Vermeulen** (VU; persuasion, misinformation correction, replication; co-director of the Digital Media & Behaviour Lab; department research manager).
- **Dissertation format: CUMULATIVE** (a set of papers, not a monograph). Plan four.
- **Duties, verbatim:** "You will design experiments, collect and analyse quantitative data (e.g., social media data, qualitative interviews), and publish your findings"; "building and maintaining public-facing outputs such as the Cambridge Online Trust and Safety Index"; "conduct interviews with key players to understand their motivations"; "build bespoke analysis pipelines of social media and financial data".
- **Profile asks:** interest in market infrastructures enabling inauthentic content; strong quantitative design; **advanced statistics including time series**; "**experience with Python and R is essential**"; excellent English; **Russian and/or Mandarin a plus**; genuinely independent (Roozenbeek is part-year in Cambridge).
- **Documents:** CV + application letter, **max 2 pages**, portal only.
- **Terms:** EUR 3,204 rising to max EUR 4,051 gross/month, 1 year then extended to 4.

## THE FLAGSHIP PAPER AND THE OPENING IT LEAVES
**Dek, Kyrychenko, van der Linden & Roozenbeek, "Mapping the online manipulation economy", *Science* 390(6778):1112-1114, 11 Dec 2025** (DOI 10.1126/science.adw8154). It launched **COTSI**, a live public index of daily prices and stock of SMS verifications across ~198 regions and 546 platforms, built from data collected 25 Jul 2024 to 27 Jul 2025. Headline finding is a time-series one: verification prices for Telegram and WhatsApp rise in the run-up to national elections.

**From COTSI's own methodology page, which is where the opening is:**
- They identified **17 vendors and include only five**. Inclusion rule: price and stock "freely available via **API, preferably without login or paywall**". Vendors were excluded for paywalls, logins, or suspected reselling and virtual numbers.
- Their own notes flag included vendors as "**suspected virtual numbers**" and "**suspected reseller**".
- Collection is "our automatic script collects data via API interfaces provided by most vendors", daily.
- The methodology page documents **no limitations, no vendor-churn policy, no gap handling**.

**And the paper states their own risk:** "There is a risk that the publication of this paper alerts SMS verification providers, who might then make access to their APIs more difficult, complicating future study."

So: a daily price index, spliced across five vendors selected because they do not defend themselves, two of them flagged as possibly not selling the same good, carrying an event-study claim about elections, with the team publicly expecting access to harden. **That is simultaneously a collection-continuity problem and a measurement-comparability problem, and Asad is unusually placed on both.**

## THE FIELD-LEVEL VERSION OF THE SAME PROBLEM (verified citations, safe to use)
- **Rauchfleisch & Kaiser, "The False positive problem of automatic bot detection in social science research", PLOS ONE, 2020** (DOI 10.1371/journal.pone.0241045). Botometer scores across five datasets, n=4,134, two languages: thresholds are unstable and imprecise, especially cross-language, so studies "unknowingly count a high number of human users as bots and vice versa".
- **Cresci, "A decade of social bot detection", Communications of the ACM 63(10):72-83, 2020.** The arms race means detectors decay as adversaries adapt.
Together these say: any estimate of a manipulation market inherits its classifier's error and that error drifts as vendors adapt. That is the bridge from Asad's paper to this project, and it is citable rather than hand-waved.

---

# THE APPLICATION LETTER (max 2 pages)

Dear Dr Roozenbeek and Dr Vermeulen,

I am applying for the PhD position in Social Data Science on the economy of digital influence operations.

The advert names one standing deliverable, the Cambridge Online Trust and Safety Index, and that is what drew me. COTSI is not a dataset, it is an instrument that has to keep running. Your methodology page says the index draws on five of the seventeen vendors you identified, selected because their price and stock data are reachable by API without a login or a paywall, and it flags two of the five as a suspected reseller and a suspected seller of virtual numbers. Your Science paper adds that publishing the index may itself push providers to close those APIs. That leaves two open problems I have spent my career on: keeping a hostile collection alive, and knowing whether the numbers still mean the same thing when it changes.

On the first. I run production collection against sources that actively resist it. At M+C Saatchi Fluency I built and operate a fleet of sixty-eight collectors with an agentic repair layer, so when a source changes its structure the system diagnoses the break, regenerates the extraction logic, tests it against live pages and only then ships. About a third of repairs need no model call at all. At Dubizzle Labs I led a three-engineer team running over five hundred collectors across fifteen countries in English, Arabic, Urdu and Hindi. I also wrote the public engineering reference on this work, web-scraping-guide.com. The failure mode I care about most is the quiet one: a collector that returns a valid-looking response containing nothing, so the series does not break, it just goes thin. On a price index that does not read as an outage. It reads as a cheaper market.

On the second, which is my research. My methods paper with Dr Ella Haig treats each social platform as a survey mode and applies psychometrics to machine-labelled text: generalizability theory, measurement invariance and differential item functioning, and score linking. In a five-hundred-replication simulation with known ground truth, an index that pools platform scores at face value reports the wrong sign of aggregate sentiment on roughly a quarter of days, purely from measurement differences. The paper goes to arXiv shortly. The question transfers directly to COTSI with vendors in place of platforms: does a price from one vendor measure the same good as a price from another, does the index stay the same instrument across vendor churn, and what does that do to an event study on pre-election price movements? The field-level version of this is familiar to you both. Rauchfleisch and Kaiser showed that Botometer thresholds are unstable enough that studies miscount humans as bots and back again, and Cresci's account of the detection arms race means that error drifts as adversaries adapt. Any estimate of a market's size inherits its classifier, and inherits the drift too.

That gives me four papers I would want to write. First, vendor equivalence: a formal test of whether COTSI's five sources measure a common good, with a linking design so the series survives a vendor leaving. Second, coverage: the index currently sees the vendors that do not defend themselves, so I would extend collection to the login-walled and paywalled half of the market and quantify how much the picture changes. Third, the election result done with the instrument accounted for, to see whether the pre-election spike survives correction for vendor churn and composition. Fourth, the regulatory question your Vidi frames, working from price and stock signals toward where intervention actually bites, whether that is SIM registration regimes, platform verification design, or payment rails.

I should be straight about what I do not bring. I have not run behavioural experiments. My quantitative work is observational and simulation-based, and the closest I have come to experimental design is the known-truth simulation in the paper, where the parameter is set and the question is whether the method recovers it. I would want to learn that properly, and Dr Vermeulen's work on correction and replication is a large part of why this post rather than another. I have also not conducted qualitative interviews, and I take seriously that interviewing people who operate an illicit market raises access, ethics and researcher-safety questions I would need to be trained into rather than improvise. On tooling, Python has been my daily working language for seven years; my R is functional rather than fluent, and I am working through the invariance and linking models from our paper in lavaan to close that gap rather than describe it away.

Why four years rather than another contract. I have spent seven years building the instruments that produce these numbers, and the thing that changed for me was looking honestly at my own. At ArtemisAI, the company I founded, our two annotation tiers agree on 82.9 per cent of sentiment labels and 0.0 per cent of toxicity labels, while the toxicity model reports 96.7 per cent average confidence. The zero turned out to be mismatched label taxonomies between the tiers rather than a failure of either model, and the dashboard's accuracy figure was inter-model agreement with no criterion behind it. Nobody built that dishonestly. It is what happens when instruments get adopted faster than anyone builds the discipline to check them. I would rather spend four years building that discipline for a market that is measured by almost nobody than another year shipping numbers I cannot defend.

I would be glad to discuss any of it.

Best wishes,
Asad Ikram

Chevening Scholar 2024/25 | MSc Data Analytics (Distinction, dissertation 78), University of Portsmouth
asad.ikram53@gmail.com | linkedin.com/in/asad-ikram98 | asad-ikram-mc.github.io/portfolio

---

## CRITICAL PATH, 11 DAYS (today is 3 Sep, deadline 14 Sep)
1. **Post the arXiv paper.** Every document says "goes to arXiv shortly". For a lab that publishes in Science and Nature, an unposted manuscript is an assertion; a link is evidence. This needs Ella's sign-off and it is the single highest-value action available. If it posts, put the link in the letter and the CV.
2. **Do a real R pass.** They call Python and R essential. Run the invariance and DIF models from your own paper in lavaan or mirt. Two evenings makes the sentence in the letter true rather than a hedge, and it is the obvious interview question.
3. **Optional but strong: a small public proof.** A two-week price series scraped from one vendor COTSI *excluded* for having a login, with the code public. It would be the only artefact in the pile that demonstrates the exact capability the index needs, and it directly evidences paper two.
4. **Keep the CV to two pages** and lead education with the Distinction and the 78, because the advert explicitly prefers dissertation grades.
5. **Submit through the portal, not by email**, well before the 23:59 wire.

## INTERVIEW PREP (21-30 Sep, expect these)
- "How would you keep COTSI running when a vendor adds a login or a paywall?" Answer with the tiered repair architecture and the escalation ladder, and be honest about cost and legality limits.
- "Describe an experiment you would run in year one." Have one ready. A vendor-facing audit design (purchasing verifications across countries and platforms to test whether advertised price and stock predict actual delivery quality) is the natural one, and the Science team already hand-tested delivery success, so it is within the lab's existing practice.
- "What is your R level?" Answer honestly with what you did in the two weeks before applying.
- "How would you approach a vendor for an interview, and what does the ethics board say?" Do not improvise this. Read VU's research ethics procedure beforehand.
- "What is the theory here?" This is Vermeulen's axis. Be ready to talk about why a market frame changes what interventions are possible, rather than only how to measure it.

## LOGISTICS FLAG NOBODY HAS CHECKED
Start date is **4 January 2027** and you would be relocating from Lahore. If an offer lands in October, Dutch **IND highly-skilled-migrant** sponsorship and the visa become the binding constraint, not the research. Ask about the timeline at interview rather than after an offer.

## ATTACH
- CV: MPI-SP Application/Asad_Ikram_CV_Academic_MPI.pdf works as-is (Research = paper + dissertation, nothing claimed as published). Add the dissertation mark 78 to the education line for this application, since they ask for it.
