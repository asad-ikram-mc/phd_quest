# Rochester Institute of Technology — Prof. Fengran Mo
# Cold outreach, two PhD places, Spring or Fall 2027
# STATUS: in Gmail drafts, NOT sent. Attach two files before sending.
# To: frmvcs@rit.edu · Cc: fengran.mo@rit.edu
# Subject: [RIT Prospective PhD] Asad Ikram

## THE ADDRESS DISCREPANCY, AND WHY BOTH ARE USED
His LinkedIn recruitment post gives **frmvcs@rit.edu** and specifies the subject line
"[RIT Prospective PhD] Your Name". His personal site gives **fengran.mo@rit.edu**. Both are
plausible RIT aliases. The draft sends to the address he named in the recruitment post and copies
the one on his site, so it lands either way.

## WHO HE IS (verified 8 Sep 2026)
- **Assistant Professor at RIT since August 2026.** Brand new faculty, which is why he is recruiting
  two students at once and why he is answering email himself.
- PhD from Université de Montréal with Jian-Yun Nie.
- Interests: conversational and interactive AI, NLP, information retrieval, LLMs, multilingualism.
- His site states plainly: "I am currently recruiting Ph.D. students starting in Spring and Fall 2027."
- Recent work: **OpenDecoder**, "Open Large Language Model Decoding to Incorporate Document Quality
  in Retrieval-Augmented Generation" (ACM Web Conference 2026); "Agentic Conversational Search with
  Contextualized Reasoning via Reinforcement Learning" (ACL 2026 Findings); ConvMix (AAAI 2026);
  UniConv (ACL 2025).

## THE HOOK, AND WHY IT IS THE RIGHT ONE
**ConvGQR**, Mo, Mao, Zhu, Wu, Huang and Nie, ACL 2023. From the abstract, verbatim:

> "However, manually rewritten queries are not always the best search queries. Thus, training a
> rewriting model on them would lead to sub-optimal queries."

That is a measurement argument wearing IR clothes. He is saying the human reference is being used as
a criterion when it is really just another instrument, and its error propagates downstream. It is
Asad's argument about machine labels, transposed. Naming that one sentence proves the paper was read
rather than the title skimmed, which is the whole point of check 1 in the email pattern.

The forward-looking question in the email comes from **OpenDecoder**: if the decoder conditions on
document quality, how stable is "quality" as a construct across models, retrieval settings and time?
That is an invariance question, it is unanswered, and it is answerable with machinery Asad already
has. It passes the Nelimarkka test because it starts where his paper stops.

## WHY THIS TARGET IS WORTH THE TIME
- **It is an email application.** No portal, no proposal, no fee. The lowest-friction item on the board.
- **A US assistantship covers tuition plus a stipend**, which sidesteps the home-to-international fee
  gap that killed Royal Holloway and rules out the Cambridge deceptive-design studentship.
- **New faculty recruiting their first cohort** are the most reachable supervisors in academia. He has
  positions, funding and no students yet.
- The formal RIT application still has to follow; this email is the relationship, not the application.

## BEFORE SENDING
1. **Attach two files.** `CV/Asad_Ikram_CV_Academic_2026.pdf` and
   `Asad_Ikram_Portsmouth_Transcript.pdf`. The email text references both. It also says the
   FAST-NUCES transcript has been requested, which is only true once Asad actually requests it, and
   that request is already on the PoliMi list for today.
2. **Decide the start term.** The draft says Fall 2027 preferred, Spring 2027 possible. Change it if
   Spring is genuinely wanted; Spring 2027 is January and would collide with a VU start.
3. Read it aloud once.

## THE HONEST PARAGRAPH, AND WHY IT STAYS
The email states plainly that Asad has not published, has not trained or fine-tuned LLMs, and has
used conversational systems rather than built them. That paragraph is doing work rather than costing
points. This is an NLP and IR group; overclaiming on model training to someone who does it for a
living is the fastest way to be dismissed. Naming the gap and offering measurement and infrastructure
in exchange is the trade that has worked in the VU and Agder letters.

## AFTER SENDING
- Log the reply in the tracker. New assistant professors usually answer quickly.
- If he is interested, the next step is the formal RIT CS PhD application, which has its own deadline
  and requirements that have not yet been checked. Check them then, not now.
- No nudge before three weeks.


---

## v2, 9 September 2026: ArtemisAI added, and a false claim removed

Asad objected to the gaps paragraph, correctly. It said he had "not trained or fine-tuned large
language models" and had "used conversational systems rather than built them", and it never
mentioned ArtemisAI at all. Reading `/Users/asad/git_projects/artemisai_prod/marvel` directly shows
the first half of that was simply false.

**What the repo actually contains.** `Fusion/fusion_classifier.py` is a trained PyTorch MLP,
1536 to 256 to 64 to 5, classifying content type over three concatenated 512-dim CLIP vectors for
the image, its OCR text and its caption. Adam, dropout, `compute_class_weight("balanced")` for
imbalance, train/val split, best-val checkpointing, classification report and confusion matrix. It
trains on a hand-built gold set of 149 examples and about 680 once production data is included.
Around it: CLIP via open_clip_torch (ViT-B/32), Whisper transcription for video, an OCR pipeline,
and a networkx affinity graph.

**The fact that makes the email work.** `Fusion/label_images.py` auto-labels images with Claude
Haiku 4.5 vision and writes a CSV "ready for fusion classifier training". So the classifier is
partly trained to imitate an LLM annotator that is itself uncertain. That is exactly Mo's ConvGQR
claim, that a model trained on an imperfect reference inherits its limits, happening inside Asad's
own production system. v2 says so plainly, including the admission that he cannot separate the
model's own error from the error it inherited. To an IR researcher that is a far better credential
than any list of technologies, because it is the problem stated from the inside.

**What remains honestly absent, and stays in the email.** No LLM fine-tuning: there is no PEFT,
LoRA, bitsandbytes or TRL anywhere in the repo, and LLMs are called through APIs. No conversational
or multi-turn systems. Nothing published. The revised sentence is "I have not fine-tuned a large
language model; I call them through APIs and treat their output as data to be validated", which is
accurate where the old wording was not.

**Lesson recorded in memory** as `artemisai-technical-facts.md`: check the repo before writing any
gaps paragraph. Understating a founder's own production system to an NLP group is a worse error than
overstating it, because it is both false and self-defeating.
