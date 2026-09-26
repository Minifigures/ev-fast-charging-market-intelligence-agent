# Market Intelligence Research Brief

**Student Name:** Marco Ayuste

**Date:** 26 September 2026

**Topic/Company:** Where should a mid-size DC fast-charging operator expand in 2026–2028? United Kingdom vs United States vs EU core (Germany and France)

---

## Decision dashboard

| Item | Summary |
|---|---|
| **Recommendation** | Prioritise the **United Kingdom** for a site-led entry: about two-thirds of motorway service areas open to competition from November 2026, and several regions are underserved. Scope **France** as phase two. **Defer the United States.** Monitor Germany for concession partnerships. |
| **Overall confidence** | **Medium.** The direction of each finding is backed by official statistics. The size of each effect is less certain, because sources define chargers differently and utilisation data is thin. |
| **Top insights** | (1) The 2023 "charging gap" in the dataset has largely closed in the UK, Germany and France; in the US the ratio is back to about its 2023 level. (2) Demand follows policy and is diverging: UK and France up, US down. (3) Utilisation and grid cost, not EV demand, are the binding constraint. (4) Competition is concentrated in the US, moderately concentrated and subsidy-shaped in Germany, and fragmented but consolidating in the UK and France. (5) The entry windows are time-bound. |
| **Top risks** | UK grid-connection delays: a 5.5-year average gap in Ofgem's June 2024 data, before the 2025–26 queue reform. The UK ZEV mandate review (consultation Aug–Oct 2026). Low utilisation: about 8% across all UK public chargers, all speeds. The US demand shock after the tax credit ended. |
| **Next 90 days** | Grid-capacity checks on shortlisted UK sites; buy UK utilisation data by charger speed and find a French source; prepare for the motorway-site tenders; monitor the ZEV mandate consultation. |

---

## 1. Research Objective

**Objective:** Decide which market a mid-size public DC fast-charging operator should prioritise for its 2026–2028 network expansion: the United Kingdom, the United States, or the EU core (Germany and France). The decision compares the three markets on four things:

- demand trajectory;
- charger supply relative to the EV fleet;
- competitive intensity;
- unit economics.

It must also be explicit about how reliable each signal is.

## 2. Scope of Research

**Included**

- **Markets:** United Kingdom; United States; EU core (Germany and France), with EU27 as a benchmark.
- **Segment:** Public DC fast charging for passenger cars. Charger definitions differ by source:
    - the dataset counts chargers above 22 kW;
    - the UK research covers 50 kW+;
    - the US research covers DC fast ports;
    - the France research covers 150 kW+ high-power charging.
- **Competitor types:** Charge point operators (CPOs), in four groups:
    - independents: InstaVolt, Osprey, Gridserve, Electra, EVgo;
    - oil-and-gas and utility-backed networks: BP Pulse, Shell Recharge, TotalEnergies, EnBW, Aral pulse;
    - automaker-backed networks: Tesla, Ionity, IONNA;
    - retailer and forecourt hosts.
- **Timeframe:** 2023 dataset baseline, external evidence from 2024 to September 2026, and a 2026–2028 decision horizon. IEA projections to 2030 are used as scenario context only.

**Excluded:** Home, workplace and fleet-depot charging; buses, vans and trucks; hardware manufacturing; financial modelling (payback, NPV, IRR); and markets outside the three candidates. China and Norway appear in the dataset only as benchmarks.

**Key constraints:** One working session in a time-limited AWS lab; three Quick Research runs (one Deep, two Fast); a 2023 cut-off for the internal dataset; and no access to paid utilisation or site-level data.

## 3. Research Approach

**Types of questions asked**

1. **Baseline questions** on the internal dataset, asked through the agent. Example: EV car stock, public fast chargers, EVs per fast charger and EV sales share for each market in 2023. These were checked against an independent recomputation (`analysis/ev_charging_gap.py`).
2. **Structured market-attractiveness questions**, one Quick Research run per market. Each run covered the same six dimensions so the three reports could be compared side by side: demand vs policy targets, charger supply growth, competitive concentration, pricing and utilisation, policy and funding, and entry risks.
3. **Counter-evidence questions:** where does the 2024–2026 evidence contradict the 2023 dataset, and which figures conflict between sources?
4. **Arithmetic and reliability checks** on specific claims, for example "the UK BEV fleet doubled" and "US ports grow 30–35% a year".
5. **Decision questions:** a ranked market priority, confidence per insight, and explicit statements of what not to conclude.

**How research effort was prioritised**

- **Dataset first.** The dataset showed the widest 2023 gap in the UK: 158 EVs per public fast charger, against 112 (US), 119 (Germany), 79 (France) and 99 (EU27). The UK therefore got the **Deep** Quick Research run (20–30 minutes). The US and EU core got **Fast** runs (5–10 minutes) as challenger checks.
- **Source rules.** Each run had preferred websites of official and industry statistics (screenshots 02, 09b, 10b):
    - UK: gov.uk, zapmap.com, smmt.co.uk, iea.org, racfoundation.org and ofgem.gov.uk.
    - US: afdc.energy.gov, energy.gov, driveelectric.gov, fhwa.dot.gov, iea.org and epa.gov.
    - EU core: the EU Alternative Fuels Observatory, europa.eu, bundesnetzagentur.de, kba.de, avere-france.org, iea.org and acea.auto.
    - Avoided in all three: reddit.com, quora.com, medium.com and social media.

    The UK research plan was revised once before it ran, widening topic 2 to cover geographic distribution (screenshot 03).
- **Benchmark against the dataset.** The Space holding the dataset was attached to each Quick Research run as a Quick asset, so every report compared its 2024–2026 findings with the 2023 figures.
- **Verification over breadth.** Remaining time went into validation rather than more research runs:
    - The agent's reliability pass, including three arithmetic checks.
    - A primary-source spot-check of 10 headline figures (Appendix D): 6 verified as written, 2 verified with a corrected citation, 1 date out of date, 1 scope error.
    - A second line-by-line review of this brief against the reports, the dataset and the agent's documents. It found the errors logged in Appendix E.

**Tools used within Amazon Quick Suite**

