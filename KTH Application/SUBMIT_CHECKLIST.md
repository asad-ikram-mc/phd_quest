# KTH, Doctoral student in Feminist AI Addressing Gender-Based Violence (PA-2026-2872)

**Deadline: TODAY, Thursday 24 September 2026, midnight CEST. That is 21:59 UTC, and 02:59 on 25 September Pakistan time.** Go by the Swedish clock.

**Apply here (KTH's recruitment system, Varbi):**
https://kth.varbi.com/en/apply/positionquick/963228/?where=4

Advert: https://kth.se/lediga-jobb/963228 (the English mirror URL returns 404; this Swedish page is the live one). Supervisor: Associate Professor Amir Hossein Payberah, payberah@kth.se.

---

## What to upload, all in this folder

| KTH asks for | Upload | Notes |
|---|---|---|
| Copies of diplomas and grades, plus proof of the English requirement | `Asad_Ikram_Certificates_and_Transcripts.pdf` | 5 pages: MSc certificate, Portsmouth transcript, BSc degree, BSc transcript, IELTS. See the warning on certification below |
| CV | `Asad_Ikram_CV_KTH.pdf` | 2 pages, machine learning first. Same as the ELLIS CV, with the language line changed from Finnish to Swedish |
| Application letter, max 2 pages | `Asad_Ikram_Application_Letter_KTH.pdf` | 2 pages. Covers why research, academic interests, how they relate to previous studies, and future goals, which is exactly what the ad asks |
| Representative publications or technical reports; for long documents, an abstract and a link | `Asad_Ikram_Representative_Work_KTH.pdf` | 1 page with the abstracts of both works, as the ad asks for long documents |
| (full texts behind that page) | `Ikram_Haig_Is_the_Platform_Part_of_the_Measurement.pdf` and `Asad_Ikram_MSc_Thesis.pdf` | Upload both if Varbi lets you. The thesis is 7.3 MB; if it is refused for size, the summary page already carries its abstract, which is what the ad accepts for long documents |

## References to type in: ACADEMIC ONLY

The ad says **"two to three academic references"**. So this is different from ELLIS: **do not name Jareed** here, because he is an employer reference.

1. **Dr Ella Haig**, Associate Professor in Artificial Intelligence, School of Computing, University of Portsmouth, UK, Ella.Haig@port.ac.uk. Supervised your MSc dissertation and co-authored the manuscript.
2. **Dr Fahad Ahmad**, Senior Lecturer, Centre for Cybercrime and Economic Crime, University of Portsmouth, UK, Fahad.Ahmad@port.ac.uk. Taught and assessed you on the MSc.

## Three things to know before you press submit

1. **Certified copies.** The ad says "Copies of originals must be certified." I do not know whether the scans in the certificates PDF are certified copies. Upload what you have tonight so the application is in on time; if KTH needs certified copies it will ask, and that is fixable later. A late application is not.
2. **The manuscript is co-authored with Dr Haig and unpublished.** SDU accepted it as a working paper on the same basis, so there is precedent, but you may want to tell her on Outlook that it went to KTH.
3. **Read the letter before you submit it.** It was written today, in your name. It opens on the toxicity finding from your own pipeline, which is exactly this project's problem: your two annotation tiers agreed on 0.0% of toxicity labels because they used different taxonomies, while the model reported 96.7% confidence. It then states three gaps plainly: no publications, no training in feminist theory, and no knowledge-graph experience beyond a networkx graph.

## How the letter was checked

An independent fact check against `MASTER_RECORD.md` and `HANDOFF_FOR_GPT.md` found two real errors, both fixed: "two annotators" read as if humans had labelled the data, when it was Claude and DeepSeek; and "I run 68 collectors" overstated it, since 62 of the 68 are active. Every other number checked out. Zero em-dashes, no publication claimed, no generative fine-tuning claimed, and ArtemisAI described as running in production ahead of launch.
