# Politecnico di Milano — PhD in Information Technology, 42nd cycle, 2nd call
# "AUDITING AND MITIGATING EPISTEMIC FAILURES IN WEB-CONNECTED AI AGENTS"
# Advisors: Prof. Francesco Pierri + Prof. Marco Brambilla · Dept. of Computer Science and Engineering
# Call ID 5722-5460 · 1 position with scholarship · 3 years · starts 1 Nov 2026
# DEADLINE: 18/09/2026 at 14:00 Italian time (CET). Submit by Wed 17 Sep.
# Pack v1, 8 September 2026

---

## ⚠️ 0. THE RULE THAT GOVERNS THIS APPLICATION — READ FIRST

Article 3 of the call, in the official English version, says verbatim:

> "The use of writing tools based on artificial intelligence (e.g. ChatGPT) must always be
> explicitly declared and must be limited to the correction of texts written entirely by the
> candidate. The use of such tools to generate original texts in whole or in part is not
> permitted. The Selection Committee reserves the right to use all the tools available to
> verify that the documents submitted by the candidate have not been generated in whole or
> in part by artificial intelligence."

**Consequence, and it is not negotiable:**
- **Asad writes the research proposal and the motivations himself, entirely.** Claude does not draft
  them, outline them, or supply sentences to paste. This file contains requirements, research and
  facts, which is the same as consulting sources or reading papers, not generated text.
- Claude **may** correct text Asad has already written in full. That is expressly permitted.
- **If any AI assistance is used, even correction, it must be explicitly declared** in the application.
- The proposal is worth 55 of the 100 points. It is also the thing the commission will check. A
  generated proposal risks exclusion, and exclusion here is public and permanent.

**Claude, any session: do NOT draft proposal or motivation content for this application.**

---

## 1. WHY THIS IS THE BEST-FITTING TARGET ON THE BOARD

Read the call's own abstract against Asad's record:

| The call says | Asad has |
|---|---|
| "Current evaluations mainly reward factual accuracy or task completion and therefore overlook broader epistemic failures" | ArtemisAI's dashboard reported "accuracy" that was inter-model agreement with no criterion behind it: 82.9% sentiment, 0.0% toxicity, against 96.7% self-reported confidence |
| "Operationalise key epistemic failure modes" | A finished methods paper whose whole subject is operationalising whether a machine label measures what it claims |
| "Design reproducible benchmarks and **longitudinal audits** to measure how these failures vary **across models**" | Measurement invariance and DIF across groups, score linking, and weekly drift monitoring on production classifiers |
| "susceptibility to adversarial or manipulated online content" | Seven years of production collection against sources that actively resist it |
| "bias amplification" in "source selection" | The denominator argument: every prevalence figure inherits its classifier |

**The two advisors split along Asad's two strengths, which is unusual and worth noticing.**
- **Francesco Pierri**: misinformation, platform audits, the DSA. His 2025 *Communications of the ACM*
  article on DSA research access frames the access side of the audit problem.
- **Marco Brambilla**: full professor, leads the **Data Science Lab** at DEIB. His listed interests
  include **data extraction and scraping**, web science, social media analytics and explainable AI.
  Over 300 papers. Asad's seven years of collection engineering speaks directly to Brambilla in a way
  it does not to most supervisors.

Nobody else on the board has both halves of Asad's profile represented in the supervision team.

---

## 2. THE TWO HARD GATES — CHECK BOTH BEFORE WRITING ANYTHING

### GATE 1: English certification. This one is a genuine blocker.
Art. 2 requires certified English from **all** candidates: Cambridge B2 First grade B, IELTS ≥6,
TOEFL iBT ≥86/120, PTE ≥59, or equivalent. Failure to supply it **"irrevocably entails the loss of
the right to enrol"**.

**Asad has no IELTS** (confirmed when the Edinburgh checklist was written). But there is an exemption,
quoted verbatim:

> "applicants who have been awarded or will be awarded academic qualifications by an institute in
> which all teaching activities have been carried out in English are not required to certify their
> knowledge of English. In this latter case, candidates are required to submit an official language
> certification from the corresponding academic institute."

