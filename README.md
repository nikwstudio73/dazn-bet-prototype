# DAZN Bet in Scores — interactive prototype

A clickable mobile prototype of betting inside the DAZN Scores app (Spain first). It is used for screen-sharing on calls and design reviews. Plain HTML/CSS/JS with no framework, no server and no dependencies.

Design source: Figma file **DAZN-Bet-in-Scores**, https://www.figma.com/design/JKfGVyF14eYu62ptYUkyzX/DAZN-Bet-in-Scores (page "❖ Local components" holds every component the prototype mirrors).

## Run it

- **Online:** the `public/` folder is the website. The GitHub repository is connected to Vercel, so every push to `main` puts the new version online in about a minute.
- **Offline:** open `dist/DAZN-Bet-in-Scores-prototype.html` in Chrome. It is a single self-contained file (fonts and images inlined) and can be sent as an attachment.
- **To edit:** change `public/index.html` (it loads files from `public/assets/`). Run `python3 build.py` to regenerate the single file in `dist/` (Python 3 only), then commit and push.

## Folder

```
public/index.html   the whole prototype: CSS (top), markup, JS (bottom)
public/assets/img/  83 PNGs and SVGs: club crests, player photos, competition logos, nav and header icons, DAZN Bet logo
public/assets/fonts/ DAZN Oscine Regular / Bold (woff2)
vercel.json         tells search engines not to index the site
build.py            public/ -> dist/ single file (not needed for the website)
dist/               the offline single-file build (not in git)
```

## Deploy (one-time setup)

1. Publish this folder to GitHub as a private repository (GitHub Desktop: Add local repository -> create a repository here -> Publish).
2. On vercel.com, team DAZNUX: Add New -> Project -> import the repository. No framework, no build command; Vercel serves `public/` by itself.
3. From then on: commit + push = new version on the same link.

## What you can do in it

The **Prototype states** panel on the left is the only navigation (see the next section). The switch in the bottom-right corner toggles iPhone 13 mini (375) and iPhone 17 Pro Max (440).

1. **Scores feed.** The Odds toggle in the header shows or hides the odds under each match, together with the gambling warning on top and the "+18. Juega con responsabilidad. Publi." footer. Odds tiles show 3-letter team codes and X. Tapping the LIVE badge filters to live matches; on another day it goes back to Today with the filter on. Live odds move every 2.6 s: the tile flashes, then a green or red line plus arrow stay about 2 s and fade out together.
2. **Picks.** Tap an odd to add it to the betslip; it turns white. Tap again to remove it. The first pick only adds to the collapsed bar above the nav and does not open the sheet. Picking another outcome of the same match and market replaces the previous pick.
3. **Collapsed bar.** Shows the count, the three newest picks and "+N", the bet type (Single / ACCA / Singles) and the total odds. Tap it to open the sheet.
4. **Betslip sheet.**
   - The gambling warning and "Odds powered by DAZN Bet" sit under the title.
   - Live picks show the score, then the minute in red with a slowly pulsing red dot (no glow, no LIVE plate). "Goal!" flashes before the minute for about 1 s when that pick's odds change.
   - The sheet starts with the gambling warning, then the "Betslip" header; the warning scrolls away, the header stays pinned.
   - The summary shows Total odds and "€10 may return €X".
   - Drag the handle down or tap outside to close.
5. **Edit mode.** Header **Edit → Confirm**.
   - A 20 px round × appears in every card, one card after another, and the card content dims to 30%.
   - The summary dims and **Place bet on DAZN Bet** is disabled (light grey, as on the approved Edit screen).
   - The sheet keeps its height while cards are removed, so nothing moves under the finger. On Confirm it eases to its new height.
   - Removing the last pick closes the sheet and shows an Undo toast.
