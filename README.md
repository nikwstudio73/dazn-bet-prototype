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
public/assets/img/  71 PNGs and SVGs: club crests, player photos, competition logos, nav and header icons, DAZN Bet logo
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

1. **Scores feed.** The Odds toggle in the header shows or hides the odds under each match, together with the gambling warning on top and the "+18. Juega con responsabilidad. Publi." footer. Odds tiles show 3-letter team codes and X. Tapping the LIVE badge filters to live matches. Live odds move every 2.6 s: the tile flashes, then a green or red line plus arrow stay about 2 s and fade out together.
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
7. **Fixture page.** Tap the Real Madrid v Atlético Madrid tile to open the Odds tab with the pre-match markets: Match Results, Total Goals, BTTS, Double Chance, 1st-half goals, Result & Both teams to score, Draw no bet. Picks stay in sync with the feed. Under "More bets on DAZN Bet" there is a **Goalscorer** carousel ("In this match", round photo): every player is his own pick, so several can be in the betslip.
8. **Finished matches.** Tap **Sat 3 Jan** in the calendar (or the state *Other screens → Finished matches*). FT tiles keep their last odds, nothing is tappable, the outcome that happened is white and the rest are grey. **Today** goes back.
9. **Competition page · Odds tab.** Tap the **UEFA Champions League** header in the feed. The page has the tabs Matches / Table / Odds / Playoff / Team stats (only Odds is built) and sub-tabs as chips:
   - **Competition winner:** a table of teams with the price to win the season.
   - **Top scorer** (Figma "Top scorer v3.2"): two **Top Picks** cards, then the list of players. A picked Top Pick turns white as a whole, with the price on a dark tile.
   - **Relegation:** the chip is in the design, its content is not designed, so it does nothing.
   - These are outright (season-long) picks. One pick per market: tapping another team or player replaces it. In the betslip the card shows the competition and the season instead of a match. The collapsed bar and the bottom nav stay on screen.

## Navigation: the "Prototype states" panel

One panel on the left, nothing else on screen except the phone and the phone-size switch.

- **Free play** (selected when the page opens). Everything on the phone works by hand. Clicking it again, or the round arrow next to it, starts over.
- **Topics.** Betslip, Suspended, Locked, Limit 20, Other screens. They hold only what cannot be reached by tapping the phone (a price that moves in a pick, suspended and locked bets, the limit of 20) plus three screens that are not obvious to find. The main flow (Odds toggle, picks, betslip, Edit, Place bet) is done by hand in Free play; its description says what to try. A topic opens its states; only one topic is open at a time. Opening a topic does not change the phone. A dot next to a folded topic marks where the current state lives.
- **States.** One click sets the whole screen (picks, statuses, prices, sheet open or closed), whatever was on screen before. The selected state shows one or two lines about the rule it demonstrates. Click it again, or the round arrow, to start the same state again.
- **Collapsed / Opened.** States that exist with the betslip folded and unfolded are one row with this switch. If you open or close the betslip on the phone by hand, the switch follows.
- The **‹** button folds the panel into a small "States" button (it starts folded in windows narrower than 1000 px).
- The panel and the phone-size switch use the same Global foundation tokens as the product UI (`--ui-*` variables in the CSS, each with its token name). The only accent is white (text/primary); no brand yellow and no orange outside the phone.

### Motion

One system everywhere. The tokens live at the top of the hand-written CSS (`MOTION TOKENS`) and are mirrored in JS (`SOFT`, `T`); use them instead of new numbers.

| Token | Value | Used for |
|---|---|---|
| `--soft` | `cubic-bezier(.32,.72,0,1)` | anything that travels or resizes: sheets, bar, toast, odds reveal, pages, text swaps |
| `--ease` | `cubic-bezier(.2,.8,.2,1)` | state changes in place: colour, press, small moves |
| `--m-press` | .12 s | press feedback |
| `--m-quick` | .2 s | colour, opacity |
| `--m-std` | .32 s | an element enters, a text swaps, a card collapses |
| `--m-layout` | .44 s | heights and pages: odds reveal, sheet resize, fixture push |
| `--m-sheet` | .5 s | sheets, collapsed bar, toast, DAZN Bet overlay |

