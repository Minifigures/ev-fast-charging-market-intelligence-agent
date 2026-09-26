# Market Intelligence Research Brief

**Student Name:** Marco Ayuste

**Date:** 26 September 2026

**Topic/Company:** Where should a mid-size DC fast-charging operator expand in 2026–2028? United Kingdom vs United States vs EU core (Germany and France)

---

## Decision dashboard

| Item | Summary |
|---|---|
| **Recommendation** | Prioritise the **United Kingdom** for a site-led entry (motorway service areas opening from November 2026, plus underserved regions). Scope **France** as phase two. **Defer the United States**; monitor Germany for concession partnerships. |
| **Overall confidence** | **Medium.** Direction is backed by official statistics; magnitudes are weakened by charger-definition mismatches and thin utilisation data. |
| **Top insights** | (1) The 2023 "charging gap" in the dataset has largely closed. (2) Demand is policy-driven and diverging: UK/France up, US down. (3) Utilisation and grid cost, not EV demand, are the binding constraint. (4) Competition is concentrated in the US and Germany and fragmented in the UK and France. (5) The entry windows are time-bound. |
| **Top risks** | UK grid-connection queues (5.5-year average gap); UK ZEV mandate review (Aug–Oct 2026); low utilisation (UK ~8% across all public chargers); US demand shock after the tax credit ended. |
| **Next 90 days** | Grid-capacity checks on shortlisted UK sites; buy rapid-specific utilisation data (UK, France); prepare for the motorway-site tenders; monitor the ZEV mandate consultation. |

---

## 1. Research Objective

**Objective:** Decide which market a mid-size public DC fast-charging operator should prioritise for its 2026–2028 network expansion: the United Kingdom, the United States, or the EU core (Germany and France). The decision needs to compare four things across the three markets: demand trajectory, charger supply relative to the EV fleet, competitive intensity, and unit economics. It must also be explicit about how reliable each signal is.

## 2. Scope of Research

**Included**

- **Markets:** United Kingdom; United States; EU core (Germany and France), with EU27 as a benchmark.
- **Segment:** Public DC fast charging for passenger cars. The dataset counts chargers above 22 kW; the external research covers 50 kW+ (UK), DC fast ports (US) and 150 kW+ high-power charging (France).
- **Competitor types:** Charge point operators (CPOs), including independents (InstaVolt, Osprey, Gridserve, Electra, EVgo), oil-and-gas and utility-backed networks (BP Pulse, Shell Recharge, TotalEnergies, EnBW, Aral pulse), automaker-backed networks (Tesla, Ionity, IONNA) and retailer/forecourt hosts.
- **Timeframe:** 2023 dataset baseline, external evidence from 2024 to September 2026, and a 2026–2028 decision horizon. IEA projections to 2030 are used as scenario context only.

**Excluded:** Home, workplace and fleet-depot charging; buses, vans and trucks; hardware manufacturing; financial modelling (payback, NPV, IRR); and markets outside the three candidates. China and Norway appear in the dataset only as benchmarks.

**Key constraints:** One working session in a time-limited AWS lab; three Quick Research runs (one Deep, two Fast); a 2023 cut-off for the internal dataset; and no access to paid utilisation or site-level data.

## 3. Research Approach

**Types of questions asked**

1. **Baseline questions** on the internal dataset, asked through the agent. Example: EV car stock, public fast chargers, EVs per fast charger and EV sales share for each market in 2023, checked against an independent recomputation (`analysis/ev_charging_gap.py`).
2. **Structured market-attractiveness questions**, one Quick Research run per market. Each run covered the same six dimensions (demand vs policy targets, charger supply growth, competitive concentration, pricing and utilisation, policy and funding, entry risks) so the three reports could be compared side by side.
3. **Counter-evidence questions:** where does the 2024–2026 evidence contradict the 2023 dataset, and which figures conflict between sources?
4. **Arithmetic and reliability checks** on specific claims, for example "the UK BEV fleet doubled" and "US ports grow 30–35% a year".
5. **Decision questions:** a ranked market priority, confidence per insight, and explicit statements of what not to conclude.

