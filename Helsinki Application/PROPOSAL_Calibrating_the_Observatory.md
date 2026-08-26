# Calibrating the Observatory: Measurement Equivalence, Instrument Drift and Epistemic Standpoint in LLM-Annotated Public Opinion

**Applicant:** Asad Ikram
**Programme:** Doctoral Programme in Social Sciences, University of Helsinki (university-funded doctoral researcher call, 24 Aug - 7 Sep 2026)
**Proposed supervisor:** Dr Matti Nelimarkka, Helsinki Social Computing Group, Centre for Social Data Science
**Status of this document:** pitch draft for joint preparation; the submitted plan will be rewritten by the applicant on the PP26 template in his own words, with AI assistance disclosed as the call requires.

---

## 1. Background and Motivation

Computational social science has changed its measurement instrument. Within three years, large language models moved from novelty to default annotator for social media text: they beat crowd workers on standard tasks at a twentieth of the cost (Gilardi et al. 2023), and the field followed. What followed too is an uncomfortable evidence base about the instrument itself. Reasonable configuration choices flip the statistical conclusions of published annotation studies about 31 per cent of the time (Baumann et al. 2025). Prompt wording alone moves label distributions by double digits, in directions that differ unpredictably by task (Camuffo et al. 2026). Proprietary models change behaviour under silent backend updates (Chen, Zaharia and Zou 2024), which is why methodologists now warn against building research on APIs whose versions cannot be pinned (Ollion et al. 2024).

At the same time, the era of single-platform research ended for structural reasons. The 2023 closure of affordable research access to Twitter/X reversed two decades of growth in platform research (Murtfeldt et al. 2024), and the social media ecosystem itself has fragmented: whole platforms now carry distinct, persistent ideological profiles, and apparent opinion shifts on one platform often reflect users sorting between platforms rather than anyone changing their mind (Di Martino et al. 2026). Any credible public opinion signal must therefore pool several platforms, read by LLM instruments, over years.

That is exactly what a social media **observatory** does, and it is where the three unsolved measurement problems of this proposal collide. An observatory that tracks discourse from 2025 to 2030 will (a) read several platforms with one instrument, without evidence the instrument measures the same construct on each; (b) cross many silent model updates, so its trend lines confound changes in the world with changes in the instrument; and (c) embed an epistemic standpoint in that instrument, since language models are not neutral readers (Nelimarkka 2026). Survey methodology solved the structural analogues of all three decades ago: mode equivalence testing, bridging designs when a questionnaire or mode changes mid-series (Kraemer et al. 2025), and explicit documentation of the instrument's perspective. No equivalent discipline exists for LLM-annotated platform data. This project builds it, and builds it where it is needed most: as operating methodology for a running observatory.

The applicant's foundation paper with Dr Ella Haig (Ikram and Haig 2026) supplies the starting machinery: a six-step psychometric protocol treating each platform as a survey mode, applying generalizability theory, measurement invariance and differential item functioning, and score linking to machine-labelled sentiment, with a 500-replication known-truth simulation showing that a naive pooled index reports the wrong sign of aggregate sentiment on roughly a quarter of days. The doctoral project carries that machinery from fine-tuned classifiers to the instruments the field now actually uses.

## 2. Research Aims and Novel Contribution

**Aim.** To develop and empirically validate a calibration discipline for LLM-annotated public opinion measurement across platforms, over time, and across epistemic standpoints, so that longitudinal multi-platform monitoring can distinguish real opinion change from instrument change.

**Research significance and novelty.** Four contributions, each occupying a cell the current literature leaves empty:

1. **Platform equivalence of LLM labels, formally tested.** The first fitted measurement invariance and DIF models on LLM-annotated opinion constructs with platform as the grouping variable. Hou, Thapa and Tay (2026) built the equivalence framework with language as the axis and left platform explicitly open; nobody has fitted the models.
2. **A bridging estimator for model updates.** Reproducibility work detects that an API model changed (Gao, Liang and Guestrin 2025) and re-validates against a fixed audit set (Cheng, Mayya and Sedoc 2024). Nothing corrects the time series when versions are not equivalent. This project ports the survey world's bridging design, parallel-run overlap windows, comparability ratios and score equating, to AI instruments, with a pre-specified gold-set refresh policy.
3. **Standpoint as a measurement facet.** The supervisor's MarxistLLM (Nelimarkka 2026) builds standpoint-conditioned instruments and evaluates them qualitatively. This project quantifies them: standpoint enters a generalizability study as a fixed facet, alongside model family, version, prompt and platform, so the share of measurement variance attributable to the instrument's epistemic configuration becomes a reported, decomposable quantity, and its invariance across platforms becomes a testable hypothesis. The aim is not to average standpoints away but to make their effect visible and reportable (Klein and D'Ignazio 2024).
4. **The criterion test: does calibration pay?** Opinion nowcasting from platform data corrects selection (who is on the platform) and stops there; the state of the art is single-platform and treats the extracted measure as if it were a survey response (Cerina and Duch 2026). This project runs the missing horse race: a measurement-calibrated multi-platform index against a naive pooled index, benchmarked against probability-sample survey series. Either result is publishable; the field has never run the comparison.

No existing paper or group holds more than one of these cells. Statistical-correction methods (Gligorić et al. 2025; Egami et al. 2023) fix estimates within one corpus and one instrument version; reliability scoring (Barrie, Palaiologou and Törnberg 2024) stops at reliability; variance-aware annotation protocols (Camuffo et al. 2026) decompose pipeline design facets but include no platform, time or standpoint facet and fit no invariance model. The unifying object, the observatory, is what makes this one project rather than four: each component is an operational requirement of running one honestly for five years.

## 3. Research Questions

1. **RQ1 (Equivalence).** Do LLM annotators measure the same opinion construct, on the same scale, across platforms discussing the same political events? Which invariance level (configural, metric, scalar) survives, and does it depend on model family and prompt?
2. **RQ2 (Drift).** How large are measurement discontinuities introduced by model updates in a running annotation pipeline, and can a bridging estimator with parallel-run overlaps keep a multi-year opinion series comparable across versions?
3. **RQ3 (Standpoint).** How much of the variance in LLM-annotated opinion measurements is attributable to the epistemic standpoint conditioned into the instrument, and are standpoint effects invariant across platforms?
4. **RQ4 (Criterion).** Does a calibrated multi-platform index nowcast survey-measured opinion better than a naive pooled index, and by how much?

## 4. Literature Context

**The instrument turn and its instability.** LLM annotation was legitimised by accuracy claims (Gilardi et al. 2023) and destabilised by their examination: conclusion-flipping configuration sensitivity (Baumann et al. 2025), unpredictable prompt effects (Camuffo et al. 2026), and hidden measurement error propagating into downstream analysis (Messing 2026). The field's own remedies are one-shot criterion validation and statistical correction against gold labels (Gligorić et al. 2025; Egami et al. 2023). All of it treats the instrument as fixed and the corpus as one population; none of it asks the survey methodologist's question of whether scores are comparable across the groups being pooled.

**Time, drift and the observatory.** Model behaviour shifts under silent updates (Chen, Zaharia and Zou 2024); black-box scoring APIs change under researchers' feet (Pozzobon et al. 2023); detection and audit-set responses exist (Gao, Liang and Guestrin 2025; Cheng, Mayya and Sedoc 2024). Media observatories are being built from scratch with serious infrastructure but no instrument-versioning methodology (Pehlivan et al. 2025). Survey research handles the structurally identical problem with bridging studies and parallel administration when instruments change mid-series (Kraemer et al. 2025); that design has never been ported to AI annotation.

**Standpoint and whose measurement.** Language models encode political and cultural positions (Santurkar et al. 2023; Rozado 2024), and the supervisor's research programme has pushed this from complaint to instrument: MarxistLLM asks whether a model can analyse from a declared theoretical perspective (Nelimarkka 2026), and the group's earlier work showed that different computational eyes see different things in the same images (Berg and Nelimarkka 2023). What is missing is the measurement bridge: treating the declared standpoint as a facet whose contribution to score variance is estimated rather than assumed, on the multi-platform data where it matters.

**The supervisor's programme is the natural home.** The group's credo, the role of theory and the importance of validity and reliability in computational analysis, is this project's method; Platformed Interactions (Nelimarkka et al. 2020) is the within-group demonstration that platforms shape political communication; the Finnish Digital Observatory (2025-2030) is the running system whose honesty this project underwrites.

## 5. Methodology

**5.1 Research design.** A computational mixed-methods design with one **data spine** shared by all four studies: one construct family (public attitudes toward government economic policy), a pre-specified set of policy anchor events in two countries (the applicant's fifteen frozen UK fiscal events, published in the foundation paper, plus a Finnish set co-designed with the supervisor around budget and election moments), and three platforms with durable research access (candidates: Reddit, YouTube, Bluesky; a pre-registered density audit decides retention). One spine, four studies, four papers.

**5.2 Data collection.** Window-scoped collection around anchor events via official APIs and licensed access, executed with the applicant's production tooling (six years of platform data engineering; 68-crawler fleets with drift alarms operated for UK government-grade analytics). A stratified human criterion sample of 1,000 to 1,500 items per country, double-coded with a 25 to 30 per cent overlap and a drafted codebook; survey anchor series on matched questions (UK trackers and the British Election Study; Finnish barometer series selected with the supervisor).

**5.3 Analytical framework.**
- **Study 1 (RQ1, months 3-18):** multi-group categorical invariance models and per-event DIF on LLM-annotated items with platform as group, across two model families and a pre-specified prompt battery; anchor-free DIF and alignment as identification checks. Extends the foundation paper's fitted-classifier protocol to LLM instruments.
- **Study 2 (RQ2, months 12-30):** a live annotation pipeline run across scheduled and vendor-forced model changes; model-equality testing as the trigger; parallel-run overlap windows around every instrument change; comparability ratios and equating transformations as the bridging estimator; pre-specified gold-set refresh policy. Produces the versioning methodology the observatory literature lacks.
- **Study 3 (RQ3, months 18-34):** a generalizability study with standpoint as a fixed facet (baseline instruction, declared-perspective variants in the MarxistLLM tradition, and a formal-neutral control), crossed with model family, prompt and platform; D-study projections for observatory design choices. Developed jointly with the supervisor.
- **Study 4 (RQ4, months 26-42):** the criterion horse race: naive pooled, platform-specific, and calibrated indices (applying Studies 1-2 corrections) nowcasting the survey criterion over rolling windows; error decomposition separating selection from measurement components (MTMM logic, with human panels treated as one more method rather than ground truth).

**5.4 Validation, robustness and staging.** All models under effect-size criteria with sensitivity analyses across model families and prompts; computational reproducibility via pinned open-weight models wherever feasible, with proprietary models handled through the Study 2 bridging machinery rather than trust. Declared drop-order if time compresses: Study 3 folds into Study 1 as an additional facet; Study 4 is scheduled early (from month 26) because the adjacent literature is moving.

## 6. Proposed Chapter Structure (Four-Paper Model on One Spine)

- **Study 0 (published foundation, not part of the thesis):** the equivalence protocol and simulation (Ikram and Haig 2026), demonstrated capability rather than promise.
- **Paper 1:** Does the platform change what the LLM measures? First fitted invariance and DIF evidence for LLM-annotated opinion. Target: ICWSM or CSCW, year 2.
- **Paper 2:** Bridging the model update: a calibration design for longitudinal LLM annotation. Target: a methods venue (Political Analysis, Sociological Methods and Research, or EPJ Data Science), year 3.
- **Paper 3:** Standpoint as a measurement facet: quantifying the epistemic configuration of LLM instruments. With the supervisor. Target: Big Data and Society or New Media and Society, year 3-4.
- **Paper 4:** Does calibration pay? Calibrated versus naive multi-platform indices against survey benchmarks. Target: ICWSM or PNAS-family venue, year 4.

## 7. Expected Contributions

**Academic.** The first equivalence evidence for LLM-annotated opinion with platform as group; the first bridging estimator for AI instrument change in longitudinal designs; the first variance decomposition of epistemic standpoint in measurement; the first calibrated-versus-naive nowcasting comparison. Together: the measurement discipline the instrument turn skipped.

**Practical and infrastructural.** An open protocol, reference implementation and reporting standard usable by any observatory; direct operating methodology for the Finnish Digital Observatory across its 2025-2030 model updates; industry relevance the applicant can state from experience, since his own production systems pool model outputs whose inter-model agreement ranges from 82.9 per cent (sentiment) to 0.0 per cent (toxicity) while individual models report high confidence.

## 8. Ethics and Risk Management

Public content only; GDPR-compliant minimisation as in the applicant's ethics-approved MSc work (Portsmouth TETHIC-2025-111094), re-approved under University of Helsinki procedures; hashed identifiers, aggregate reporting, paraphrased quotations, paid annotators. Platform terms govern collection modes; the density audit absorbs the resulting asymmetries by design. Risks: (i) scope, managed by the shared spine and the declared drop-order; (ii) criterion regress, since human panels are themselves imperfect, managed by MTMM treatment of panels as methods and external termination in the survey criterion; (iii) conceptual pushback on treating standpoint as a facet, addressed by modelling it as fixed rather than random and framing the estimate as making the instrument's perspective reportable; (iv) scoop risk on Paper 4, managed by early scheduling; (v) proprietary model access costs, managed by open-weight defaults and a modest inference budget in the funding plan.

## 9. Timeline (4 Years, Jan 2027 - Dec 2030)

| Year | Key activities |
|---|---|
| 1 | Ethics approvals both countries; spine collection (platforms, anchors, criterion samples); Study 1 modelling begins; doctoral coursework; group integration. |
| 2 | Paper 1 submitted; live pipeline for Study 2 running across model updates; Study 4 baseline indices built; present at group and at SICSS-style venues. |
| 3 | Paper 2 submitted; Study 3 G-study with the supervisor; Study 4 calibrated indices and first criterion results. |
| 4 | Papers 3 and 4 submitted; protocol and software release; article-based thesis compilation and defence preparation. |

## 10. Conclusion

The field rebuilt its measurement stack on instruments that change silently, read differently on every platform, and carry a standpoint nobody quantifies, and it did so exactly when multi-platform, multi-year monitoring became the only viable design. This project does for the LLM-annotated observatory what survey methodology once did for the interview: it makes the instrument part of the science. The applicant brings the unusual combination the project needs, a published psychometric protocol, six years of production platform-data engineering, and daily operational contact with the problem, and the Helsinki Social Computing Group is the one place where the measurement machinery, the standpoint theory and the running observatory already sit in the same room.

---

## References

1. Barrie, C., Palaiologou, E. and Törnberg, P. (2024) 'Prompt stability scoring for text annotation with large language models', arXiv:2407.02039.
2. Baumann, J., Röttger, P., Urman, A., Wendsjö, A., Plaza-del-Arco, F.M., Gruber, J.B. and Hovy, D. (2025) 'Large language model hacking: quantifying the hidden risks of using LLMs for text annotation', arXiv:2509.08825.
3. Berg, A. and Nelimarkka, M. (2023) 'Do you see what I see? Measuring the semantic differences in image-recognition services' outputs', Journal of the Association for Information Science and Technology, 74(11), pp. 1307-1324.
4. Bisbee, J., Clinton, J.D., Dorff, C., Kenkel, B. and Larson, J.M. (2024) 'Synthetic replacements for human survey data? The perils of large language models', Political Analysis, 32(4), pp. 401-416.
5. Bradley, V.C., Kuriwaki, S., Isakov, M., Sejdinovic, D., Meng, X.-L. and Flaxman, S. (2021) 'Unrepresentative big surveys significantly overestimated US vaccine uptake', Nature, 600, pp. 695-700.
6. Camuffo, A., Gambardella, A., Kazemi, S., Malachowski, J. and Pandey, A. (2026) 'Variance-aware LLM annotation for strategy research: sources, diagnostics, and a protocol for reliable measurement', arXiv:2601.02370.
7. Cerina, R. and Duch, R. (2026) 'Artificially intelligent opinion polling', Royal Society Open Science, 13(3), 251150.
8. Cernat, A., Keusch, F., Bach, R.L. and Pankowska, P.K. (2025) 'Estimating measurement quality in digital trace data and surveys using the MultiTrait MultiMethod model', Social Science Computer Review (online first 2024).
9. Chen, L., Zaharia, M. and Zou, J. (2024) 'How is ChatGPT's behavior changing over time?', Harvard Data Science Review, 6(2).
10. Cheng, X., Mayya, R. and Sedoc, J. (2024) 'To err is human; to annotate, SILICON? Toward robust reproducibility in LLM annotation', arXiv:2412.14461.
11. Di Martino, E., Galeazzi, A., Cinelli, M., Starnini, M. and Quattrociocchi, W. (2026) 'Platform sorting drives ideological fragmentation in the social media ecosystem', arXiv:2606.10575.
12. Egami, N., Hinck, M., Stewart, B.M. and Wei, H. (2023) 'Using imperfect surrogates for downstream inference: design-based supervised learning for social science applications of large language models', NeurIPS 2023.
13. Gao, I., Liang, P. and Guestrin, C. (2025) 'Model equality testing: which model is this API serving?', ICLR 2025.
14. Gilardi, F., Alizadeh, M. and Kubli, M. (2023) 'ChatGPT outperforms crowd workers for text-annotation tasks', Proceedings of the National Academy of Sciences, 120(30), e2305016120.
15. Gligorić, K., Zrnic, T., Lee, C., Candès, E. and Jurafsky, D. (2025) 'Can unconfident LLM annotations be used for confident conclusions?', NAACL 2025.
16. Hou, D.X., Thapa, S. and Tay, L. (2026) 'Bridging cultures in the era of big data: a cross-language equivalence framework in machine-learning research with social media texts', Advances in Methods and Practices in Psychological Science.
17. Ikram, A. and Haig, E. (2026) 'Is the platform part of the measurement? A protocol and simulation study for cross-platform equivalence of machine-labelled policy sentiment', arXiv preprint.
18. Klein, L. and D'Ignazio, C. (2024) 'Data feminism for AI', ACM Conference on Fairness, Accountability, and Transparency (FAccT 2024).
19. Kraemer, F., Lugtig, P., Struminskaya, B., Silber, H., Weiß, B. and Bosnjak, M. (2025) 'Monitoring attitudes over time: real change or the result of repeated interviewing?', Sociological Methods and Research.
20. Messing, S. (2026) 'Hidden measurement error in LLM pipelines distorts annotation, evaluation, and benchmarking', arXiv:2604.11581.
21. Murtfeldt, R., Paik, S., Alterman, N., Kahveci, Z. and West, J.D. (2024) 'RIP Twitter API: a eulogy to its vast research contributions', arXiv:2404.07340.
22. Nelimarkka, M. (2026) 'MarxistLLM: fine-tuning a language model with a Marxist worldview', Big Data and Society, 13(2).
23. Nelimarkka, M., Laaksonen, S.-M., Tuokko, M. and Valkonen, T. (2020) 'Platformed interactions: how social media platforms relate to candidate-constituent interaction during Finnish 2015 election campaigning', Social Media + Society, 6(2).
24. Ollion, É., Shen, R., Macanovic, A. and Chatelain, A. (2024) 'The dangers of using proprietary LLMs for research', Nature Machine Intelligence, 6, pp. 4-5.
25. Pehlivan, Z., Park, S., Abrahams, A.S., Desblancs-Patel, M., Steel, B.D. and Bridgman, A. (2025) 'Building a media ecosystem observatory from scratch: infrastructure, methodology, and insights', arXiv:2506.10942.
26. Pozzobon, L., Ermis, B., Lewis, P. and Hooker, S. (2023) 'On the challenges of using black-box APIs for toxicity evaluation in research', arXiv:2304.12397.
27. Rozado, D. (2024) 'The political preferences of LLMs', PLOS ONE, 19(7), e0306621.
28. Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P. and Hashimoto, T. (2023) 'Whose opinions do language models reflect?', ICML 2023.

**Word count (sections 1-10):** ~2,150 words.