6. **Place bet on DAZN Bet.** Opens a mock DAZN Bet overlay. Closing it clears the betslip, as in the real flow, because nothing comes back from DAZN Bet.
7. **Fixture page.** Every match of today opens its own page: tap its tile. Real Madrid v Atlético Madrid is the one drawn in Figma; the other seven use the same template with generated demo data (see "Demo data" below). A live match shows the score and the running minute in the header and only the markets that still make sense for the score. The **Odds tab** follows the Figma frame "[V2] Odds Pre-game" (`4326:231817`): the markets come in groups, top to bottom. **Match Result** — one card with the glow of both teams: crests and "Who will win?", the implied chance of the three outcomes as a bar (the block of Live updates), the three 1X2 prices, **Double chance** (1X / X2 / 12; the chevron folds it) and **Draw no bet**. **Goals** — one card: the switch Full Time / 1st half / 2nd half, **Total Goals** with a line stepper (− 2.5 +) and the Over / Under pair of that line, **Both Teams to Score** (folds) and **Combinations** (1 & BTTS, 2 & BTTS, X & BTTS); in a half only Total Goals is shown, because the other two exist for the whole match only. Then the **Goalscorer** carousel ("In this match"; Figma component `Odds/Goalscorer card`: cut-out photo, name, club, price on a dark tile; a picked card turns white; players without a cut-out photo show the silhouette; every player is his own pick, so several can be in the betslip), **Handicap** (tabs with the two crests, a line stepper from -3 to +3, three outcomes per line; the Away tab shows the same market from the other side) and "More bets on DAZN Bet". The markets and the picks are the ones the page had before; picks stay in sync with the feed, Live updates and the betslip. A live match has no half switch and shows "X" for the draw; a finished match has no half switch and no Goalscorer.
   - **Team colours** (task C2): the glow of the match header, of Match Result (Odds, Overview) and of a goal card in Live updates, and the two outer segments of the chance bar take the colour of each team — the main colour of its crest (`TCOL` in the code; a team with a white or black-and-white crest glows white; a dark colour is lightened with the same hue until it reads on the dark cards, one rule for all teams — `tcLift()`; when both teams have the same colour the away side takes the second colour of its crest (`TCOL2`) or white — `pairCols()`). The gradients stay in the CSS as drawn for Real Madrid – Atlético; `teamGlow()` repaints them per match. The favourite-team popup keeps the drawn colours.
   - **Overview tab** (Figma "B · Top Bets carousel after Match Results" `4369:236502`, task O1): the gambling warning, **Match Results** (glow of both teams, crests, "Who will win?", the three 1X2 prices — the same picks as the feed, Odds and Live updates), then the **Top Bets** carousel (Figma `Odds/Top Bet`): each card a ready-made combination of this match — label, match, league and date, three legs, "+N more selections" and one price. A tap on the price puts the whole combination into the betslip as **one card** (all legs, "All N must win"); a second tap takes it out. In the bar one Top Bet shows its match and "Top Bet"; with any other pick the slip reads "Singles". It counts as one of the 20, leaves only as a whole, and a suspended or locked Top Bet drops out as a whole (working assumptions, open with the owner and the PM). Below, drawn by the frame and not tappable: Form, League position, Match info, Next matches and the footer. A live or finished match has no Top Bets.
8. **Days.** Every day of the calendar opens its own feed, and the calendar scrolls sideways (finger, mouse drag or wheel): days before today hold finished matches, days after today hold matches that have not started (`DAY_ADD` in the code).
   **Finished matches.** Tap **Sat 3 Jan** in the calendar (or the state *Other screens → Finished matches*). FT tiles keep their last odds, nothing is tappable, the outcome that happened is white and the rest are grey. Tap a tile: its page shows the final score with "FT" and the same rule on every market. **Today** goes back.
   - **Live updates tab** (Figma "Live Updates with Odds" `4365:194526`, task L2). On a match page the tabs **Odds** and **Live updates** switch; a match opens on Odds. A live match has the **Live bet** block on top: the gambling warning, the red label, "Who scores the next goal?" and three prices — home, No goal, away (market "Next team to score"; picks go to the same betslip). It stays pinned under the compact header while the feed scrolls under it (L4, owner 16 Nov; L3 had unpinned it). Below it: the switch **All / Key Events**, then the events, newest first — commentary, goal, yellow card, substitution, half-time, kick-off. The feed has no odds. A goal card has the glow of its side (home from the left, away from the right), a large ball and the diagram of the shot. A finished match shows only the events; a match that has not started shows "Live updates start at kick-off"; neither has the Live bet block or the legal texts, because there are no odds on the tab. **The feed is alive:** with the minute new events come in (`LQ`, `luQueue()`), a goal changes the score everywhere — header, feed tiles, betslip. Motion: a new event opens on top and pushes the feed down; if the feed is scrolled away nothing moves and a pill "1 new update" shows under the compact header (tap: back to the top of the feed); a goal is an event like any other and the score in the header changes softly; the prices of the Live bet block move by the pattern of any price; the dotted line of the shot draws once the card has landed.