**How research effort was prioritised**

- **Dataset first.** The dataset showed the widest 2023 gap in the UK: 158 EVs per public fast charger, against 112 (US), 119 (Germany), 79 (France) and 99 (EU27). The UK therefore got the **Deep** Quick Research run (20–30 minutes). The US and EU core got **Fast** runs (5–10 minutes) as challenger checks.
- **Source rules.** Official and industry-statistics sites were set as preferred websites: gov.uk/DfT, SMMT, Ofgem, Zapmap, IEA, AFDC/DOE, FHWA, EIA, ACEA, Bundesnetzagentur, Avere-France and the EU Alternative Fuels Observatory. Reddit, Quora, Medium and social media were set as websites to avoid. The UK research plan was reviewed and revised before it ran.
- **Benchmark against the dataset.** The Space holding the dataset was attached to each Quick Research run as a Quick asset, so every report compared its 2024–2026 findings with the 2023 figures.
- **Verification over breadth.** Remaining time went into validation rather than more research runs:
    - The agent's reliability pass.
    - Three arithmetic checks.
    - A primary-source spot-check of 10 headline figures (6 verified as written, 2 verified with a corrected citation, 1 date out of date, 1 scope error).

**Tools used within Amazon Quick Suite**

- **Spaces:** the "EV Fast-Charging Market Intelligence 2026-2028" Space holds the dataset, a dataset reference note, the three research reports, the Market Analysis, the Reliability Evaluation and both versions of the brief.
- **Quick Research:** three reports, using preferred and avoided websites, Quick assets, plan revision, and export to the Space and PDF.
- **Custom chat agent:** "Market Intelligence Agent – EV Fast Charging". It has a purpose statement, scope, source-labelling rules, a rule to show both figures when sources conflict, response formats and scope limits (no investment advice, no NPV or IRR). Its knowledge source is the Space.
- **Agent features:** code execution for dataset arithmetic, table views, and document artifacts added to the Space as Word files.
- **Scope test:** a request for IRR/payback, a stock pick and a 2035 EV-fleet forecast. The agent refused all three and cited its scope limits (screenshot 16).

Outside Quick, a standard-library Python script re-derived every dataset metric, and 10 cited figures were checked against their primary sources.

Evidence of AI-assisted work is in `screenshots/`: Space set-up (01), research set-up and plan (02–03), agent configuration and first test (04–07), research reports (08–10), Market Analysis (11a–11e), Reliability Evaluation (12a–12e), Brief v1 (13a–13d), Brief v2 (14a–14c), the Space contents (15a), a scope test (16), and the charts from the research reports (`visuals/`).

## 4. Key Market Insights

### Insight 1: The 2023 "charging gap" has largely closed; build-out is now outrunning the fleet in every market

- **Insight Summary:** The internal dataset shows EVs per public fast charger rising in the UK from 69 in 2018 to 158 in 2023, which reads as a widening undersupply. The 2024–2026 evidence reverses that: charger counts grew faster than the fleet in all four markets. A 2026 entry thesis built on national undersupply is out of date. The case now rests on where individual sites are still thin, and on how well they are used.
- **Supporting Evidence or Signals:**
    - **Dataset, 2023** (IEA Global EV Data 2024; EVs per public fast charger, chargers above 22 kW, BEV+PHEV): UK 158 (1.58 M EVs ÷ 10,000 chargers); US 112 (4.82 M ÷ 43,000); Germany 119 (2.50 M ÷ 21,000); France 79 (1.57 M ÷ 20,000); EU27 99, where fast chargers grew +67% in 2023.
    - **UK:** 50 kW+ chargers went from 10,118 (Jan 2024) to 28,887 (1 Jul 2026) [Research: UK report; DfT statistics, verified]. That is about 66 BEVs per 50 kW+ charger by mid-2026 [Research: UK report, DfT Apr 2026]. The BEV fleet grew from about 1.33 M (end-2024) to about 2.1 M (mid-2026). That is +58%; the report's claim that it "doubled" is wrong.
    - **Germany:** DC fast points went from 21,000 (2023) to 40,777 (Jul 2025) to 48,729 (Jan 2026) to 54,341 (Jul 2026) [Research: EU report; Bundesnetzagentur via heise/electrive, verified]. That gives about 71 EVs per fast charger in mid-2025.
    - **France:** 150 kW+ points went from 19,848 (Feb 2024) to 31,335 (Feb 2025) [Research: EU report; Avere-France]. That gives about 46 EVs per high-power point.
    - **US:** DC fast ports went from 43,000 (2023) to 50,428 (Dec 2024), about 68,000 (end-2025) and 76,236 (Sep 2026) [Research: US report; evchargingstations.com, verified]. That gives about 96–106 EVs per port.