JS helpers: `soft()` (play an element in), `setTxt()` (swap a text), `smoothH()` (ease a height), `rise(dir)` (start position of a new number). With **Reduce motion** switched on in the system nothing travels, springs or pulses; states still change.

- **Odds toggle:** visible cards open one after another, prices fade in and rise, the gambling banner and the footer collapse and expand with the cards (`--o-*` variables, cascade in `setOddsOn()`). If the feed is scrolled, the first visible tile stays where it is (`holdAnchor()`).
- **A price moves — one pattern everywhere** (feed tile, the same tile on the fixture page, betslip card, Total odds, bar total): the new number comes in along the direction of the move (up: rises from below, down: drops from above) and an arrow shows the direction. A tile that is not picked keeps tint + arrow about 2 s and fades 1.5 s. Everything that belongs to my pick (its tile, its card, the totals) keeps the arrow about 5 s and fades .6 s (`CHG_T` in JS, `--chg-*` in CSS). The arrow in the bar grows and shrinks in width, so the total pill does not jump.
- **Collapsed betslip:** appears with a short rise and fade; the selection list, bet type and total swap softly when they change. It does not hide for the sheet: the sheet slides over it and uncovers it again.
- **Sheets (betslip, favourite-team popup):** native iOS behaviour: slide up from the bottom edge (`--soft`, `--m-sheet`), the dimming fades with it. Drag by the handle or by the header: the sheet follows the finger, the dimming lightens, pulling up gives a little rubber band. Releasing past a quarter of the height or with a quick flick closes it, otherwise it springs back; either way the release continues at the speed of the finger (`dragSheet()`).
- **Inside the sheet:** a pick that becomes Suspended or Locked dims softly and its price swaps with a small rise; the summary and the limit message change height smoothly. "Goal!" fades in and out.
- **Edit mode:** the × buttons appear one card after another, only for the cards on screen (max 6 steps). A removed card collapses on its own; several can be removed quickly one after another.
- **Limit 20 · tap on a 21st odd** (Figma N): nothing is added; the tapped odd gets a light press and a small spring back (no colour), an orange tongue slides out from behind the collapsed betslip ("You’ve reached maximum number of bets allowed.") and the counter pulses; the tongue hides after ~2.6 s (`denyLimit()`). With the sheet open the toast is used instead.
- **Feed:** switching the day slides the list in from the side of that day (yesterday from the left, today from the right); the LIVE filter fades it in from below (`swapFeed()`). A tapped odd changes text colour together with its background.

### Club crests

`public/assets/img/{ars,ath,atm,bar,bay,che,liv,mci,new,psg,psv,rm,val,vil}.png` are exported from the Graphic Assets library (`Football-club-logo`) in the proportions of the 28 px slot of the match tile.

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
| 1108–1129 | Fixture Odds tab |
| 1130–1179 | Favourite-team popup, `STATES` (ready-made states), `setState()`, `buildNav()` / `paintNav()` (navigation panel) |
| 1180–1247 | Event wiring, drag-to-close, device fit, `init()` |

## Showing it on a call: ready-made states

- **24 screens in 17 rows.** Seven rows are a Collapsed / Opened pair. The topics follow the rows of the Figma section "Betslip states · PRD".
- **Keyboard.** **→ / ←** step through all 24 screens in order (the panel follows). **L** pauses and resumes the live price ticker.
- **Repeatable numbers.** A ready-made state pauses the live price ticker and uses fixed prices, so the totals are the same every time (for example Odds changed: 16.97 → 17.06). Arrows and the limit message stay on screen while the state is shown. Free play turns the ticker back on.
- To add or reorder a state, edit the `STATES` array in `index.html`: `g` = topic, `k` = name of the row, `v` = `'bar'` / `'sheet'` for a Collapsed / Opened pair (two neighbouring entries with the same `g` and `k`), `n` = the note under the row, `run()` = what to set. The panel is built from this array.