9. **Competition page · Odds tab.** Tap a competition header in the feed or a league in the row under the header (the row scrolls sideways): **UEFA Champions League** (drawn in Figma); **LaLiga**, **Premier League**, **Serie A**, **Bundesliga**, **Ligue 1**, **Europa League** and **Conference League** use the same template with demo data. The page has the tabs Matches / Table / Odds / Playoff / Team stats (Matches and Odds are built and switch; the others are labels). Header and tab row follow the Scores-Redesign frame `212:99096` (file `x9vLS7m4JClz89DW39Ppjg`) on every page — league, team, match: 16 px before the first tab, 16 px on each side of every label, the row scrolls sideways when the tabs do not fit. The Odds tab has sub-tabs as chips:
   - **Competition winner:** a table of teams with the price to win the season (row 66, crest 36, name 14 px, no place number). The table glows in the colour of the competition: blue for the Champions League and red for LaLiga are drawn in Figma; the other six competitions use the main colour of their logo (`.cp-table.g-*`, owner 16 Nov).
   - **Top scorer** (Figma "Top scorer v3.2"): two **Top Picks** cards, then the list of players. A picked Top Pick turns white as a whole, with the price on a dark tile.
   - **Relegation** (not drawn in Figma): the same table with the price to be relegated, from the most likely team. Only leagues have it; Champions League, Europa League and Conference League show no such chip. Betslip card: "<team> to be relegated", market "Relegation".
   - The whole card or row is the tap target, not only the price (the same on the Goalscorer cards of a match).
   - **Matches tab** (not drawn in Figma): the calendar of the feed and the tiles of this competition only, drawn by the same `tileHTML()`, so picks and live prices are in sync with the feed, the match page and the betslip. It has its own selected day (`S.cpDay`; starts on the day of the feed) and its own LIVE filter. A tile opens the match page; back returns to this tab. A day without matches shows "No matches on this day". Conference League has no matches in the demo data.
   - In the Competition winner and Relegation tables the crest and the name of a team open its page (see 10); the rest of the row still picks the price.
   - These are outright (season-long) picks. One pick per market: tapping another team or player replaces it. In the betslip the card shows the competition and the season instead of a match. The collapsed bar and the bottom nav stay on screen.
10. **Team page** (not drawn in the new UI; the old-UI frame `4309:169173` gives only its content and order). Tap the crest or the name of a team in the header of a match page, or in the Competition winner / Relegation tables of a league page. Header: back, crest, name, competition and season, the Follow button (as on a league page). Tabs Matches / Overview / Table / Squad / Team stats (Matches and Overview are built and switch; the others are labels).
   - **Matches:** the team's matches in the chosen competition, oldest first, each under a line with its matchday and day. The tiles are the feed's own `tileHTML()`, so picks and live prices are in sync with the feed, the match page and the betslip. The list opens at the match being played or the next one. The **Matchday** select under the tabs (dropdown "Small - 32px" of Scores-Redesign, `868:67227`) opens a list of matchdays; picking one brings the list to it. The gambling warning stays under the tabs with it. A tile opens the match page; Back returns to the team page, on the same tab.
   - **Competition:** a team that plays in more than one (LaLiga and Champions League) has a small menu on the line under its name. The page opens in the competition it was opened from.
   - **Overview:** one block, the nearest match of the team in any competition (the one being played first): the same tile with its three Match Result prices, under "Next match" / "Live now" and a line with the competition, matchday, day and time. No match to come: "No upcoming matches", nothing about betting on screen (AZ Alkmaar: Conference League → Competition winner).
   - Match pages and team pages open one from another (match → team → match → the other team …); Back goes the same way back, one page at a time.

## Navigation: the "Prototype states" panel

One panel on the left, nothing else on screen except the phone, the "Copy screen" button under it and the phone-size switch.