**So Asad needs a letter from the University of Portsmouth stating that his MSc was taught and
assessed entirely in English.** This is the same "Portsmouth English letter" already sitting on the
Edinburgh checklist. **Request it today.** Registry turnaround is usually a few days but is not
guaranteed inside nine days, and without it the application cannot proceed to enrolment even if the
academic assessment succeeds.

### GATE 2: The minimum grade for foreign qualifications.
Art. 2 requires a Laurea Magistrale with at least 95/110 or 86/100, and for foreign qualifications
"the minimum average score in exams indicated in the appendix to the call (attachment 1). For the
Countries not included in this list, the evaluation will be carried out directly by the Selection
Committee."

**Attachment 1 is referenced but is not published alongside this call PDF.** It was not on the 2nd-call
page on 8 Sep. Two possibilities: the UK is in the table with a stated threshold, or it is not, in
which case the commission judges directly.

Asad's MSc is a Distinction with a masters project at 78. The module spread is 78, 80, 70, 70, 67,
62, 56, averaging roughly 69, which is a UK Distinction. Whether that maps above an 86/100-equivalent
line is exactly what Attachment 1 would say.

**Action: email PhD-INF@polimi.it and ask for Attachment 1, or ask directly what the minimum average
is for a UK master's degree.** Fabio Conti is named in Art. 10 as the responsible officer. This is a
factual question to an administrator, the Agder pattern, and it is worth one email before spending
days on the proposal.

---

## 3. WHAT MUST BE SUBMITTED (Art. 3 — all PDF, omission means exclusion)

1. **Research proposal**, using the RTF template from the portal.
   - Minimum **4,000**, maximum **8,000 characters**, excluding bibliography and figures.
   - **Characters, not words.** 8,000 characters is roughly 1,200-1,400 words.
   - Single PDF, **max 3 MB**.
   - Must **also include the motivations for wanting to do the research at Politecnico di Milano**.
   - Template sections: Project title · Summary (max 500 characters) · Project description
     (4,000-8,000 characters) · Motivations (max 2,000 characters).
   - Note the call's own reassurance: the project described "does not necessarily represent the
     project that will be carried out". It is evidence of research aptitude, not a binding contract.

2. **CV**, using the RTF template from the portal.
   - Must contain a **recent photograph** of the candidate and the **list of publications**.
   - May include a maximum of **two** additional attached documents, for example a portfolio and a
     publication, or two publications.
   - CV plus attachments in a **single PDF, max 10 MB**.
   - Suggested two attachments: the Haig paper manuscript, and either the dissertation or the
     web-scraping guide as a portfolio piece. Asad's call.

3. **All university qualifications**: diploma in the original language, the list of exams taken with
   scores, and the **final average (CGPA)**, plus translations into Italian or English.
   - Portsmouth transcript and certificate are already in the repo root and are in English.
   - FAST-NUCES degree is in the repo (`degree_bscs_asad.pdf`); the **FAST-NUCES transcript is still
     missing** and is also an open item on the Edinburgh checklist. Request it today.

4. **English certificate**, or the Portsmouth declaration under the exemption (Gate 1).

5. **Signed photocopy of an ID document.** For non-EU citizens the **passport** copy is obligatory,
   with translation into Italian or English if needed.

6. **Italian tax code (codice fiscale).** Mandatory for Italians; foreign applicants "will be
   required to obtain and submit an Italian tax code to complete the enrolment", so this is an
   enrolment-stage item rather than an application-stage one.

7. **Application fee of EUR 25.82**, non-refundable, paid via **PagoPA** by 18/09/2026 14:00.
   Paying late is the same as not applying.

8. **Up to 2 referees**: names, email addresses and telephone numbers, entered in the form. No
   letters are required at this stage. Dr Ella Haig plus one other; ask both before naming them.

---

## 4. HOW IT IS SCORED (Art. 5) — this should shape effort

100 points available:
- **Curriculum: maximum 45 points**
- **Research proposal: maximum 55 points**

