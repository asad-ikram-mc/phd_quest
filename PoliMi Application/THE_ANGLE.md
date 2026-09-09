# THE ANGLE — what the research actually concluded
# Read this before the 57,000-word brief. 9 September 2026.

---

## THE HEADLINE: ALL FOUR ANGLES WERE REFUTED, AND THREE OF THEM POINTED AT THE SAME DOOR

Eleven agents ran. Six researched the field, four attacked one candidate angle each, one synthesised.
Every one of the four angles came back **refuted as the spine of a thesis**. That is not a bad
result. It cost an afternoon of machine time instead of a rejection letter in October.

The four angles tested, and why each died:

| Angle | Verdict | Killed by |
|---|---|---|
| Live-web vs fixed-corpus retrieval auditing | REJECT as spine | Gundelach, Mühlhäuser & Herrmann, arXiv 2606.14525, **June 2026** — 10,000 sites × 4 browser configs, the anti-bot half already executed at scale. Plus Hannak (WWW 2013) and Kliman-Silver (IMC 2015) for personalisation/geography. |
| The reference-standard problem (LLM as ground truth) | REFUTED as spine | Statistically **solved and packaged**: Prediction-Powered Inference (Angelopoulos et al., *Science* 2023), control variates (Chaganty, ACL 2018), DSL (Egami). Domain half owned by REFLECT (Yale/IBM, arXiv 2605.19196). |
| Measurement invariance on agent-evaluation metrics | REFUTED as stated | **Scooped twice in five months.** Cacioli, arXiv 2604.27405 (Apr 2026) — Reliable Change Index across model versions. Zheng & Yang, arXiv 2609.00482 — DIF across model families, **posted 31 August 2026, nine days before this was written**. |
| Shadow-anchored bridging for silent model updates | REFUTED as stated | Habba et al., arXiv 2604.12843 (Apr 2026) — fixed-parameter IRT calibration, locked anchors, explicitly for cross-time comparability. Plus arXiv 2606.15474 on drift attribution and Wiese, *PLOS ONE* (Feb 2026). |

**Read the pattern, because it is the important part.** Every angle Asad would naturally have
proposed is the same move: *port psychometrics to LLM evaluation*. Between April and August 2026,
at least six groups made that move and published it. The instinct was right and it was right about
five months too late. Writing any of these would ask Pierri and Brambilla to fund a result that is
already on arXiv, using a method for which **neither of them, nor anyone in their department, has a
single publication**.

---

## WHAT SURVIVED — and three independent agents found it separately

The verdicts on angles 2, 3 and 4 were written by different agents attacking different targets. All
three, unprompted, arrived at the same reframing.

> **Build controlled, provenance-labelled information environments. Manipulate the evidence
> distribution while holding the model, harness and prompt fixed. Measure how the agent's epistemic
> failures respond.**

Why this one survives when the others did not:

1. **It is objective 3 of the call, verbatim** — "controlled experiments with open models and
   modular agent architectures". Not a stretch, not a reframing. The call's own words.
2. **It is the one grouping variable in objective 2 that nobody has occupied.** Everyone varies the
   model, the judge, the prompt, the persona or the harness, because those are free. **Nobody varies
   the retrieved evidence set under experimental control**, because that means building and holding
   a corpus with known provenance, known source-quality distribution and known contamination, and
   serving it to an agent as if it were live. That is web-collection engineering.
3. **It makes evidence laundering and source omission directly measurable rather than inferred.**
   If you planted the document, you know what the agent should have said about it.
4. **It opens a clean path to objective 4** (source verification, provenance-aware generation),
   which every other angle failed to reach. Angle 1's fatal flaw was exactly this: *"there is no
   safeguard for Cloudflare."* A thesis that only reports that measurement is hard will not win a
   single scholarship.
5. **It needs no DSA Article 40 access.** Pierri's own *CACM* paper says the process is slow and
   adversarial and first decisions were expected only in late February 2026. Do not build on it.
