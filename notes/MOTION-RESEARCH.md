# Motion tool research, 2026-11-17

Raw output of a research run made by the product chat for the owner: an audit of the current motion gallery, web research, three independent concepts, one merged recommendation and an adversarial critique of it. Nothing here is a decision. Agents marked what they could not verify; treat web claims as leads, not facts. Written in English by the agents; talk to the owner in Russian.

Owner answers so far (17.11): the production app is native iOS and Android. Open: where motion values officially live (this tool or Figma), whether a saved decision is applied to the prototype, which pattern goes end to end first.

---

## 1. Recommendation (merged from three concepts)

VERIFICATION NOTE
I judged and merged from the supplied audit, research and concepts only. I opened no files, ran nothing and did no web search, so every fact about current behaviour is inherited and unverified by me. Effort estimates are judgement.

1. SCORES (designers / developers / feasibility / first stone)

| Concept | Des | Dev | Feas | Stone | Reasoning |
|---|---|---|---|---|---|
| 1 Workbench | 9 | 6 | 7 | 6 | Best daily tool and closest to today's page, but motion stays a list of 46 separate things. |
| 2 Spec | 6 | 9 | 5 | 7 | Answers the main developer complaint; risks false precision and needs developers nobody has asked yet. |
| 3 System | 7 | 7 | 6 | 9 | Only one that creates a language (patterns, roles, principles); risk of a tidy system built before anyone uses it. |

Merge: Concept 3's structure, Concept 1's tuning flow, Concept 2's spec card and "exact / confirm on device" labels.

2. THE RECOMMENDED TOOL

Promise: every animation in the product is an instance of a named pattern built from tokens. You watch it on the real screen, tune it with tokens, and hand it over as numbers through one link.

Sections
- Patterns: home page with 8 patterns and 4 principles; each pattern has one recipe, a reduced-motion variant and its instances.
- Library: all animations (M-IDs) by pattern, with a status, an honest coverage counter and "coming soon" rows for the uncovered ones.
- Stage: the real prototype with today's playback (speed, loop, compare, close-up), plus a spec card and token-first tuning.
- Tokens: the scale as a page, with "used by N animations" and a health counter of numbers outside tokens.
- Handoff: decisions, exceptions with reasons, token file, per-animation status.

Core interactions
- Designer tunes a pattern:
  1. Open Sheet; the recipe reads "duration sheet 500 ms, curve soft".
  2. Step to a neighbouring token; free values sit behind a visible "off-scale" switch.
  3. See "affects 6 animations", walk them with the arrow keys, flip A/B on one phone.
  4. Save with one line of why, or mark one instance as an exception.
- Developer builds from a ticket:
  1. The link opens one animation in its state.
  2. The spec card shows trigger, phases as bars, from/to, tokens, interruption and reduced motion.
  3. Replay at 0.1x and copy the values.
- A decision is done only when applied: after the owner's "ок" the agent updates the prototype and the data, and the status changes.

3. ROADMAP

Tomorrow (realistic overnight, on the existing page)
1. Link to one exact animation and speed, plus a 0.25x speed.
2. Pattern tags on the 26 existing items, a "26 / 46" counter and "coming soon" rows.
3. One hand-written spec card with phase bars for the price change.

Before demoing: nobody has watched the gallery since the Odds tab rebuild on 16 Nov, so run all 26 scenarios first. Everything else (token page, health panel, export, native values, reduced-motion preview) should be described in words, not faked.

First month
- One data file for the inventory; the cards, the Library and MOTION.md all come from it.
- Token set v2 as one proposal for the owner's "ок".
- Tuning snapped to the token scale, replacing the XS-XL multipliers.
- Scenarios for the missing animations, live-data ones first.
- Reduced-motion switch (needs a small flag in the prototype) and a field per animation.
- Automatic token health panel and a JSON token export.
- The "apply after ок" flow.
- Pilot: five cards read by one iOS and one Android developer.
- A phone view with three controls (replay, speed, A/B).

Later
- Springs with per-platform values tuned on devices, and one reference sample per platform.
- Gesture specs and haptics.
- A scripted live match for data-driven motion.
- Other sports; Figma motion variables.

4. THE MOTION LANGUAGE

Principles, each written as a test a proposal can fail
- Real change only: motion fires on a real data change, never on re-render and never to create urgency.
- Quiet often, loud rarely: frequent actions (odds taps, price ticks) are short and calm; expression is kept for rare moments (bet placed, goal).
- Never in the way of a bet: motion does not cover, shift or delay betting controls; a suspension applies immediately; everything can be interrupted.
- Readable without motion: every end state makes sense with motion off; meaning is never carried by motion alone.

Token layers
- Primitives: 5 durations and 3 curves (say three honestly), plus proposed distance (about 3 steps), press scale (1) and stagger step (1).
- Holds: pauses, not motion (price highlight, toast, arrows). This is original work, since no public system covers it.
- Roles: enter, exit, move, feedback, value change; each is one duration plus one curve.
- Patterns: recipes built from roles.
- Springs wait until the stack is known.
- The project rule forbids new tokens without asking, so all of this is a proposal.

Patterns
1. Press feedback.
2. Value change: price tick, score roll, the "my pick" variant, and a burst rule for many changes at once.
3. Enter / Exit, including the toast.
4. Sheet and overlay.
5. List change: add, remove, height, feed insertion with the "N new updates" pill.
6. Page.
7. Availability: suspend, resume, locked.
8. Live moment: goal, live dot, match state change.

A pattern needs three or more instances; one-offs and celebrations stay outside the system.

5. HOW SPECS REACH NATIVE DEVELOPERS

- Start with what ports to any stack: durations and bezier curves port exactly; roles, patterns and behaviour rules port as text.
- One spec card format with fixed fields:
  - trigger, element, property, from/to in pt/dp;
  - duration and curve tokens, delay, phases;
  - interruption rule;
  - reduced motion: keep / fade / instant / off;
  - system default or custom, per platform;
  - acceptance checks.
- Every value is labelled "exact" or "starting point, confirm on device".
- No springs and no generated animation code until the stack is confirmed. Hand over values and rules only.
- Flag one known trap: a 500 ms CSS sheet is roughly a 0.3 s spring in Apple's terms. This is calculated, not checked on a device.
- Ship one token file in the standard design-token format; each platform reads it its own way.

6. QUESTIONS FOR THE OWNER

1. Production stack?
   - Options: native iOS and Android / React Native or Flutter / web inside the app / unknown.
   - Recommendation: ask engineering this week; until then, work on roles, durations and curves only.
2. Where do motion values officially live?
   - Options: this tool's data / Figma motion variables / both.
   - Recommendation: this tool. It needs an explicit exception to "Figma wins".
3. What happens to a saved decision?
   - Options: stays a record / the agent applies it after "ок" / applies itself.
   - Recommendation: applied after "ок".
4. Token v2 scope?
   - Options: keep 5 + 3 and add roles / also add distance, stagger, press scale and holds / full rebuild.
   - Recommendation: the second, approved as one list.
5. Which pattern goes end to end first?
   - Options: Value change (odds) / Sheet / Press feedback.
   - Recommendation: Value change, the most frequent and most sports-specific.
6. Developer partner for the pilot?
   - Options: one iOS and one Android developer for 30 minutes each / one developer / nobody yet.
   - Recommendation: both; with nobody, build only the "tomorrow" tier.

7. THE 60-SECOND PITCH

"Today motion in our product is decided by eye and handed over as a video. We audited the prototype: 46 animations, 30 timings outside any system, the same colour change done with three different curves.

Here is the first stone. Every animation plays on the real screen, slowed down, next to its numbers. Each belongs to one of eight patterns, such as price change, suspend or goal, built from a small set of tokens.

A designer changes a token and sees every animation it touches. A developer opens one link and gets the trigger, the timeline, exact values and what happens with Reduce Motion on.

We show how much is covered and what is still by eye. Next month: one pattern, price change, carried from design to an iOS and an Android developer, to prove the format before we scale."

Files referenced (none changed)
- public/motion.html
- notes/MOTION.md
- public/index.html
- README.md

---

## 2. Critique of the recommendation (read this before acting on section 1)

VERIFICATION
Re-read parts of public/motion.html, notes/MOTION.md, and ran read-only git status. Nothing was run in a browser, no web search. Anything not marked "checked" is inherited from the audit.

1. UNSUPPORTED OR WRONG CLAIMS
- "26 / 46 honest counter": the denominator is false. The inventory misses about ten animations (Live updates feed, pill, tab switches, team page). Real total unknown.
- "A pattern needs three or more instances" breaks on its own list (checked in MOTION.md): Availability = M16 only; Page = M38, M39; Live moment = M19, M20. "Score roll" does not exist in the inventory.
- "Quiet often: price ticks are short" contradicts the flagship pattern: M21 is 0.8 s in + 2 s hold + 1.5 s fade, 5 s hold for my pick (checked). The principle fails its first test unless motion and hold are separated.
- Pitch, "decided by eye, handed over as video": no developer was asked. Unsupported.
- Pitch, "30 timings outside any system": that describes the HTML prototype's code, not the shipped app. An engineer will say so in the first minute.
- Pitch uses present tense for things that do not exist: token tuning with "affects N animations", developer link with timeline and Reduce Motion.
- "Standard design-token format": two research reports disagree on whether it covers duration and curves; no spring type; no ready native converters. "Each platform reads it its own way" is unowned work.

2. "TOMORROW" ITEMS
- Link to one animation + 0.25x: realistic (hash link and speed buttons exist, checked). The page is desktop-only (min-width 1100 px), so the link breaks on a phone.
- Pattern tags + coming-soon rows: an evening technically, but it publishes a taxonomy the owner has not approved, adds a fourth classification, and leaves 40%+ of the list as dead rows someone will click. Cut.
- Spec card for price change: realistic for M21 only. It is a sixth hand-kept copy of the same numbers. M22 (my pick) has no scenario (checked), so "value change end to end" cannot be demoed.
- Demo risks: 26 scenarios unwatched since 16 Nov; index.html has uncommitted changes now (checked), so local and published differ; motion.html is in public/, so any push shows it to stakeholders; spring presets in the page contradict "no springs yet".

3. WILL NOT SURVIVE NATIVE DEVELOPERS
- Sheet, page push and back gesture are OS-owned. "Sheet 500 ms, soft", the recommendation's own tuning example, will not be built. Say: "system default; we specify only what happens inside".
- Height changes: native animates a state, not "height 440 ms". Say what grows, which edge is anchored, what neighbours do.
- "Exact" is true for a number, not for feel. Both platforms default to springs; developers will ask on day one. Say: "bezier is the reference; a spring is fine if it matches the 0.1x recording".
- Live price ticks in recycled list cells: no coalescing rule, no performance budget.
- A developer cannot open this page on a device. Each card needs a slow-motion recording.
- px to pt/dp: unverified.

4. OVER-ENGINEERED, CUT
- Five sections: keep list + stage with card.
- Four token layers: keep primitives, holds, five or six patterns. Roles later.
- JSON export, health panel, phone view, per-platform status, token-snapped tuning rewrite: all before any developer has used one card.

5. MISSING
- The shipped app: no look at how it moves today or whether the company design system already has motion values. Unverified either way.
- Developer interview first, not as a month-end pilot.
- Governance: who approves, where deviations go. "Figma wins" and "no new tokens" in project rules both conflict with the plan and need the owner's explicit "ок".
- One decision actually applied. None has been.
- QA acceptance method, haptics, a legal view on motion around odds (unverified).

6. WHAT ROTS FIRST
- Hand-kept selector lists in motion.html and MOTION.md itself: dated 13 Nov, already behind after three days.
- Prevention: add "motion changed: inventory row and scenario updated" to every task's done criteria; a read-only check listing scenario selectors missing from index.html and literal times in transitions; one data file only if MOTION.md is generated from it; the reviewer agent checks it.

7. CORRECTED ROADMAP
1. Tonight: watch all 26 scenarios; hide broken ones.
2. Tonight: link to one animation and speed; add 0.25x.
3. Tonight: one M21 card, labelled "draft format".
4. Demo: show only what works; future tense for the rest; no taxonomy on screen.
5. Week 1: ask engineering about stack, minimum OS, system versus custom sheets and navigation, existing motion constants.
6. Week 1: screen-record the ten most frequent motions in the shipped app.
7. Week 2: 30 minutes with one iOS and one Android developer over the M21 card; rewrite the format from their questions.
8. Week 2: owner approves one list: principles, patterns, holds, the Figma exception.
9. Week 3: apply one real decision to the prototype (one curve for colour changes).
10. Week 3: inventory as one data file that generates MOTION.md and cards, plus the drift check.
11. Week 4: scenarios for live-data motion (M22, M16, M20, Live updates) and the reduced-motion flag; this touches index.html, so one chat at a time.
12. Later: springs on devices, gestures, haptics, token file, other sports.

Files read (none changed)
- public/motion.html
- notes/MOTION.md
- public/index.html (grep only)

---

## 3. Audit of the current tool (public/motion.html, notes/MOTION.md, tokens)

MOTION TOOL AUDIT (read-only, from code; nothing was run)

Verification status
- Read in full: public/motion.html (713 lines), notes/MOTION.md (185 lines), README.md "Motion" section (lines 81-105), MOTION TOKENS block (index.html 272-282, 423), JS mirror and helpers (index.html 1871-1881), gallery hooks (index.html 2818-2842).
- UNVERIFIED: live behaviour of the gallery. No preview server was running on 4173 and I was not allowed to start one, so everything below about what the page "does" is read from code, not watched. Whether every one of the 26 scenarios still plays after the 16 Nov rebuild of the match Odds tab is unverified (the functions and ids they call all still exist in index.html; M02 `#mkts .choice` on match m4 is the one I would check first).
- UNVERIFIED: that production is native iOS/Android (the task says so too).
- No web search was done; native remarks are general knowledge.

