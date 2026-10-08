# Master Motivation Letter Pattern · v3 (advanced)

Set 8 Oct 2026 from the Corvinus (Wachs) rewrite, which Asad approved. Use it for every motivation letter and the CV that goes with it.
Worked example: `Corvinus Application/letter.html` and `cv.html`.

## Before writing (no drafting until all five are done)
1. **Advert verbatim.** Copy the "You", "Requirements" or "Profile" lines from the live page into a criteria map: each line, then the evidence in the advert's own words.
2. **Professor's work.** Read 2 or 3 of their recent papers. Note one result with its number, and one limit the paper itself states.
3. **Fit screen.** Topic is social media research or web scraping and data collection (see phd-search-focus). Check eligibility, fees and degree field.
4. **Facts.** Every number must be in MASTER_RECORD.md. Where his account and the records differ, use the records until he confirms.
5. **Do-not list.** See Rules.

## Letter structure (2 pages maximum)
| # | Paragraph | What goes in it |
|---|---|---|
| 1 | **Hook (STAR, 5 to 7 lines)** | **S:** their phenomenon or data, joined to his social media work in one line. The first sentence is under 25 words, literally true, with no metrics and no life story. **T:** what the advert asks, naming its criteria. **A:** three things he brings, one clause each. **R:** what he wants to do with them in their group. |
| 2 | **Your work** | One or two of their papers: the result in their numbers, the limit they state, and how it matches what he sees. This is what the professor cares about most. |
| 3 to 5 | **One paragraph per criterion** | The bold lead uses the advert's words (e.g. "Computational methods for social questions."). Inside, a mini STAR: role, then action, then result. Research and analysis come first; infrastructure gets one clause. |
| 6 | **Why social media, and my connection** | His passion for social media work. The platform-trace bridge to their data. His personal link to their population or question. |
| 7 | **A question I could contribute to** | Their vocabulary, one of their papers, and his validity habit (visibility rules versus behaviour). |
| 8 | **Why a PhD, and why now** | Apply what he learned in the MSc, at Fluency and at Artemis AI; learn methods industry did not teach; carry results back into practice. |
| 9 | **What I do not yet bring** | Honest gaps taken from the advert's "useful" list, and how he will close them. |
| 10 | **Practicalities** | Start date, relocation, two referees with roles and emails. |

## CV mirrors the letter
- **Profile:** led by the criteria, not his life story. The freelance origin gets one line, as his link to the question.
- **"What the position asks for":** one row per advert criterion, with two lines of evidence each.
- **Order:** Research before Education. The most relevant roles come first (social media: Fluency, Artemis AI). Small roles are merged into one row.
- **Community row:** web-scraping-guide.com, plus mentoring students and juniors into remote work.

## Rules
- Story stays short: at most one line of biography in paragraph 1.
- AI framing: he **builds** agents (self-healing crawler agent, builder agent) and decides what ships; AI coding assistants help him. Never write that AI writes his code.
- Artemis AI evaluation: say he reads the literature and designs evaluation around human-labelled data. The label-validity and audit findings were learning, not an achievement, so leave them out.
- Never name clients under NDA. Never promise arXiv dates. No code or DOI links for the paper unless he asks.
- No em dashes. No model metrics in paragraph 1. Write in British English, with contractions where natural.
- Use web-scraping-guide.com (not Zyte) for public work.

## Final checks
1. **30-second test (professor persona):** can every advert criterion be ticked from paragraphs 1 to 5 alone?
2. **Their-words test:** does each criterion paragraph use the advert's phrasing?
3. **Fact test:** is every number in MASTER_RECORD.md?
4. **AI test:** read it aloud. If it sounds like a model, redraft.
5. **Render:** 2 pages, 0 em dashes (`pdftotext | grep -c "—"`).