- **Spaces:** the "EV Fast-Charging Market Intelligence 2026-2028" Space holds:
    - the dataset and a dataset reference note;
    - the three research reports;
    - the agent's Market Analysis and Reliability Evaluation;
    - both versions of the agent's brief;
    - this brief.
- **Quick Research:** three reports, using preferred and avoided websites, Quick assets, plan revision, and export to the Space and to PDF.
- **Custom chat agent:** "Market Intelligence Agent – EV Fast Charging" (screenshots 04–06). Its instructions cover purpose, scope, source-labelling rules, a rule to show both figures when sources conflict, response formats and scope limits (no investment advice, no NPV or IRR). Its knowledge source is the Space.
- **Agent features:** code execution for dataset arithmetic and charts, table views, and document artifacts added to the Space as Word files (downloaded to `deliverables/agent_outputs/`).
- **Tests:**
    - A dataset-only test: the agent's 2023 table matches the dataset (screenshots 07a–07b).
    - A scope test: a request for IRR/payback, a stock pick and a 2035 EV-fleet forecast. The agent refused all three and cited its scope limits (screenshot 16).

Outside Quick, a standard-library Python script re-derived the 2023 dataset metrics and the 2030 STEPS stock used here. Separately, 10 cited figures were checked against their primary sources.

**Evidence of AI-assisted work** is in `screenshots/`:

| Screenshots | What they show |
|---|---|
| 01 | Space set-up |
| 02–03 | UK research set-up and revised plan |
| 04–06 | Agent configuration and knowledge source |
| 07a–07b | First agent test |
| 08, 09a–09b, 10a–10b | Research reports and their materials |
| 11a–11e | Market Analysis |
| 12a–12e | Reliability Evaluation |
| 13a–13d | Brief v1 |
| 14a–14c | Brief v2 |
| 15a–15b | Space contents |
| 16 | Scope test |

The charts are in `visuals/`.

## 4. Key Market Insights

### Insight 1: The 2023 "charging gap" has largely closed

Build-out has outrun the fleet in the UK, Germany and France. The US is back to its 2023 level.

- **Insight Summary:**
    - The internal dataset shows EVs per public fast charger rising in the UK from 69 in 2018 to 158 in 2023, which reads as a widening undersupply.
    - The 2024–2026 evidence reverses that in the UK, Germany and France, where charger counts grew faster than the fleet.
    - In the US the ratio rose in 2024 and has since fallen back to about its 2023 level, not below it.
    - A 2026 entry case built on national undersupply is therefore out of date. It now rests on where individual sites are still thin, and on how well they are used.