1. What the gallery page does today (public/motion.html)
- Desktop-only page (min-width 1100 px), not linked from anywhere, opened by its own address. Three columns: list on the left, phone in the middle, controls on the right.
- Left list: 6 groups (Press feedback, State change, Numbers and texts, Reveal and cascade, Sheets and overlays, Pages) holding 26 animations. A decided group shows the preset name and a tick. Bottom button "Decisions and export" with a counter "n / 6".
- Middle: the real prototype (index.html?embed) in a frame. Clicking an animation puts the prototype in the right state instantly and plays that one animation, usually there-and-back (open then close).
- Presets: per group, "Original" plus 4-5 named presets by feel (Subtle, Soft return, Bouncy, Firm, Domino...). 28 presets in total.
- Two rows of five steps XS-XL under a preset: "how strong" (depth / travel / gap / bounce) and "how long" (duration), with the resulting value shown.
- Viewing: speed 1x / 0.5x / 0.1x (slows timers and all animations together), Play again, Loop, "Compare with the original" (two phones side by side: untouched vs with your decisions), Close-up (crops and zooms to the element, up to 3x). Keyboard: up/down walks the list, Space or R replays.
- Advanced (collapsed): sliders with number fields for the group's own values (scale, opacity, offset), duration 0-2000 ms, easing dropdown (7 curves + 4 named springs + custom spring with bounce), a tiny curve picture, per-item delay for the cascade group, a "Today" list of 1-3 lines saying what the preset replaces, and a free-text note per group.
- Saving: "Save for the group" or "Save for <this animation> only" (an exception). Status line says what is on the phone versus what is saved. Stored in the browser's localStorage.
- "Decisions and export" screen: one line per group, exceptions, scope note, the "why" note, a fixed list of 6 "For development" caveats, and two buttons: Copy decisions (plain text) and Copy link (the decisions packed into the address).
- Shows a banner if the system has Reduce motion on ("previews do not move").
- It only previews on top of the prototype (extra CSS plus a few wrapped functions); index.html is never changed by it.

2. Designer: can / cannot
Can
- Explore: see 26 real animations in the real product screen, in context, slowed down, looped, zoomed.
- Compare: current motion versus "my decisions" side by side.
- Tune: presets, XS-XL steps, exact values, springs with duration + bounce.
- Decide: one preset per group plus per-animation exceptions, with a written reason.
- Share: paste a text summary or send a link that restores the same decisions.
Cannot
- Judge motion on a phone, with a finger. Desktop only; a press is faked by applying the :active styles for 300 ms; the sheet drag (M33) cannot be shown at all.
- See 20 of the 46 product animations: limit denial (M08), day switch (M13, M40), LIVE filter (M41), suspended/locked (M16), scroll hints (M18), live dot (M19), Goal! (M20), my-pick price (M22), card removal (M25, M36), summary height (M29, M30), drag (M33), and the whole new match Odds tab (M45-M48). The entire Live updates feed is missing too.
- Compare two candidates against each other (only original vs chosen), scrub a timeline, or see phases laid out in time.
- Tune a token. The controls tune a group; nowhere does the page show the token scale or say "this is --m-std".
- Stay inside the system: XS-XL multiplies durations by .5/.75/1.5/2.2, so results like 240, 480, 700 ms are new numbers off the five-step scale.
- Preview or design the Reduce motion version (the page just stops moving).
- See an animation's description (trigger, phases) while looking at it; that lives only in MOTION.md.
- Keep a shared, versioned record: decisions live in one browser; no history, no "approved by", no comments; nothing writes back to the prototype or to Figma.
- Design haptics or sound together with motion (the prototype has one `navigator.vibrate(12)`, undocumented).

3. Developer: can / cannot take
Can take
- Token values: 5 durations and 2-3 curves as cubic-bezier (README table, CSS block).
- MOTION.md: per animation, what moves, trigger, phases with duration and curve, off-token numbers, interruption behaviour. Plus a general interruption rule and a reduced-motion rule.
- From an export: per group, a line such as "ease cubic-bezier(...), 300 ms" or "spring Gentle (duration 500 ms, bounce 15%, settles in N ms)". The spring is defined the SwiftUI way (stiffness = (2pi/duration)^2, damping = 1 - bounce), so it maps to SwiftUI directly.
- Six honest caveats ("matched by eye in a native sample", duplicated numbers, etc.).
Cannot take
- Any machine-readable output: no JSON / tokens file, no Swift, Kotlin/Compose or CSS snippet. Export is one text blob.
- Native equivalents: no stiffness/damping pair for Android/Compose or UIKit, no mapping of --soft to a platform spring (one CSS comment says "close to the UIKit sheet spring" and that is all), no per-platform values.
- A per-animation spec card in the tool (properties, from/to, duration, curve, delay, sequence diagram). The gallery shows none of this; the developer must read a Russian markdown table and CSS selectors.
- Full from/to values: distances and scales are scattered (5, 4, 6, 8, 12, 18, 30 px; .97/.98/.985) and several are missing from the inventory rows.
- Sequences as data: multi-phase chains (M08, M21, M25, M28, M36) are prose with timers, no timeline.
- A reduced-motion spec per animation: there is one global CSS kill-switch (index.html 614) and a few JS rules; nothing says what each animation becomes.
- Gesture specs (velocity thresholds, rubber band) beyond "220 ms, thresholds and coefficients".
- Coverage of what was built after 13 Nov (Live updates, team page, goalscorer).
- Confidence that a decision is final: decisions are not applied anywhere, so prototype, export and inventory can all disagree.

4. Token system
Coherent core
- Five durations with clear roles (press .12 / quick .2 / std .32 / layout .44 / sheet .5) and two curves by role (--soft travels and resizes, --ease changes in place). Real usage is high: in index.html var(--m-quick) x45, --m-std x21, --m-press x12, --m-layout x11, --m-sheet x6; var(--soft) x36, var(--ease) x19; JS T.std x20, T.layout x9.
- JS mirror exists (T, SOFT) and the embed hook MOTION.tokens() re-syncs it from CSS.
Where it leaks
- The block says "Two curves and five durations" but actually holds three curves (--exit) and eight durations (--chg-in .8, --chg-fade 1.5, --chg-fade-pick .6), plus a second family --o-* at line 423 (110 ms, .16 s, 70 ms, 6 px). README's table lists only the 2 + 5.
- MOTION.md itself counts 30 product places with numbers outside tokens (hold times 1000/2000/2600/5000, delays 60/80/90/110, staggers 32 and 45 ms, 120 ms feed exit, .6 s keyframes, 2.4 s pulse...).
- 26 of 93 transition declarations carry a literal time (about half are prototype chrome, the rest are product delays/staggers).
- Curve keywords instead of tokens: ease-out x15, ease-in, ease-in-out, linear; most colour transitions have no curve at all (browser default), so "state change" uses three different curves.
- Duplicated truth: CHG_T {2000,1500,5000,600} in JS repeats --chg-* by hand; T is typed numbers, not read from CSS at load; --m-press, --ease, --exit have no JS mirror.
- Borrowed tokens: a duration token used as a delay (card removal starts "--m-press into the fade"); the bar's release takes --m-sheet by accident.
Naming
- Mixed logic: --m-press and --m-sheet are named by component, --m-quick/--m-std by speed, --m-layout by property. Curves have no prefix (--soft, --ease, --exit) and "--ease" collides in meaning with the CSS keyword. JS names (SOFT, T.std) differ from CSS names. No tiering (primitive vs semantic).
Gaps
- No tokens for: delays, stagger step, hold/dwell times (toast, arrow, Goal!), distances (7 different entrance offsets), press scales (3 values), opacity levels (dim 30/40/60/70%), springs, exit curve as a first-class token, reduced-motion alternatives, haptics, per-platform values, gesture thresholds.

5. The inventory (notes/MOTION.md)
- 48 numbered entries, M01-M48, in 8 sections: 46 product animations and 2 prototype-chrome ones (M43, M44). Header and README still say "M01...M44".
- Each row: what moves, trigger (with the JS function name), phases with duration and curve, off-token numbers, interruption behaviour. Then two strong extras: 15 "similar things done differently" findings and a table of 30 off-token numbers.
- Enough to rebuild without code? For simple ones (press, colour change, page push, sheet) yes. For complex ones only partly: from/to values are incomplete, curves inside keyframes are "four own curves" with no numbers (M08), gesture maths is not given (M33), sequences have no timeline, there is no picture or recording, and identifiers are CSS classes and JS function names. It is written in Russian for the author, not as a spec for an iOS/Android developer.
- It is a hand-kept snapshot dated 13 Nov and already drifting: about 50 motion-related lines were added to index.html since it was first written, but only M45-M48 were added. Not in the inventory at all: Live updates event entering and pushing the feed (index.html 1036-1043), the shot line drawing, the "1 new update" pill (1045), header score fade, probability bar, All / Key Events switch, Odds / Live updates tab switch, team-page menus and push, goalscorer card, Top Bet legs dimming.
- Three taxonomies do not line up: 8 inventory sections, 6 gallery groups, 5 duration tokens.

6. Main weaknesses, by impact
1. The gallery and the token system are two different models. You tune "groups" with free values, the system is tokens; nothing translates a decision into "change --m-sheet to X" (motion.html `apply` functions write raw ms and curves on selectors).
2. Decisions go nowhere. Save = localStorage plus copied text; index.html, MOTION.md and README are never updated, and no decision has been applied (motion.html 501, 543; README "index.html is not changed by it").
3. Nothing for a developer to consume. Export is one plain-text paragraph per group; no JSON, no platform code, no Android spring values (motion.html `decisionsText`, DEVNOTES: "has to be matched by eye in a native sample").
4. Coverage is half and shrinking. 26 of 46 product animations have a scenario; Live updates and the new Odds tab have none (MOTION.md line 4: "сценариев в галерее у них пока нет").
5. The spec is not in the tool. Trigger, phases and tokens per animation are only in a Russian markdown file; the gallery shows a 1-3 line "Today" note per group (TASKS.md A2 "Готово, когда" asked for the composition per animation and token sliders; the page evolved away from that).
6. Everything is maintained by hand in parallel copies: SCN scenarios, FOCUS selectors, preset CSS selector lists (e.g. PRESS at motion.html 384 does not include the newer `.ox-step button`, `.fx-team`, `.lu-new`; the state group misses `.lu-seg button`), wrapped function names. Each prototype change silently makes previews less true.
7. Token discipline is declared but not held: 30 off-token product numbers, three curves for colour changes, 7 entrance distances, 3 press scales, no tokens for delay / stagger / hold / distance (MOTION.md sections "Где похожее сделано по-разному" and "Числа мимо токенов").
8. The tool itself produces off-scale numbers: XS-XL multiplies durations by .5-2.2 (motion.html 513), so "a decision" is usually a brand-new value.
9. Not testable where motion is felt: desktop only, simulated press, no drag, no real device, no haptics (motion.html body min-width 1100px; `G.press`).
10. No timeline view: multi-phase sequences cannot be seen as phases, scrubbed or stepped; only 3 speeds and replay.
11. Reduced motion is a kill-switch, not a design: one global rule plus "previews do not move" banner; no per-animation alternative and no way to preview it (index.html 614; motion.html 203).
12. Documentation disagrees with itself: README says M01-M44 and "two curves, five durations", omits --exit and --chg-*, and still mentions `releaseHeight()` which is gone from the code; CSS comment repeats the "two curves and five durations" claim two lines above --exit.

7. Already good, worth keeping
- The real prototype is the stage: animations play in the true screen and state, not in isolated demos.
- The embed hook design: one clock (`MOTION.rate`) that slows timers, CSS and Web Animations together, `MOTION.clear`, `MOTION.tokens` that re-syncs the JS mirror. This is the right foundation for a timeline or token editor.
- Deterministic scenarios: setup puts a state instantly (freeze class), live prices paused, same numbers every run.
- Side-by-side compare, close-up on the element, loop, slow motion, keyboard walking.
- Springs done properly: SwiftUI-style duration + bounce, simulated as a real damped spring, with opacity never overshooting.
- Decision model: group preset + per-animation exception + written "why" + explicit scope note saying what a preset does not touch.
- Shareable link with validation of saved data (out-of-range or unknown values are dropped).
- The inventory's honesty: stable IDs M01..., interruption behaviour per animation, the list of 15 inconsistencies and 30 off-token numbers. That list is effectively the backlog for a v2 token set.
- The core scale itself (five durations by role, travel curve vs in-place curve) and its high adoption in the code.
- The "one pattern everywhere" rules already written in README (price change, sheets, card removal): these are the first real motion principles of the product.

Files
- public/motion.html
- notes/MOTION.md
- README.md (lines 81-105)
- public/index.html (tokens 272-282 and 423; helpers 1871-1881; CHG_T 2049; reduced motion 614 and 1048; gallery hooks 2818-2842)

---

## 4. Research: motion in design systems

# Motion systems research: how mature design systems structure motion

Verification key: [V] = read in the primary source this session. [S] = search snippet only, page not readable. [U] = not verified. Nothing in the repo was changed; I only read notes/MOTION.md for context.

