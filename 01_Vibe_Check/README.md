<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](../00_Docs/Session_Sheets/01_Vibe_Check.md) |[Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: `technical knowledge and ability to teach`
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: `summarization`
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: `creativity`
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: `math and reasoning`
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: `paraphrasing / tone alignment`

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer:
The answers are generally correct and helpful for the questions being asked. It should be noted that this is a chatbot with a mental health focus, so it ideally wouldn't be asked these types of questions.

1. Accurate explanation of OOP with easy-to-follow examples
2. Distills the important information from the article, removing the color
3. Creative story from a short prompt - perhaps too creative, haven't heard of "song of servos" before
4. Gives the correct answer
5. Same content as original source using slightly different words; output reminds me of using a thesaurus to dress up my high school essays.
---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: `What are the pros and cons of AI Engineer versus senior frontend engineer as the next step in my career?`
   - Result: `Great question. Both paths can be rewarding, but they scratch different itches. Here's a clear side‑by‑side to help you decide, plus a way to test before you commit.`

`AI Engineer: pros`
`- High upside and momentum: rapid growth, premium comp at top orgs, interesting problems.`
`- Broad impact: you can unlock new product capabilities (assistants, copilots, automation) across domains.`
`- Intellectual variety: mix of prototyping, data work, evaluations, systems and product thinking.`
`- Optionality: can move toward ML platform, data, infra, or AI product leadership.`

`AI Engineer: cons`
`- Volatility and ambiguity: fast‑moving tools, shifting best practices, research churn; more failed experiments.`
`- Skill ramp: Python/ML foundations, data engineering, evaluation frameworks, serving/inference, cost/perf tradeoffs.`
`- Fewer clearly defined ladders in some companies; titles vary and expectations can be inconsistent.`
`- On‑site/IP sensitivity in some roles; less pixel polish, more systems/debugging than many expect.`

`Senior Frontend Engineer: pros`
`- Strong, steady demand and clearer career ladders; easier to demonstrate value quickly.`
`- Direct user impact: ownership of UX, performance, accessibility, design systems; visible wins.`
`- Mature tooling and patterns; fast time‑to‑product.`
`- Transferable leadership: cross‑functional influence with PM/Design; path to Staff/Principal FE.`

`Senior Frontend Engineer: cons`
`- Market more saturated; some commoditization pressure and outsourcing risk for basic work.`
`- Less access to the "AI premium" unless you own AI‑powered UX or platform surfaces.`
`- Can feel repetitive if you want deep algorithmic or data/infra challenges.`

`Day‑to‑day contrast`
`- AI Engineer: mix of prototyping (Python, notebooks), model and prompt iterations, retrieval/RAG, evaluation harnesses, data cleaning, cost/perf tuning, deployment and monitoring. Lots of reading, experimentation, and debugging edge cases.`
`- Senior FE: TypeScript/React/Next (or your stack), design reviews, accessibility and performance work, testing, design systems, mentoring, close PM/Design collaboration, shipping highly polished features.`

`Skills you'd lean on and build`
`- AI Engineer: Python, PyTorch/Transformers, APIs for LLMs, vector stores, RAG/agents, evals/guardrails, observability, cloud/K8s, data quality. Product sense to choose simple solutions over flashy ones.`
`- Senior FE: Deep TypeScript, performance (Core Web Vitals), SSR/SSG/streaming, state management, testing, accessibility, design systems, microfrontends, edge functions; stakeholder leadership.`

`Market and compensation (general)`
`- AI roles at top companies/startups can pay a premium, often with equity upside, but hiring is spiky and expectations high.`
`- Senior FE comp is strong and predictable; leadership IC roles (Staff/Principal) remain well‑compensated.`

`Stability and risk`
`- AI: higher variance, faster obsolescence of tools, but long‑term secular growth.`
`- FE: steadier demand across industries; less likely to be cut for core product surfaces.`

`Personal fit signals`
`Choose AI Engineering if most of these feel true:`
`- You enjoy ambiguity, experiments, and reading/trying new techniques weekly.`
`- You like data problems, evaluation design, and systems/debugging more than pixel‑perfect UI.`
`- You're comfortable with Python/ML or excited to invest 6–12 months to ramp.`
`- You want to ride a fast wave and accept higher variance for higher upside.`

`Choose Senior Frontend if most of these feel true:`
`- You get energy from crafting delightful interfaces and measurable UX wins.`
`- You want clearer scope, faster time to visible impact, and a well‑defined ladder.`
`- You like mentoring engineers, leading design systems, and driving product quality.`
`- You prefer stability with the option to sprinkle AI into UX where it makes sense.`

`A practical hybrid you might love`
`- Become the "AI‑powered Frontend" specialist: own end‑to‑end user experiences that leverage LLMs (smart search, copilots, inline suggestions). You'll stay senior in FE while building credible AI chops: prompt/eval, RAG basics, latency/cost tradeoffs, safety/guardrails, and UX patterns for AI.`

`Low‑risk 60–90 day test plan`
`- Month 1: Build and ship one LLM-backed feature.`
`  - Pick a domain you know. Implement RAG with a hosted model/API, add evals and telemetry, deploy, and measure latency/cost. Write a short doc on trade‑offs you made.`
`- Month 2: Double down where you felt flow.`
`  - If you loved it: implement guardrails, batch evals, cost optimization, and a small A/B with different prompts or retrieval settings.`
`  - If you didn't: ship a performance‑focused FE project (SSR + streaming + hydration strategy), hit Core Web Vitals targets, and lead a design system or accessibility push.`
`- Month 3: Tell the story.`
`  - Package your work into a portfolio case study. Talk to 3–5 engineers in roles you're considering. Ask for shadowing or code review on one PR/notebook.`

`Resume/portfolio focus`
`- AI Engineer: shipped features with measurable impact; evaluation methodology; data quality work; latency/cost improvements; monitoring and failure‑mode analysis.`
`- Senior FE: performance improvements with numbers; accessibility wins; design system ownership; complex state/SSR architecture; mentoring and cross‑team leadership.`

`A few clarifying questions to tailor advice`
`- What's your current stack and strongest skills today?`
`- Which work gives you more "flow": polishing UX and performance, or experimenting with data/models and evaluations?`
`- How much time are you willing to invest to pivot (nights/weekends vs on‑the‑job)?`
`- What's your risk tolerance around market volatility and role ambiguity?`
`- Do you want to stay IC, or are you aiming for Staff/Principal leadership soon?`

`If you share these, I can suggest a more personalized path and a concrete learning roadmap for the next 8–12 weeks.`

2. Prompt: `Help me plan a birthday surprise for my wife.`
   - Result: `I'd love to help you craft something she'll genuinely feel loved by. Here are a few curated surprise concepts plus a simple timeline. Pick one that fits her personality, and I'll tailor all the details once I know more about her.`

`Four strong surprise concepts`
`1) The Day of Little Joys (micro-surprises across the day)`
`- What: Stagger small delights every few hours.`
`- Flow:`
`  - Morning: favorite coffee + handwritten note; a playlist link.`
`  - Midday: flower delivery at work/home; lunch from her favorite spot.`
`  - Afternoon: a 60-min massage or spa appointment (mobile therapist if at home).`
`  - Evening: dinner reservation or a transformed dining room at home; dessert with a short video montage from friends.`
`- Why: Thoughtful, low stress, works with any schedule.`
`- Budget: Low to high depending on choices.`

`2) Private "Restaurant" and Spa at Home`
`- What: Turn your home into a boutique spa + restaurant.`
`- Flow:`
`  - Spa: bath setup, plush robe, candles, calming playlist; you handle chores so she fully relaxes.`
`  - Dinner: hire a local private chef or do a tasting menu with elevated takeout; printed menu with inside jokes; custom mocktail/cocktail.`
`  - After: gift and a slow-dance song that matters to you both.`
`- Why: Intimate, pampering, great if she's introverted or hates big surprises.`
`- Budget: Medium to high (can be done budget-friendly with DIY).`

`3) Memory Lane Scavenger Hunt`
`- What: Clues leading to meaningful places or people.`
`- Flow: 4–6 stops (first date spot, a park bench, favorite bakery), each with a small note/gift; friends at one stop with a Polaroid; final stop is you with a picnic or dinner.`
`- Why: Romantic and personal; creates a story for the day.`
`- Budget: Low to medium.`

`4) Sunset Picnic + Outdoor Movie`
`- What: Cozy setup at a scenic spot (or backyard).`
`- Flow: picnic with her favorites, fairy lights/lanterns, projector + her favorite film, cake under the stars.`
`- Weather backup: Indoor "fort" picnic and movie.`
`- Budget: Low to medium.`

`Personal touches that elevate any plan`
`- Love language lens: Include at least two—words (letter), acts (you handling tasks), quality time (tech-free hours), gifts (meaningful, not pricey), touch (slow dance, massage).`
`- Letter prompt: "Five moments this year I loved with you…" + "What I admire most about you is…"`
`- Custom playlist named "Wife's Birthday [Year]" with 12 tracks tied to memories.`
`- Small signature detail: her favorite flower, candle scent, or color palette appearing throughout.`

`Simple planning timeline`
`- 2 weeks out: Choose concept and budget; book any reservations/services; loop in one trusted friend as your secret helper; order gift and any decor.`
`- 1 week out: Confirm bookings; write notes/clues; assemble playlist; plan child care/pet care.`
`- 2–3 days out: Grocery and gear run; charge projector/camera; wrap gifts; prep printed menu or schedule.`
`- Day before: Stage what you can; confirm deliveries; weather check and finalize backup plan.`
`- Day of: Start with a note; keep cushion in the schedule; take a couple candid photos; be present.`

`Gift ideas that pair well`
`- Experience: pottery/painting class for two, weekend day trip, concert/comedy tickets.`
`- Personalized: custom illustration of a favorite photo, engraved jewelry with a meaningful date/phrase.`
`- Cozy luxury: cashmere wrap, high-end robe, or a gorgeous throw with a hardcover of her favorite author.`

`Common pitfalls to avoid`
`- Over-scheduling; leave breathing room.`
`- Forgetting a heartfelt card.`
`- Last-minute venue changes without a backup.`
`- Surprises she can't opt out of—give a gentle "dress code + vibe" hint the day before if needed.`

`Quick questions so I can tailor a perfect plan`
`- Date and rough budget?`
`- Does she prefer intimate/quiet or social/energetic?`
`- Any must-include favorites (foods, music, flowers) or dietary needs?`
`- Kids/pets to plan around and do you want them involved?`
`- Is she into surprises, or should we reveal the plan the morning of?`
`- One thing she's been stressed about lately (so we can remove that load on her day)?`

`Share a bit about her, and I'll turn your pick into a step-by-step checklist with scripts, vendors, and a shopping list.`

3. Prompt: `What can I cook with chicken meatballs, green beans, rice, and chimichurri sauce in the fridge?`
   - Result: `Great combo—you've got the makings of a fast, flavorful meal. Here are a few easy options:`

`1) Chimichurri meatball rice bowls (15 minutes)`
`- Blister green beans in a hot skillet with a little oil and salt (5–7 minutes).`
`- Warm the meatballs (same pan or oven/microwave; if uncooked, cook through to 165°F/74°C).`
`- Warm the rice (microwave with a splash of water).`
`- Bowl it up: rice, meatballs, green beans, generous drizzle of chimichurri. Optional: squeeze of lemon, a dollop of yogurt, or crumbled feta.`

`2) Chimichurri fried rice`
`- Dice the meatballs.`
`- Stir-fry green beans in a hot pan with oil and a pinch of salt until crisp-tender.`
`- Add diced meatballs; then add cold cooked rice and toss until hot. Season with salt/pepper (a splash of soy or lemon is nice if you have it).`
`- Turn off heat and fold in chimichurri so it stays bright. Optional: top with a fried egg.`

`3) Sheet-pan meatballs and green beans`
`- Roast meatballs and green beans tossed with oil, salt, and pepper at 425–450°F (220–230°C) for 12–15 minutes, flipping once.`
`- Serve over warm rice and drizzle chimichurri. Optional: mix chimichurri with a little yogurt or mayo for a creamy drizzle.`

`4) Warm rice salad`
`- Blanch or sauté green beans until just tender; slice meatballs.`
`- Warm rice and toss everything with chimichurri thinned with a bit of olive oil and a splash of vinegar or lemon. Optional add-ins: toasted nuts or seeds.`

`If you tell me how much time you have or what kitchen tools you prefer (stovetop, oven, one-pan), I'll tailor it to that.`

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer:
These answers are pretty good for not having much context about me. However, this could certainly be improved by giving more information about myself and my preferences. The chatbot notes this in each response, asking for additional information that would lead to a better answer.
1. Good overview of the two job roles, but the chatbot admits to needing more info on my career background/interests
2. Offers clever ideas for different budgets, but asks follow up questions for a more "tailored" plan
3. Admittedly an easy answer with the ingredients given, but it answers with what I would make and gives at least 1 other that sounds appetizing
---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: `When should I go to the gym based on my schedule for tomorrow?`
   - Result: `I can help you lock in a realistic gym window. Can you share a quick snapshot of your day tomorrow?`

`- Fixed commitments with times (work/classes/appointments)`
`- Wake-up and target bedtime`
`- Commute time to/from the gym and gym hours`
`- How long you want to work out (and if you need shower time)`
`- When you usually have the most energy (morning, midday, evening)`
`- Any must-avoid times (meetings, childcare, etc.)`

`If you’d rather not list it all, here are two simple options that work for most people:`
`- Morning: Go soon after waking, before the day gets hectic. Great for consistency; aim for a 45–60 min session.`
`- Post-work: Go directly after work/school before going home. Good for stress relief and follow-through.`

`Once you share your schedule, I’ll suggest the best 1–2 time slots and a quick plan to make it stick.`

2. Prompt: `What time should I leave for Charlotte in order to make it to the comedy show I have tickets for?`
   - Result: `Great question—planning your timing now will make the night feel a lot smoother. I can give you a precise leave-by time, I just need a few details:`
`- Where you’re leaving from (neighborhood or city)`
`- Venue name in Charlotte`
`- Show date and start time`
`- How you’re getting there (driving, rideshare, light rail)`
`- Will you need to find parking or pick up tickets at will call?`

`Rule of thumb if you want a quick answer now:`
`- Aim to be at the venue/parking area 30–45 minutes before showtime (for parking, security, bathroom, and finding your seats).`
`- Add your estimated travel time from a maps app.`
`- Add a traffic cushion: +20–30% outside rush hour, +40–60% during rush hour or big-event nights.`

`Example: If the show is at 8:00 pm and your maps app says 25 minutes, leave around 6:45–7:00 pm (25 min drive + ~20–30 min cushion + 30–45 min early arrival).`

`Pro tips to reduce stress:`
`- Check live traffic and parking 2–3 hours before you go; set a “latest leave time” reminder.`
`- If driving, pre-select a parking garage and save the walking route.`
`- If using rideshare, plan for surge times by booking a bit earlier.`

`Share your details and I’ll give you a specific leave-by time.`

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer:
The chatbot does not know my schedule (when I start work, when the comedy show is) so can only answer with "best practices". While it gives good advice for how to approach these questions, it is unable to give specific answers. The chatbot would likely need access to my schedule, destinations, and real time traffic info to answer these with specific answers.
---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2.
3.
4.
5.


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
