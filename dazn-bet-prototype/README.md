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
public/assets/img/  43 PNGs and SVGs: club crests, competition logos, nav and header icons, DAZN Bet logo
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

The device switcher at the top toggles iPhone 13 mini (375) and iPhone 17 Pro Max (440). **Reset ⟲** (bottom right) restarts from the initial state. **Scenarios** (bottom left) triggers the states that the real app gets from DAZN Bet.

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
7. **Fixture page.** Tap the Real Madrid v Atlético Madrid tile to open the Odds tab with the pre-match markets: Match Results, Total Goals, BTTS, Double Chance, 1st-half goals, Result & Both teams to score, Draw no bet. Picks stay in sync with the feed.
8. **Finished matches.** Tap **Sat 3 Jan** in the calendar (or the scenario). FT tiles keep their last odds, nothing is tappable, the outcome that happened is white and the rest are grey. **Today** goes back.

## Scenarios panel

| Button | What it shows |
|---|---|
| Favourite team popup | "Real Madrid play today" with 1X2 over the feed. The favourite team's win is preselected; tapping another odd moves the highlight; "Add to my Betslip" closes the popup and the pick sits in the bar. |
| Finished matches (yesterday) | Same as tapping Sat 3 Jan. |
| Odds change on my pick | The price of a pick moves (up, then down, alternating). In the betslip the card price, Total odds and the bar total show an arrow and take its colour for about 5 s; the return is recalculated. |
| Suspend my pick | The bet is cancelled by DAZN Bet: the card dims and reads "Suspended", its odd in the feed shows a lock, it leaves Total odds but still counts. |
| Lock my pick | Same, with a lock instead of "Suspended". |
| Lock a market in the feed | Chelsea v Newcastle: all three odds show a lock and are not tappable. Press again to unlock. |
| Fill betslip to 20 | Tops the betslip up to the maximum. Counters turn orange, the sheet ends with "Maximum number of selections allowed is 20", and tapping any other odd only shows that message as a toast. |
| Restore odds | Clears suspended and locked states. |

The three "my pick" buttons act on a live 1X2 pick if there is one and add "Real Madrid to win" if the betslip is empty. If every pick is suspended or locked, the sheet shows Total odds 0, no return line and a disabled button.

## Where things live in `public/index.html`

| Lines (approx.) | What |
|---|---|
| 11–262 | Design tokens and component values originally generated from Figma (spacing, colours, type, radii per component). Change values here, not inline. |
| 264–675 | Hand-written layout CSS: feed, legal banner and footer, tiles, odds tile states, nav, bar, toast, sheet, cards, fixture, popup, scenario panel |
| 676–803 | Markup: status bar, header, calendar, feed, fixture, bar, nav, sheet, popup, toast, overlay, scenario panel |
| 806–856 | `IMG` asset map, `EXTRA` (matches used only by "Fill betslip to 20"), `INIT` (the 8 demo matches), `FT` (yesterday), `FX` (Odds-tab markets) — edit demo data here |
| 858–900 | Feed: `tileHTML()`, `renderFeed()`, Odds toggle, day switch |
| 901–952 | Selections, limit of 20, `act()` (picks that still have a price), `betType()`, totals, collapsed bar |
| 953–1043 | Sheet: cards, `applyEdit()` / `releaseHeight()`, `updateSummary()`, remove + Undo, overlay |
| 1044–1107 | Live engine: `liveTick()`, `changeOdd()`, `animateOdd()` (odds animation timings), event flash, arrows |
| 1108–1129 | Fixture Odds tab |
| 1130–1179 | Favourite-team popup and `runScn()` (scenarios) |
| 1180–1247 | Event wiring, drag-to-close, device fit, `init()` |

## Showing it on a call: ready-made states and walkthrough

- **Scenarios panel (left).** 27 numbered states in five groups: Flow, Odds change, Suspended, Locked, Limit 20, More. One click sets the whole screen (picks, statuses, prices, sheet open or closed), whatever was on screen before. The groups follow the rows of the Figma section "Betslip states · PRD".
- **Walkthrough.** The same 27 states are one story. Step with the **→ / ←** keys or the arrows on the card to the right of the phone; the card shows the step number, its name and the rule it demonstrates.
- **Repeatable numbers.** A ready-made state pauses the live price ticker and uses fixed prices, so the totals are the same every time (for example Odds changed: 16.97 → 17.06). Arrows and the limit toast stay on screen while the state is shown. Only "Live odds moving" lets prices tick. The **L** key or the "Live odds" button at the bottom of the panel pauses and resumes the ticker.
- **On the current betslip.** The old triggers are still at the bottom of the panel for free play: change the price of my pick (fixed 5 % step), suspend it, lock it, lock a market, fill to 20, restore.
- **Reset ⟲** returns to free play with live prices moving.
- To add or reorder a state, edit the `STATES` array in `index.html`: `g` = group, `t` = name, `n` = note on the card, `run()` = what to set.

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

## Not in the prototype yet

- **Top Bet / Bet Boost** cards exist in Figma (`Odds/Top Bet`, `.Bet/Price button`) but not here.
- The **DAZN Bet promo banner** on top of the feed, and odds on the **Competition** and **Team** pages.
- **Live Updates** carousels after match events.
- English legal texts: DAZN Bet has not sent them, the Spanish ones are shown.

Synced with the Figma components and the "Main flow", "Betslip states · PRD", "FT" and "Betting popup" sections on 10 Nov 2026. On the same day every screen was compared with Figma pixel by pixel (text positions, sizes, weights, colours, letter-spacing, icons) and the differences were fixed; icons that differed (bottom nav, status bar, DAZN Bet logo, arrows, back chevron, plus) are Figma SVG exports.

## Notes

- **Figma sync tooling is not included.** Originally the design values in the token block (lines 11–260) were extracted from Figma by a script pipeline. That tooling is not part of this handover. Values are now edited by hand; keep them in line with the Figma components.
- **Fonts.** DAZN Oscine is DAZN's proprietary typeface. Keep this package inside DAZN projects.
- **Images.** Club and competition logos come from the DAZN Graphic Assets library and are for internal mock-ups only.