Could not read: m3.material.io (JS-rendered; Material values come from Google's Android docs and Compose source instead), the Polaris motion guidance page (now redirects), LDS 2 kinetics, and all Medium posts (403).

## 1. Token structures that recur

**Duration scales** (5-16 steps, named by size or speed, never by component)
- Material 3 [V]: 16 steps. short1-4 = 50/100/150/200 ms, medium1-4 = 250/300/350/400, long1-4 = 450/500/550/600, extraLong1-4 = 700/800/900/1000.
- Carbon [V]: 6 steps with a usage each. fast-01 70 ms (buttons, toggles), fast-02 110 (fades), moderate-01 150 (small expansion), moderate-02 240 (expansion, toasts), slow-01 400 (large expansion), slow-02 700 (background dimming).
- Fluent [V, repo]: 8 steps. ultraFast 50, faster 100, fast 150, normal 200, gentle 250, slow 300, slower 400, ultraSlow 500.
- Atlassian [V]: 8 steps. instant 0, xxshort 50, xshort 100, short 150, medium 200, long 250, xlong 400, xxlong 600.
- Polaris tokens [V, repo]: motion-duration-0/50/100/.../500, plus 5000.
- Swiggy [V]: no fixed scale. A formula: t = (object area / viewport area) x 200 + 100 ms, range 100-300 ms on mobile, with multipliers (ease-in x0.8, linear x0.7, expressive +10%).

**Easing families** (three roles: enter = decelerate, exit = accelerate, move in place = standard; often in two intensities)
- Material 3 [V]: standard (0.2,0,0,1), standard-decelerate (0,0,0,1), standard-accelerate (0.3,0,1,1), emphasized-decelerate (0.05,0.7,0.1,1), emphasized-accelerate (0.3,0,0.8,0.15), linear.
- Carbon [V]: 3 roles x 2 styles. Productive: standard (0.2,0,0.38,0.9), entrance (0,0,0.38,0.9), exit (0.2,0,1,0.9). Expressive: standard (0.4,0.14,0.3,1), entrance (0,0,0.3,1), exit (0.4,0.14,1,1).
- Fluent [V, repo]: accelerate, decelerate and easyEase, each in Max/Mid/Min (e.g. decelerateMid (0,0,0,1), easyEase (0.33,0,0.67,1)), plus linear.
- Atlassian [V]: "practical" vs "bold". out-bold (0,0.4,0,1) for entering, in-out-bold (0.4,0,0,1) for repositioning, in-practical (0.6,0,0.8,0.6) for exits, out-practical (0.4,1,0.6,1) for hovers and popups.
- Polaris tokens [V, repo]: ease, ease-in, ease-out (0.19,0.91,0.38,1), ease-in-out, linear.

**Springs** (the newer layer in both mobile platforms)
- Material 3 physics [V, Compose source]: 6 springs = 3 speeds (fast for small parts, default for partial-screen such as bottom sheets, slow for full-screen) x 2 kinds (spatial = position and size, may overshoot; effects = colour and opacity, never overshoots).
  - Standard scheme: spatial damping 0.9 with stiffness 1400/700/300 (fast/default/slow); effects damping 1.0 with stiffness 3800/1600/800.
  - Expressive scheme: spatial 0.6/800, 0.8/380, 0.8/200; effects identical to standard.
  - Standard is for utilitarian UI and recurring interactions; expressive for prominent, hero moments.
- Apple [V]: SwiftUI's default animation is a spring. `.spring()` = duration 0.5 s, bounce 0 (older API: response 0.5, dampingFraction 0.825). Two parameters only: perceptual duration and bounce.
  - WWDC23 guidance: bounce 0 is the general-purpose default; about 0.15 is barely bouncy; about 0.3 is noticeable; above 0.4 is too much for UI.
  - Presets .smooth / .snappy / .bouncy exist; their numeric values are not in the docs [U].
  - WWDC18: start at 100% damping; add bounce only when the gesture carried momentum (Music's Now Playing: 100% on tap, 80% on swipe).

**Distance, stagger, hold**
- Stagger: Carbon [V] uses 20 ms between items and keeps the whole sequence within 500 ms. Fluent [V] says short offsets, and skip stagger for very large groups.
- Distance and scale: Atlassian keyframe tokens [V] (fade in/out, scale 95-100%); Polaris keyframes [V] (appear-above/below offset by a spacing token, bounce, pulse, spin). None of the systems read publishes a full distance scale.
- Hold/dwell times (how long a toast or a change indicator stays): no system read tokenises these.

## 2. How the layers are separated

- **Primitives**: raw durations, curves, springs (all systems).
- **Semantic roles**:
  - Carbon: `motion(entrance, productive)`, i.e. role x style.
  - Material: spatial vs effects, by speed.
  - Atlassian: enter = bold and slower; exit = practical and 50-100 ms shorter.
- **Patterns**:
  - Material transition patterns [V, Android docs]: container transform, shared axis X/Y/Z, fade through, fade. The default durations listed on that page contradict its own token table, so treat those numbers as [U].
  - Fluent transition types [V]: enter/exit, elevation, top-level (quick fade), container transform.
  - Salesforce micro-patterns [V]: border swirl, spotlight, ripple, directional underline.
- **Component specs**:
  - Atlassian semantic tokens [V] bundle duration + easing + properties: `motion.modal.enter`, `motion.flag.exit`, `motion.popup.enter.top`. Rule: use semantic tokens before base ones.
  - Salesforce keeps component motion in the component blueprints, not in the motion guide [V].
- Smashing/Val Head [V]: keep the named-effects library as small as possible; it is the costliest layer to maintain.

## 3. Principles (3-4 each, never more)

- Carbon [V]: purposeful, responsive, meticulous, unobtrusive. Plus the productive/expressive split.
- Fluent 2 [V]: functional, natural, consistent, appealing.
- Atlassian [V]: human, clarity, accessible, performant.
- Salesforce Kinetics [V]: functional, structural, expressive. Personality: nimble, sensible, considerate, charismatic.
- Firefox [V]: quick, informative, whimsical.
- Apple HIG [V], as rules: add motion purposefully; make motion optional; prefer system motion; feedback follows the gesture; keep it brief; avoid motion on frequent interactions; let people cancel motion.
- Apple WWDC18 [V]: response, redirection/interruption, spatial consistency, hinting, behaviour over animation.
- Material 3 principles: [U].
- Shared across them: every system has one "serves a purpose" principle and one "fast, does not block" principle. Most have a two-speed idea: quiet for frequent actions, expressive for rare moments.

## 4. How one animation is documented for developers

- Atlassian [V]: a one-line spec "Component, easing, duration" ("Flag entrance, easing out bold, 250 ms") or a single semantic token. Each concept has a live demo with Play, plus do/don't.
- Swiggy [V], the fullest format found:
  - per component: one page with the interaction, text specs and tokens;
  - for multi-element motion: a sequencing graph with rows = elements and columns = property, duration, easing, offset, delay.
  - Per-component specs alone did not scale to simultaneous motion, which is why they added the graph.
- Carbon [V]: code API, not a document. Developers call `motion(standard, productive)` and `$duration-fast-01`.
- Salesforce [V, Trailhead]: a motion brief (role and value of the animation, which existing patterns it reuses) and storyboards before production.
- Firefox [V]: bypassed specs. After Effects to JSON to SVG sprite to CSS, because hand re-creation was tedious and lost nuance.
- Generic checklist [S]: duration, easing, delay, animated property, start and end values, trigger, reduced-motion behaviour. Numbers, never adjectives.
- Gap: no source read specifies interruption behaviour as a spec field. Apple treats it as mandatory behaviour.

## 5. Governance: how teams started

- Firefox [V]: two people named themselves the motion team, then
  1. audited by screen-recording every animation on each platform;
  2. found the top problems were consistency and perceived performance;
  3. defined one curve and three principles;
  4. got buy-in at a team week;
  5. animated components once visuals were near final.
- Swiggy [V]: audit first. It separated repeated patterns (systematise) from one-offs (leave out). It found no easing or duration rules, "what looked right", and weak choreography. They kept loaders and celebrations outside the system as a separate Lottie library.
- Smashing/Val Head [V]: interview the people who will use the system first; do not copy another brand's guidelines; ship v1 and iterate. Photon ran on one duration and one curve.
- Salesforce [V]: three implementation tiers (CSS first, then JS, then Lottie); teams are not expected to create motion from scratch.
- What failed or hurt:
  - hand re-implementation loses nuance (Firefox);
  - per-component specs break on choreography (Swiggy);
  - pixel-fixing after handoff took hours (Swiggy);
  - Atlassian's semantic motion tokens are still Early Access behind a flag, and Figma cannot carry motion variables, so complex motion goes through prototypes [V].
- Gojek and Firefly write-ups: [S] only.

## 6. Accessibility and performance

- WCAG 2.3.3 [V] (AAA): motion triggered by interaction can be disabled unless essential. Colour and opacity changes are not "motion animation". 2.2.2 covers auto-started motion.
- Apple, when Reduce Motion is on [V]: tighten springs to remove bounce; replace x/y/z transitions with fades; avoid z-depth animation and animating blurs; reduce automatic and repetitive motion. Never make motion the only carrier of information; pair it with haptics.
- Atlassian [V]: with reduced motion, motion is off and instant; the UI must stay fully usable with all motion disabled; avoid flashing and large sweeps.
- Fluent [V]: offer a no-motion setting; use live regions for information conveyed by animation.
- Android [S]: "Remove animations" is read through the animator duration scale. Primary doc not found.
- Budgets:
  - respond to input within 100 ms; about 10 ms of work per frame at 60 fps (web.dev RAIL [V]);
  - Android [V]: 16 ms per frame at 60 fps, 11 ms at 90, 8 ms at 120; frozen frame above 700 ms; animate translation, rotation and alpha, not layout properties;
  - Apple hitches [V]: good is 10 ms/s or less, warning up to 25, critical up to 50;
  - Carbon [V]: micro-interactions 90-120 ms;
  - Atlassian [V]: high-frequency motion under 150 ms; animate one or two properties, transform and opacity only.

## 7. Lessons most transferable to two designers laying the first stone

1. **The audit is the first stone, and it already exists.** Firefox and Swiggy both started there. The M01-M48 inventory with its "done differently" list is exactly that artefact. The next step is collapsing duplicates, not adding more.
2. **Keep the primitive set small and add roles.** Five durations and three curves is already more than Photon had. What is missing compared with every system above is the semantic layer: enter / exit / move / feedback, each mapped to one duration and one curve, so colour changes stop having three different curves.
3. **Tokenise what the inventory shows drifting**: entry distance (4-30 px today), stagger step (32 vs 45 ms), press scale (.97/.98/.985), and hold times. Hold times matter most for live data and no public system covers them, so this is original work.
4. **Adopt the two-speed rule.** Quiet and under about 150 ms for high-frequency actions (odds taps, live price changes); expressive only for rare moments (bet placed, goal).
5. **Name patterns, not animations.** A handful (sheet, value change, item add/remove, height change, page push, toast) covers most of the inventory. Keep one-offs and celebrations outside the system.
6. **Use one spec format with a fixed field list**: trigger, element, property, from/to, duration token, easing token, delay, interruption, reduced-motion variant. Add a sequencing table for multi-element cases. The inventory columns are already close.
7. **Decide the platform question before going deeper on values.** If production is native, both platforms now default to springs. Curve and duration tokens port everywhere; spring tokens do not map 1:1 to CSS (my inference, not from a source). Designing roles first keeps the system valid either way.
8. **Three or four principles, written as tests** a proposal can fail, and a live gallery as the source of truth, as Atlassian and Carbon do with demos.

## Sources

- Material (Android docs): https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- Material (Compose source): https://github.com/androidx/androidx/blob/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens/StandardMotionTokens.kt and .../tokens/ExpressiveMotionTokens.kt and .../MotionScheme.kt
- Material site (not readable): https://m3.material.io/styles/motion/overview/how-it-works
- Apple HIG Motion: https://developer.apple.com/design/human-interface-guidelines/motion
- Apple HIG Accessibility: https://developer.apple.com/design/human-interface-guidelines/accessibility
- SwiftUI spring: https://developer.apple.com/documentation/swiftui/animation/spring(duration:bounce:blendduration:)
- WWDC23 Animate with springs: https://developer.apple.com/videos/play/wwdc2023/10158/
- WWDC18 Designing Fluid Interfaces: https://developer.apple.com/videos/play/wwdc2018/803/
- Apple hitches: https://developer.apple.com/documentation/xcode/understanding-hitches-in-your-app
- Carbon: https://carbondesignsystem.com/elements/motion/overview/ , /choreography/ , /code/
- Fluent 2: https://fluent2.microsoft.design/motion
- Fluent tokens: https://github.com/microsoft/fluentui/blob/master/packages/tokens/src/global/durations.ts and curves.ts
- Atlassian: https://atlassian.design/foundations/motion and https://atlassian.design/foundations/motion/applying-motion
- Polaris tokens: https://github.com/Shopify/polaris/blob/main/polaris-tokens/src/themes/base/motion.ts
- Salesforce Kinetics: https://v1.lightningdesignsystem.com/kinetics/overview/
- Salesforce Trailhead: https://trailhead.salesforce.com/content/learn/modules/motion-pattern-creation/understand-the-salesforce-kinetics-system-design-process
- Salesforce Medium post [S]: https://medium.com/salesforce-ux/what-you-need-to-know-about-the-new-salesforce-kinetics-system-ce10e9ae66a9
- Firefox motion team: https://blog.mozilla.org/ux/2018/06/firefox-has-a-motion-team-yes-we-do/
- Swiggy motion design system: https://contra.com/p/WcRlLgZF-motion-design-system-at-swiggy
- Smashing, Including Animation In Your Design System: https://www.smashingmagazine.com/2019/02/animation-design-system/
- IBM motion specs [S]: https://medium.com/design-ibm/working-together-ux-motion-specs-for-design-and-development-249b12d60909
- Gojek [S]: https://blog.gojek.io/setting-the-superapp-world-in-motion
- Firefly [S]: https://medium.com/firefly-design/how-we-developed-our-motion-design-guidelines-2a216beb9b76
- WCAG 2.3.3: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- web.dev RAIL: https://web.dev/articles/rail
- Android rendering: https://developer.android.com/topic/performance/vitals/render
- Android reduced motion [S]: https://dev.to/eevajonnapanula/android-animations-and-reduced-motion-2em2

---

## 5. Research: tools and interface patterns for motion handoff

MOTION TOOL RESEARCH: tools, interface patterns, handoff complaints, what to build

Scope notes
- Read-only: nothing in the repo was changed, no server started, Figma not touched. Web queries were generic.
- I looked at public/motion.html and notes/MOTION.md only by reading the files; I did not run the page.
- Already in motion.html (from its code and comments): presets per group, Amount/Duration variants, Advanced sliders, spring presets by duration + bounce, Compare with the original (two framed prototypes), close-up, slow motion, loop, Copy decisions (text), Copy link (#d= hash), localStorage, a notice when Reduce motion is on.
- Most sources on tools are vendor pages; treat their claims as vendor-stated. Unverified items are listed at the end.

1 + 2. Feature catalogue (what tools do / serves / effort in plain HTML-CSS-JS, no build / best example)

Play / replay
- Tools: every tool; Chrome DevTools Animations panel captures animation groups and replays them; Storybook Interactions panel replays a scripted flow.
- Serves: both. Effort: easy (exists). Best: Chrome DevTools Animations panel.

Slow motion and scrubbing
- Tools: DevTools Animations (speed control, draggable playhead); Figma Motion timeline scrub; Android Studio Animation Preview for Compose (play, pause, scrub, speed, freeze one animation); Storybook step-through (pause, rewind, step).
- Serves: both; developers most (they verify against it).
- Effort: slow motion easy to medium (document.getAnimations() + playbackRate covers CSS transitions/animations; chains on JS timers need a slowed clock, which motion.html already has). True scrubbing: hard for a real prototype, because getAnimations() returns only animations currently in effect and timer chains cannot be rewound. Fixed speeds plus replay give about 90% of the value.
- Best: Chrome DevTools Animations panel.

Side-by-side A/B compare
- Tools: Easing Wizard (compare against linear); Linear Easing Generator; motion.html already does two framed prototypes.
- Serves: designers and stakeholders. Effort: medium (exists). Cheap addition: A/B flip on one phone, which shows small differences better than two phones.
- Best: no listed tool does this on a real product screen; the current page is already ahead here.

Live parameter tuning
- Tools: Tweakpane and lil-gui (vanilla, framework-neutral), Leva (React only), dat.GUI (unmaintained), DialKit (React/Solid/Svelte/Vue; spring editor with two modes: duration + bounce, or stiffness/damping/mass), Storybook Controls, Motion's editor and VS Code extension.
- Serves: designers; developers when values are copyable. Effort: easy (exists).
- Best: DialKit for the spring control pattern; Tweakpane if a ready panel is wanted without a framework.

Curve and spring graphs
- Tools: Linear Easing Generator (spring, bounce, elastic presets to CSS linear()), Easing Wizard (bezier, spring, bounce, wiggle, overshoot), Motion Studio bezier editor, EaseMaster, Figma Motion easing curves, cubic-bezier editors.
- Serves: both (shared vocabulary). Effort: easy for cubic-bezier (one SVG path); easy to medium for springs (closed-form damped spring, sampled).
- Best: Linear Easing Generator for springs; Easing Wizard for breadth.

Onion-skin / ghost frames
- Tools: found only in character and 3D tools (Spine ghosting, Blender, Cinema 4D). I found no UI motion tool from the requested list that offers it.
- Serves: designers, marginally. Effort: medium to hard on real DOM. Best: Spine. Low value for UI transitions.

State-to-state transition matrix
- Tools: Rive state machine (states, transitions, boolean/number/trigger inputs; a graph, not a matrix); dotLottie state machines (since late 2025 per one comparison); Storybook (one story per state); Play's State Manager.
- Serves: both; developers and QA most. Effort: medium: a from/to grid where each cell runs a scenario; the prototype's "Prototype states" panel is the base.
- Best: Rive state machine editor.

Sequence / choreography timeline
- Tools: Figma Motion timeline (keyframes for position, scale, rotation, opacity; read-only timeline in Dev Mode); DevTools Animations (auto-captured lanes with delay and duration); Theatre.js sequence editor; the hand-made "animation graph" from a travel-company design team (element, property, start, end, curve).
- Serves: both; this is the artefact developers ask for.
- Effort: medium as a read-only bar chart drawn from data (MOTION.md already holds phases, delays, curves); hard if editable or auto-captured.
- Best: DevTools Animations (read-only), Figma Motion (authoring).

Copy-as-code and export
- Tools: Figma Dev Mode Motion tab (copy as CSS, React, JSON; the blog also names motion.dev); Motion editor (Motion code, CSS, URL); Theatre.js (state JSON); Play (SwiftUI to Xcode); Inspector Spacetime (After Effects script that generates motion specs for engineers, not code); LottieFiles motion tokens.
- Serves: developers. Effort: easy for tokens as text templates (CSS variables, JSON, Swift and Kotlin constants); medium to get spring conversion right.
- Best: Figma Dev Mode Motion tab. It outputs web formats only; no native code was mentioned.

Sharing a tuned variant by link
- Tools: Motion editor outputs a URL; Play shares via App Clips; motion.html has Copy link.
- Serves: both. Effort: easy (exists). Missing piece: a link to one exact animation, state and speed, not only the set of decisions.
- Best: Motion editor.

Recording to video / GIF
- Tools: Figma Motion (MP4, GIF, SVG, WEBM), Jitter (GIF, Lottie, video up to 4K), Principle (MP4/GIF).
- Serves: designers and stakeholders. Effort: medium to hard and fragile: getDisplayMedia + MediaRecorder needs a permission prompt each time and records the whole tab; cropping to an element (Region Capture) is Chromium desktop only; GIF needs an encoder.
- Best: Jitter / Figma Motion. For this tool: OS screen recording.

Reduced-motion preview
- Tools: Chrome DevTools Rendering tab emulation (from prior knowledge; not confirmed by this session's searches); OS setting.
- Serves: both, plus QA and accessibility. Effort: easy to medium: a page cannot switch the media query, so the prototype must also honour a class or URL flag (a small change in index.html).
- Best: Chrome DevTools.

Device and frame-rate simulation
- Tools: DevTools CPU throttling (4x, 6x, 20x) and Frame Rendering Stats; Android Studio Animation Preview; real devices. One QA article notes motion that feels premium at 120 Hz visibly degrades at 60 Hz.
- Serves: developers. Effort: device sizes easy (exists); frame-rate or slow-device simulation in a web page is medium to hard and misleading for a native app.
- Best: Chrome DevTools; real phones for the truth.

3. What people complain about (real sources)

Developers
- A video or GIF plus "make it look like this": they pick the clip apart to guess what changes at what rate; one author spent six hours eyeballing a GIF (A List Apart).
- Missing numbers: duration, easing, delay, exact start and end values, trigger; "something subtle" means guessing (agency handoff guide, InVision, GetYourGuide).
- After Effects exports nothing usable for timing (Stack Overflow answer); Lottie arrives late or in the wrong format; Lottie supports only part of After Effects and can differ between iOS and Android (LottieFiles forum, Airbnb guidelines).
- Motion seems to cost too much for the payoff, so it is the first thing cut (GetYourGuide, A List Apart).
- Spring values do not map between tools and platforms: Figma to Android needed extra tweaking (Figma forum); Compose takes dampingRatio + stiffness, SwiftUI takes duration + bounce.
- Even with Figma Motion (launched 24 June 2026, open beta) a November 2026 forum post says developers cannot click a layer and see its exact motion values; staff logged it as a feature request.
- Coded prototypes are poor documentation: only code-literate people can read them (A List Apart). This applies directly to a single HTML file.

Designers
- Loss of control: the shipped motion does not match and "feels off" (Anima survey of 400+ designers and developers; Hike playbook).
- Pacing and intent live in one person's head; static tools cannot express choreography (Figma-to-AE article, practitioner posts).
- Review turns into arguing whether it "looks close" (cross-platform motion spec article).
- No owner: values drift, guidelines sit in static docs and are re-interpreted at every handoff (LottieFiles Motion System page; vendor framing, but it matches the owner's situation).
- Recurring remedies: video for intent plus a graph for specifics; a small named set of curves and durations; exact from/to values; a shared vocabulary of patterns; a spec with trigger, elements, properties, timeline, interruptibility and a fallback for weak devices.

4. Most value for least effort (single HTML file embedding the real prototype)

1. Spec card per animation, drawn from data: trigger, elements, properties, from and to values, phases as bars on a time axis, curve, delay, interruption rule, reduced-motion behaviour. This means moving the MOTION.md inventory into one data object the page renders. It answers the top developer complaint.
2. Copy as code in several dialects from the same tokens: CSS variables, JSON tokens, Swift constants, Kotlin/Compose constants, with one spring definition (duration + bounce) converted per platform.
3. Deep link to one animation, state, tuned values and speed, so a ticket or chat message points at the exact thing. Extends the existing Copy link; also the low-noise answer to the "journal" worry.
4. Speed steps (1x, 0.5x, 0.25x, 0.1x), replay and loop with a live milliseconds readout, instead of a scrubber.
5. Curve and spring graph beside the sliders, current and tried curves overlaid.
6. A/B flip on one phone, alongside the existing side-by-side.
7. Reduced-motion switch inside the tool, plus the reduced-motion line in each spec card.
8. Token health panel: an automatic list of durations and curves outside the tokens, and a count of animations on tokens. It replaces the hand-kept "numbers outside tokens" table and gives the system a measurable state.
Optional ninth, cheap: a status per animation (draft, agreed, built on iOS, built on Android).

5. Attractive traps for a small team

- An editable keyframe timeline: that is Figma Motion, Theatre.js and Rive territory; the tool should show sequences, not author them.
- In-page video or GIF recording: permission prompts, whole-tab capture, Chromium-only cropping.
- Frame-rate and slow-device simulation in the browser: says little about a native app.
- Generating native code for whole animations: generated snippets are rarely production-usable; hand off values and rules.
- Rive or Lottie for interface transitions: they suit self-contained illustrated moments (a goal celebration, a mascot, a loader). One engineering article puts native animation at about 70% of the work and says not to use Lottie for element transitions.
- Springs without a decision: CSS cannot carry finger velocity into an interrupted spring; parameters differ per platform. Choose one definition and a conversion table first.
- Storybook now: needs a build step and real components, and the production stack is not confirmed. Shape the data so each animation can become a story later.
- Panel libraries: Leva is React-only, dat.GUI is unmaintained; Tweakpane or lil-gui from a CDN would break the offline build made by build.py.
- A comment system inside the tool: Figma Motion already pins comments to a moment in time; links into existing channels are enough.
- Onion-skin: looks impressive, adds little for UI.
- Two sources of truth: Figma Motion now has its own Dev Mode handoff. The owner should decide where motion values officially live (this tool's tokens or Figma motion variables).
- Too many knobs: a slider for each of the ~30 off-token numbers produces noise, not a system.

Unverified or weakly sourced
- Apple acquiring Play: one newsletter snippet only.
- Whether W3C design tokens (DTCG 2025.10) cover duration and cubicBezier types: two sources contradict each other.
- Spring conversion: stiffness = (2π / duration)² is cited from Apple's WWDC23 talk via notes; dampingRatio = 1 − bounce for Compose is my own derivation.
- Chrome DevTools reduced-motion emulation and the iOS Simulator "Slow Animations" option: from prior knowledge, not confirmed by this session's searches.
- Safari support for CSS linear(): one third-party page says 17.4+; not checked.
- Framer "share converted values for iOS, Android and Web": an old launch snippet only. Principle web sharing: sources conflict. Knapsack and Supernova motion documentation: nothing found. zeroheight: confirmed only that it embeds Lottie and has a "display animation" help article.
- Rive onion-skin: not found. Tweakpane size (~30 KB vs lil-gui ~5 KB): one blog post.
- Whether Figma Dev Mode shows motion values per layer: staff said yes, the user's follow-up was about static specs; unresolved.
- Motion Studio pricing and the DialKit copy button: not confirmed in detail.

Sources
- Figma Motion announcement: https://www.figma.com/blog/introducing-figma-motion/
- Figma help, hand off animations: https://help.figma.com/hc/en-us/articles/41296356954263
- Figma forum, motion values per layer: https://forum.figma.com/share-your-feedback-26/figma-motion-developers-can-t-inspect-animation-values-per-layer-which-makes-design-to-dev-handoff-difficult-59608
- Figma forum, spring duration: https://forum.figma.com/archive-21/how-does-spring-animation-duration-work-33227
- Chrome DevTools Animations panel: https://developer.chrome.com/docs/devtools/css/animations
- Chrome DevTools performance (CPU throttling): https://developer.chrome.com/docs/devtools/performance
- CSS linear() easing: https://developer.chrome.com/docs/css-ui/css-linear-easing-function
- Region Capture: https://developer.chrome.com/docs/web-platform/region-capture
- Screen recording pattern: https://web.dev/articles/media/screen-record
- MDN getAnimations(): https://developer.mozilla.org/docs/Web/API/Document/getAnimations
- Android Studio Animation Preview: https://developer.android.com/develop/ui/compose/tooling/animation-preview
- Compose animation customisation: https://developer.android.com/develop/ui/compose/animation/customize
- WWDC23 Animate with springs (notes): https://wwdcnotes.com/notes/wwdc23/10158
- Storybook interactions: https://storybook.js.org/docs/9/essentials/interactions
- Theatre.js with HTML/SVG: https://www.theatrejs.com/docs/latest/getting-started/with-html-svg
- Motion editor: https://motion.dev/edit
- Motion Studio: https://motion.dev/magazine/introducing-motion-studio
- DialKit: https://github.com/joshpuckett/dialkit
- Tweakpane docs: https://tweakpane.github.io/docs/v3/misc/
- lil-gui vs dat.gui: https://discourse.threejs.org/t/lib-why-changed-dat-gui-to-lil-gui/62124
- Rive state machines: https://rive.app/docs/runtimes/state-machines.md
- Rive inputs (Android): https://rive.app/docs/runtimes/android/inputs
- Rive as a Lottie alternative: https://rive.app/blog/rive-as-a-lottie-alternative
- dotLottie state machines: https://docs.lottiefiles.com/en/format/dotlottie/interactivity/state-machines
- LottieFiles motion tokens: https://docs.lottiefiles.com/en/integrations/after-effects/03_motion-tokens
- LottieFiles Motion System: https://lottiefiles.com/motion-system
- Lottie guidelines (Airbnb): https://airbnb.gitbook.io/lottie/after-effects/general-tips-and-guidelines
- LottieFiles forum, iOS issue: https://forum.lottiefiles.com/t/animation-issues-when-implemented-ios/4656
- Inspector Spacetime: https://google.github.io/inspectorspacetime
- Google Design on Sketch and After Effects: https://medium.com/google-design/d83b3e729c93
- Jitter: https://jitter.video/product/
- Play dev handoff: https://docs.createwithplay.com/en/articles/dev-handoff
- Principle review: https://www.viget.com/articles/designers-tooling-around-principle/
- ProtoPie vs Principle (competitor page): https://www.protopie.io/blog/protopie-vs-principle
- zeroheight display animation: https://zeroheight.com/help/article/display-animation/
- A List Apart, Communicating Animation: https://alistapart.com/article/communicating-animation
- Motion design handovers made easy: https://www.getyourguide.careers/posts/motion-design-handovers-made-easy
- Motion comps: https://valhead.com/2017/05/19/motion-comps-moving-beyond-static-design-deliverables/
- Stop leaving animation to the last minute: https://24ways.org/2017/stop-leaving-animation-to-the-last-minute/
- Cross-platform motion spec: https://xckevin.github.io/en/blog/motion-spec-design-to-code-collaboration/
- QA for complex animations: https://www.ramotion.com/blog/qa-for-complex-animations/
- Motion design documentation playbook: https://playbook2.hike.one/methods/design/motion-design/motion-design-documentation
- Designer pain points survey: https://www.animaapp.com/blog/industry/the-top-4-pain-points-ux-ui-designers-are-facing-2/
- Handoff mistakes: https://www.webstacks.com/blog/design-to-developer-handoff-mistakes
- InVision on animation coding: https://invisionapp.com/inside-design/animation-coding
- Flinto spring handoff: https://medium.com/flinto-software/handing-off-your-prototype-spring-options-c7f3eba11849
- Stack Overflow mirror, perfectly timed animations: https://kiwix.lema.org/stackoverflow.com_en_all_2023-11/questions/36026217/implementing-perfectly-timed-animations
- Spine ghosting: https://es.esotericsoftware.com/spine-ghosting.md

---

## 6. Research: mapping web motion values to native iOS / Android and token formats

# Web motion values to native: research report

Scope note: read-only. Nothing in the repository was changed. Files read: public/index.html (MOTION TOKENS block, lines 272-283; JS mirrors at 1872-1881), notes/MOTION.md, public/motion.html (spring presets, lines 359-372).

Verification legend: [V] = confirmed in a primary doc this session, [C] = my own calculation, [U] = unverified (from memory or secondary sources only).

## 1. Mapping

### 1a. Cubic-bezier + duration (example: `--m-std` 320 ms with `--ease` cubic-bezier(.2,.8,.2,1))

The four numbers and the duration port exactly on every platform. Only the units differ (seconds on Apple, milliseconds elsewhere).

- CSS: `transition: transform 320ms cubic-bezier(.2,.8,.2,1)`
- SwiftUI: `.timingCurve(0.2, 0.8, 0.2, 1, duration: 0.32)` [V]
- UIKit: `UIViewPropertyAnimator(duration: 0.32, controlPoint1: CGPoint(x: 0.2, y: 0.8), controlPoint2: CGPoint(x: 0.2, y: 1)) { ... }` [V: initializer exists; exact argument form U]
- Core Animation: `CAMediaTimingFunction(controlPoints: 0.2, 0.8, 0.2, 1)` plus `animation.duration = 0.32` [U]
- Jetpack Compose: `tween(durationMillis = 320, easing = CubicBezierEasing(0.2f, 0.8f, 0.2f, 1f))` [V]
- Android Views: `PathInterpolator(0.2f, 0.8f, 0.2f, 1f)` plus `setDuration(320)` (API 21+) [V]
- MotionLayout: `motion:duration="320"` on `<Transition>` [V]; `motion:motionInterpolator="cubic(0.2,0.8,0.2,1)"` [U]. The Android docs now open with "Try the Compose way", so treat MotionLayout as legacy for new work.
- Material Components (Views): theme attributes `motionDurationMedium2` / `motionEasingStandardInterpolator` [V]
- React Native Reanimated: `withTiming(v, { duration: 320, easing: Easing.bezier(0.2, 0.8, 0.2, 1) })` [V]
- Flutter: `Cubic(0.2, 0.8, 0.2, 1)` with `Duration(milliseconds: 320)` [V]

Two traps:
- CSS keywords are not native keywords. `ease`, `ease-in`, `ease-out` and "no curve" (used across most colour changes in MOTION.md) must be exported as four numbers. Native defaults are different: SwiftUI and Compose default to springs [V]; Reanimated defaults to 300 ms with `Easing.inOut(Easing.quad)` [V].
- Curves with y outside 0..1 (overshoot) are legal in CSS and in the token spec [V]; behaviour on each native API is [U]. None of the three product curves overshoot.

### 1b. Spring parameter conversions

Three vocabularies describe the same spring:
- Apple: `duration` (perceptual) + `bounce`, or `response` + `dampingFraction`
- Physics: `mass`, `stiffness`, `damping`
- Android: `stiffness` + `dampingRatio`

Formulas (mass = 1):
- stiffness = (2π / duration)² [V, Apple WWDC23]
- damping = 4π × (1 − bounce) / duration, for bounce ≥ 0 [C, checked against Apple's own example: duration 0.5, bounce 0.3 gives 157.9 and 17.6 [V]]
- dampingRatio (= dampingFraction) = 1 − bounce, for bounce ≥ 0 [C, consistent with Apple's inverse example]
- response = duration [U: Apple calls both "approximate duration"; treat as equal]
- dampingRatio = damping / (2 × √(stiffness × mass)) [V, Flutter docs state c = ζ·2·√(m·k)]
- Back: duration = 2π / √(stiffness / mass); bounce = 1 − dampingRatio
- Negative bounce (overdamped): the formula printed in Apple's session is typeset ambiguously [U]. Recommendation: do not allow negative bounce in tokens.

Per-platform call for a spring token `duration 0.5 s, bounce 0.3`:
- SwiftUI (iOS 17+): `.spring(duration: 0.5, bounce: 0.3)`; older: `.spring(response: 0.5, dampingFraction: 0.7)` [V]
- UIKit (iOS 17+): `UIView.animate(springDuration: 0.5, bounce: 0.3) { ... }` [U: exact label; the session shows a duration+bounce form]; `UISpringTimingParameters(duration: 0.5, bounce: 0.3)` [V] or `UISpringTimingParameters(mass: 1, stiffness: 157.9, damping: 17.6, initialVelocity: .zero)` [V]
- Core Animation: `CASpringAnimation(perceptualDuration: 0.5, bounce: 0.3)` [V, shown in session]
- Compose: `spring(dampingRatio = 0.7f, stiffness = 157.9f)` [V for API; mass is not exposed, mass = 1 assumed U]
- Reanimated: `withSpring(v, { mass: 1, stiffness: 157.9, damping: 17.6 })`. Always pass `mass: 1`: the default mass is 4, stiffness 900, damping 120 [V]. Its own `duration`/`dampingRatio` form says "actual duration is 1.5× this value" [V].
- Flutter: `SpringDescription.withDurationAndBounce(duration: Duration(milliseconds: 500), bounce: 0.3)` [V exists; formula U] or `SpringDescription(mass: 1, stiffness: 157.9, damping: 17.6)` [V]
- CSS: no spring. Sample the curve into `linear(...)` (Baseline since Dec 2023) [V]. motion.html already does this.

Reference points for orientation:
- SwiftUI presets: `.snappy` = duration 0.5, bounce 0.15 [V]; `.smooth` = no bounce, `.bouncy` = higher bounce [V]; their exact numbers [U].
- Compose stiffness constants: High 10000, Medium 1500 (default), MediumLow 400, Low 200, VeryLow 50; damping ratios 0.2 / 0.5 / 0.75 / 1 [V]. In Apple terms these are perceptual durations of 0.06 / 0.16 / 0.31 / 0.44 / 0.89 s [C].
- Material spring tokens (damping, stiffness): fast spatial 0.9/1400, fast effects 1/3800, default spatial 0.9/700, default effects 1/1600, slow spatial 0.9/300, slow effects 1/800 [V].

### 1c. What the product's three curves are in spring terms [C]

Best fit by smallest maximum deviation, coarse grid:
- `--soft` at 500 ms: close to a spring with damping ratio 0.9-1.0 and stiffness 400-484, deviation 3-4% of the travel. That is `.spring(duration: 0.3, bounce: 0)` on iOS and `spring(1f, 400f)` (= `StiffnessMediumLow`) on Android. Note the 0.3: a no-bounce spring visually settles at about 1.5× its perceptual duration [C], so "500 ms sheet" in CSS is "0.3 s spring" in Apple's vocabulary. This naming gap is the single most likely source of wrong hand-offs.
- `--ease` at 320 ms: no good spring match (7% off when critically damped). Keep it as a bezier everywhere.
- `--exit` (symmetric in-out): springs cannot do this shape (9-13% off). Keep it as a bezier.

## 2. What does not translate one to one, and what the spec must say instead

- Springs vs beziers. A spring has no fixed end; it reacts to starting velocity and keeps that velocity when retargeted [V, Apple and Android docs both state this]. A bezier is a fixed recording. Spec must say: which of the two, and for springs give duration + bounce (never a bezier "that looks like it").
- "Duration" has three meanings: bezier end time, spring perceptual duration, spring settling time. Spec must name which.
- Interruption. CSS transitions reverse from the current point; JS entrances in the prototype restart from the start (MOTION.md "Прерывание"). Native springs retarget with velocity; tweens restart or jump. Spec must say per animation: reverse from current, restart, queue or ignore.
- Gesture-driven motion (M33 sheet drag). The prototype's "duration from finger speed, 220-500 ms" is a web workaround. Native equivalent: hand the release velocity to a spring. Spec must give: what follows the finger 1:1, rubber-band rule, dismiss thresholds (fraction of height, velocity in pt/s or dp/s), the release spring, and what happens when grabbed mid-flight.
- Height and layout changes (M25, M28-M30, M45, M47). On the web this is animating `height`, which is the expensive path [V]. Native does not animate "height 440 ms"; it animates a state change and the layout follows (SwiftUI `withAnimation`, Compose `animateContentSize` / `AnimatedVisibility`, list item animations) [U for API names]. Spec must say: what grows or shrinks, which edge is anchored, what neighbours do, whether content is clipped, how content inside appears.
- Shared-element transitions. Not present in the prototype (pages slide). Native has them with their own constraints: Compose `SharedTransitionLayout` with matching keys, no interop with Views-based dialogs or bottom sheets [V]; iOS 18 zoom navigation transition, with reported quirks [U, forum reports]. Spec must name source, destination, what is shared (the element or only its bounds), and a fallback.
- System-owned transitions. Page push, sheets and back gestures are provided by the OS on native [U, general practice]. Spec must mark each as "system default" or "custom, because ...". Custom versions of M32/M38 will fight back-swipe on iOS and predictive back on Android.
- Keyframe animations (`deny`, `nope`, `bump`, `livedot`). Portable only as a table: time, value, easing per segment. Compose `keyframes` supports per-segment easing [V]; SwiftUI keyframe APIs need iOS 17 [U].
- Holds and timers (2000 / 5000 ms arrows, toast times). These are not motion and must be a separate token group. Android's animation scale does not shorten them [U].
- Stagger. Portable as "step ms, max steps, order", but lazy lists only know about visible items; say so.
- Number changes. iOS and Compose have native idioms for rolling numbers [U]; the spec should state intent (new value enters from below when the price rises, 5 px travel) rather than the web technique.

## 3. Proposed minimal token schema (W3C Design Tokens Format 2025.10)

What the spec gives [V]: `duration` = `{ "value": n, "unit": "ms" | "s" }`; `cubicBezier` = four numbers, x within 0..1; composite `transition` = `duration`, `delay`, `timingFunction`; aliases `{group.token}`; `$description`, `$deprecated`, `$extensions` (vendor key, reverse-domain recommended). There is no spring type [V]. So a spring is stored as two standard tokens (duration + number) and the derived physics goes into `$extensions`.

```json
{
  "motion": {
    "duration": {
      "$type": "duration",
      "press":  { "$value": { "value": 120, "unit": "ms" }, "$description": "Press feedback" },
      "quick":  { "$value": { "value": 200, "unit": "ms" }, "$description": "Colour, opacity, small state changes" },
      "std":    { "$value": { "value": 320, "unit": "ms" }, "$description": "An element enters, a text swaps" },
      "layout": { "$value": { "value": 440, "unit": "ms" }, "$description": "Heights and pages" },
      "sheet":  { "$value": { "value": 500, "unit": "ms" }, "$description": "Sheets, bar, toast, overlay" }
    },
    "easing": {
      "$type": "cubicBezier",
      "ease": { "$value": [0.2, 0.8, 0.2, 1],  "$description": "State changes in place" },
      "soft": { "$value": [0.32, 0.72, 0, 1],  "$description": "Travel: quick start, long landing" },
      "exit": { "$value": [0.4, 0, 0.6, 1],    "$description": "Things that hide behind something" }
    },
    "spring": {
      "sheet": {
        "$description": "Sheet and bar travel. Web plays the fallback curve.",
        "duration": { "$type": "duration", "$value": { "value": 300, "unit": "ms" } },
        "bounce":   { "$type": "number",   "$value": 0 },
        "$extensions": {
          "com.example.motion": {
            "kind": "spring",
            "mass": 1, "stiffness": 438.6, "dampingRatio": 1, "damping": 41.9,
            "webFallback": "{motion.transition.sheet}"
          }
        }
      }
    },
    "transition": {
      "$type": "transition",
      "sheet": {
        "$value": { "duration": "{motion.duration.sheet}", "delay": { "value": 0, "unit": "ms" }, "timingFunction": "{motion.easing.soft}" },
        "$extensions": { "com.example.motion": { "reducedMotion": "fade", "nativePreferred": "{motion.spring.sheet}" } }
      }
    }
  }
}
```

Notes on the example: the spring numbers are illustrative (duration 300 ms, bounce 0, from the fit in 1c) and must be confirmed by eye on a device. Group-level `$extensions` is in the spec's group properties [U for every tool honouring it]. Odds-change timings (`--chg-*`) belong in a separate `motion.hold` group.

How each platform consumes it:
- Web: Style Dictionary built-ins `time/seconds`, `cubicBezier/css`, `transition/css/shorthand` produce CSS variables [V]. Springs: generate `linear()` or use the fallback.
- iOS, Android, Flutter: Style Dictionary has no built-in motion transform for these platforms [V]. One small custom format per platform is needed, emitting: Swift `TimeInterval` constants, `Animation.timingCurve(...)`, `Spring(duration:bounce:)`; Kotlin `Int` millis, `CubicBezierEasing(...)`, `spring(dampingRatio, stiffness)`; Dart `Duration`, `Cubic`, `SpringDescription`.
- React Native: plain TS object; remember `mass: 1`.
- Material apps: can map to Material's own duration/easing/spring theme attributes instead [V].

## 4. Per-animation spec fields

Identity
- ID (M-number), name, group, status (proposed / approved / shipped per platform)
- Purpose in one line: feedback, state change, hierarchy, attention

Trigger and scope
- Trigger (tap, live data event, gesture, timer), and which screens
- Target element(s), named as in the design file
- Preconditions and neighbouring states

Motion
- Properties animated, each with from and to in pt/dp (not px), and transform origin
- Per property: token for duration, token for easing or spring, delay
- Phases in order (enter, hold, exit) with their own timing; enter and exit listed separately
- Stagger: step, max steps, order
- Keyframe table where applicable: time %, value, easing per segment
- Hold times, marked as "pause, not motion"

Behaviour
- Interruption rule: reverse from current, retarget with velocity, restart, queue, ignore
- Repeat rule when triggered again while running
- Gesture rules: 1:1 tracking, thresholds, velocity units, release animation
- Layout effect: what resizes, anchor edge, neighbours, clipping
- Z-order and what is covered during motion
- Final state and cleanup (what is removed from the tree and when)

Platform
- System default or custom, per platform, with the reason if custom
- Native mapping line for iOS and Android (the exact call from section 1)
- Minimum OS if an API requires it
- Haptic or sound paired with it

Accessibility and quality
- Reduced-motion fallback (section 5 vocabulary)
- Performance class: transform/opacity only, or layout-affecting
- Frequency: how often it can fire (live prices), and coalescing rule
- Reference: link to the live scenario in the gallery plus a slow-motion capture
- Acceptance check: 3-5 observable statements a reviewer can tick

## 5. Reduced motion

Platform standards
- Web: `prefers-reduced-motion: reduce`. WCAG 2.3.3 (AAA): motion triggered by interaction can be disabled unless essential; colour and opacity changes are not "motion animation" [V].
- iOS: `UIAccessibility.isReduceMotionEnabled` + change notification; SwiftUI `@Environment(\.accessibilityReduceMotion)`; `prefersCrossFadeTransitions` (iOS 14+) [V via Apple docs summary and WWDC notes].
- Apple's App Store criteria [V]: when Reduce Motion is on, change or disable parallax and depth, multi-axis and multi-speed motion, spinning, vortex effects, auto-advancing or ongoing motion. Decorative motion: stop. Meaningful motion: do not delete it, replace with dissolve, highlight fade or colour shift. Do not strip all animation.
- Android: "Remove animations" sets the animator duration scale to 0 [U for the setting-to-scale link; secondary sources]. `ValueAnimator.areAnimatorsEnabled()` (API 26) and `getDurationScale()` (API 33); scale 0 means animations end immediately; Battery Saver can also disable them [V]. Compose `MotionDurationScale`: factor 0 ends motion on the next frame [V].
- Key asymmetry: iOS expects a replacement (fade). Android's standard switch is all-or-nothing: everything jumps to the end state, so every end state must be readable without motion.
- Reanimated: default `ReduceMotion.System`; springs and timings jump to target, delays are skipped, infinite repeats do not start, exiting and shared transitions are omitted [V].
- Flutter: `MediaQuery.disableAnimations` reflects Android's setting; iOS Reduce Motion is a separate flag, `AccessibilityFeatures.reduceMotion` [V].

How the spec should express it: one field per animation with a closed vocabulary.
- `keep`: colour, opacity, tint (price up/down tint, selection)
- `fade`: replace travel or scale with a short crossfade on `duration.quick` (sheets, pages, toast, text swaps)
- `instant`: jump to the end state (height changes, cascades)
- `off`: decorative or looping (live dot pulse, counter bump, deny shake)
- Plus two global rules: holds and timers do not change; meaning carried by motion alone (the limit "deny") needs a non-motion signal.

Current prototype state for comparison: one CSS rule collapses everything to 0.01 ms and JS keeps a 120 ms fade (MOTION.md). That matches Android's behaviour, not Apple's guidance.

Also check: the endless live-dot pulse against WCAG 2.2.2 Pause, Stop, Hide [U, not checked this session].

## 6. Open risks: native vs web-based production app

If native (SwiftUI/UIKit + Compose/Views)
- Only durations and beziers port exactly. Springs chosen in the gallery are sampled fixed curves; on device they must be re-tuned (the gallery already says this in DEVNOTES).
- The 500 ms vs 0.3 s naming gap (1c) will cause wrong values unless tokens state which duration they mean.
- OS-owned transitions (push, sheet, back gesture) may override the custom page and sheet timings; decide per animation.
- Height animations are reimplemented, not ported; cost and feel differ.
- API floors: duration+bounce springs and `Spring` need iOS 17 [V]; zoom transition iOS 18 [U]; Material spring attributes need library 1.13 [V]. Minimum OS of the production app is unknown.
- 120 Hz: iPhone needs the Info.plist key `CADisableMinimumFrameDurationOnPhone` to exceed 60 Hz for custom animations [U, Apple page not fetched directly; secondary coverage agrees]. Frame budget is 16.7 ms at 60 Hz and 8.3 ms at 120 Hz [C]. Specs must never be in frames.
- Compose performance: values that change every frame should be read in layout or draw (lambda `offset {}`, `drawBehind {}`), not in composition [V].
- Two teams will drift without one reference sample per platform reading the same token file.

If React Native or Flutter
- Tokens port through one custom format. Reanimated mass default (4) and its 1.5× duration rule are the known traps [V].

If web-based (WebView or hybrid)
- Tokens and `linear()` springs port 1:1. Risk moves to performance: only `transform` and `opacity` are cheap; `height`, blur and shadow animations drop frames [V], and the prototype animates height in several places.

Regardless of stack
- The token spec has no spring type; the extension shape is a team convention and tool support varies.
- The gallery's truth is a desktop browser. Feel on a phone (touch latency, refresh rate) differs; device review is needed before values are frozen.
- High-frequency live price changes: animation cost and battery, and a rule for coalescing bursts, are not yet specified.
- No owner for native reduced-motion behaviour yet; Apple's App Store accessibility label for Reduced Motion requires re-evaluation at every release [V].

## Could not verify this session
- Apple HIG Motion page and the ProMotion article (pages did not render to text).
- m3.material.io token pages (used the Material Components Android doc instead).
- Whether `UIViewPropertyAnimator` ignores `duration` with physics-based spring parameters.
- Compose unit-mass assumption; Flutter duration/bounce formula; SwiftUI `.smooth` / `.bouncy` exact numbers.
- Overshoot bezier support per native API; Reanimated shared-element maturity.

## Sources
- Design Tokens Format Module 2025.10: https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/ and https://www.designtokens.org/TR/drafts/format
- Style Dictionary built-in transforms: https://styledictionary.com/reference/hooks/transforms/predefined/
- Apple, SwiftUI Spring: https://developer.apple.com/documentation/swiftui/spring
- Apple, SwiftUI Animation: https://developer.apple.com/documentation/swiftui/animation
- Apple, snappy(duration:extraBounce:): https://developer.apple.com/documentation/swiftui/animation/snappy(duration:extrabounce:)
- Apple, WWDC23 "Animate with springs": https://developer.apple.com/videos/play/wwdc2023/10158/
- Apple, UISpringTimingParameters: https://developer.apple.com/documentation/uikit/uispringtimingparameters
- Apple, UIViewPropertyAnimator: https://developer.apple.com/documentation/uikit/uiviewpropertyanimator
- Apple, Reduced Motion evaluation criteria: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria
- Apple, WWDC19 session 244 (cross-fade preference): https://developer.apple.com/videos/play/wwdc2019/244/
- Apple, WWDC24 "Enhance your UI animations and transitions" (notes): https://wwdcnotes.com/documentation/wwdc24-10145-enhance-your-ui-animations-and-transitions/
- Apple HIG Motion (not readable): https://developer.apple.com/design/human-interface-guidelines/motion
- Android, Customize animations (Compose): https://developer.android.com/develop/ui/compose/animation/customize
- Compose Spring constants: https://composables.com/jetpack-compose/androidx.compose.animation/animation-core/objects/Spring
- Compose MotionDurationScale: https://composables.com/docs/androidx.compose.ui/ui/interfaces/MotionDurationScale
- Android, shared elements in Compose: https://developer.android.com/develop/ui/compose/animation/shared-elements
- Android, Compose performance best practices: https://developer.android.com/develop/ui/compose/performance/bestpractices
- Android, ValueAnimator: https://developer.android.com/reference/android/animation/ValueAnimator
- Android, PathInterpolator: https://developer.android.com/reference/android/view/animation/PathInterpolator
- Android, MotionLayout: https://developer.android.com/develop/ui/views/animations/motionlayout
- Material Components Android, Motion tokens: https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- Android reduced motion (secondary): https://dev.to/eevajonnapanula/android-animations-and-reduced-motion-2em2
- Reanimated withSpring: https://docs.swmansion.com/react-native-reanimated/docs/animations/withSpring
- Reanimated withTiming: https://docs.swmansion.com/react-native-reanimated/docs/animations/withTiming
- Reanimated accessibility: https://docs.swmansion.com/react-native-reanimated/docs/guides/accessibility
- Flutter SpringDescription: https://api.flutter.dev/flutter/physics/SpringDescription-class.html
- Flutter Cubic: https://api.flutter.dev/flutter/animation/Cubic-class.html
- Flutter disableAnimations: https://api.flutter.dev/flutter/widgets/MediaQueryData/disableAnimations.html
- WCAG 2.3.3 Animation from Interactions: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- MDN linear() easing: https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/linear
- web.dev animations guide: https://web.dev/articles/animations-guide
- ProMotion coverage (secondary): https://www.macrumors.com/2021/09/24/apple-promotion-third-party-app-support/amp/

---

## 7. Research: decision log formats, hub ideas, sports-specific motion patterns

# What the repository records today (read-only check)

- Decisions already live in four places at once: `PRD.md` (rule text with "решение 12.11.2026" in headings), `TASKS.md` ("Решение владельца" lines inside tasks), `STATUS.md` (done table and "Известные дыры"), and `notes/HANDOFF.md` ("Открытые решения": about 20 long paragraphs mixing open questions, owner decisions and chat assumptions).
- The real test case is spread over all four files, with 10+ mentions:
  - L1: Match Result pinned (variant B), 16.11.
  - L3: not pinned, commit `c09fbc7`, 16.11 18:34.
  - L4: pinned again, commit `ac2106f`, 16.11 19:45.
  - By commit time the reversal took about 70 minutes, not "a few hours". The time of the decisions themselves is unverified.
- One note is already stale: `notes/HANDOFF.md` line 17 says the PRD rule and task L4 "ещё не обновлены", but commit `4f42f74` updated both. This is the drowning risk in miniature.
- The project already separates three kinds of statement, which a log should keep apart: owner decisions, "решения чата, которые владелец может поменять" (assumptions), and open questions.
- `CLAUDE.md` already has the natural trigger for an automatic entry: "Решение принято, только когда Nik сказал «ок»".

Files read:
- PRD.md
- notes/HANDOFF.md
- notes/MOTION.md
- README.md (Motion section)
- public/motion.html (outline only)
- TASKS.md and STATUS.md (headings and grep only)

# Task A. Decision log

## What the research says
- ADR (Fowler, Nygard): one short record per decision. An accepted record is never edited; a change is a new record that supersedes the old one, with a link. Brevity is the main quality. Verified on martinfowler.com.
- MADR: only four parts are required (title, context, options, outcome); status and date are optional; it says it suits any decision, not only architecture. Its "bare" and "minimal" templates are mentioned but I did not open them (unverified content).
- Y-statement (Zimmermann): the whole decision in one sentence: context, concern, chosen option, goal, accepted downside. Practitioners note the sentence gets long. Verified via search summaries only.
- Keep a Changelog: written for people, grouped by type, newest first. It states that raw commit logs make bad changelogs because they are noise. Verified on keepachangelog.com.
- Git trailers: `Key: value` lines at the end of a commit message, parseable with `git interpret-trailers --parse`. Verified via git docs summary.
- Vendor posts on decision logs agree on the failure mode: logs die when they are heavy, hidden, or detached from the work. Low-quality sources, but consistent.

## Rules that prevent drowning (apply to all three formats)
- Log only three things: a product rule changed, an earlier decision was reversed, or a stakeholder (not the owner) decided something.
- Comments, discussion and options considered are never stored.
- One line per decision, with at most one "why" clause.
- The agent writes the entry at the moment the owner says "ок"; the owner never types it.
- Open questions stay in HANDOFF; they are not decisions.
- Chat assumptions are a separate status and are hidden by default.
- Entries are never edited; a new entry replaces the old one and the old one collapses.

## Format 1. "Last decision wins" rule page (history tail under each rule)
- What it is: each PRD rule shows only the current truth, with one collapsed line of history under it. This is closest to what PRD.md already does.
- Effort: near zero; the agent already edits the PRD and just moves the old sentence into the tail.
- Show by default: the current rule, date, who decided.
- Hide by default: the history tail (collapsed, shows only a count).
- Weak point: no single chronological view.
- Example:
  - Live updates · Live bet block
  - Now: pinned under the compact header together with the legal banner; the event feed scrolls under it. (16.11, owner, L4, frame `4365:210691`)
  - History (2, collapsed): 16.11 L3, not pinned, scrolls with the feed (pinned block looked odd on scroll) · 16.11 L1, Match Result pinned (variant B)

## Format 2. Decision trailers in commits, log generated automatically
- What it is: the agent adds 3 or 4 trailer lines to the commit that implements a decision. A page or file is generated from `git log`; nobody writes the log.
- Only commits carrying a `Decision:` trailer count, which answers the "commit logs are noise" objection.
- Effort: zero for the owner; S once for a generator (`build.py` already exists, or the agent regenerates the page). The generator is not built and not tested here (unverified).
- Show by default: the latest decision per screen.
- Hide by default: superseded entries, hashes, task IDs.
- Weak point: decisions with no commit (pure product rules) need an empty or docs commit.
- Example commit message:
  - `L4: блок Live bet закреплён сверху`
  - `Decision: Live bet block is pinned under the compact header; feed scrolls under it`
  - `Screen: match/live-updates`
  - `Supersedes: L3`
  - `Decided-by: owner`
- Generated lines:
  - `16.11 19:45 · match/live-updates · Live bet block pinned · replaces L3`
  - `16.11 18:34 · match/live-updates · Match Result not pinned · replaced by L4` (collapsed)

## Format 3. One-line ledger, shown only on the screen or component it concerns
- What it is: a single append-only file (for example `notes/DECISIONS.md` or a JSON), one line per decision, tagged with screen and component. The hub shows a small chip on that screen or component page. There is no global feed to read.
- Effort: zero for the owner; the agent appends a line. S/M to render chips in the hub.
- Show by default: current decision, date, one-line why, and a "changed 2×" badge. That badge is itself a useful signal of an unstable area.
- Hide by default: superseded lines (expand on tap), chat assumptions awaiting "ок" (count only), and everything unrelated to the open screen.
- Weak point: needs stable screen and component names.
- Example (IDs are illustrative, they do not exist in the repository):
  - `D-031 | 2026-11-16 | match/live-updates | live-bet-block | Pinned under compact header, feed scrolls under it | why: matches frame 4365:210691 | by: owner | replaces D-030 | task L4`
  - `D-030 | 2026-11-16 | match/live-updates | live-bet-block | Not pinned, scrolls with feed | why: pinned block looked odd on scroll | by: owner | replaces D-012 | superseded by D-031 | task L3`
- On-screen chip: "Live bet block: pinned · 16.11 · changed 2×"

## Recommendation
- Use format 3 as the single store and format 1 as the default view (current rule on the screen, history collapsed).
- Add format 2 trailers later as the automatic feed into the ledger.
- The pinned / not pinned case shows why a per-screen "current truth" beats a chronological journal: the reader needs "what is true now", and only occasionally "it flipped twice in one evening".

# Task B. Future ideas for the hub (ranked)

Effort assumes a no-build, single-repo HTML project maintained with AI agents. Structural caveat: the prototype is one 2845-line `public/index.html` and two chats cannot edit it at once, so anything that isolates components (ideas 2, 11) costs more than it looks.

| # | Idea | What it is | Who benefits | Effort | Type |
|---|---|---|---|---|---|
| 1 | Deep link to any state | A URL opens an exact screen, state, phone size and theme | everyone | S/M | long-term utility |
| 2 | Component pages with a state matrix and specs (PITCH) | Pick a component, see every state side by side with sizes, tokens and rules | developer, QA, designer | M/L | long-term utility |
| 3 | Motion spec cards (PITCH) | Each animation as a card: trigger, phases, tokens, slow-motion replay, reduced-motion variant, values per platform | developer, designer | M | both |
| 4 | Figma parity view (PITCH) | Prototype screen next to or overlaid on the exported Figma frame, with a slider | designer, QA, design lead | M | both |
| 5 | Match director | A scripted live match (goal, price move, suspension, half-time) played on demand with a scrubber | stakeholder, PM, developer, QA | M | demo-day wow |
| 6 | Status badges and coming-soon cards | Each flow, screen and component carries Draft / In review / Ready for dev / Built | PM, developer, stakeholder | S | long-term utility |
| 7 | "What changed" page | A weekly, human-language changelog produced by the agent from commits and decisions | stakeholder, PM | S | long-term utility |
| 8 | Token page with export | Colours, type, spacing and motion tokens read live from the CSS, exportable as JSON | developer | S/M | long-term utility |
| 9 | Copy table | All interface strings in one table by screen, with language columns and legal strings marked locked | PM, legal, localisation, developer | M | long-term utility |
| 10 | Flow map | A bird's-eye map of the screens in a flow with arrows; each tile opens the live screen | PM, stakeholder | M | demo-day wow |
| 11 | Visual change check | Before and after screenshots of every ready state on each change; the agent flags differences | designer, QA | M | long-term utility |
| 12 | Accessibility and device checks | Contrast, tap-target size, larger text, reduced motion, small and large phone | QA, developer | S/M | long-term utility |
| 13 | Screenshot pack export | One click exports all states of a screen as images for decks | stakeholder, designer | M | demo-day wow |
| 14 | In-hub comments and pins (AVOID) | Comments pinned to screens inside the hub | nobody yet | L | — |
| 15 | Real Storybook plus hosted visual testing (AVOID) | Move to Storybook with Chromatic or Percy | developer | L | — |
| 16 | Native code snippets per component (AVOID) | Swift / Kotlin snippets next to each component | developer | L | — |

Notes per idea:
- 1: `index.html` only understands `?embed` today (verified by grep); `motion.html` already has a share link. Deep links are the base for ideas 2, 5, 6 and the decision chips.
- 2: this is the "stories" idea from Storybook and the "later: сторибук для разработки" stage in PRD.md.
- 3: nobody else in the list offers this; it builds on the existing `notes/MOTION.md` inventory (M01–M48) and `motion.html`.
- 4: targets the main pain written in HANDOFF ("прототип отстаёт от Figma, сверка руками"). Needs the agent to export frame images from Figma.
- 6: mirrors Figma's "Ready for dev" and public component status pages (USWDS, Morningstar).
- 8: W3C token format and Style Dictionary conversion to iOS and Android are from search summaries (unverified against primary docs).
- 11: feasible because of the existing rule that ready states give the same numbers every time. Needs a local screenshot tool such as Playwright (not installed, unverified).
- 12: partly present already (two phone sizes, reduced-motion rule).
- 13: a single-screen "Copy screen" button (P1) already exists. Video export is harder (L) and unreliable in browsers; leave it out.
- 14: needs accounts and storage, and is exactly the comment flood the owner fears. Figma comments already exist.
- 15: needs a component framework and a build step; Chromatic is built around Storybook; both are paid cloud services that would receive unreleased designs.
- 16: the production platform is not confirmed, and wrong snippets destroy developer trust.

Three to mention in a pitch to a design lead: 2 (component state matrix with specs), 3 (motion spec cards), 4 (Figma parity view). Idea 5 is the best optional demo-day wow.

Three to avoid for now: 14, 15, 16.

Platform claims above come mostly from vendor pages and third-party summaries. The Storybook feature list is confirmed from its docs navigation, and the Percy / Chromatic comparison comes from third-party and competitor blogs. zeroheight, Supernova, Knapsack and Zeplin details are vendor marketing (unverified in product).

# Task C. Sports-specific motion patterns a system should define

1. Price change (odds tick).
   - Direction-coded, one short pulse then rest; fires only on a real feed change, never on re-render.
   - A separate variant for "my selection".
   - In the prototype: M21–M24.
   - One external spec suggests a 500–1000 ms highlight; the prototype uses 0.8 s in, 2 s hold, 1.5 s fade (5 s hold for my pick). Worth a deliberate decision.
2. Market suspend / resume (and locked).
   - Applies in the same frame as the feed, with no easing delay before controls disable; dim plus an explicit label; a defined return.
   - Sportradar's model: suspended means keep showing odds but accept no bets.
   - In the prototype: M16.
3. Score change (digit roll).
   - The number rolls in the direction of change, the row gets a brief highlight, and only the changed digits move.
   - iOS has a native numeric text transition for this.
   - No dedicated score-roll entry in the inventory (unverified whether one exists in code).
4. Goal moment.
   - The one sanctioned expressive moment, in tiers: feed row, match header, timeline card.
   - It must never cover or shift betting controls, and needs a reduced-motion fallback.
   - In the prototype: M20 ("Goal!" label).
5. Live indicator and match clock.
   - A pulse while live, clock tick, start and stop at kick-off, half-time and full-time.
   - In the prototype: M19, 2.4 s, outside the tokens.
6. Timeline event insertion.
   - A new event enters at the top and existing items shift.
   - When the user has scrolled away, a "N new updates" pill appears instead of moving content under the finger.
   - Owner decisions on this exist in HANDOFF (L2).
7. Match state transition.
   - Pre-match to live to half-time to full-time; the tile or header changes layout and markets appear or leave.
   - Bet settlement (won / lost) belongs here.
8. Data freshness.
   - First load (skeleton), stale or offline values (frozen, marked), reconnect and resync.
   - Rule for bursts: when many prices change at once, stagger or suppress the flashes so the screen does not strobe.

Candidates for later: selection added to betslip (M27 bump), probability / momentum bar movement (exists in the Match Result block), countdown to kick-off.

Cross-cutting rules the research supports:
- Honest motion: animate only real data changes. Manufactured urgency around money is treated as a dark pattern (single vendor blog; the regulatory claim is unverified).
- Apple caps animations in Live Activities at 2 seconds and advises animating only the most important update (Apple docs, via search summary).
- Easing curves port across web, iOS and Android; springs do not map one-to-one and need per-platform values (third-party sources, unverified against Apple and Material primary docs).
- The inventory's own gaps matter for the patterns above: no distance tokens, three curves used for the same colour change, 30 numbers outside tokens, and the price-change timings outside the token table.

Gap in the research: I found no published case study from a major live-score or betting product documenting the timing or accessibility of goal or score animations. Patterns 3, 4, 6, 7 and 8 are synthesised from general practice plus this prototype, not from a cited standard.

# Sources

Decision records and changelogs
- https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html (fetched)
- https://adr.github.io/madr/ (fetched)
- https://adr.github.io/adr-templates (search result)
- https://socadk.github.io/design-practice-repository/artifact-templates/DPR-ArchitecturalDecisionRecordYForm (search result)
- https://medium.com/olzzio/y-statements-10eb07b5a177 (search result)
- https://keepachangelog.com/en/1.1.0/ (fetched)
- https://git-scm.com/docs/git-interpret-trailers (search result)
- https://orhun.dev/git-cliff (search result)
- https://www.atlassian.com/software/confluence/templates/design-decision (search result)
- https://plane.so/blog/decision-log-what-it-is-why-teams-use-it-and-template (search result)
- https://arda-cards.github.io/about/templates/decision-log/ (search result)

Design-system and handoff platforms
- https://storybook.js.org/docs (fetched)
- https://storybook.js.org/blog/component-test-with-storybook-and-vitest/ (search result)
- https://help.figma.com/hc/en-us/articles/15023124644247 (search result)
- https://www.figma.com/blog/dev-mode-ga/ (search result)
- https://zeplin.io/features/document/ (search result)
- https://blog.logrocket.com/ux-design/zeplin-design-handoff-figma-dev-mode (search result)
- https://www.zeroheight.com/vs/supernova (vendor, search result)
- https://www.supernova.io/vs/zeroheight (vendor, search result)
- https://www.knapsack.cloud/zeroheight-vs-knapsack (vendor, search result)
- https://chromatic.com/compare/percy (vendor, search result)
- https://argos-ci.com/blog/best-visual-regression-testing-tools (competitor blog, search result)
- https://testdino.com/blog/playwright-vs-percy (search result)
- https://designsystem.digital.gov/components/status/ (search result)
- https://design.aetna.com/ios/status.html (search result)
- https://designsystems.surf/directories/component-status (search result)

Motion and sports / betting
- https://docs.sportradar.com/uof/data-and-features/messages/event/odds-change (fetched)
- https://www.fairplaysportsmedia.com/insights/sports-data-infrastructure/odds-grid-widgets-complete-technical-specification (fetched)
- https://vp0.com/blogs/bet365-odds-display-ui-react-native (fetched; vendor blog)
- https://www.sportmonks.com/blogs/building-a-real-time-livescore-app-with-a-football-api-best-practices/ (search result)
- https://www.sportmonks.com/glossary/in-play-betting/ (search result)
- https://developer.apple.com/tutorials/data/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities.md (search result)
- https://developer.apple.com/documentation/swiftui/contenttransition.md (search result)
- https://vp0.com/blogs/live-activities-lock-screen-sports-scores-ui (search result)
- https://designsystemproblems.pages.dev/cross-platform-consistency/motion-design-tokens (third party, search result)
- https://designsystemproblems.pages.dev/cross-platform-consistency/easing-curves-cross-platform (third party, search result)
- https://focusstate.substack.com/p/winning-by-design-deceptive-ux-patterns (search result, not opened)

Not done: no files were edited, no servers started, Figma not touched. All web queries were generic.

---

## 8.1 Concept 1 (one of three independent proposals)

# Concept: Motion Workbench (designer first)

Verification: read-only. I ran nothing and did no web search; this builds on the supplied audit plus one grep of `public/motion.html` (confirmed: link carries only decisions in `#d=`, duration steps are multipliers .5/.75/1/1.5/2.2 at line 513, "Today" notes are per group). All effort estimates are judgement, unverified.

## 1. Promise
Open any moment of the product, watch its motion on the real screen, try an alternative built from system tokens, and save a decision a developer can read as a spec.

## 2. Sections
- **Library**: every animation (M-IDs) grouped by pattern, with status (no scenario / draft / decided / applied) and an honest coverage counter. Missing ones are shown as "coming soon" rows.
- **Workbench** (main screen): phone stage; playback bar (speed, replay, loop, A/B, close-up); spec card (trigger, phases as bars, tokens used); tuning panel.
- **Tokens**: the scale as a page. Click a token to see every animation using it; change it and the whole prototype previews the change.
- **Patterns and principles**: 6-8 named patterns (press, value change, enter/exit, height change, sheet, page, plus sports ones: price change, suspend, goal, feed insert) and 3-4 principles written as tests.
- **Decisions and handoff**: current decisions, exceptions, reasons, export, link.

## 3. Core interactions
**Job A: "This feels off, try an alternative."**
1. Pick the animation in Library. The phone jumps to the right state and plays it.
2. Spec card shows what it is today: "rises 5 px, --m-std 320 ms, --soft".
3. Slow to 0.25x, loop, close-up.
4. In tuning, pick another token step (quick / std / layout) or curve role. Free values sit behind an "off-scale" switch and are tagged as such.
5. Press A/B: the same phone flips between today and candidate on each replay.
6. Save for the pattern or as an exception, with one line of why. Status becomes "decided".
7. Copy link: opens this exact animation, candidate and speed.

**Job B: "If I change a token, what moves?"**
1. Open Tokens, click --m-sheet. The list shows all animations on it.
2. Change the value. Walk the list with arrow keys; each plays with the new value.
3. Compare view shows old and new side by side.
4. Save as a token decision. One line in the export: "--m-sheet 500 to 440 ms, affects M31-M35".

## 4. Features
**Can be shown tomorrow** (each under about two hours, on the existing page)
- Deep link to one animation, preset and speed (extend the existing `#d=` link).
- 0.25x speed and a milliseconds readout while playing.
- A/B flip on one phone (toggle the preview layer and replay).
- Duration steps snap to the five tokens instead of multipliers; anything else gets an "off-scale" tag.
- Token names in the "Today" notes ("--m-std, 320 ms").
- "Coming soon" rows for the 20 uncovered animations plus a "26 / 46" counter.
- Doc fixes: README and CSS comment say M01-M44 and "two curves, five durations".

**First month**
- One data file for the inventory; Library, spec card and phase bars render from it. MOTION.md is generated from it or retired.
- Tokens page with live token editing (through the existing `MOTION.tokens()` hook).
- Scenarios for the missing animations, live-data patterns first.
- Reduce motion switch with a per-animation field: keep / fade / instant / off (needs a small flag in index.html).
- Phone mode: open the link on a phone, real finger, three controls (replay, speed, A/B).
- Token health panel: automatic count of numbers outside tokens.
- "Apply" step: a saved decision becomes an exact task for the agent; after owner "ок" it lands in the prototype and status becomes "applied".
- JSON export of tokens and decisions.

**Later**
- Native value table (Swift / Kotlin constants, spring conversion) once the stack is confirmed.
- One reference sample per platform reading the same token file.
- Haptics column; scripted live match for data-driven motion; other sports; Figma motion variables sync.

## 5. Token system and inventory changes
- Say the truth: three curves; separate "motion durations" from "hold times" (price-change holds, toast, arrows).
- Add a role layer: enter, exit, move, feedback, value change, each mapped to one duration and one curve.
- Propose small new groups: distance (2-3 steps), stagger (1), press scale (1), dim levels. Project rule forbids new tokens without the owner's "ок", so each is a proposal, not a change.
- Inventory: single data source, fixed fields (trigger, element, from/to, tokens, phases, interruption, reduced-motion, status), one pattern taxonomy instead of three, stable M-IDs, add Live updates and the new Odds tab.

## 6. For developers
- The spec card is their page: numbers, phase bars, interruption rule, reduced-motion variant, token names.
- A deep link in a ticket points at the exact animation in slow motion.
- JSON tokens and a status per animation tell them what is final.
- Honest limit: no native code or spring values until the stack is known.

## 7. Biggest risk
It stays a pleasant playground: free knobs produce new numbers, decisions never reach the prototype, hand-kept copies drift, coverage shrinks.
Limits:
- tuning is token-first, off-scale is a visible exception;
- a decision is not done until applied;
- one data file feeds everything;
- coverage counter always visible;
- desktop feel is not phone feel, so no value is frozen before a phone check.

## 8. Questions for the owner
1. **Production stack?** (a) native iOS + Android, (b) React Native / Flutter, (c) web inside the app, (d) unknown. Recommendation: ask the developers this week; until answered, decide roles and curve/duration tokens only, freeze no springs.
2. **Where does motion truth live?** (a) the prototype's token file, (b) Figma motion variables, (c) both. Recommendation: (a), Figma mirrors later. Note: today's rule says Figma wins on conflicts, so motion needs an explicit exception.
3. **What does a saved decision do?** (a) stays a record, (b) the agent applies it to the prototype after your "ок", (c) applies itself. Recommendation: (b).
4. **How free is tuning?** (a) tokens only, (b) tokens first, marked off-scale exceptions, (c) fully free as now. Recommendation: (b).
5. **What to finish first?** (a) all 46 animations shallowly, (b) live-data patterns in depth (price change, suspend, goal, feed insert), (c) betslip core. Recommendation: (b): it is the part no public system covers and the most specific to a sports product.

---

## 8.2 Concept 2 (one of three independent proposals)

# Concept: Motion Spec (developer first)

Basis: built only from the audit and research supplied in the task. I did not re-open the files or run the gallery. All effort estimates are my judgement, unverified.

## 1. Promise
Open any animation by link and get everything needed to build it the same on iOS, Android or web (exact values, sequence, behaviour, reduced-motion variant) with the real product playing it beside the numbers.

## 2. Sections
- **Specs (home).** List of all animations by ID, filtered by pattern, screen and status. Each opens a card:
  - live phone in the right state;
  - timeline bars (element x property, delay, duration);
  - from/to table;
  - behaviour (interruption, repeat, cleanup);
  - reduced-motion line;
  - iOS / Android / Web tabs with copyable values;
  - acceptance checks and status.
- **Tokens.** Durations, curves, distances, stagger, holds and springs. Each token shows its role, which cards use it and its value per platform. Export as CSS, JSON, Swift or Kotlin.
- **Patterns.** About 8-10 named patterns with one rule each: press, change in place, enter/exit, height change, sheet, page push, list add/remove, price change, suspend, toast. Every animation belongs to exactly one.
- **Health.** Coverage (has a card, has a scenario), numbers outside tokens, entries missing from the inventory, built status per platform.
- **Lab.** Today's gallery (presets, compare, close-up), but tuning snaps to token steps and ends in a proposal.

## 3. Core interactions
**A. A developer builds one animation from a ticket**
1. Clicks the link in the ticket (e.g. `motion.html#M21`).
2. The card opens; the phone sets the state and plays the animation once.
3. Reads the timeline: which element moves, when, for how long.
4. Switches to their platform tab: values in pt/dp, tokens by name, the exact call. Each line is marked "exact" (duration, bezier) or "starting point, confirm on device" (spring).
5. Presses Copy.
6. Reads Behaviour and Reduced motion, replays at 0.1x beside their device.
7. Ticks the acceptance checks; status becomes "Built on iOS".

**B. A designer changes a value and developers find out**
1. Opens the card and presses Tune (Lab).
2. Picks another token step or curve, not free milliseconds.
3. Flips A/B on the same phone.
4. Presses Propose: one line ("M31: duration.sheet to duration.layout") plus a deep link, copied for chat.
5. After the owner's "ок", the agent updates the data file and the prototype. The card shows "changed" with the date, and cards built on the old value are flagged.

## 4. Features
**Can be shown tomorrow (each under two hours, on top of the gallery)**
- Deep link to one animation and speed.
- Spec panel for 5 pilot animations, entered by hand from MOTION.md: trigger, phases, tokens, interruption.
- Token name beside every value ("320 ms = m-std").
- Read-only timeline bars for those 5.
- "Copy tokens as" CSS / JSON / Swift / Kotlin, durations and beziers only.
- 0.25x speed and a millisecond readout.
- Status chip per animation, stored in data.

**First month**
- One spec data file as the single source; MOTION.md is generated from it.
- Cards for all 46 product animations plus the missing ones (Live updates feed, new Odds tab, team page).
- Token set v2 and a standard-format token file.
- Reduced-motion field per card and a preview switch (needs a small flag in the prototype).
- Health panel with an automatic off-token scan.
- Lab snapped to tokens, plus the Propose flow.
- Card readable on a phone.
- English text, pt/dp units.

**Later**
- One reference sample per platform reading the same token file (needs developers).
- Gesture specs: sheet drag thresholds, release behaviour.
- Haptics field.
- Sports patterns: score change, goal, feed insertion with the "new updates" pill, match state change, burst rule for many prices at once.
- Per-component stories once the stack is known.
- Change history per card.

## 5. Token system and inventory
**Tokens**
- Two tiers: primitives (duration, easing, spring) and roles (enter, exit, move, feedback, value change), each role mapped to one duration and one curve.
- New groups: distance, press scale, stagger, delay, hold (price change, toast, arrow).
- Honest count: three curves; price-change timings move into hold.
- Curve keywords replaced by tokens; JS reads values from CSS rather than repeating them.
- Springs stored as duration + bounce with derived per-platform numbers.
- The project rule forbids new tokens without asking, so v2 is an owner decision.

**Inventory**
- Becomes data with a fixed field list: ID, pattern, trigger, elements, per-phase rows (property, from, to, token, delay), interruption, repeat, layout effect, reduced motion (keep / fade / instant / off), system default or custom per platform, status, acceptance checks.
- One taxonomy (patterns) replaces the 8 sections and 6 groups.

## 6. Designers
- The card is the review surface: intent, numbers and live motion in one link.
- Lab stays; snapping to tokens turns "I like this" into a system decision.
- Patterns give a shared vocabulary; Health gives a visible backlog and a number to report upward.
- Figma remains the source for static design.

## 7. Biggest risk
False precision: a spec that looks exact but has drifted from the prototype, or gives native values nobody tried on a device.

How to limit it:
- One data file feeds the cards, and Health shows drift.
- Every native value is labelled exact or "confirm on device".
- Values only, no generated whole-animation code.
- Test the 5 pilot cards with one real iOS and one Android developer before scaling to 46.

## 8. Questions for the owner
1. **Production stack?** (a) native iOS + Android, (b) React Native / Flutter, (c) web-based, (d) unknown. Recommendation: ask engineering this week; until answered, export durations and beziers only, no springs.
2. **Where do motion values officially live?** (a) this tool's data file, (b) Figma motion variables, (c) both. Recommendation: (a).
3. **Pilot scope?** (a) all 46 at once, (b) 5 animations covering five patterns (press, price change, sheet, card removal, height change), (c) tokens only. Recommendation: (b).
4. **Token set v2?** (a) one proposal with all new groups, approved together, (b) one group at a time, (c) keep the current set. Recommendation: (a).
5. **Developer partner for the pilot?** (a) one iOS and one Android developer for 30 minutes each, (b) one developer, (c) nobody yet. Recommendation: (a); with (c), build only the "tomorrow" tier.

---

## 8.3 Concept 3 (one of three independent proposals)

CONCEPT: SYSTEM FIRST

Verification: built from the supplied audit and research only. I did not re-read the files or run the page, so every claim about current behaviour is inherited from the audit and unverified by me. Effort estimates are judgement, not measured. Nothing was changed.

## 1. Promise
One home for the product's motion language: every animation is an instance of a named pattern built from tokens, playable in the real screen and readable as numbers.

## 2. Sections
- **Principles**: 3-4 rules written as tests a proposal can fail, the two-speed rule (quiet for frequent actions, expressive for rare moments), "animate only real data changes", and the checklist for adding an animation.
- **Tokens**: the scale as playable rows (durations, curves, then distance, stagger, hold, press scale). Each row shows its role, its value and "used by N animations", plus a health counter of numbers outside tokens.
- **Patterns**: at most seven: Press feedback, Enter/Exit, Value change, Sheet, List change (add, remove, height), Page, Live event. Each has one recipe (role to token), a reduced-motion variant, an interruption rule and its list of instances.
- **Instances**: today's gallery (M01...) on the real prototype, regrouped by pattern, each with a status and a "deviates from pattern, because..." flag.
- **Handoff**: token file, per-animation spec cards, deep links, and a list of approved changes.

## 3. Core interactions
**Designer: tune a pattern, not an animation**
1. Opens Patterns, then Sheet. The phone plays the first instance.
2. The right panel shows the recipe in words: "duration: sheet 500 ms, curve: soft".
3. Changes it in one of two ways: steps to a neighbouring token on the scale, or edits the token's value.
4. A line appears: "affects 6 animations". Arrow keys walk through them on the phone; Compare shows before and after.
5. One instance looks wrong: marks it as an exception and writes why.
6. Saves. The decision reads "sheet 500 to 440 ms", not a loose number.

**Developer: what exactly do I build**
1. Opens a deep link from a ticket (animation, state, speed).
2. Sees the spec card beside the phone: pattern, trigger, phases as bars on a time axis, from/to values, tokens with numbers, interruption, reduced-motion behaviour.
3. Replays at 0.1x.
4. Copies the spec or the token block.

## 4. Features
**Can be shown tomorrow** (each under two hours)
- Pattern tag on the 26 existing items and a "by pattern" switch for the left list.
- Read-only token strip: five durations and three curves, with the current animation's tokens highlighted.
- Duration steps snap to the token scale, replacing the XS-XL multipliers.
- Deep link to one animation and speed, and a 0.25x speed.
- Export gains a JSON block of durations and curves, and decisions phrased as token changes.
- Hand-written spec text for five flagship animations (odds change, sheet, card removal, press, page).

**First month**
- Inventory moved into one data object; spec cards with phase bars for everything, MOTION.md generated from it.
- Token set v2 (section 5), with the prototype migrated pattern by pattern.
- Token health panel, counted automatically.
- Reduced-motion variant per pattern, with a switch to preview it (needs a small flag in the prototype).
- Scenarios for the 20 missing animations and for Live updates.
- Status per animation (draft, agreed, built iOS, built Android).
- Swift and Kotlin constants for durations and curves only.
- Principles page.

**Later**
- Sports patterns as first-class: score roll, goal tiers, suspend/resume, burst rule for many price changes.
- Springs with per-platform values, tuned on devices.
- Haptics paired with patterns.
- Phone-friendly view of the tool.
- A reference sample per platform reading the same token file.
- Other sports.

## 5. Token system and inventory
- Two tiers: primitives (5 durations, 3 curves, about 3 distances, 1 press scale, 1 stagger step) and roles (enter, exit, move, feedback, value change, sheet), each role one duration plus one curve.
- A separate "hold" group for pauses (toast, arrow, price highlight): marked "pause, not motion".
- One naming scheme across CSS, JS and export; JS reads values from CSS instead of repeating them.
- Inventory record gets fixed fields: pattern, tokens, from/to, phases, interruption, reduced motion (keep / fade / instant / off), status, deviation reason.
- Patterns replace the three taxonomies that do not line up today.
- Project rules forbid new tokens without the owner's approval, so v2 needs his "ok" on the exact list.

## 6. The second audience: developers
- They build seven patterns as reusable pieces, not 46 separate animations.
- They get numbers in a file, not a video or a Russian table.
- Each card states "system default or custom" per platform, so nobody fights the OS back gesture by accident.
- Statuses and deep links make a ticket point at one exact thing.

## 7. Biggest risk
A tidy system that real animations do not fit, built before anyone used it, on a platform still unconfirmed.
- Derive patterns only from the inventory: three or more instances make a pattern; one-offs stay outside.
- Cap at seven patterns.
- Carry one pattern end to end, and have one developer read it, before generalising.
- No springs until the platform is known.

## 8. Questions for the owner
1. **Production platform?** Native iOS and Android / React Native or Flutter / web or hybrid / unknown. Recommendation: ask the engineering lead this week; until then, roles and curves only.
2. **Where do motion values officially live?** This tool's token data / Figma motion variables / both. Recommendation: this tool; Figma shows intent.
3. **What happens to an approved decision?** Export only / the agent applies it to the prototype after "ok" / the tool writes live. Recommendation: applied after "ok", so prototype, inventory and export stop disagreeing.
4. **Scope of token v2?** Keep 5 + 3 and add roles / also add distance, stagger, hold and press scale / full rebuild. Recommendation: the second.
5. **Which pattern goes first end to end?** Value change (odds) / Sheet / Press feedback. Recommendation: Value change: most frequent, most sports-specific, and no public system covers hold times.