- **Free play** (selected when the page opens). Everything on the phone works by hand. Clicking it again, or the round arrow next to it, starts over.
- **Topics.** Betslip, Suspended, Locked, Limit 20, Fixture, Competition, Team, Other screens. They hold only what cannot be reached by tapping the phone (a price that moves in a pick, suspended and locked bets, the limit of 20) plus the screens that are not obvious to find, one topic per screen: Fixture (Odds tab, Live match, Live updates, Goalscorer), Competition (Winner, Top scorer, Relegation, Matches), Team (Matches, Matchday menu, Overview, Overview · live) and Other screens (Finished matches, Favourite team popup). The main flow (Odds toggle, picks, betslip, Edit, Place bet) is done by hand in Free play; its description says what to try. A topic opens its states; only one topic is open at a time. Opening a topic does not change the phone. A dot next to a folded topic marks where the current state lives.
- **States.** One click sets the whole screen (picks, statuses, prices, sheet open or closed), whatever was on screen before. The selected state shows one or two lines about the rule it demonstrates. Click it again, or the round arrow, to start the same state again.
- **Collapsed / Opened.** States that exist with the betslip folded and unfolded are one row with this switch. If you open or close the betslip on the phone by hand, the switch follows.
- The **‹** button folds the panel into a small "States" button (it starts folded in windows narrower than 1000 px).
- **Copy screen** (under the phone, desktop only). Copies the phone with its frame as a PNG: a real picture of the tab (Screen Capture), cut to the frame, transparent outside the rounded corners, at the density of the screen. The browser asks for permission once; the stream stays alive until the page is closed or "Stop sharing" is pressed. It needs a browser that can share a single tab (Chrome, Edge). Without clipboard access the picture is saved as `dazn-bet-screen.png`. Code: block "P1 · Copy screen" (`shotFrame()`); `fit()` keeps 64 px under the biggest phone for the button.
- The panel and the phone-size switch use the same Global foundation tokens as the product UI (`--ui-*` variables in the CSS, each with its token name). The only accent is white (text/primary); no brand yellow and no orange outside the phone.

### Motion

One system everywhere. The tokens live at the top of the hand-written CSS (`MOTION TOKENS`) and are mirrored in JS (`SOFT`, `T`); use them instead of new numbers.

| Token | Value | Used for |
|---|---|---|
| `--soft` | `cubic-bezier(.32,.72,0,1)` | anything that travels or resizes: sheets, bar, toast, odds reveal, pages, text swaps |
| `--ease` | `cubic-bezier(.2,.8,.2,1)` | state changes in place: colour, press, small moves |
| `--m-press` | .12 s | press feedback |
| `--m-quick` | .2 s | colour, opacity |
| `--m-std` | .32 s | an element enters, a text swaps, a removed card's place closes |
| `--m-layout` | .44 s | heights and pages: odds reveal, sheet resize, fixture push |
| `--m-sheet` | .5 s | sheets, collapsed bar, toast, DAZN Bet overlay |

- **Inventory:** `notes/MOTION.md` lists every animation (M01…M44): what moves, trigger, phases, tokens, numbers written outside the tokens, and where similar things are done differently.
- **Presets:** `public/motion.html` (open it by its own address; nothing links to it) shows the real prototype (`index.html?embed` in a frame) and lets you try motion presets per group of animations — variants, exact values, compare with the current motion, slow motion — and copy the decisions. It previews on top of the prototype; `index.html` is not changed by it.

JS helpers: `soft()` (play an element in), `setTxt()` (swap a text), `smoothH()` (ease a height), `rise(dir)` (start position of a new number). With **Reduce motion** switched on in the system nothing travels, springs or pulses; states still change.

