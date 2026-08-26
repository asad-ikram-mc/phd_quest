# Draft reply to Dr Ella Haig (paste into Outlook)

**To:** ella.haig@port.ac.uk
**Subject:** Re: ICWSM paper proposal - feasibility of the changes, and a meeting

---

Hi Dr Ella,

Thank you for sending Eni's notes, and please pass on my thanks to her as well. I have gone through the whole conversation carefully and I agree with the diagnosis. The idea holds; the data underneath it does not yet.

Here is my honest view on feasibility, point by point.

**1. The 200-post validation set.** Agreed, it is too small to anchor anything psychometric. I will expand it to roughly 1,000 to 1,500 hand-labelled posts, drawn only from the anchor-event windows and split evenly across platforms (about 300 to 400 each). I would like a second annotator on a subset so the agreement figure can be defended properly rather than resting on my own kappa of 0.78. That annotation work is the real cost here: a few weeks of careful labelling. It is the one part I cannot shortcut.

**2. Anchor events.** Agreed, and this is the part I should have done before writing the brief. I will run an anchor-density audit first: list 5 to 10 UK fiscal shocks (the September 2022 mini-budget as the centrepiece, plus Budgets, Autumn Statements and a handful of Bank of England rate decisions), define 48-hour and two-week windows around each, and count what the existing corpus actually holds per platform per window. That takes me a day or two and it decides everything else. Three outcomes: all four platforms are dense enough (proceed as planned); only two or three are (narrow to those, which is fine, a two-group invariance test is the cleanest case and "four platforms" was never load-bearing); or even the big platforms are thin (collect a targeted patch of new data in those windows). I will have the counts before we meet.

**3. Dataset size.** Partly agreed. The "millions of posts" bar applies to empirical-discovery papers; for a measurement-methods paper what matters is density inside the anchor windows, not raw corpus size, and Eni's own notes pivot to the same point. The per-platform totals in the dissertation are also internally inconsistent, so I will recount from the raw data rather than trust the tables.

**4. Collecting more data.** This is the one part that is not a bottleneck for me. I run scraping pipelines for a living, so hyper-collecting a dense patch of event-window data across the platforms is squarely in my wheelhouse if the audit says it is needed.

**5. The reframe.** I agree with moving from an empirical-discovery paper to a methods paper: the contribution is the measurement-equivalence framework for machine-labelled cross-platform text, built around the mini-budget as the case study, with the multilevel model (posts within events, platform as the fixed effect) and the naive-versus-adjusted index simulation to show the "danger" concretely. The five-step method in the brief maps onto this already; what changes is the framing and the explicit anchor-events-plus-bigger-gold-set requirement. I will update the brief once we have agreed the direction so it reflects what we actually plan to do.

**6. Venue and timing.** I agree with Eni that the poster / short-paper track is the right target first, with the full paper later. I checked the ICWSM 2027 call: the 15 September round accepts full papers only, and posters (up to 5 pages) are accepted only in the 15 January 2027 round. That settles it for me. The 15 September round is four weeks away and I could not do the annotation properly in that window anyway, so the plan I would propose is: reframed analysis first, arXiv preprint before the end of the year (which is what my Edinburgh application in early January will cite), then the poster to the 15 January round. I would rather hold the arXiv posting until the reframed version exists than put the current framing up now.

On a meeting: I am free most days next week and the week after. Would any of these work for you (UK time)?

- Tuesday 25 August, 10:00 to 12:00
- Wednesday 26 August, 10:00 to 12:00
- Thursday 27 August, 14:00 to 16:00

If none suit, send me two or three slots and I will fit around you. I will bring the anchor-density counts and a one-page summary of the reframed plan.

Thank you again for pushing on this. It is a much better paper for it.

Best wishes,
Asad

---

*Notes for you (not part of the email):*
- *No em-dashes used; British spelling throughout.*
- *ICWSM 2027 dates verified on icwsm.org/2027/submit: Round 2 = 15 Sep 2026 23:59 AoE, full papers only; Round 3 = 15 Jan 2027 23:59 AoE, full papers plus posters (up to 5 pages), demos and datasets.*
- *Meeting slots are suggestions; change them to suit your week.*