- **Why This Insight Matters:** Each charger now serves fewer EVs than in 2023, so revenue per charger falls unless a site sits where demand is still concentrated. It changes the question leadership should ask, from "which country is short of chargers?" to "which sites are short of chargers, and can we win them?". It also means the 2023 dataset alone would have pointed the operator the wrong way.
- **Signal freshness:** UK 1 Jul 2026 (DfT, published 27 Aug 2026); Germany Jul 2026; US Sep 2026; France Feb 2025. The France figure is the oldest; the other three are current.
- **What would change our mind:** Q3/Q4 2026 statistics showing BEV fleet growth outpacing charger growth again, or UK BEVs per 50 kW+ charger rising back above ~80.

### Insight 2: EV demand is policy-driven and diverging; the UK has a statutory floor, France has momentum, the US has lost its federal support

- **Insight Summary:** New-car demand in all four markets tracks policy almost one-for-one. The UK ZEV mandate sets a legal floor that rises steeply to 2028. France is accelerating with subsidies extended. Germany recovered after cutting and then reintroducing grants. The US fell sharply once the federal credit expired.
- **Supporting Evidence or Signals:**
    - **UK:**
        - BEV share was 19.6% in 2024 (381,970 cars) and 23.4% in 2025 (473,348) [SMMT, verified].
        - The mandate targets 28% for 2025, 33% for 2026 and 52% for 2028 [Research: UK report; VETS Order].
        - A formal review of the mandate launched in August 2026 [Research: UK report; gov.uk].
        - Two 2026 year-to-date shares conflict: about 25% (H1 2026, Car Magazine) and about 29.8% (Jan–Aug 2026, EY/Roadgenius). Both are shown and neither is averaged.
    - **France:** BEV share rose from 16.9% (2024) to 20.0% (2025). H1 2026 registrations were +62.9% year on year [ACEA, verified], and August 2026 set a monthly record of 38.8% [Research: EU report; Avere-France].
    - **Germany:** BEV share fell from 18.4% (2023) to 13.5% (2024) after the purchase subsidy (Umweltbonus) ended, then rose to 19.1% (2025). H1 2026 was +48%, helped by a new grant of up to €6,000 from January 2026 [Research: EU report; ADAC/KBA/heise].
    - **US:**
        - The $7,500 credit expired on 30 Sep 2025. BEV share hit 12% that September, then fell below 6% in Q4 2025 [EIA, verified].
        - BEV share was 7.7% for 2025 [NADA].
        - Mid-2026 registrations were down about 31% year on year [Research: US report; single press source].
        - IEA STEPS had projected 20% for 2025 [Dataset, projection].
- **Why This Insight Matters:** For a 2026–2028 horizon, the operator is effectively betting on policy. The UK floor and French subsidies reduce downside risk on demand. The US needs a new incentive before demand growth resumes.
- **Signal freshness:** All figures are from Jan–Sep 2026 except the US 2025 annual figure. The UK review outcome is still open; the consultation runs August–October 2026.
- **What would change our mind:** A UK review that materially cuts the 2027–2028 targets, or a new US federal purchase incentive.