- **Odds toggle:** visible cards open one after another, prices fade in and rise, the gambling banner and the footer collapse and expand with the cards (`--o-*` variables, cascade in `setOddsOn()`). If the feed is scrolled, the first visible tile stays where it is (`holdAnchor()`).
- **A price moves — one pattern everywhere** (feed tile, the same tile on the fixture page, betslip card, Total odds, bar total): the new number comes in along the direction of the move (up: rises from below, down: drops from above) and an arrow shows the direction. A tile that is not picked keeps tint + arrow about 2 s and fades 1.5 s. Everything that belongs to my pick (its tile, its card, the totals) keeps the arrow about 5 s and fades .6 s (`CHG_T` in JS, `--chg-*` in CSS). The arrow in the bar grows and shrinks in width, so the total pill does not jump.
- **Collapsed betslip:** appears with a short rise and fade; the selection list, bet type and total swap softly when they change. It does not hide for the sheet: the sheet slides over it and uncovers it again.
- **Sheets (betslip, favourite-team popup):** native iOS behaviour: slide up from the bottom edge (`--soft`, `--m-sheet`), the dimming fades with it. Drag by the handle or by the header: the sheet follows the finger, the dimming lightens, pulling up gives a little rubber band. Releasing past a quarter of the height or with a quick flick closes it, otherwise it springs back; either way the release continues at the speed of the finger (`dragSheet()`).
- **Inside the sheet:** a pick that becomes Suspended or Locked dims softly and its price swaps with a small rise; the summary changes height smoothly. "Goal!" fades in and out.
- **Edit mode:** the × buttons appear one card after another, only for the cards on screen (max 6 steps). A removed card leaves in two phases, like an iOS list row: it fades and shrinks slightly at full height (`--m-quick`), then its place closes (`--m-std` on `--exit`, a curve with a gentle start and a gentle landing, so the cards below never jerk; it starts while the card is almost gone, so there is no stop between the phases); Total odds, the return and the counter change when the place starts to close. Several can be removed quickly one after another.
- **Limit 20 · tap on a 21st odd** (Figma N): nothing is added; the tapped odd gets a light press and a small spring back (no colour), an orange tongue slides out from behind the collapsed betslip ("You’ve reached maximum number of bets allowed.") and the counter pulses; the tongue hides after ~2.6 s (`denyLimit()`). With the sheet open there is no message: the odd only springs back.
- **Feed:** switching the day slides the list in from the side of that day (yesterday from the left, today from the right); the LIVE filter fades it in from below (`swapFeed()`). A tapped odd changes text colour together with its background.

### Club crests

`public/assets/img/{ars,ath,atm,bar,bay,che,liv,mci,new,psg,psv,rm,val,vil}.png` are exported from the Graphic Assets library (`Football-club-logo`) in the proportions of the 28 px slot of the match tile.

The 46 clubs added later (`TEAMS` in the code) come from the same library: `k.png` is a 112 px square for the tile slot, `t_k.png` the same crest without padding. League logos (`seriea`, `bundes`, `ligue1`, `uel` and their `chip_*` versions for the row of leagues) come from the Quick-link logos of that library. Write image paths out in full in `index.html`: `build.py` inlines only literal paths.

## Where things live in `public/index.html`

| Lines (approx.) | What |
|---|---|
| 11–262 | Design tokens and component values originally generated from Figma (spacing, colours, type, radii per component). Change values here, not inline. |
| 264–675 | Hand-written layout CSS: feed, legal banner and footer, tiles, odds tile states, nav, bar, toast, sheet, cards, fixture, popup, prototype chrome (`--ui-*`), navigation panel |
| 676–803 | Markup: status bar, header, calendar, feed, fixture, bar, nav, sheet, popup, toast, overlay, navigation panel, phone-size switch |
| 806–856 | `IMG` asset map, `EXTRA` (matches used only by "Fill betslip to 20"), `INIT` (the 8 demo matches), `FT` (yesterday), `FX` (Odds-tab markets) — edit demo data here |
| 858–900 | Feed: `tileHTML()`, `renderFeed()`, Odds toggle, day switch |
| 901–952 | Selections, limit of 20, `act()` (picks that still have a price), `betType()`, totals, collapsed bar |
| 953–1043 | Sheet: cards, `applyEdit()` / `releaseHeight()`, `updateSummary()`, remove + Undo, overlay |
| 1044–1107 | Live engine: `liveTick()`, `changeOdd()`, `animateOdd()` (odds animation timings), event flash, arrows |
| before the Live updates tab | Fixture Odds tab (U4): `oddsHTML()` (the groups), `mrTop()` (Match Result block), `goalsHTML()` + `setOxPer()` / `setOxLine()` (half and line of Total Goals; U6: the − / + of the line are hidden, `oxStep()` shows them for `OX_HOLD`, `oxHint()` plays that once per page load), `oxToggle()` (folded blocks: Both Teams to Score and, since U5, the lower half of Match Result behind "Show more" / "Show less" — `S.ox.mr`, open from the start when a Double chance or Draw no bet pick of the match is in the betslip), `hcHTML()` / `setHc()`; what is open on the page lives in `S.ox` and `S.hc`; its CSS is the `.ox-*` block at the end of the stylesheet |
| after the fixture Odds tab | Fixture · Overview tab (O1): `TB` (Top Bets of the drawn match), `tbOf()` (Top Bets of any other match, worked out from its 1X2), `tbGet()`, `tbLegs()`, `overHTML()`; a Top Bet pick is `{m, g:'tb:<id>', o:'y'}` with one price (`oddsOf`), its card lists the legs (`cardHTML`); CSS block `.ovw` … `.ov-ft` |
| after the Overview tab | Fixture · Live updates tab (L2): `LU` (hand-written feed), `luBase()` (generated feed), `luOf()` (base + events that came in, `S.lu`), `LQ` / `luQueue()` (events still to come), `luDue()` / `luPush()` / `luInsert()` (the feed grows), `luShot()` (shot diagram), `ntsOf()`, `liveHTML()`, `luCard()`, `luPill()` / `luTop()`, `setFxTab()`, `setLuKey()`; its CSS is the block `.lu-top` … `.lu-new` |
| after the competition page | Team page: `buildTeamPage()` (clones `#cp` into `#tm`), `teamMatches()` / `teamList()` / `teamNext()`, `renderTeam()`, Matchday menu, and the stack of pages (`S.stack`, `openTeam()`, `pageBack()`); its demo data (`tmRows()`) sits after `DAY_ADD` |
| 1130–1179 | Favourite-team popup, `STATES` (ready-made states), `setState()`, `buildNav()` / `paintNav()` (navigation panel) |
| 1180–1247 | Event wiring, drag-to-close, device fit, `init()` |