6. **It is the one capability a psychometrician does not have and Pierri's audit work needs.**
   Sixty-eight collectors across ten platforms with an automated repair layer, five hundred across
   fifteen countries, and a published public reference on anti-bot systems and agentic browsers.
   In a linking-constants proposal that background is decoration. Here it is load-bearing.

**And the inversion that makes it honest.** The call's objective 4 asks for **weak-model oversight**:
build a system where a weaker model checks a stronger one. That *is* the reference-standard problem
with the sign flipped. Everything Asad knows about judge error propagation stops being a discovery
he is claiming and becomes the reason his safeguard is designed correctly and validated honestly.

---

## THE THING HE MUST DEMOTE

The ArtemisAI benchmark switch — v1–v3 scored against the 97-post human holdout (64.7, 66.4, 71.6),
v4–v5 against Claude's labels (81.8, 85.8), so part of that rise is the reference moving — is the
single most persuasive first-person fact he owns. Two of the four verdicts said so independently.

**Both also said it is motivation, not contribution.** It earns the methods point in one paragraph.
It is not a three-year research programme, and a committee will notice if it is asked to be one.

Same for the psychometrics. Keep measurement literacy as an instrument used *inside* the design —
to show that a failure metric does not survive an environment swap — not as the thesis.

---

## THE TWO THINGS THAT CHANGE HOW HE WRITES

**1. Pierri has signed his name to the position that LLM-based measurement needs psychometric
validation, and has never performed any.** He is a co-author on GUIDE-LLM, *"A reporting checklist
for large language models in behavioural science"*, *Nature Human Behaviour* 2026,
DOI 10.1038/s41562-026-02492-7, 14 consensus items covering psychometric validation, causal
validity and reproducibility. Meanwhile the research found **no publication by Pierri or his group**
using generalizability theory, measurement invariance, DIF or score linking.

That gap is simultaneously the opening and the risk. The opening: he has publicly committed to a
standard he has no in-house method for. The risk: **there is no supervisor in that department who
can catch a naive psychometric design, or defend it to a committee.** Lead with psychometrics and
he is asking two computational social scientists to fund a method neither has ever used.

**2. His own retrieval-layer question is still unanswered and it is load-bearing.** The email to
Pierri of 8 Sep 13:35 UTC asks exactly the right thing — live web or fixed corpus. He has not
replied. Note that the surviving angle **answers the question in the proposal's favour**: a
controlled provenance-labelled environment is neither the live web nor a passive fixed corpus. It
is a third option, and it is the one that makes the experiments identifiable.

---

## GUARDRAILS IF HE TAKES THE SURVIVING ANGLE

- **Name the harness as a controlled factor from page one.** The literature says harness effects
  dominate, and a committee that knows this will look for it.
- **At least one chapter must deliver an objective-4 safeguard**, evaluated in those environments.
- **Cite PPI and DSL explicitly and position against them.** A DEIB committee will include someone
  quantitative. Presenting a known estimator as a discovery is worse than having no angle.
- **Verify every arXiv number against the PDF before citing it.** Several 2026 items in the brief
  were read through a summarising fetch. REFLECT and DeepTRACE especially.
- **Do not propose anything that depends on DSA Article 40 data.**

---

## STATUS

The full 106,000-word reading pack is `RESEARCH_BRIEF_Pierri_Brambilla.md` in this folder:
both supervisors profiled, the field mapped failure mode by failure mode, the benchmarks a
committee expects him to know, the questions he currently cannot answer, and a hard
do-not-claim list. Section 5 now carries all four verdicts verbatim.

**Correction applied to the brief.** It shipped saying verdicts 3 and 4 were never received and
that some were reconstructed from surrounding evidence. That was false. All four were delivered
and complete; they are now pasted in from the run journal. Where sections 4 and 6 of the brief
reason from only two verdicts, section 5 overrules them.