- **Supporting Evidence or Signals:**
    - **Dataset, 2023** (IEA Global EV Data 2024; EVs per public fast charger, chargers above 22 kW, BEV+PHEV fleet):
        - UK 158 (1.58 M EVs ÷ 10,000 chargers);
        - US 112 (4.82 M ÷ 43,000);
        - Germany 119 (2.50 M ÷ 21,000);
        - France 79 (1.57 M ÷ 20,000);
        - EU27 99, where fast chargers grew 67% in 2023.
    - **UK:**
        - Chargers rated 50 kW+ went from 10,118 devices (Jan 2024) to 28,887 chargers (1 Jul 2026) [DfT, verified].
        - The two counts are not like-for-like. DfT switched from counting devices to counting connectors in January 2026; on the old basis, July 2026's 121,171 chargers are 97,266 devices [Research: UK report].
        - The UK report's "about 66 BEVs per 50 kW+ charger" (attributed to DfT, April 2026) could not be reproduced. Recomputed as 2.1 M BEVs ÷ 28,887, it is about 73 in mid-2026 (our calculation). Either way it is far below the dataset's 158, though that figure counted BEV+PHEV per charger above 22 kW.
        - The BEV fleet grew from about 1.33 M (end-2024) to about 2.1 M (mid-2026). That is +58%, not the "doubled" the report claims.
    - **Germany:**
        - Public fast points (IEA, above 22 kW) were 21,000 in 2023.
        - DC fast points (Bundesnetzagentur) reached 40,777 (Jul 2025), 48,729 (Jan 2026) and 54,341 (Jul 2026) [Research: EU report; heise 31 Jul 2026 and electrive 4 Feb 2026, verified].
        - The EU report gives about 71 EVs (BEV+PHEV) per fast charger in mid-2025. The IEA and Bundesnetzagentur may not use the same "fast" threshold.
    - **France:**
        - Points of 150 kW and above went from 19,848 (Feb 2024) to 31,335 (Feb 2025) [Research: EU report; Avere-France].
        - The report's "about 46 EVs per high-power point" has no stated derivation. On the dataset's BEV+PHEV basis it is at least 50: the end-2023 fleet alone, 1.57 M, divided by 31,335. So 46 is probably a BEV-only figure.
        - Either way the ratio is below the 2023 baseline of 79, which counted all chargers above 22 kW.
    - **US:**
        - Public fast chargers were about 43,000 in 2023. That is the IEA figure for chargers above 22 kW, not an AFDC count of DC ports.
        - DC fast ports reached 50,428 (Dec 2024), about 68,000 (end-2025) and 76,236 (3 Sep 2026) [Research: US report; evchargingstations.com, verified].
        - On a BEV+PHEV basis, that is about 127 EVs per port at end-2024 and about 115–118 in 2025–26 (our estimate). The estimate takes 4.82 M EVs in 2023, adds about 1.6 M plug-in sales a year (from the US report's sales shares) and ignores scrappage.
        - The US report's "96–106" cannot be reproduced and is not used.
- **Why This Insight Matters:**
    - In the UK, Germany and France each charger now serves fewer EVs than in 2023, so revenue per charger falls unless a site sits where demand is still concentrated.
    - In the US, supply has only caught up with the fleet; it has not overtaken it.
    - Leadership's question changes from "which country is short of chargers?" to "which sites are short of chargers, and can we win them?".
    - The 2023 dataset alone would have pointed the operator the wrong way.
- **Signal freshness:**
    - Charger counts: UK 1 Jul 2026 (DfT, published 27 Aug 2026); Germany Jul 2026; US 3 Sep 2026; France Feb 2025.
    - The ratios are older than the counts: the UK report's 66 is April 2026 (our recomputation is mid-2026), Germany's 71 is mid-2025, and France's 46 is Feb 2025.
    - Recomputed at the latest counts, the UK, German and French ratios would be lower still. That strengthens the direction of this insight.
- **What would change our mind:** Q3/Q4 2026 statistics showing BEV fleet growth outpacing charger growth again, or UK BEVs per 50 kW+ charger (about 73 in mid-2026) rising back above ~80.

### Insight 2: EV demand follows policy and is diverging

The UK has a mandate target, France has momentum, and the US has lost its federal support.

- **Insight Summary:**
    - Policy is the biggest single driver of new-car EV demand in all four markets, though not the only one.
    - The UK ZEV mandate sets targets that rise steeply to 2028, but compliance flexibilities soften their effect on actual sales.
    - France is accelerating with demand support still in place.
    - Germany slumped when its grant ended in 2024, recovered in 2025 on fleet and corporate buying before any grant returned, and was boosted in 2026 by high fuel prices plus a new grant.
    - US demand fell sharply once the federal credit expired.
- **Supporting Evidence or Signals:**
    - **UK:**
        - BEV share was 19.6% in 2024 (381,970 cars) and 23.4% in 2025 (473,348) [SMMT, verified].
        - The mandate targets are 22% for 2024, 28% for 2025, 33% for 2026 and 52% for 2028 [Research: UK report; VETS Order].
        - Actual BEV share ran 2.4 points (2024) and 4.6 points (2025) below target, yet all manufacturers complied through borrowing, trading and CO₂ transfers [Research: UK report].
        - The penalty per car short of target was cut from £15,000 to £12,000, and borrowing was extended to 2029 [Research: UK report].
        - So the target is compliance pressure on manufacturers, not a guaranteed sales level.
        - A formal review of the mandate launched in August 2026 [Research: UK report; gov.uk].
        - Two 2026 year-to-date shares conflict: about 25% (H1 2026, Car Magazine) and about 29.8% (Jan–Aug 2026, EY/Roadgenius). Both are shown and neither is averaged.
    - **France:**
        - BEV share rose from 16.9% (2024) to 20.0% (2025).
        - H1 2026 registrations were up 62.9% year on year [ACEA, verified].
        - August 2026 set a single-month record of 38.8% [Research: EU report; Avere-France].
        - Demand support continues: the "coup de pouce" bonus replaced the bonus écologique and runs into 2026. A third social-leasing round (July 2026) offers 50,000 BEVs at capped payments of €200 a month [Research: EU report].
    - **Germany:**
        - BEV share fell from 18.4% (2023) to 13.5% (2024) after the Umweltbonus purchase subsidy ended.
        - It rose to a record 19.1% in 2025, driven mainly by fleet and corporate purchases while no grant was in force [Research: EU report].
        - H1 2026 was up 48%, driven by high fuel prices and reinforced by a new grant of up to €6,000 from 1 January 2026 [Research: EU report; heise; EU Alternative Fuels Observatory].
    - **US:**
        - The $7,500 credit expired on 30 Sep 2025. BEV share hit 12% that September, then fell below 6% in Q4 2025 [EIA, verified].
        - BEV share was 7.7% for 2025 [NADA].
        - Mid-2026 registrations were down about 31% year on year [Research: US report; single press source].
        - IEA STEPS had projected a 20% EV (BEV+PHEV) sales share for 2025 [Dataset, projection]. The actual all-plug-in share was just under 10% [Research: US report; IEA Global EV Outlook 2026], about half the projection. The 7.7% above is BEV-only and not directly comparable.
- **Why This Insight Matters:**
    - For a 2026–2028 horizon, the operator is effectively betting on policy.
    - The UK mandate's compliance pressure and France's demand support reduce downside risk on demand, though UK flexibilities mean sales can keep running below target.
    - The US needs a new incentive before demand growth resumes.
- **Signal freshness:**
    - Full-year shares cover 2023–2025.
    - 2026 figures are H1 or Jan–Aug year-to-date, and the French August record is a single month.
    - The UK review outcome is still open; the consultation runs August–October 2026.
- **What would change our mind:** A UK review that materially cuts the 2027–2028 targets, or a new US federal purchase incentive.

### Insight 3: Utilisation and grid cost, not EV demand, are the binding constraint on returns

- **Insight Summary:**
    - In every market with data, chargers are used for a small share of the day, and fixed grid costs are large.
    - The ability to secure cheap, timely grid capacity decides returns more than the size of the EV fleet does.
- **Supporting Evidence or Signals:**
    - **UK:**
        - Utilisation is about 8% (about 2 hours a day), which is the Zapmap average for all public chargers. The UK report's body labels it that way, but its summary and conclusion apply it to rapid chargers.
        - The same report gives rapid and ultra-rapid devices about 4 sessions a day of about 38 minutes (roughly 10–11% of the day). Elsewhere it assumes about 2 sessions a day. The two are not reconciled [Research: UK report].
        - Rapid and ultra-rapid devices handle 72% of sessions from 23% of devices [Research: UK report; Zapmap].
        - Grid standing charges for one operator's typical ultra-rapid hub rose from £99 a year (2022) to £8,600 (2024) [Osprey, an operator source].
        - Ofgem reported a 5.5-year average gap between requested and offered connection dates for all connecting customers (June 2024 data). The queue was then dominated by renewables and storage. This predates the reform that has since moved 221 GW out of the queue (April 2026). No post-reform or charger-specific figure was found [Research: UK report].
        - The average rapid price is about 77p/kWh, against 7–8p on a home smart tariff [Research: UK report].
    - **US:**
        - National DC fast utilisation was 16.6% in Q1 2025 [Paren] and 16.1% in mid-2025 [theevreport.com].
        - The profitability threshold is estimated at about 15% [Stable Auto via Fortune, 2024].
        - At low utilisation, demand charges can exceed 90% of a station's electricity cost [RMI rate-design guidance].
    - **EU:**
        - No German or French utilisation or payback data was found. This is a gap, not a finding.
        - The EU report's "6–12 year payback" comes from a global review of solar-powered charging stations, not grid-connected high-power charging in Germany or France, so it is not used.
- **Why This Insight Matters:**
    - Site choice should favour locations that already have grid capacity or funded network upgrades.
    - Examples are motorway service areas, retail forecourts and battery-buffered sites. Ofgem's £300 M Green Recovery Scheme, announced in 2021, funded network upgrades at 37 motorway service areas; many are complete and already host chargers.
    - Utilisation data by charger speed is the most valuable missing input.
- **Signal freshness:**
    - UK utilisation is updated quarterly; the page blocked direct access, so the wording was checked via search results. US utilisation data is 2025.
    - Grid figures: standing charges 2022–2024; connection gap June 2024 (pre-reform); queue reform April 2026. The RMI demand-charge guidance is older.
- **What would change our mind:** Published UK rapid-specific utilisation consistently above 15%, or post-reform Ofgem data showing connection times for charging sites well below the pre-reform 5.5-year average.

### Insight 4: Competition differs sharply by market

The US is concentrated; Germany is moderately concentrated and shaped by subsidy; the UK and France are fragmented but consolidating.

- **Insight Summary:**
    - A mid-size entrant faces a dominant incumbent in the US: Tesla, with about 50% of DC ports.
    - In Germany, share is only moderately concentrated: EnBW has about 16% of fast points and the top 5 about 40%. The harder barrier is the subsidised Deutschlandnetz concession network being rolled out.
    - The UK and France have more room, but consolidation is under way and capital intensity is high.
- **Supporting Evidence or Signals:**
    - **US:**
        - Tesla has 37,995 of 76,236 DC ports (49.8%, Sep 2026), down from about 54.6% in Jul 2025.
        - The "Other" network category grew 44% year on year [evchargingstations.com, verified].
        - IONNA, backed by automakers, had 1,458 ports in Sep 2026 [Research: US report]. It targets about 30,000 charging bays by 2030; the US report says "sites".
    - **Germany:**
        - End-2024 fast chargers: EnBW 6,005, Tesla 3,110, Aral pulse 2,317, Allego 1,541, EWE Go 1,531; Ionity is 8th with 1,084 [EV Boosters ranking; the EU report lists Ionity 5th].
        - Together the top 5 hold 14,504 of about 36,600 DC fast points at 1 Jan 2025. That figure is derived from 48,729 in Jan 2026, which was 33% up on the year.
        - The Deutschlandnetz programme plans about 9,000 points of 200 kW or more at more than 1,000 locations [Research: EU report]. It is a pipeline of subsidised competition rather than capacity already installed.
    - **UK:**
        - There are about 100–150 CPOs, and industry leaders expect consolidation to 5–6 players [Guardian, Feb 2026].
        - The top 5 hold about a third of all UK public chargers, AC and DC combined [Research: UK report; Drax/Zapmap]. The rapid segment is more concentrated: 8,728 ultra-rapid (150 kW+) connectors are run by just 18 networks (Sep 2025) [Research: UK report].
        - Rapid-charger counts differ by source. Zapmap (Feb 2026) lists MFG EV Power 2,789, Osprey 2,578 and BP Pulse 2,506. The UK report's own table puts InstaVolt first at about 2,600+.
        - £460 M of financing was raised in 2025–26: InstaVolt £250 M debt refinancing (May 2026), Osprey £110 M senior debt (Jul 2025) and Gridserve £100 M equity (Jul 2025).
    - **France (May 2025, points of 100 kW+, by location segment)** [Research: EU report; EV Boosters]:
        - Highways: TotalEnergies 850, Ionity 688, ENGIE Vianeo 632, Electra 323, Fastned 265.
        - Near-highway: Tesla 2,453, Powerdot 1,369, Electra 1,181 (about 1,504 in total, after a €304 M Series B).
        - Retail and urban: Powerdot 2,116, Izivia 865, IECharge 597.
        - No single operator leads every segment.
- **Why This Insight Matters:**
    - In the US, winning share means competing against Tesla's scale and IONNA's automaker funding.
    - In Germany, the practical barrier is subsidised concessions more than any one rival.
    - In the UK and France, fragmentation leaves room for a mid-size operator, but rivals' new financing sets a high bar for site acquisition.
- **Signal freshness:** US Sep 2026; UK Jul 2025 to Jul 2026; Germany end-2024 (the oldest); France May 2025.
- **What would change our mind:** A major acquiring a mid-size UK or French operator, which would signal that consolidation is closing the window. Or Tesla's US share dropping below about 40% as open networks scale.

### Insight 5: The entry windows are time-bound and favour the UK first and France second

- **Insight Summary:** Dated catalysts favour the UK and France within the 2026–2028 horizon, while US federal support is shrinking.
- **Supporting Evidence or Signals:**
    - **UK motorway sites:** Under a 2022 CMA undertaking, Gridserve will not enforce exclusive rights at about two-thirds of motorway service areas after November 2026 [gov.uk/CMA, verified].
    - **UK underserved regions:** Rapid chargers per 100,000 people, against a UK average of 41.7 [DfT, verified]:
        - Northern Ireland 19.3;
        - London 27.9;
        - Yorkshire and the Humber 36.6;
        - North East 37.1;
        - Scotland is best served at 59.1.
    - **UK funding:** The 2025 Spending Review set aside £400 M for EV charging infrastructure in England over 2026–2030, including the strategic road network. An indicative £190 M goes to the Strategic Charging Infrastructure scheme for grid upgrades at motorway service areas (consultation June–July 2026) [gov.uk].
    - **France:**
        - ADVENIR's budget is about €520 M, the envelope for its extension to end-2027 (target 250,000 points).
        - Avere-France says the programme now runs to 2030. No added budget for 2028–2030 was found.
        - France 2030's €300 M high-power-charging call (up to 40% of eligible costs) closed to new projects at the end of 2024 [IEA policy database]. It is not counted as entry-window funding.
        - A motorway master plan targets 22,000 car charging points at 150 kW across about 900 service areas by 2035 [Research: EU report].
    - **US:**
        - $503.8 M of NEVI federal charging funds was repurposed in March 2026 [FHWA notice; confirmed via search results only].
        - 84% of NEVI funds were still unobligated in May 2025 [Research: US report].
        - State money remains in California: Fast Charge California ($55 M, 2025) [Research: US report; CEC].
        - New York's $28.5 M corridor round (Dec 2024) was federal NEVI money run by NYSERDA, so it carries the same federal risk. The US report calls it a state programme.
- **Why This Insight Matters:**
    - UK motorway sites combine high traffic with a tender window that is short. Competitors with new financing (Insight 4) will bid.
    - Whether any of the 37 Green Recovery Scheme sites are among those opening to tender still needs checking.
    - France offers subsidised capital costs via ADVENIR, which suits a second phase.
- **Signal freshness:**
    - The CMA undertaking dates from 2022 and its November 2026 deadline is two months away; it needs a check for any later change.
    - ADVENIR status is as of Aug 2026. The France 2030 call closed at end-2024. The NEVI notice is from March 2026.
- **What would change our mind:** Any CMA or Gridserve update that delays or narrows the motorway opening, or cuts to ADVENIR funding.

## 5. Visual Evidence

Where each visual comes from:

- **V1–V7:** produced by Amazon Quick Research inside the three reports (exported PDFs in `deliverables/quick_research_reports/`).
- **V8:** a table view from the agent's Market Analysis.
- **V9 and V10:** charts the agent generated with code execution for its combined analysis document (`deliverables/agent_outputs/05_…docx`).

**Where to find them:**

- **Image files:** `screenshots/visuals/v1_…` to `v10_…`, and `screenshots/11b_market_analysis_comparison_table.png`.
- **Embedded copies:** all ten are embedded at the end of the PDF and Word versions of this brief. The Markdown version links to the files instead.
- **Figure numbers:** numbers printed inside the images come from the source reports; this brief refers to the images as V1–V10.
- **Excluded charts:** two flawed agent charts are kept apart in `screenshots/visuals/excluded_flawed_agent_charts/` (see Appendix E).

| # | Chart type | What the visualisation shows | How it supports an insight |
|---|---|---|---|
| V1 | Line chart with shaded compliance gap | UK BEV share (19.6% 2024, 23.4% 2025) and SMMT forecasts against ZEV mandate targets from 2024 to 2035 | **Insight 2.** The gap to target widens to about 6 points by 2027 while targets jump to 52% in 2028. The target binds manufacturers' compliance but is softened by borrowing and trading, and it is under review. |
| V2 | Stacked bar chart | UK 50 kW+ chargers split into rapid (50–149 kW) and ultra-rapid (150 kW+): 10,118 (Jan 2024, DfT devices), 17,356 (Oct 2025, DfT devices), 26,378 (end-2025, Zapmap chargers) and 28,887 (Jul 2026, DfT chargers) | **Insight 1.** Supply rose steeply, so the 2023 gap closed. The bars mix device and connector counts, so part of the rise is a change in counting method. |
| V3 | Horizontal bar chart against the UK average | Rapid chargers per 100,000 people by UK region: Northern Ireland 19.3, London 27.9 … Scotland 59.1 | **Insight 5.** Shows where local white space remains even though national supply has caught up. |
| V4 | Line chart, actual vs projection | US DC fast ports (43K to about 75K) against the IEA STEPS path (100K by 2025, 280K by 2030). The 2023 point is the IEA figure for chargers above 22 kW. | **Insights 1–2.** The US is 32% short of the 2025 projection, but demand is short of projection too, so the shortfall is not an opportunity on its own. |
| V5 | Bar chart | US DC ports by network, Sep 2026: Tesla 37,995 (49.8%) and Other 12,382 (16.2%). Networks ranked 7th to 10th (about 6,100 ports) are not drawn. | **Insight 4.** Tesla's scale and the fragmented long tail. |
| V6 | Grouped bar chart | EVs per fast charger, IEA 2023 vs latest: Germany 119 → 71, France 79 → 46 (report figure; at least 50 on the dataset's BEV+PHEV basis) | **Insight 1.** Supply outpaced the fleet in the EU core. Definitions differ, so the chart shows direction, not exact size. |
| V7 | Paired horizontal bar charts | Top high-power operators: Germany (EnBW 6,005, end-2024) and France (Tesla 3,019, May 2025). The German panel shows Ionity 5th, but EV Boosters has EWE Go (1,531) 5th and Ionity 8th. The French panel mixes location segments and draws Electra (1,504) above TotalEnergies (1,543). | **Insight 4.** Germany has one clear leader. France's leadership is split by segment; read it from the Insight 4 bullets. |
| V8 | Table view (agent output) | The 2023 dataset baseline next to the latest research for all four markets, with charger definitions labelled. This is the agent's first version: its UK utilisation cell (~8%, all chargers) sits next to the US DC-only ~16% with no caveat. The corrected table is in `deliverables/agent_outputs/01_…docx`. | **Insights 1–3.** The side-by-side comparison that the ranking rests on, read with the utilisation caveat in Insight 3. |
| V9 | Grouped bar chart (agent, from dataset and research) | EVs per fast charger, 2023 dataset baseline vs latest research: UK 158 → 66, US 112 → 101, Germany 119 → 70, France 79 → 46 | **Insight 1.** All four markets on one chart; the chart notes that definitions differ, so it shows direction only. It uses the reports' ratios. Recomputed, they are about 73 (UK), about 115–118 (US) and at least 50 (France; see Insight 1). The US bar therefore overstates the fall. |
| V10 | Line chart (agent) | US DC fast ports: about 43,000 (2023, IEA chargers above 22 kW), 50,428 (2024), about 68,000 (2025) and 76,236 (Sep 2026), with the report's "30–35% a year" marked as true for 2024→2025 only | **Insight 4.** US build-out is slowing in 2026, to about 18–19% annualised. The last point is September 2026, although the chart title says "End-of-Year". |

## 6. Confidence Assessment

| Insight | Source quality | Consistency across sources | Timeliness | Confidence |
|---|---|---|---|---|
| 1. The 2023 gap has closed (UK, Germany, France) | High: IEA, DfT, Bundesnetzagentur, AFDC-based trackers, Avere-France | Direction agrees in the UK, Germany and France. In the US the ratio fell from about 127 (end-2024) to about 115–118 (2025–26), back to the 2023 level of 112. Magnitudes are not comparable (above 22 kW vs 50 kW+ vs 150 kW+; BEV-only vs BEV+PHEV). The reports' UK 66 and US 96–106 ratios could not be reproduced. The UK "doubled" claim is wrong (+58%). DfT changed its counting method in Jan 2026. | Baseline 2023; charger counts Jul–Sep 2026 (France Feb 2025); ratios from Apr 2026 (UK), mid-2025 (Germany) and Feb 2025 (France) | **Medium.** Direction is High for the UK, Germany and France. |
| 2. Policy-driven, diverging demand | High: SMMT, ACEA, EIA, NADA, gov.uk | Sources agree on direction. The two conflicting UK 2026 year-to-date shares (~25% vs ~29.8%) are both shown. The US "−31% registrations" figure is single-sourced from the press. | Full years 2023–2025; 2026 year-to-date to August | **Medium.** Direction is High; 2026 magnitudes are Medium. |
| 3. Utilisation and grid cost bind | Mixed: Zapmap, Paren and theevreport.com (trackers); Osprey (an operator with an interest); RMI; Ofgem | Utilisation figures cover different scopes (UK all chargers vs US DC only), and the UK report's two rapid figures conflict. No EU utilisation or payback data. The grid-connection gap predates the queue reform. | Utilisation 2025–26; standing charges 2022–2024; connection gap June 2024; RMI guidance older | **Low.** Grid-cost direction is Medium; utilisation magnitudes are Low. |
| 4. Competitive structure | Medium: industry trackers (self-reported counts), press, and two Wikipedia citations in the US report (neither relied on) | Operator rankings differ by source and date. The research reports misranked Germany's top 5, mixed France's location segments and gave IONNA's target in sites instead of charging bays. All three are corrected here. | US Sep 2026; UK Jul 2025 to Jul 2026; France May 2025; Germany end-2024 | **Medium** |
| 5. Time-bound windows | High: CMA/gov.uk, DfT, FHWA, Avere-France, IEA policy database, CEC/NYSERDA | The ADVENIR end date conflicts (end-2027 in the report vs 2030 per Avere-France); the brief uses 2030 with no assumed extra budget. The France 2030 call has closed. New York's round is federal money, not state. The NEVI amount was confirmed from search results only. | CMA undertaking 2022; France 2030 call closed end-2024; everything else 2025–26 | **Medium** |

**Overall confidence level: Medium.** The direction of every insight is supported by official statistics. Three things reduce precision:

1. **Charger definitions** differ across sources.
2. **Utilisation data** is thin, with none at all for Germany or France.
3. **23 errors in AI-generated material were found** during review (Appendix E): 12 in the Quick Research reports and 11 in the agent's outputs. None is carried into this brief. The agent corrected two of its own errors (A1 and A2) when they were pointed out. The two flawed agent charts are excluded from the Visual Evidence.

## 7. Limitations and Risks

- **Missing data:**
    - No German or French utilisation data, and no EU-specific payback data.
    - No reconciled rapid-only UK utilisation figure: the UK report gives both about 4 and about 2 sessions a day. Search results cite 12.8% for 150 kW+ chargers in Q4 2025, but this was not verified and is not used.
    - No site-level traffic, grid-capacity or land-cost data, and no post-reform UK grid-connection times.
    - No price elasticity.
    - The internal dataset stops at 2023. Its 2025/2030 values are IEA scenario projections made before the US credit expired and before Germany's subsidy changes.
- **Conflicting signals:**
    - The UK "doubled" claim vs the arithmetic (+58%).
    - US port growth of "30–35% a year" (2024→25) vs about 18–19% annualised from end-2025 to 3 Sep 2026 in the same report.
    - UK 2026 year-to-date BEV share: ~25% vs ~29.8%.
    - ADVENIR ends in end-2027 (report) vs 2030 (Avere-France).
    - UK public funding: "over £1 billion" (UK report; £1.08 B in the agent's briefs) vs £400 M from the Spending Review, the only new money aimed at the charging network.
    - The UK 50 kW+ count jump partly reflects DfT's January 2026 change of counting method.
- **Potential bias or ambiguity:**
    - Operator-authored sources have an interest in the story: Osprey says costs are high, and tracker counts are self-reported.
    - One US demand figure (−31%) comes from a single press article with no URL.
    - The US report cites Wikipedia twice, including for the Tesla cost-per-stall claim; neither is used here.
    - Twenty-three AI errors were found (Appendix E), which shows that model outputs need human arithmetic and source checks.
    - Comparisons of EVs per charger across markets mix BEV-only and BEV+PHEV fleets and different kW thresholds.
- **Assumptions:**
    - A mid-size operator can bid for motorway sites and finance 150 kW+ hubs.
    - Policy stays roughly as legislated through 2028.
    - The UK's pre-reform 5.5-year connection gap (June 2024, all customer types, mostly generation and storage) is taken as indicative for charging sites; the reform's effect on demand connections is unknown.

## 8. Strategic Implications

**What decisions could this inform?**

- **Market sequencing:** Commit 2026–2027 development resources to the UK, keep France as a funded phase-two option, and move the US to monitor-only until a federal or state incentive restores demand.
- **UK site strategy:**
    - Prioritise motorway-site tenders from November 2026.
    - In site diligence, favour tendered sites with existing grid capacity. Check each one against the 37 motorway service areas with Green Recovery Scheme upgrades; no source links those 37 to the tendered sites, so this is an assumption to test.
    - Also target underserved regions: Northern Ireland, London (rapid chargers), Yorkshire and the Humber, and the North East.
    - Avoid greenfield sites that need a new grid connection.
- **Diligence to fund now:** Grid-capacity feasibility on a UK shortlist, and utilisation data by charger speed for the UK (Zapmap) and France (a source still to be found).

**Impact vs effort of recommended actions (with confidence)**

| Action | Impact | Effort | Confidence behind it |
|---|---|---|---|
| Grid-capacity check on 20–30 shortlisted UK sites | High | Low–Medium | High (grid cost and delay are the main risk) |
| Buy UK utilisation data by charger speed (Zapmap) and find a French source | High | Low | High (largest data gap) |
| Prepare motorway-site tender bids for November 2026 | High | Medium | Medium (the 2022 undertaking needs a recheck) |
| France phase-two scoping and ADVENIR application | Medium | Medium | Medium |
| Watch Germany's Deutschlandnetz concessions for partnership entry | Low–Medium | Low | Medium |
| US: monitor-only; revisit if a federal incentive returns | Low (for now) | Low | Medium |

**What should not be concluded from this research?**

- **Do not conclude any market is undersupplied from national ratios of EVs per charger.** The 2023 dataset gap has largely closed, and the ratios use different charger definitions. White space exists only at site and region level.
- **Do not conclude the UK is profitable, or unprofitable.** No payback, NPV or IRR was modelled, and the ~8% utilisation figure covers all public chargers, not rapid ones.
- **Do not conclude the US is permanently unattractive.** The weakness is policy-driven, and the US remains the largest absolute market.
- **Do not treat IEA 2025/2030 projections as forecasts, or the UK mandate as a guaranteed sales level.** The US is running at roughly half the STEPS 2025 sales-share projection. UK manufacturers complied in 2024–2025 while sales ran below target.
- **Do not rank Germany against France on EVs per charger.** France's latest count is 150 kW+ only; Germany's covers all DC fast chargers.

## 9. Summary for Leadership

**Executive Summary:**

1. The 2023 dataset's warning of a charging shortfall is out of date: since 2024, fast-charger build-out has outpaced EV fleet growth in the UK, Germany and France, and in the US it has only caught back up to its 2023 level.
2. As a result, returns now depend on winning well-connected sites and on utilisation, not on a national charger shortage.
3. Demand follows policy: the UK ZEV mandate sets a statutory target of 52% of new-car sales for 2028, currently missed through compliance flexibilities, and France is accelerating (BEV registrations up 62.9% in H1 2026), while US BEV share fell below 6% after the federal credit ended.
4. The UK is the recommended first market because about two-thirds of motorway service areas open to competition from November 2026 and underserved regions such as Northern Ireland (19.3 rapid chargers per 100,000 people vs a 41.7 UK average) remain, with France as phase two and the US deferred.
5. Overall confidence is Medium: directions are backed by official statistics, but charger definitions differ across sources, utilisation data is thin, and 23 errors in AI-generated research and agent outputs were found and kept out of this brief.
6. The immediate next steps are grid-capacity checks on a UK site shortlist, buying utilisation data by charger speed, and tracking the UK ZEV mandate consultation before any capital commitment.

---

## Appendix A. Research questions that produced the strongest evidence

These are paraphrased. Fragments of the requests are visible in screenshots 07a, 11a, 12a, 13a and 16.

1. For each market, compare 2023 EV car stock, public fast chargers and EVs per fast charger from the dataset with the latest charger counts, BEV share and utilisation from the research, labelling definitions where they differ. (Agent; produced V8.)
2. How attractive is UK public 50 kW+ charging for a mid-size entrant in 2026–2028? Cover demand vs ZEV targets, supply growth, regional gaps, competition, pricing and utilisation, policy and risks, benchmarked against the IEA 2023 baseline. (Quick Research, Deep mode; produced V1–V3.)
3. Where does the 2024–2026 evidence confirm or contradict the 2023 dataset? (Agent; Market Analysis section 3.)
4. Check three claims and show the arithmetic: UK BEV fleet "doubled"; US ports growing "30–35% a year"; Germany 119 → 71 EVs per charger. (Agent; confirmed errors R1 and R4 in Appendix E.)
5. What should leadership not conclude from this research? (Agent; Brief v1 and v2.)

## Appendix B. Contents of the Quick Space (and repository mirror)

| Space item | Repository location |
|---|---|
| IEA Global EV Data 2024.csv (full Kaggle file) | `data/IEA Global EV Data 2024.csv` |
| Focus-market filter (695 rows) | `data/iea_ev_cars_and_charging_focus_markets_2018_2030.csv` |
| DATASET_REFERENCE.md | `data/DATASET_REFERENCE.md` |
| Quick Research: UK, US, Germany/France reports | `deliverables/quick_research_reports/*.pdf` |
| Market Analysis - EV Fast Charging 2026-2028.docx (agent document) | `deliverables/agent_outputs/01_…docx`. This is the corrected version, regenerated after Brief v2; screenshots 11a–11e show the first, pre-correction version. |
| Reliability Evaluation - EV Fast Charging 2026-2028.docx (agent document) | `deliverables/agent_outputs/02_…docx`. This is the corrected version; screenshots 12a–12e show the first version. |
| Market Intelligence Brief (v1) and Market Intelligence Brief v2 (.docx, agent documents) | `deliverables/agent_outputs/03_…docx` and `04_…docx`; screenshots 13a–13d and 14a–14c |
| Combined Market Analysis and Reliability document with four agent charts (chat file, not in the Space) | `deliverables/agent_outputs/05_…docx` |
| This brief (PDF) | `deliverables/Market_Intelligence_Research_Brief.*` |

## Appendix C. Key primary sources

- **Dataset:** IEA Global EV Data 2024 (Kaggle mirror `patricklford/global-ev-sales-2010-2024`, CC BY 4.0).
- **UK:**
    - DfT EV charging infrastructure statistics (1 Jul 2026, published 27 Aug 2026).
    - SMMT full-year 2025 release (6 Jan 2026).
    - CMA motorway charging undertakings (8 Mar 2022).
    - VETS Order 2023 (gov.uk).
    - 2025 Spending Review charging allocation and Strategic Charging Infrastructure consultation (gov.uk).
    - Zapmap utilisation and network statistics.
    - Ofgem connections reform (blog, 17 Jul 2024; DESNZ/Ofgem letter, Apr 2026).
- **US:**
    - EIA Today in Energy 67144 (9 Feb 2026) and 67885.
    - NADA Dec 2025 Market Beat.
    - evchargingstations.com, DC fast charging, Sep 2026 (3 Sep 2026).
    - FHWA Notice N 4510.913 (12 Mar 2026).
    - Paren Q1 2025 industry report; theevreport.com.
    - RMI rate-design guidance.
    - IONNA announcement (ionna.com).
    - CEC Fast Charge California; NYSERDA corridor round (Dec 2024).
- **EU core:**
    - ACEA H1 2026 registrations (23 Jul 2026).
    - Bundesnetzagentur figures via heise (31 Jul 2026) and electrive (4 Feb 2026).
    - Avere-France barometers and ADVENIR page.
    - IEA policy database (France 2030).
    - EU AFIR summary (EUR-Lex).
    - EV Boosters operator rankings.

## Appendix D. Primary-source spot-check log (26 September 2026)

| # | Figure checked | Result | Note |
|---|---|---|---|
| 1 | UK 50 kW+ chargers 28,887 (1 Jul 2026); regional density NI 19.3, London 27.9, UK 41.7 | Verified | DfT statistics, published 27 Aug 2026 |
| 2 | UK BEV 381,970 (19.6%) in 2024 and 473,348 (23.4%) in 2025 | Verified; citation corrected | The figures are in SMMT's 6 Jan 2026 full-year release, not the page the report cites |
| 3 | Gridserve's exclusive motorway rights end November 2026 | Verified | CMA undertaking of 8 Mar 2022: rights not enforced after Nov 2026 (about two-thirds of motorway service areas) |
| 4 | Tesla 37,995 of 76,236 US DC ports (49.8%); "Other" up 44% | Verified | evchargingstations.com, 3 Sep 2026 |
| 5 | US credit expired 30 Sep 2025; BEV share 12% in Sep, below 6% in Q4 2025 | Verified | EIA, 9 Feb 2026 |
| 6 | $503.8 M of NEVI funds repurposed in March 2026 | Verified (search-result text; the page itself returned 403) | Exact figure $503,756,000, repurposed rather than rescinded |
| 7 | Germany DC fast points 54,341 (Jul 2026) and 48,729 (Jan 2026) | Verified; citation corrected | heise 31 Jul 2026; the January figure is from electrive, 4 Feb 2026 |
| 8 | ADVENIR extended to end-2027 with €200 M more (about €520 M total) | Amount verified; end date out of date | Avere-France now says the programme runs to 2030 |
| 9 | France H1 2026 BEV registrations +62.9% | Verified | ACEA, 23 Jul 2026 |
| 10 | UK rapid utilisation about 8% (about 2 hours a day) | Wrong scope | The figure is Zapmap's average for all public chargers, not rapid chargers |

## Appendix E. Errors found in AI-generated material

None of these errors is carried into this brief.

| ID | Where | Error | Correct figure or handling |
|---|---|---|---|
| R1 | UK Quick Research report | BEV fleet "doubled" from about 1.33 M to about 2.1 M, in the summary and the body | +58% |
| R2 | UK report | Summary and conclusion apply the ~8% all-charger utilisation to rapid chargers | The body labels it correctly; the brief uses the all-charger scope |
| R3 | UK report | "Over £1 billion" of funding counts the £400 M twice (as SCI and as the Spending Review) | Itemised; only the £400 M is new charging-network money |
| R4 | US report | "30–35% a year" growth in DC ports, against its own later figures | True for 2024→25; about 18–19% annualised from end-2025 to 3 Sep 2026 |
| R5 | US report | "96–106 EVs per port" | Cannot be reproduced; recomputed at about 115–118 (2025–26) |
| R6 | US report | IONNA "targets 30,000 sites" | The target is about 30,000 charging bays |
| R7 | US report | New York's $28.5 M described as a state programme | It is a round of federal NEVI money |
| R8 | EU report | Germany's top 5 lists Ionity 5th | EWE Go (1,531) is 5th; Ionity (1,084) is 8th |
| R9 | EU report | France's top 5 mixes location segments | Reported by segment |
| R10 | EU report | "6–12 year payback" for Germany and France | Taken from a global review of solar-powered charging; not used |
| R11 | EU report | ADVENIR "extended to end-2027" | Now runs to 2030 (Avere-France) |
| R12 | EU report | France 2030's €300 M presented as current support | The call closed at end-2024 |
| A1 | Agent reliability table (first version) | UK 2023 EV sales share given as 22.3%, with a "dip" to 19.6% | The dataset says 24% (BEV+PHEV), which is not comparable with a BEV-only share; corrected by the agent before Brief v1 |
| A2 | Agent Brief v1 | Scotland and Wales listed as underserved | Scotland is best served (59.1); corrected by the agent in Brief v2 |
| A3 | Agent Briefs v1 and v2 | UK ranked first partly on ">£1B" / "£1.08B" of public funding | Only the £400 M applies to the charging network |
| A4 | Agent Market Analysis | France's HPC-only count means "the true DC fast ratio is higher" | Backwards: counting all DC chargers lowers the ratio |
| A5 | Agent Reliability Evaluation | US port growth 2023→24 of "+17.3%", mixing IEA chargers above 22 kW with DC ports | The report's own figures imply about +36% |
| A6 | Agent Reliability Evaluation | Says the UK report's body text is "more careful" than its summary | The body also says "doubled" |
| A7 | Agent Reliability Evaluation | France's +62.9% called an EU-wide ACEA figure | It is France-specific |
| A8 | Agent documents (corrected versions) | "ADVENIR runs to 2030" cited to the EU report | The 2030 date came from the primary-source check (Appendix D) |
| A9 | Agent Briefs v1 and v2 | About 920 words of prose against the agent's own 600-word limit | Noted; this brief is the leadership deliverable |
| A10 | Agent chart (excluded) | US operator pie shows Tesla at 54.2% | It divides by 70,095 listed ports instead of the 76,236 total; the correct share is 49.8% |
| A11 | Agent chart (excluded) | BEV-share bar chart compares France's single-month 38.8% with full-year and year-to-date shares elsewhere | Excluded |