## Product rules baked in

- Odds math: total = product of the odds that still have a price; return = €10 × total.
- Maximum 20 picks. At the limit no odd can be added or swapped; removing a pick lifts the limit.
- At the limit the message "Maximum number of selections allowed is 20" is pinned above the button (orange icon + text, no box), so it is visible as soon as the sheet opens.
- Dropped picks (suspended / locked) are explained by a small second line under "Total odds": "Excludes N suspended selection(s)" (or "locked", or "unavailable" when both kinds are present). When no active pick is left the total shows a dash and the line reads "Your selection is locked / suspended"; the collapsed bar shows a dash too (the PRD says 0; open with the PM).
- A selected tile whose price moves stays white and shows a dark green / dark red arrow next to the price.
- A suspended or locked pick stays in the betslip and in the count, leaves the total, and is not sent to DAZN Bet. Its odd is not tappable; it can be removed in Edit mode.
- While a pick is **locked**, the total is struck through and "Place bet on DAZN Bet" is disabled (Figma screen J). A suspended pick does not block the button.
- Picks on the same match are labelled "Singles" in the bar, but the sheet still shows Total odds. This is open with the PM.
- There is no stake input and no login. DAZN Bet handles those inside its overlay.
- Legal copy (top warning, footer, text under the summary) is fixed by legal; don't rewrite it.

### Open points of the new pages (ask Roey / Marko)

- **Winner prices.** Figma shows 3.30 in every row (a placeholder). The prototype uses demo prices from favourite to outsider, because the PRD says the list is sorted by odds.
- **Outright + match picks in one betslip.** Not in the spec. The prototype follows the existing rule: picks that share a match or a competition are labelled "Singles" in the bar, the sheet still shows Total odds.
- **Top Picks numbers.** Both cards say "01" in Figma; the prototype numbers them 01 and 02.
- **Top scorer on 375.** Built as on the "Pro Max size" frame: legal banner and chips on top, then Top Picks (the 375 frame "v3.2" has no banner and chips).
- **Goalscorer.** Two variants are drawn under "More bets"; the one with the round photo is built (Nik, 12 Nov). The market name on the betslip card is "Goalscorer", as the title in Figma (Roey's list calls it "Anytime Goalscorer").

## Not in the prototype yet

- **Top Bet / Bet Boost** cards exist in Figma (`Odds/Top Bet`, `.Bet/Price button`) but not here.
- The **DAZN Bet promo banner** on top of the feed, odds on the **Team** page, and on the **Competition** page everything except the Odds tab (Matches tab with 1X2, Relegation sub-tab).
- **Live Updates** carousels after match events.
- English legal texts: DAZN Bet has not sent them, the Spanish ones are shown.

Synced with the Figma components and the "Main flow", "Betslip states · PRD", "FT" and "Betting popup" sections on 10 Nov 2026. On the same day every screen was compared with Figma pixel by pixel (text positions, sizes, weights, colours, letter-spacing, icons) and the differences were fixed; icons that differed (bottom nav, status bar, DAZN Bet logo, arrows, back chevron, plus) are Figma SVG exports.

## Notes

- **Figma sync tooling is not included.** Originally the design values in the token block (lines 11–260) were extracted from Figma by a script pipeline. That tooling is not part of this handover. Values are now edited by hand; keep them in line with the Figma components.
- **Fonts.** DAZN Oscine is DAZN's proprietary typeface. Keep this package inside DAZN projects.
- **Images.** Club and competition logos come from the DAZN Graphic Assets library and are for internal mock-ups only.