### Insight 3: Utilisation and grid cost, not EV demand, are the binding constraint on returns

- **Insight Summary:** In every market with data, chargers are used for a small share of the day, and fixed grid costs are large. The ability to secure cheap, timely grid capacity decides returns more than the size of the EV fleet does.
- **Supporting Evidence or Signals:**
    - **UK:**
        - Utilisation is about 8% (about 2 hours a day). Our fact-check found this is the Zapmap average for all public chargers, not rapid chargers as the research report implied.
        - Rapid and ultra-rapid devices handle 72% of sessions from 23% of devices [Research: UK report; Zapmap].
        - Grid standing charges for an ultra-rapid hub rose from £99 a year (2022) to £8,600 (2024), according to an operator source (Osprey).
        - The average gap between requested and offered grid-connection dates is 5.5 years, for all connecting customers [Research: UK report].
        - The average rapid price is about 77p/kWh, against 7–8p on a home smart tariff [Research: UK report].
    - **US:**
        - National DC fast utilisation was 16.6% (Q1 2025) and 16.1% (mid-2025) [Paren].
        - The profitability threshold is estimated at about 15% [Stable Auto via Fortune, 2024].
        - At low utilisation, demand charges can exceed 90% of a station's electricity cost [RMI].
    - **EU:**
        - Estimated payback is 6–12 years [Springer, 2025].
        - No German or French utilisation data was found. This is a gap, not a finding.