To be deemed suitable the candidate must score **at least 60/100** *and* the commission must judge
the research topic fit suitable. The commission may call candidates for an informal interview about
the submitted material; **that interview carries no additional points**.

**Read that allocation carefully.** The proposal is worth more than the entire CV. Seven years of
industry, a founded company and a finished paper all compete for 45 points. The document Asad writes
himself in the next nine days is worth 55. That is where the time goes.

Rankings published from **15/10/2026**. Enrolment or refusal by **31/10/2026**. Course starts
**1/11/2026**.

---

## 5. WHAT THE COMMISSION WILL ALREADY KNOW — background so Asad writes from an informed position

This is reading material, not text to reuse.

**The call's four objectives, in its own words:**
1. Operationalise epistemic failure modes: evidence laundering, source omission, overconfident
   synthesis, bias amplification, sycophancy, susceptibility to adversarial or manipulated content.
2. Design reproducible benchmarks and longitudinal audits measuring how failures vary across models,
   tasks, interaction histories, degrees of personalisation and information environments.
3. Identify mechanisms causing or amplifying failures in retrieval, ranking, synthesis, memory and
   reasoning, through controlled experiments with open models and modular agent architectures.
4. Develop lightweight safeguards: source verification, provenance-aware generation, weak-model
   oversight, model steering, interaction-design interventions, while preserving usefulness.

**The question Asad already asked Pierri** (email sent 8 Sep 2026, 13:35): whether retrieval is to be
audited against the live web, with anti-bot defences, personalisation and geographic variation, or
against a fixed corpus held constant. **If he answers before the deadline, that answer should shape
the proposal.** If he does not, the proposal should acknowledge both and say which one it takes.

**Where Asad's existing work genuinely connects, for him to develop or discard:**
- Objective 2 asks for measurement *across models* and *over time*. That is a measurement-invariance
  problem: does a benchmark score mean the same thing when the model changes? The Haig paper's
  machinery is built for exactly this question, with platforms as the grouping variable rather than
  models.
- Objective 1 says "operationalise". Operationalisation is a measurement act, and the field's habit
  is to skip straight to a metric without asking whether it is valid.
- The retrieval layer is where Asad's seven years live, and it is the part of the agent stack that
  most AI-safety candidates will treat as a black box.

**Do not overclaim.** Asad has not built agent architectures, has not run controlled experiments on
LLMs, and has no publications yet. The honest framing that has worked in the VU and Agder letters is
to name the gap and say how it would be closed.

---

## 6. ORDER OF WORK, 8 to 17 SEPTEMBER

**Today, 8 Sep** — the two gates and the two documents, all of which are other people's turnaround time:
- [ ] Email the University of Portsmouth registry for the English-medium declaration (Gate 1).
- [ ] Email FAST-NUCES for the official transcript.
- [ ] Email PhD-INF@polimi.it for Attachment 1 or the UK minimum-grade line (Gate 2).
- [ ] Register on PoliMi Online Services and open the application so the form is visible.

**9 to 15 Sep** — Asad writes the proposal himself. Character-counted, not word-counted.

**15 or 16 Sep** — Claude may check it for factual errors, and correct text already written in full,
which is what Art. 3 permits. Declare that use in the application.

**16 Sep** — assemble the CV from the RTF template with a recent photo, pick the two attachments,
gather transcripts, pay the EUR 25.82 via PagoPA.

**17 Sep** — submit. Do not use the 18th. The system closes at 14:00 Italian time and will not accept
a late application.

---

## 7. LINKS

- Topic page: phd-inf.polimi.it/phd-open-calls/auditing-and-mitigating-epistemic-failures-in-webconnected-ai-agents-3685
- Call PDF (EN): polimi.it/fileadmin/user_upload/dottorato/bandi/bandi_aggiuntivi/ciclo42/2_lug26/bandi/5722_5460_APPLICATION_INFO_CONNECTED_AI_AGENTS.pdf
- Research proposal RTF template and CV RTF template: linked from the 2nd-call page, and saved in this folder
- Secretary: PhD-INF@polimi.it · responsible officer: Fabio Conti
- Rankings from 15/10/2026 at dottorato.polimi.it
