# ETH AI Center Doctoral Fellowship 2027: video script

**What the portal asks for:** "a short video of yourself (2-5 minutes) in which you describe your research interests for the fellowship".
**Length:** about 3.5 minutes. The script below is about 500 spoken words: about 3:20 at 150 words a minute, just under 4:00 at a calm 130. Anything from 2:30 to 4:30 is fine; never over 5:00.
**Matches the motivation letter:** same question (opinion, instrument or platform), same mentors (Prof. Elliott Ash as main mentor, Prof. Celestine Mendler-Dünner as co-mentor), same three ETH words (trustworthy, accessible, inclusive).

**How to use it**
- Read it through twice out loud before you record.
- Do not read it word for word on camera. Put the bold cue lines on a sticky note beside the lens and talk.
- If a sentence feels unnatural in your mouth, say it your way. The facts must stay the same.

---

## The script

### 0:00 to 0:20 · Hook
*On screen: face to camera, head and shoulders. No title card needed.*
**Cue: trusted my own system, and it misled me**

> Hello, I'm Asad Ikram. I want to find out when AI can be trusted to tell us what the public thinks. I ask because I trusted my own system, and it misled me.

### 0:20 to 0:55 · Who I am
*On screen: face to camera.*
**Cue: nearly eight years, Artemis, Fluency, Chevening**

> For nearly eight years I've worked with web and social media data, and today I build systems whose numbers brands act on. I'm co-founder and CTO of Artemis AI, a UK start-up building social media intelligence for creators and small businesses who couldn't otherwise afford it; our invited beta opens on 15 December. I also build LLM labelling and AI agents at M+C Saatchi Fluency in London. I hold an MSc in Data Analytics from the University of Portsmouth, which I studied as a Chevening Scholar.

### 0:55 to 1:30 · The turning point
*On screen: face to camera.*
**Cue: three problems, dropped, alike, agreed**

> My dissertation read public reaction to UK economic policy on X, Reddit, YouTube and Quora. When I looked closely, I found three problems. It had quietly dropped the comments written in Urdu and Hindi. It treated four platforms as if they measured alike. And it only looked accurate because it agreed with the lexicon that made its training labels. I see the same thing at Artemis: two models agreeing looks like accuracy, but it isn't.

### 1:30 to 2:20 · The question
*On screen: face to camera. Optional cut-away for 10 seconds: the simulation figure (see "Optional visuals" below).*
**Cue: opinion, model, or platform? Scripts, feeds, updates**

> So here is my question. When an LLM says comments on a policy are more negative on Reddit than on X, is that the opinion, the model, or the platform deciding which posts get written and seen? With my supervisor, Dr Ella Haig, I wrote a preprint that borrows tools from survey methodology for the measurement part of this question. It's a protocol and a simulation, not yet run on real data. The doctorate would run it.
>
> First: does an LLM read the same political message the same way in Urdu script, Roman Urdu and English, judged against native speakers? Second: the same news story on two platforms, checking the model against human labels on each, and comparing the comments a platform shows first with all of them, to separate model error from the platform's effect. And third: when the model is updated, did opinion change, or did the instrument? Open models like Apertus make that last question testable.

### 2:20 to 2:55 · Two mentors, two fields
*On screen: face to camera.*
**Cue: Ash, social science. Mendler-Dünner, platforms. Need both**

> This sits between two fields, which is why the Center's model of two mentors fits it so well. Professor Elliott Ash's group studies how LLMs can measure what social scientists care about, and where human annotators disagree. Professor Celestine Mendler-Dünner studies how much platforms shape what people see and click, and whether LLM survey answers can stand in for real people. I need both: the social science to know which differences matter, and the machine learning to formalise what the platform does.

### 2:55 to 3:20 · Why ETH, and close
*On screen: face to camera. Smile at the end and hold for two seconds before you stop recording.*
**Cue: trustworthy, accessible, inclusive. Builder's habits. Artemis testbed**

> The Center's aim is trustworthy, accessible and inclusive AI. Those are the three problems I keep meeting: is the number right, who can afford it, and whose language does it leave out? I'd bring a builder's habits, like verification gates and versioned prompts, and I'd like to join the entrepreneurial track, because Artemis is a live testbed for this research. Thank you for watching.

---

## Optional visuals (only if they help; face to camera alone is completely fine)

1. **Slide of the measurement problem (recommended if you add anything).** Use `/Users/asad/git_projects/asad_phd/phd_quest/Paper with Ella/LinkedIn/figure1.png` ("Simulated cost of assuming equivalence"). Show it for about 10 seconds during "The question". If you point at the blue line, say "in the simulation, where the true measurement functions are known". Do not quote any wrong-sign-day numbers.
2. **Artemis screen share.** Only if nothing on screen shows a real page name, a real comment, a commenter, a customer, a pilot name, credentials or internal figures. If in doubt, skip it. A wrong frame here costs more than it gains.
3. **Do not show** the CV, transcripts, emails or anything with an address, phone number or ID.

If you add visuals, keep your face on screen for at least the first 20 seconds and the last 20 seconds. They want to see you.

---

## Recording tips

**Set-up (5 minutes)**
- Phone in **landscape**, at eye level (stack books), about an arm's length away. Rear camera if you can see yourself; front camera is fine.
- Quiet room, door closed, fan and AC off for the take. Soft carpet or curtains help the sound.
- Face a window or lamp so light falls on your face. No bright window behind you.
- Plain background. Plain shirt, no logos.
- Wired earphones with a mic, or the phone's own mic within an arm's length. Do a 10-second test and play it back.

**Delivery**
- Calm pace. Pause for a breath at each heading. 3.5 to 4 minutes is fine; do not rush to fit more in.
- Look at the lens, not at your own face on the screen.
- One clean take is fine. Small stumbles are fine; just carry on. If you lose your place, pause, look at the cue, and continue, then trim the pause.
- No music, no captions needed, no editing tricks.

**File**
- The portal's video field has two buttons: **"Record Video"** (records in the browser with your laptop camera) and **"Upload Video"**.
- Accepted formats: **mp4, mpg, avi, mov, mkv, wmv, ogv, webm, flv**. Use **.mp4** or .mov.
- Length: the official instruction is **2 to 5 minutes**. The widget's technical cap is 600 seconds (10 min), but stay inside 5:00.
- **Size limit: not shown on the portal for the video field (verify).** The portal's general label for files says "up to 50MB", so aim for **under 50 MB** to be safe. A 3-minute phone video at 1080p is often 150 to 400 MB, so shrink it first. On this Mac (ffmpeg is installed), run in Terminal from the folder with the video:

```
ffmpeg -i input.mov -vf "scale=-2:720" -c:v libx264 -crf 26 -preset veryfast -c:a aac -b:a 128k -movflags +faststart Asad_Ikram_ETH_video.mp4
```

  That gives a 720p mp4 of roughly 20 to 45 MB for 3 minutes. Watch the output once before uploading (sound in sync, nothing cut off).
- If the upload stalls, use **"Record Video"** in the browser with the laptop camera as the fallback, with the same script.
- Upload the video **first**, before filling the rest of the form, so a slow upload does not eat your last minutes before 16:00 CET (20:00 Lahore).

**Time budget (deadline 20:00 PKT today)**
- Set up and test: 10 min. Two practice runs: 10 min. Record: 10 min. Compress and check: 5 min. Upload: 5 to 10 min.
- Start recording by **18:45 PKT** at the latest.