## Showing it on a call: ready-made states

- **34 screens in 27 rows.** Seven rows are a Collapsed / Opened pair. The topics follow the rows of the Figma section "Betslip states · PRD".
- **Keyboard.** **→ / ←** step through all 34 screens in order (the panel follows). **L** pauses and resumes the live price ticker.
- **Repeatable numbers.** A ready-made state pauses the live price ticker and uses fixed prices, so the totals are the same every time (for example Odds changed: 16.97 → 17.06). Arrows stay on screen while the state is shown. Free play turns the ticker back on.
- To add or reorder a state, edit the `STATES` array in `index.html`: `g` = topic, `k` = name of the row, `v` = `'bar'` / `'sheet'` for a Collapsed / Opened pair (two neighbouring entries with the same `g` and `k`), `n` = the note under the row, `run()` = what to set. The panel is built from this array.

## Product rules baked in

- Odds math: total = product of the odds that still have a price; return = €10 × total.
- Maximum 20 picks. At the limit no odd can be added or swapped; removing a pick lifts the limit.
- At the limit the open sheet shows no extra message (owner, 15 Nov): the number of picks is only in the header, "Betslip 20". A tap on a 21st odd still gets the orange tongue above the collapsed bar.
- Dropped picks (suspended / locked) are explained by a small second line under "Total odds": "Excludes N suspended selection(s)" (or "locked", or "unavailable" when both kinds are present). When no active pick is left the total shows a dash and the line reads "Your selection is locked / suspended"; the collapsed bar shows a dash too (the PRD says 0; open with the PM).
- A selected tile whose price moves stays white and shows a dark green / dark red arrow next to the price.
- A suspended or locked pick stays in the betslip and in the count, leaves the total, and is not sent to DAZN Bet. Its odd is not tappable; it can be removed in Edit mode.
- While a pick is **locked**, the total is struck through and "Place bet on DAZN Bet" is disabled (Figma screen J). A suspended pick does not block the button.
- Picks on the same match are labelled "Singles" in the bar, but the sheet still shows Total odds. This is open with the PM.
- There is no stake input and no login. DAZN Bet handles those inside its overlay.
- Legal copy (top warning, footer, text under the summary) is fixed by legal; don't rewrite it.

### Demo data (not from Figma, not real prices)