- **Why This Insight Matters:** Site choice should favour locations that already have grid capacity or funded network upgrades. Examples are motorway service areas (Ofgem's £300 M Green Recovery Scheme upgraded 37 of them), retail forecourts, and battery-buffered sites. Utilisation data by charger speed is the most valuable missing input.
- **Signal freshness:** UK utilisation is updated quarterly (the page blocked direct access; wording checked via search results). US utilisation data is 2025. The grid-cost figures are 2024–2026.
- **What would change our mind:** Published UK rapid-specific utilisation consistently above 15%, or Ofgem's demand-connection reform (launched Feb 2026) materially cutting queue times for charging sites.

### Insight 4: Competition is concentrated in the US and Germany and fragmented, but consolidating, in the UK and France

- **Insight Summary:** A mid-size entrant faces scale incumbents in the US (Tesla) and Germany (EnBW, plus the subsidised Deutschlandnetz). The UK and France have more room, but consolidation is under way and capital intensity is high.
- **Supporting Evidence or Signals:**
    - **US:** Tesla has 37,995 of 76,236 DC ports (49.8%, Sep 2026), down from about 54.6% in Jul 2025. The "Other" network category grew 44% year on year [evchargingstations.com, verified]. IONNA, backed by automakers, targets 30,000 sites [Research: US report].
    - **Germany (end-2024 fast chargers):** EnBW 6,005, Tesla 3,110, Aral pulse 2,317, Allego 1,541, Ionity 1,084. The Deutschlandnetz programme has about 9,000 points of 200 kW or more at more than 1,000 locations [Research: EU report].
    - **UK:**
        - About 100–150 CPOs; the top 5 hold about a third of the market; industry leaders expect consolidation to 5–6 players [Research: UK report; Guardian Feb 2026].
        - Rapid-charger leaders in Feb 2026: MFG EV Power 2,789, Osprey 2,578, BP Pulse 2,506 [Zapmap].
        - More than £460 M was raised in 2025–26 by InstaVolt (£250 M), Osprey (£110 M) and Gridserve (£100 M).
    - **France (May 2025, high-power points):** Tesla 3,019, TotalEnergies 1,543, Electra 1,504 (after a €304 M Series B), Ionity 688, Fastned 265 [Research: EU report; EV Boosters].
- **Why This Insight Matters:** In the US, winning share means competing against Tesla's cost base and IONNA's automaker funding. In the UK and France, fragmentation leaves room for a mid-size operator, but the capital raised by rivals sets a high bar for site acquisition.
- **Signal freshness:** US Sep 2026; UK Feb–May 2026; Germany end-2024 (the oldest); France May 2025.
- **What would change our mind:** A major acquiring a mid-size UK or French operator, which would signal consolidation is closing the window; or Tesla's US share dropping below about 40% as open networks scale.

### Insight 5: The entry windows are time-bound and favour the UK first and France second

- **Insight Summary:** Two dated catalysts favour the UK and France within the 2026–2028 horizon, while federal support in the US is shrinking.
- **Supporting Evidence or Signals:**
    - **UK motorway sites:** Under a 2022 CMA undertaking, Gridserve will not enforce exclusive rights at about two-thirds of motorway service areas after November 2026 [gov.uk/CMA, verified].
    - **UK underserved regions** (rapid chargers per 100,000 people, against a UK average of 41.7) [DfT, verified]: Northern Ireland 19.3, London 27.9, Yorkshire and the Humber 36.6, North East 37.1. Scotland is best served at 59.1.
    - **UK funding:** £400 M from the 2025 Spending Review is committed to strategic road network charging.
    - **France:**
        - The ADVENIR subsidy programme has a budget of about €520 M and now runs to 2030 [Avere-France; the research report's "end-2027" was out of date].
        - France 2030 provides €300 M covering up to 40% of eligible costs.
        - A motorway master plan targets 22,000 car charging points at 150 kW across about 900 service areas by 2035 [Research: EU report].
    - **US:**
        - $503.8 M of NEVI federal charging funds was repurposed in March 2026 [FHWA notice; search-engine text only].
        - 84% of NEVI funds were still unobligated in May 2025.
        - State programmes remain: California's Fast Charge California ($55 M) and New York ($28.5 M) [Research: US report].
- **Why This Insight Matters:** Motorway sites in the UK come with high traffic and, in 37 cases, upgraded grid connections. The tender window is short, and competitors with fresh capital (Insight 4) will bid. France offers subsidised capital costs through 2030, which suits a second phase.
- **Signal freshness:** The CMA undertaking dates from 2022, with a November 2026 deadline two months away; it needs a check for any later change. ADVENIR status is as of Aug 2026. The NEVI notice is March 2026.
- **What would change our mind:** Any CMA or Gridserve update that delays or narrows the motorway opening, or cuts to ADVENIR or France 2030 funding.

## 5. Visual Evidence

All charts below were produced by Amazon Quick Research inside the three reports (exported PDFs in `deliverables/quick_research_reports/`). The last item is a table view from the agent's Market Analysis. Image files: `screenshots/visuals/v1_…` to `v7_…` and `screenshots/11b_market_analysis_comparison_table.png`; all eight are reproduced at the end of this brief.

| # | Chart type | What the visualisation shows | How it supports an insight |
|---|---|---|---|
| V1 | Line chart with shaded compliance gap | UK BEV share (19.6% 2024, 23.4% 2025) and SMMT forecasts against ZEV mandate targets from 2024 to 2035 | **Insight 2.** The mandate gap widens to about 6 points by 2027 while targets jump to 52% in 2028. The floor is real but under review. |
| V2 | Stacked bar chart | UK 50 kW+ chargers split into rapid (50–149 kW) and ultra-rapid (150 kW+): 10,118 (Jan 2024), 17,356 (Oct 2025), 26,378 (end-2025), 28,887 (Jul 2026) | **Insight 1.** Supply nearly tripled in 30 months, so the 2023 gap closed. Part of the jump comes from DfT switching its count from devices to connectors in Jan 2026. |
| V3 | Horizontal bar chart against the UK average | Rapid chargers per 100,000 people by UK region: Northern Ireland 19.3, London 27.9 … Scotland 59.1 | **Insight 5.** Shows where local white space remains even though national supply has caught up. |
| V4 | Line chart: actual vs projection | US DC fast ports (43K to about 75K) against the IEA STEPS path (100K by 2025, 280K by 2030) | **Insights 1–2.** The US is 32% short of the 2025 projection, but demand is short of projection too, so the shortfall is not an opportunity on its own. |
| V5 | Bar chart | US DC ports by network, Sep 2026: Tesla 37,995 (49.8%), Other 12,382 (16.2%) | **Insight 4.** Tesla's scale and the fragmented long tail. |
| V6 | Grouped bar chart | EVs per fast charger, IEA 2023 vs latest: Germany 119 → 71, France 79 → 46 | **Insight 1.** Supply outpaced the fleet in the EU core. Definitions differ, so the chart shows direction, not exact size. |
| V7 | Paired horizontal bar charts | Top-5 high-power operators: Germany (EnBW 6,005) and France (Tesla 3,019) | **Insight 4.** Germany is more concentrated than France. |
| V8 | Table view (agent output) | The 2023 dataset baseline next to the latest research for all four markets, with charger definitions labelled | **Insights 1–3.** The side-by-side comparison, with definition caveats, that the ranking rests on. |

## 6. Confidence Assessment

| Insight | Source quality | Consistency across sources | Timeliness | Confidence |
|---|---|---|---|---|
| 1. The 2023 gap has closed | High: IEA, DfT, Bundesnetzagentur, AFDC-based trackers, Avere-France | Direction agrees everywhere. Magnitudes are not comparable (above 22 kW vs 50 kW+ vs 150 kW+; BEV-only vs BEV+PHEV). The UK "doubled" claim is wrong (+58%). DfT changed its counting method in Jan 2026. | 2023 baseline, then Jul–Sep 2026 (France Feb 2025) | **Medium.** Direction is High. |
| 2. Policy-driven, diverging demand | High: SMMT, ACEA, EIA, NADA, gov.uk | Agreement across sources. Conflicting UK 2026 year-to-date shares (~25% vs ~29.8%) are both shown. The US "−31% registrations" figure is single-sourced from the press. | Jan–Sep 2026 | **High** for direction; **Medium** for 2026 magnitudes |
| 3. Utilisation and grid cost bind | Mixed: Zapmap and Paren (trackers); Osprey (an operator with an interest); RMI; a Springer study | Utilisation figures cover different scopes (UK all chargers vs US DC only). No EU utilisation data. The UK figure was mis-scoped in the research report. | 2024–2026; utilisation 2025–26 | **Medium-Low** |
| 4. Competitive structure | Medium: industry trackers (self-reported counts), press, one Wikipedia citation (the Tesla cost claim, not relied on) | Operator rankings differ by source and date. The UK report's table mixes total and rapid counts. | US Sep 2026; Germany end-2024 | **Medium** |
| 5. Time-bound windows | High: CMA/gov.uk, DfT, FHWA, Avere-France, CEC/NYSERDA | The ADVENIR end date conflicts (end-2027 in the report vs 2030 per Avere, now) and the brief uses 2030. The NEVI amount was verified from search-engine text only. | The CMA undertaking is from 2022; everything else 2025–26 | **Medium** |

**Overall confidence level: Medium.** The direction of every insight is supported by official statistics. Three things reduce precision:

1. **Charger definitions** differ across sources.
2. **Utilisation data** is thin, with none at all for Germany or France.
3. **Four errors were caught** in AI-generated material during review:
    - The UK research report's "doubled" claim.
    - The US report's growth-rate inconsistency.
    - The agent's 22.3% UK dataset figure.
    - The agent's list of underserved regions, which included Scotland.

All four were corrected before Brief v2.

## 7. Limitations and Risks

- **Missing data:**
    - No German or French utilisation data.
    - No rapid-only UK utilisation figure. Search results cite 12.8% for 150 kW+ chargers in Q4 2025, but this was not verified and is not used.
    - No site-level traffic, grid-capacity or land-cost data.
    - No price elasticity.
    - The internal dataset stops at 2023. Its 2025/2030 values are IEA scenario projections made before the US credit expired and before Germany's subsidy changes.
- **Conflicting signals:**
    - The UK "doubled" claim vs the arithmetic (+58%).
    - US port growth of "30–35% a year" (2024→25) vs about 16.5% annualised (end-2025 → Sep 2026) in the same report.
    - UK 2026 year-to-date BEV share: ~25% vs ~29.8%.
    - ADVENIR ends in 2027 vs 2030.
    - The UK 50 kW+ count jump partly reflects DfT's January 2026 change of counting method.
- **Potential bias or ambiguity:**
    - Operator-authored sources have an interest in the story. Osprey says costs are high; tracker counts are self-reported.
    - One US demand figure (−31%) comes from a single press article with no URL.
    - The Tesla cost-per-stall claim comes from Wikipedia and is excluded from the reasoning.
    - AI synthesis errors (four caught) show that model outputs need human arithmetic and source checks.
    - Comparisons of EVs per charger across markets mix BEV-only and BEV+PHEV fleets and different kW thresholds.
- **Assumptions:**
    - A mid-size operator can bid for motorway sites and finance 150 kW+ hubs.
    - Policy stays roughly as legislated through 2028.
    - The UK's 5.5-year average connection gap (all customer types) is indicative of charging sites.

## 8. Strategic Implications

**What decisions could this inform?**

- **Market sequencing:** Commit 2026–2027 development resources to the UK, keep France as a funded phase-two option, and move the US to monitor-only until a federal or state incentive restores demand.
- **UK site strategy:** Prioritise motorway-site tenders from November 2026 (especially the 37 sites with Ofgem-funded grid upgrades). Also target underserved regions: Northern Ireland, London (rapid chargers), Yorkshire and the Humber, and the North East. Avoid greenfield sites that need a new grid connection.
- **Diligence to fund now:** Grid-capacity feasibility on a UK shortlist, and rapid-specific utilisation data for the UK and France.

**Impact vs effort of recommended actions (with confidence)**

| Action | Impact | Effort | Confidence behind it |
|---|---|---|---|
| Grid-capacity check on 20–30 shortlisted UK sites | High | Low–Medium | High (grid cost/queue is the main risk) |
| Buy UK and France utilisation data by charger speed (Zapmap/Paren) | High | Low | High (largest data gap) |
| Prepare motorway-site tender bids for November 2026 | High | Medium | Medium (the 2022 undertaking needs a recheck) |
| France phase-two scoping and ADVENIR application | Medium | Medium | Medium |
| Watch Germany's Deutschlandnetz concessions for partnership entry | Low–Medium | Low | Medium |
| US: monitor-only; revisit if a federal incentive returns | Low (for now) | Low | Medium |

**What should not be concluded from this research?**

- **Do not conclude any market is undersupplied from national ratios of EVs per charger.** The 2023 dataset gap has largely closed, and the ratios use different charger definitions. White space exists only at site and region level.
- **Do not conclude the UK is profitable, or unprofitable.** No payback, NPV or IRR was modelled, and the ~8% utilisation figure covers all public chargers, not rapid ones.
- **Do not conclude the US is permanently unattractive.** The weakness is policy-driven, and the US remains the largest absolute market.
- **Do not treat IEA 2025/2030 projections as forecasts.** The US is running at roughly half the STEPS 2025 sales-share projection.
- **Do not rank Germany against France on EVs per charger.** France's latest count is 150 kW+ only; Germany's covers all DC fast chargers.

## 9. Summary for Leadership

**Executive Summary:**

1. The 2023 dataset's warning of a charging shortfall is out of date: since 2024, fast-charger build-out has outpaced EV fleet growth in the UK, US, Germany and France.
2. As a result, returns now depend on winning well-connected sites and on utilisation, not on a national charger shortage.
3. Demand is set by policy: the UK ZEV mandate gives a statutory floor rising to 52% of new-car sales by 2028, and France is accelerating (+62.9% BEV registrations in H1 2026), while US BEV share fell below 6% after the federal credit ended.
4. The UK is the recommended first market because motorway service areas open to competition from November 2026 and underserved regions such as Northern Ireland (19.3 rapid chargers per 100,000 people vs a 41.7 UK average) remain, with France as phase two and the US deferred.
5. Overall confidence is Medium: directions are backed by official statistics, but charger definitions differ across sources, utilisation data is thin, and four errors in AI-generated material were caught and corrected during review.
6. The immediate next steps are grid-capacity checks on a UK site shortlist, buying utilisation data by charger speed, and tracking the UK ZEV mandate consultation before any capital commitment.

---

## Appendix A. Research questions that produced the strongest evidence

Paraphrased; the full requests are visible in the agent screenshots.

1. For each market, compare 2023 EV car stock, public fast chargers and EVs per fast charger from the dataset with the latest charger counts, BEV share and utilisation from the research, labelling definitions where they differ. (Agent; produced V8.)
2. How attractive is UK public 50 kW+ charging for a mid-size entrant in 2026–2028? Cover demand vs ZEV targets, supply growth, regional gaps, competition, pricing and utilisation, policy and risks, benchmarked against the IEA 2023 baseline. (Quick Research, Deep mode; produced V1–V3.)
3. Where does the 2024–2026 evidence confirm or contradict the 2023 dataset? (Agent; Market Analysis section 3.)
4. Check three claims and show the arithmetic: UK BEV fleet "doubled"; US ports growing "30–35% a year"; Germany 119 → 71 EVs per charger. (Agent; found two errors in the research reports.)
5. What should leadership not conclude from this research? (Agent; Brief v1 and v2.)

## Appendix B. Contents of the Quick Space (and repository mirror)

| Space item | Repository location |
|---|---|
| IEA Global EV Data 2024.csv (full Kaggle file) | `data/IEA Global EV Data 2024.csv` |
| Focus-market filter (695 rows) | `data/iea_ev_cars_and_charging_focus_markets_2018_2030.csv` |
| DATASET_REFERENCE.md | `data/DATASET_REFERENCE.md` |
| Quick Research: UK, US, Germany/France reports | `deliverables/quick_research_reports/*.pdf` |
| Market Analysis - EV Fast Charging 2026-2028.docx (agent document) | `screenshots/11*` |
| Reliability Evaluation - EV Fast Charging 2026-2028.docx (agent document) | `screenshots/12*` |
| Market Intelligence Brief (v1) and Market Intelligence Brief v2 (.docx, agent documents) | `screenshots/13*`, `screenshots/14*` |
| Market_Intelligence_Research_Brief.pdf (this brief) | `deliverables/Market_Intelligence_Research_Brief.*` |

## Appendix C. Key primary sources

- IEA Global EV Data 2024 (Kaggle mirror `patricklford/global-ev-sales-2010-2024`, CC BY 4.0).
- UK: DfT EV charging infrastructure statistics (1 Jul 2026, published 27 Aug 2026); SMMT full-year 2025 release (6 Jan 2026); CMA motorway charging undertakings (8 Mar 2022); VETS Order 2023 (gov.uk); Zapmap utilisation and network statistics; Ofgem connections reform.
- US: EIA Today in Energy 67144 (9 Feb 2026) and 67885; NADA Dec 2025 Market Beat; evchargingstations.com DC fast charging Sep 2026 (3 Sep 2026); FHWA Notice N 4510.913 (12 Mar 2026); Paren Q1 2025 industry report; RMI rate-design guidance.
- EU core: ACEA H1 2026 registrations (23 Jul 2026); Bundesnetzagentur figures via heise (31 Jul 2026) and electrive (4 Feb 2026); Avere-France barometers and ADVENIR page; EU AFIR summary (EUR-Lex); EV Boosters operator rankings.