- **Live updates.** Real Madrid v PSG has a hand-written feed of events (`LU`) and three events still to come (`LQ`: commentary, a goal at 86’, commentary); every other match gets a feed worked out from its score and minute (`luBase()`: goals spread over fixed minutes, scorers from the Goalscorer list of the match, one yellow card, half-time, kick-off) and its own three coming events (`luQueue()`: the favourite scores once, a few minutes in). So in Free play every live match of the feed gets one more goal within a few minutes; the markets of its Odds tab are worked out at load and do not follow that goal. "Next team to score" (`ntsOf()`) is priced from the goals still expected. The base feed and the opening prices are worked out once, so they are the same on every load; ready-made states pause the ticker, so nothing comes in there (the state "Live updates · goal" pushes one goal itself). Shot positions are not in the data: four fixed ones, picked by the minute of the goal. Team colours are not in the data either: a home goal glows white and an away goal red on every match.
- **Match pages.** `fxOf()` builds the markets of a match from its 1X2 prices in the feed: implied chances, expected goals, a 6 % margin, prices rounded the way a bookmaker rounds them. So the numbers are consistent with each other and plausible, but invented. Total Goals of the 2nd half (`ou2hOf()`) uses the formula of the 1st half with the other 56 % of the expected goals. Live matches: goal lines start above the goals already scored; no half markets and no "Result & both teams to score" market; no "Both teams to score" once both have scored. Goalscorers per match are in `SCORERS`.
- **Team pages.** The calendar holds 1–2 matches per team, so `tmRows()` adds the rest of the season around its eight days (`CLUBS`, `PWR`, `TM_ROUNDS`, `TM_NEXT`): finished rounds back to Matchday 1 and, for a league, eight coming rounds. It is a round-robin of the clubs that have a crest (LaLiga has seven, so opponents come back every seven rounds, home and away in turn), prices worked out from a fixed strength of each club, finished rounds with a fixed score. Nothing is random: the same matches, prices and scores on every load. They are in no feed and on no league page. Matchday numbers on a team page count one by one from that team's match of today; the list starts at Matchday 1.
- **LaLiga and Premier League pages.** Teams, players and prices in `CP` are close to the real season, not real odds. LaLiga has seven teams in the winner table because the Figma crest set has only those seven Spanish clubs.
- **Photos.** The Figma file has photos of eleven players. They are reused wherever that player appears; everyone else shows initials on the same round plate.
- **Crests.** From the Figma set "Football club assets 2026–27". `t_*.png` are the feed crests without their inner padding.
- **Not drawn in Figma:** the header of a live match (score + red minute), the tabs of a league page (Matches / Table / Odds / Team stats / Player stats), the team page. The page of a finished match (built from the live header and the Result / Disabled states of the odds components; outcomes that happened are worked out from the final score, the 1st-half market is left out).

### Open points of the new pages (ask Roey / Marko)

- **Winner prices.** Figma shows 3.30 in every row (a placeholder). The prototype uses demo prices from favourite to outsider, because the PRD says the list is sorted by odds.
- **Outright + match picks in one betslip.** Not in the spec. The prototype follows the existing rule: picks that share a match or a competition are labelled "Singles" in the bar, the sheet still shows Total odds.
- **Top Picks numbers.** Both cards say "01" in Figma; the prototype numbers them 01 and 02.
- **Top scorer on 375.** Built as on the "Pro Max size" frame: legal banner and chips on top, then Top Picks (the 375 frame "v3.2" has no banner and chips).
- **Goalscorer.** Two variants are drawn under "More bets"; the one with the round photo is built (Nik, 12 Nov). The market name on the betslip card is "Goalscorer", as the title in Figma (Roey's list calls it "Anytime Goalscorer").

## Not in the prototype yet

- **Bet Boost** (the second type of `Odds/Top Bet` in Figma) is not here; Top Bet is (Overview tab of a match).
- The **DAZN Bet promo banner** on top of the feed, on the **Team** page the tabs Table, Squad and Team stats, and on the **Competition** page the tabs Table, Playoff, Team stats and Player stats.
- **Live updates:** the pre-match carousel of markets, and the tabs H2H, Lineups and Stats of a match page (labels only).
- English legal texts: DAZN Bet has not sent them, the Spanish ones are shown.

Synced with the Figma components and the "Main flow", "Betslip states · PRD", "FT" and "Betting popup" sections on 10 Nov 2026. On the same day every screen was compared with Figma pixel by pixel (text positions, sizes, weights, colours, letter-spacing, icons) and the differences were fixed; icons that differed (bottom nav, status bar, DAZN Bet logo, arrows, back chevron, plus) are Figma SVG exports.

## Notes

- **Figma sync tooling is not included.** Originally the design values in the token block (lines 11–260) were extracted from Figma by a script pipeline. That tooling is not part of this handover. Values are now edited by hand; keep them in line with the Figma components.
- **Fonts.** DAZN Oscine is DAZN's proprietary typeface. Keep this package inside DAZN projects.
- **Images.** Club and competition logos come from the DAZN Graphic Assets library and are for internal mock-ups only.
