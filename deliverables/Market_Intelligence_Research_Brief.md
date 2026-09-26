# Market Intelligence Research Brief

**Student Name:** Marco Ayuste

**Date:** 26 September 2026

**Topic/Company:** Where should a mid-size DC fast-charging operator expand in 2026–2028? United Kingdom vs United States vs EU core (Germany and France)

---

## Decision dashboard

| Item | Summary |
|---|---|
| **Recommendation** | Prioritise the **United Kingdom** for a site-led entry. Gridserve's exclusive rights at about two-thirds of motorway service areas stop being enforced after November 2026, although Moto and Roadchef are building their own networks and Extra is expanding with Ionity. Several regions are underserved, and UK supply has overtaken the fleet less than in the EU core. Scope **France** as phase two. **Defer the United States.** Monitor Germany for concession partnerships. |
| **Overall confidence** | **Medium.** The supply, demand and policy findings (Insights 1, 2, 5) rest on official statistics. The utilisation and competition findings (Insights 3, 4) rest mainly on industry trackers and operator sources. How large each effect is remains uncertain, because sources define chargers differently and utilisation data is thin. |
| **Top insights** | (1) The 2023 "charging gap" in the dataset has closed in Germany and France. It has narrowed only modestly in the UK once a 2026 counting change is allowed for, and eased only slightly in the US. (2) Demand is driven largely by policy and is diverging: UK and France up, US down. (3) Utilisation and grid cost, not EV demand, are the binding constraint. (4) Competition is concentrated in the US, moderately concentrated and subsidy-shaped in Germany, and fragmented in the UK and France. (5) The entry windows are time-bound but contested. |
| **Top risks** | UK grid-connection delays (a 5.5-year gap between requested and offered connection dates in Ofgem's July 2024 blog, before the queue reform). Service-area operators taking the freed motorway sites for their own networks or partners. The UK ZEV mandate review (consultation Aug–Oct 2026). Low utilisation (about 8% across all UK public chargers, all speeds). The US demand shock after the tax credit ended. |
| **Next 90 days** | Grid-capacity checks on shortlisted UK sites; open site-access talks with Moto, Roadchef and Extra; buy UK utilisation data by charger speed and find a French source; monitor the ZEV mandate consultation. |

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
    - IEA dataset: chargers above 22 kW.
    - UK: 50 kW+ chargers (DfT).
    - US: DC fast ports (AFDC-based trackers).
    - Germany: all DC fast-charging points (Bundesnetzagentur).
    - France: 150 kW+ high-power points (Avere-France) for supply, and 100 kW+ points (EV Boosters) for the operator rankings.
- **Competitor types:** Charge point operators (CPOs):
    - independents (InstaVolt, Osprey, Gridserve, Electra, EVgo);
    - oil-and-gas and utility-backed networks (BP Pulse, Shell Recharge, TotalEnergies, EnBW, Aral pulse);
    - automaker-backed networks (Tesla, Ionity, IONNA);
    - site owners that run their own networks (motorway service-area operators, retailers).
- **Timeframe:** A 2023 dataset baseline and a 2026–2028 decision horizon. External evidence is mostly from 2024 to September 2026. Older items are Ofgem's 2021 Green Recovery Scheme, the 2022 CMA motorway commitments, the 2022–2024 standing-charge example, AFDC's end-2023 port count and RMI's demand-charge guidance. IEA projections to 2030 are used as scenario context only.

**Excluded:** Home, workplace and fleet-depot charging; buses, vans and trucks; hardware manufacturing; financial modelling (payback, NPV, IRR); and markets outside the three candidates. China and Norway appear in the dataset only as benchmarks.

**Key constraints:** One working session in a time-limited AWS lab; three Quick Research runs (one Deep, two Fast); a 2023 cut-off for the internal dataset; and no access to paid utilisation or site-level data.

## 3. Research Approach

**Types of questions asked**

1. **Baseline questions** on the internal dataset, asked through the agent. For example: EV car stock, public fast chargers, EVs per fast charger and EV sales share for each market in 2023. The answers were checked against an independent recomputation (`analysis/ev_charging_gap.py`).
2. **Structured market-attractiveness questions**, one Quick Research run per market. Each covered the same six dimensions so the three reports could be compared side by side:
    - demand vs policy targets;
    - charger supply growth;
    - competitive concentration;
    - pricing and utilisation;
    - policy and funding;
    - entry risks.
3. **Counter-evidence questions:** where does the 2024–2026 evidence contradict the 2023 dataset, and which figures conflict between sources?
4. **Arithmetic and reliability checks** on specific claims, for example "the UK BEV fleet doubled" and "US ports grow 30–35% a year".
5. **Decision questions:** a ranked market priority, confidence per insight, and explicit statements of what not to conclude.

**How research effort was prioritised**

- **Dataset first.** The dataset showed the widest 2023 gap in the UK: 158 EVs per public fast charger, against 112 (US), 119 (Germany), 79 (France) and 99 (EU27). The UK therefore got the **Deep** Quick Research run, which Quick estimated at 20–30 minutes (screenshot 02b). The US and EU core got **Fast** runs as challenger checks; no screenshot captured their run mode.
- **Source rules.** Each run had preferred websites of official and industry statistics (screenshots 02, 09b, 10b):
    - UK: gov.uk, zapmap.com, smmt.co.uk, iea.org, racfoundation.org and ofgem.gov.uk.
    - US: afdc.energy.gov, energy.gov, driveelectric.gov, fhwa.dot.gov, iea.org and epa.gov.
    - EU core: the EU Alternative Fuels Observatory, europa.eu, bundesnetzagentur.de, kba.de, avere-france.org, iea.org and acea.auto.
    - All runs avoided reddit.com, quora.com, medium.com and social media.

    The UK research plan was revised once before it ran. Screenshot 03 shows the plan after that revision, with the clarifying questions. The revision request itself was not captured.

- **Benchmark against the dataset.** The Space holding the dataset was attached to each Quick Research run as a Quick asset. That way every report compared its 2024–2026 findings with the 2023 figures.
- **Verification over breadth.** The remaining time went into validation rather than more research runs:
    - The agent's reliability pass, including three arithmetic checks.
    - A primary-source spot-check of 10 headline figures (Appendix D): 7 verified as written, 1 verified with a corrected citation, 1 date out of date, and 1 scope error.
    - Three line-by-line reviews of this brief against the reports, the dataset and the agent's documents.

    Together these found the errors logged in Appendix E.

**Tools used within Amazon Quick Suite**

- **Spaces:** the "EV Fast-Charging Market Intelligence 2026-2028" Space holds:
    - the dataset and a dataset reference note;
    - the three research reports;
    - the agent's Market Analysis and Reliability Evaluation;
    - both versions of the agent's brief;
    - this brief.
- **Quick Research:** three reports, using preferred and avoided websites, Quick assets, plan revision, and export to the Space and to PDF.
- **Custom chat agent:** "Market Intelligence Agent – EV Fast Charging" (screenshots 04–06). Its instructions cover:
    - purpose and scope;
    - source-labelling rules;
    - a rule to show both figures when sources conflict, and never to average them;
    - response formats;
    - scope limits (no investment advice, no NPV or IRR).

    Its knowledge source is the Space.

- **Agent features:** code execution for dataset arithmetic and charts, table views, and document artifacts added to the Space as Word files. The files are downloaded to `deliverables/agent_outputs/`.
- **Tests:**
    - A dataset-only test: the agent's 2023 table matches the dataset (screenshots 07a–07b).
    - A scope test: a request for IRR/payback, a stock pick and a 2035 EV-fleet forecast. The agent refused all three and cited its scope limits (screenshot 16).

Outside Quick, a standard-library Python script re-derived the 2023 dataset metrics. The IEA projection values quoted in this brief (STEPS 2025/2030) were read directly from the dataset CSV. Separately, 10 cited figures were checked against their primary sources.

**Evidence of AI-assisted work** is in `screenshots/`:

| Screenshots | What they show |
|---|---|
| 01 | Space set-up |
| 02, 02b, 03 | UK research set-up, Deep run in progress, and revised plan |
| 04–06 | Agent configuration and knowledge source |
| 07a–07b | First agent test |
| 08, 09a–09b, 10a–10b | Research reports and their materials |
| 11a–11e | Market Analysis |
| 12a–12e | Reliability Evaluation |
| 13a–13d | Brief v1 |
| 14a–14c | Brief v2 |
| 15a–15b | Space contents |
| 16 | Scope test |

The charts are in `screenshots/visuals/`.

## 4. Key Market Insights

### Insight 1: The 2023 "charging gap" has closed in Germany and France, narrowed in the UK, and eased only slightly in the US

- **Insight Summary:**
    - **2023 baseline:** the internal dataset shows EVs per public fast charger rising in the UK from 69 in 2018 to 158 in 2023, which reads as a widening undersupply.
    - **Germany and France:** since then, charger counts have clearly grown faster than the fleet.
    - **UK:** like for like, the improvement is modest. BEVs per 50 kW+ device held at about 97–100 from January 2024 to October 2025 and is about 90 in mid-2026. The larger fall to about 73 relies on DfT's new counting unit from January 2026.
    - **US:** on a consistent count of DC ports, EVs per port are only about 6–9% below end-2023.
    - **So what:** an entry case built on national undersupply is out of date. It now rests on where individual sites are still thin, and on how well they are used.
- **Supporting Evidence or Signals:**
    - **Dataset, 2023** (IEA Global EV Data 2024; EVs per public fast charger, chargers above 22 kW, BEV+PHEV fleet):
        - UK 158 (1.58 M EVs ÷ 10,000 chargers). On a BEV-only basis it is 98 (980,000 ÷ 10,000).
        - US 112 (4.82 M ÷ 43,000).
        - Germany 119 (2.50 M ÷ 21,000).
        - France 79 (1.57 M ÷ 20,000).
        - EU27 99; EU27 fast chargers grew 67% in 2023.
    - **UK:**
        - **Charger count:** 50 kW+ chargers went from 10,118 devices (Jan 2024) to 28,887 chargers (1 Jul 2026) [DfT, verified].
        - **Counting change:** the two counts are not like for like. From January 2026 DfT counts "EV chargers" (EVSEs, each able to charge one vehicle at a time) instead of charging devices. On the old basis, July 2026's 121,171 chargers are 97,266 devices [DfT, 1 Jul 2026].
        - **Like-for-like ratio (our estimates):** BEVs per 50 kW+ device were about 97 in Jan 2024 (980,000 ÷ 10,118) and about 100 in Oct 2025 (about 1.75 M ÷ 17,356; the fleet figure is interpolated between end-2024 and April 2026). In mid-2026 the ratio is about 90: 2.1 M ÷ about 23,200 devices, which assumes 50 kW+ chargers convert to devices in the same proportion as all chargers.
        - **New-unit ratio:** on DfT's new unit the mid-2026 ratio is about 73 (2.1 M ÷ 28,887).
        - **Report figure not used:** the UK report's "about 66" (attributed to DfT, April 2026) could not be reproduced.
        - **Fleet growth:** the BEV fleet grew from about 1.33 M (end-2024) to about 2.1 M (mid-2026). That is +58%, not the "doubled" the report claims.
    - **Germany:**
        - Public fast points (IEA, above 22 kW) numbered 21,000 in 2023.
        - DC fast points (Bundesnetzagentur) reached 40,777 (Jul 2025), 48,729 (Jan 2026) and 54,341 (Jul 2026) [Research: EU report; heise 4 Feb 2026 and 31 Jul 2026, verified].
        - The EU report gives about 71 EVs (BEV+PHEV) per fast charger in mid-2025. The IEA and the Bundesnetzagentur may not use the same "fast" threshold.
    - **France:**
        - Points of 150 kW and above went from 19,848 (Feb 2024) to 31,335 (Feb 2025) [Research: EU report; Avere-France].
        - The report's "about 46 EVs per high-power point" has no stated derivation. On the dataset's BEV+PHEV basis it is at least 50 (the end-2023 fleet alone, 1.57 M, divided by 31,335), so 46 is probably a BEV-only figure.
        - Either way the ratio is below the 2023 baseline of 79, which counted all chargers above 22 kW.
    - **US:**
        - The dataset's 43,000 is IEA chargers above 22 kW. On AFDC's own count there were 38,271 public DC fast ports at end-2023 [AFDC/NREL, Q4 2023 trends report].
        - DC fast ports then reached 50,428 (Dec 2024), about 68,000 (end-2025) and 76,236 (1 Sep 2026) [Research: US report; evchargingstations.com, verified].
        - **Our estimate of EVs (BEV+PHEV) per DC port:** about 126 at end-2023, 127 at end-2024, 118 at end-2025 and 115–119 in Sep 2026. The range depends on whether 2026 plug-in sales run at the 2025 rate or at the lower 2026 share.
        - **Method:** start from 4.82 M EVs in 2023 and add about 1.6 M plug-in sales a year, taken from the US report's sales shares. Scrappage is ignored.
        - The US report's "96–106" cannot be reproduced; its 96 equals the 2023 fleet divided by December 2024 ports. It is not used.
- **Why This Insight Matters:**
    - In Germany and France, each charger now serves clearly fewer EVs than in 2023, so revenue per charger falls unless a site sits where demand is still concentrated.
    - The UK and US are where supply has overtaken the fleet least. That supports utilisation at well-chosen UK sites, subject to grid access (Insight 3).
    - Leadership's question changes from "which country is short of chargers?" to "which sites are short of chargers, and can we win them?".
    - The 2023 dataset alone would have overstated the UK shortfall.
- **Signal freshness:**
    - Charger counts: UK 1 Jul 2026 (DfT, published 27 Aug 2026); Germany Jul 2026; US 1 Sep 2026 (published 3 Sep 2026); France Feb 2025.
    - UK ratio: recomputed at the 1 Jul 2026 count; the report's 66 was an April 2026 figure.
    - Germany: the 71 is mid-2025. Its DC count grew about 33% from Jul 2025 to Jul 2026, so its ratio is probably at or slightly below 71 now.
    - France: no count after Feb 2025, so its ratio cannot be updated.
- **What would change our mind:** UK BEVs per 50 kW+ device (about 90 in mid-2026) rising back above about 100, or Q3/Q4 2026 statistics showing fleet growth outpacing charger growth again in Germany or France.

### Insight 2: EV demand is driven largely by policy and is diverging: the UK has a mandate target, France has momentum, and the US has lost its federal support

- **Insight Summary:**
    - Policy is a major driver of new-car EV demand in all four markets, but not the only one.
    - The UK ZEV mandate sets targets that rise steeply to 2028. BEV sales currently run below those targets, and manufacturers met the 2024 target through compliance flexibilities.
    - France is accelerating with demand support still in place.
    - Germany's Umweltbonus ended in December 2023 and sales slumped in 2024. They recovered in 2025 on fleet and corporate buying before any grant returned. In 2026 they were lifted by high fuel prices plus a new grant.
    - US demand fell sharply once the federal credit expired.
- **Supporting Evidence or Signals:**
    - **UK:**
        - BEV share was 19.6% in 2024 (381,970 cars) and 23.4% in 2025 (473,348) [SMMT, verified].
        - The mandate targets are 22% for 2024, 28% for 2025, 33% for 2026 and 52% for 2028 [Research: UK report; VETS Order].
        - Actual BEV share ran 2.4 points (2024) and 4.6 points (2025) below target. All manufacturers complied in 2024 through borrowing, trading and CO₂ transfers [Research: UK report]. Official manufacturer-level results for 2025 were not in our sources.
        - The penalty per car short of target was cut from £15,000 to £12,000, and borrowing was extended to 2029 [Research: UK report]. The target is compliance pressure on manufacturers, not a guaranteed sales level.
        - A formal review of the mandate launched in August 2026 [Research: UK report; gov.uk].
        - 2026 year to date: 25.6% for January–August 2026 (355,746 of 1,388,735 registrations) [SMMT, 4 Sep 2026]. This is consistent with about 25% in H1 2026 [Car Magazine]. The UK report's "about 29.8% YTD" is August's single-month share and is not used.
    - **France:**
        - BEV share rose from 16.9% (2024) to 20.0% (2025). H1 2026 registrations were up 62.9% year on year [ACEA, verified].
        - August 2026 set a single-month record of 38.8% [Research: EU report; Avere-France].
        - Demand support continues. The "coup de pouce" bonus replaced the bonus écologique and runs into 2026. A third social-leasing round (July 2026) offers 50,000 BEVs at capped payments of €200 a month [Research: EU report].
    - **Germany:**
        - BEV share fell from 18.4% (2023) to 13.5% (2024) after the Umweltbonus ended in December 2023.
        - It then rose to a record 19.1% in 2025, driven mainly by fleet and corporate purchases while no grant was in force [Research: EU report].
        - H1 2026 was up 48%, driven by high fuel prices and reinforced by a new grant of up to €6,000 from 1 January 2026 [Research: EU report; heise; EU Alternative Fuels Observatory].
    - **US:**
        - The $7,500 credit expired on 30 Sep 2025. BEV share hit 12% that September, then fell below 6% in Q4 2025 [EIA, verified].
        - BEV share was 7.7% for 2025 [NADA].
        - Mid-2026 registrations were down about 31% year on year [Research: US report; single press source].
        - IEA STEPS had projected a 20% EV (BEV+PHEV) sales share for 2025 [Dataset, projection]. The actual all-plug-in share was just under 10% [Research: US report; IEA Global EV Outlook 2026], about half the projection. The 7.7% above is BEV-only and not directly comparable.
- **Why This Insight Matters:**
    - For a 2026–2028 horizon, the operator is partly betting on policy.
    - The UK mandate's compliance pressure and France's demand support reduce downside risk on demand, though UK flexibilities mean sales can keep running below target.
    - The US needs a new incentive before demand growth resumes.
- **Signal freshness:**
    - Full-year shares cover 2023–2025.
    - 2026 figures are H1 or January–August year to date; the French August record is a single month.
    - The UK review outcome is still open (consultation August–October 2026).
- **What would change our mind:** A UK review that materially cuts the 2027–2028 targets, or a new US federal purchase incentive.

### Insight 3: Utilisation and grid cost, not EV demand, are the binding constraint on returns

- **Insight Summary:** In every market with data, chargers are used for a small share of the day, and fixed grid costs are large. The ability to secure cheap, timely grid capacity decides returns more than the size of the EV fleet does.
- **Supporting Evidence or Signals:**
    - **UK:**
        - Utilisation is about 8% (about 2 hours a day): Zapmap's average for all public chargers. The UK report's body labels it that way, but its summary and conclusion apply it to rapid chargers.
        - Zapmap's own figure for rapid and ultra-rapid devices is about 4 sessions a day of about 38 minutes, roughly 10–11% of the day. Like the 8%, this was read from search results. The UK report's revenue estimate instead assumes about 2 sessions a day and cites the same Zapmap page, which gives about 4. So the 2-a-day figure is not used [Research: UK report; Zapmap].
        - Rapid and ultra-rapid devices handle 72% of sessions from 23% of devices [Research: UK report; Zapmap].
        - Grid standing charges for a typical UK ultra-rapid hub rose from £99 a year (2022) to £8,600 (2024). The example comes from the operator Osprey [Osprey].
        - Ofgem's blog of 17 July 2024 reports a 5.5-year difference between requested connection dates and connection offers for connecting customers, when the 714 GW queue was dominated by renewables and storage. This predates the reform that has since moved 221 GW out of the queue (April 2026). No post-reform or charger-specific figure was found [Research: UK report].
        - The average rapid price is about 77p/kWh, against 7–8p on a home smart tariff [Research: UK report].
    - **US:**
        - National DC fast utilisation was 16.6% in Q1 2025 [Paren] and 16.1% in mid-2025 [theevreport.com].
        - The profitability threshold is estimated at about 15% [Stable Auto via Fortune, 2024].
        - At low utilisation, demand charges can exceed 90% of a station's electricity cost [RMI rate-design guidance].
    - **EU:**
        - No German or French utilisation or payback data was found. This is a gap, not a finding.
        - The EU report's "6–12 year payback" comes from a global review of solar (PV)-powered charging stations, not grid-connected high-power charging in Germany or France. It is not used.
- **Why This Insight Matters:**
    - Site choice should favour locations that already have grid capacity or funded network upgrades: motorway service areas, retail forecourts and battery-buffered sites.
    - Ofgem's £300 M Green Recovery Scheme, announced in 2021, funded network upgrades at 37 motorway service areas; many are complete and already host chargers.
    - Utilisation data by charger speed is the most valuable missing input.
- **Signal freshness:** UK utilisation is updated quarterly; the page blocked direct access, so the wording was checked via search results. US utilisation data is from 2025. The grid figures are older: standing charges 2022–2024, the connection gap July 2024 (pre-reform), and the queue reform April 2026. The RMI demand-charge guidance is older still.
- **What would change our mind:** Published UK rapid-specific utilisation consistently above 15%, or post-reform Ofgem data showing connection times for charging sites well below the pre-reform 5.5-year gap.

### Insight 4: Competition is concentrated in the US, moderately concentrated and subsidy-shaped in Germany, and fragmented in the UK and France

- **Insight Summary:**
    - A mid-size entrant faces one dominant incumbent in the US: Tesla, with about 50% of DC ports.
    - In Germany, share is only moderately concentrated: EnBW has about 16% of fast points and the top 5 about 40%. The harder barrier is the subsidised Deutschlandnetz concession network being rolled out.
    - The UK is fragmented but consolidating. France is fragmented and split by location type.
    - Capital intensity is high in both.
- **Supporting Evidence or Signals:**
    - **US:**
        - Tesla has 37,995 of 76,236 DC ports (49.8%, Sep 2026), down from about 54.6% in Jul 2025. The "Other" network category grew 44% year on year [evchargingstations.com, verified].
        - IONNA, backed by automakers, had 1,458 ports in Sep 2026 and ranks 8th [Research: US report; evchargingstations.com]. It targets at least 30,000 charging bays across North America by 2030 [ionna.com]; the US report says "sites".
    - **Germany:**
        - End-2024 fast chargers: EnBW 6,005, Tesla 3,110, Aral pulse 2,317, Allego 1,541 and EWE Go 1,531. Ionity is 8th with 1,084 [EV Boosters ranking; the EU report lists Ionity 5th].
        - The top 5 hold 14,504 of 36,652 DC fast points on 1 January 2025 (about 40%), and EnBW about 16% [electrive, 4 Feb 2026, for the base]. The EU report calls this "a substantial majority".
        - The Deutschlandnetz programme plans about 9,000 points of 200 kW or more at more than 1,000 locations [Research: EU report]. It is a pipeline of subsidised competition rather than capacity already installed.
    - **UK:**
        - About 100–150 CPOs, with industry leaders expecting consolidation to 5–6 players [Guardian, Feb 2026].
        - The top 5 hold about a third of all UK public chargers, AC and DC combined [Research: UK report; Drax/Zapmap].
        - The ultra-rapid (150 kW+) segment is likely more concentrated, but no share figure is available. What Car? (citing Zapmap) counts 8,728 ultra-rapid connectors across 18 networks at end-September 2025. Zapmap's own count for that date is 9,290 ultra-rapid devices, so those 18 networks do not cover the whole segment [Research: UK report; Zapmap].
        - Rapid-charger counts differ by source. Zapmap (Feb 2026) lists MFG EV Power 2,789, Osprey 2,578 and BP Pulse 2,506; the UK report's own table puts InstaVolt first at about 2,600+.
        - £460 M of financing was raised in 2025–26: InstaVolt £250 M debt refinancing (May 2026), Osprey £110 M senior debt (Jul 2025) and Gridserve £100 M equity (Jul 2025).
    - **France (May 2025, points of 100 kW+, by location segment)** [Research: EU report; EV Boosters]:
        - Highways: TotalEnergies 850, Ionity 688, ENGIE Vianeo 632, Electra 323, Fastned 265.
        - Near-highway: Tesla 2,453, Powerdot 1,369, Electra 1,181, TotalEnergies 693, Izivia 683. Electra's highway plus near-highway total is 1,504, after a €304 M Series B.
        - Retail and urban: Powerdot 2,116, Izivia 865, IECharge 597, Tesla 566.
        - No single operator leads every segment.
- **Why This Insight Matters:**
    - **US:** winning share means competing against Tesla's scale and IONNA's automaker funding.
    - **Germany:** the practical barrier is subsidised concessions more than any one rival.
    - **UK and France:** fragmentation leaves room for a mid-size operator, but rivals' new financing sets a high bar for site acquisition.
- **Signal freshness:** US Sep 2026; UK Jul 2025 to Jul 2026; Germany end-2024 (the oldest); France May 2025.
- **What would change our mind:** A major acquiring a mid-size UK or French operator, which would signal consolidation is closing the window; or Tesla's US share dropping below about 40% as open networks scale.

### Insight 5: The entry windows are time-bound but contested, and favour the UK first and France second

- **Insight Summary:** Dated catalysts favour the UK and France within the 2026–2028 horizon, but incumbents and site owners are moving too, while US federal support is shrinking.
- **Supporting Evidence or Signals:**
    - **UK motorway sites:**
        - Under legally binding commitments accepted by the CMA in 2022, Gridserve will not enforce exclusive rights at about two-thirds of motorway service areas after November 2026 [gov.uk/CMA, verified].
        - The commitments end the exclusivity; they do not require the site owners to tender.
        - The owners are moving first. Moto launched its own Moto Charge network in December 2025 [Zapmap]. Roadchef has installed its first own-branded hub on the M6, though it did not appear to be live in early August 2026 [The Fast Charge, 6 Aug 2026]. Extra is expanding its sites with Ionity [electrive, Aug 2025].
        - No source shows that the freed sites will be offered to third-party operators.
    - **UK underserved regions** (rapid chargers per 100,000 people; UK average 41.7) [DfT, verified]:
        - Northern Ireland 19.3;
        - London 27.9;
        - Yorkshire and the Humber 36.6;
        - North East 37.1;
        - Scotland is best served, at 59.1.

        This is density per person, not per EV or per unit of use, so it is a screening signal only.

    - **UK funding:** The 2025 Spending Review set aside £400 M for EV charging infrastructure in England over 2026–2030, including the strategic road network. An indicative £190 M goes to the Strategic Charging Infrastructure scheme for grid upgrades at motorway service areas (consultation June–July 2026) [gov.uk].
    - **France:**
        - ADVENIR's €520 M was the envelope for its extension to end-2027 (target 250,000 points).
        - On 7 July 2026 the government announced a further extension to 2030, with about €400 M, roughly €100 M a year [AEF info; les-energies-renouvelables.eu].
        - The April 2026 electrification plan says the new money will go preferentially to truck, coach and bus charging and to collective-residential charging [ecologie.gouv.fr, 23 Apr 2026]. Whether it covers public passenger-car fast charging is not confirmed.
        - France 2030's €300 M high-power-charging call closed to new projects at the end of 2024 [IEA policy database], so it is not counted.
        - A motorway master plan targets 22,000 car charging points at 150 kW across about 900 service areas by 2035 [Research: EU report].
    - **US:**
        - $503.8 M of NEVI federal charging funds was repurposed in March 2026 [FHWA notice; confirmed via search results only].
        - USDOT reported 84% of NEVI funds unobligated in May 2025, during its own review of the programme [Research: US report].
        - California has run state-funded rounds (Fast Charge California, $55 M, 2025) [Research: US report; CEC]. On 18 Aug 2026 the CEC approved a $95.2 M FY2026–27 ZEV infrastructure plan that includes $48 M for light-duty charging, focused on DC fast and home or near-home charging [Research: US report; CEC]; how much of it reaches public fast-charging rounds is not known.
        - New York's $28.5 M corridor round (Dec 2024) was federal NEVI money run by NYSERDA, so it carries the same federal risk. The US report calls it a state programme.
- **Why This Insight Matters:**
    - UK motorway sites combine high traffic with a short access window that the service-area operators' own networks and existing partners also contest. Competitors with new financing (Insight 4) will compete for it too.
    - Whether any of the 37 Green Recovery Scheme sites are among those freed from exclusivity still needs checking.
    - France's ADVENIR money to 2030 favours heavy-vehicle and residential charging, so its support for a phase-two car network must be confirmed first.
- **Signal freshness:**
    - The CMA commitments date from 2022, with a deadline two months away; they need a check for any later change.
    - Site-owner moves are dated August 2025 (Extra with Ionity) to August 2026 (Roadchef).
    - ADVENIR status is as of July 2026. The France 2030 call closed at end-2024.
    - New York's round is from December 2024; the NEVI notice is from March 2026.
- **What would change our mind:** Any CMA or Gridserve update that delays or narrows the motorway opening; Moto, Roadchef and Extra filling the freed sites with their own networks or existing partners; or ADVENIR's 2027–2030 money excluding public car fast charging.

## 5. Visual Evidence

**Sources of the visuals:**

- **V1–V7** were produced by Amazon Quick Research inside the three reports (exported PDFs in `deliverables/quick_research_reports/`).
- **V8** is a table view from the agent's Market Analysis.
- **V9 and V10** are charts the agent generated with code execution for its combined analysis document (`deliverables/agent_outputs/05_…docx`).

**Files and conventions:**

- All ten are embedded at the end of the PDF and Word versions of this brief.
- Figure numbers printed inside the images come from the source reports; this brief refers to them as V1–V10.
- Several images show errors as they were produced. Their rows below say so, and the errors are logged in Appendix E.
- Image files:
    - [V1](../screenshots/visuals/v1_uk_bev_share_vs_zev_mandate_line.png), [V2](../screenshots/visuals/v2_uk_rapid_ultrarapid_charger_growth_stacked_bar.png), [V3](../screenshots/visuals/v3_uk_regional_rapid_density_bar.png), [V4](../screenshots/visuals/v4_us_dc_ports_actual_vs_iea_steps_line.png), [V5](../screenshots/visuals/v5_us_networks_by_port_count_bar.png)
    - [V6](../screenshots/visuals/v6_de_fr_evs_per_fast_charger_bar.png), [V7](../screenshots/visuals/v7_de_fr_top_hpc_operators_bar.png), [V8](../screenshots/11b_market_analysis_comparison_table.png), [V9](../screenshots/visuals/v9_agent_evs_per_fast_charger_2023_vs_latest.png), [V10](../screenshots/visuals/v10_agent_us_dc_port_growth_2023_2026.png)
    - Two flawed agent charts are kept apart in `screenshots/visuals/excluded_flawed_agent_charts/`.

| # | Chart type | What the visualisation shows | How it supports an insight |
|---|---|---|---|
| V1 | Line chart with shaded compliance gap | UK BEV share (19.6% 2024, 23.4% 2025) and SMMT forecasts against ZEV mandate targets from 2024 to 2035 | **Insight 2.** The gap to target widens to about 6 points by 2027 while targets jump to 52% in 2028. The target binds manufacturers' compliance but is softened by borrowing and trading, and it is under review. |
| V2 | Stacked bar chart | UK 50 kW+ chargers split into rapid (50–149 kW) and ultra-rapid (150 kW+): 10,118 (Jan 2024, DfT devices), 17,356 (Oct 2025, DfT devices), 26,378 (end-2025, Zapmap chargers) and 28,887 (Jul 2026, DfT EV chargers) | **Insight 1.** Supply rose steeply. The bars mix device and EV-charger (EVSE) counts, so part of the rise is a change in counting method (see the like-for-like ratios in Insight 1). |
| V3 | Horizontal bar chart against the UK average | Rapid chargers per 100,000 people by UK region: Northern Ireland 19.3, London 27.9 … Scotland 59.1 | **Insight 5.** Shows where local white space may remain. The measure is per person, not per EV, so it is a screening signal. |
| V4 | Line chart: actual vs projection | US DC fast ports (43K to about 75K) against the IEA STEPS path (100K by 2025, 280K by 2030). The 2023 point is the IEA figure for chargers above 22 kW. | **Insights 1–2.** The US is 32% short of the 2025 projection, but demand is short of projection too, so the shortfall is not an opportunity on its own. |
| V5 | Bar chart | US DC ports by network, Sep 2026: Tesla 37,995 (49.8%) and Other 12,382 (16.2%). Four top-10 networks are not drawn: Blink (6th, 2,059), EV Connect (7th, 1,731), Ford Charge (9th, 1,264) and Rivian (10th, 1,087), 6,141 ports in all. IONNA, drawn sixth, is 8th (R14). | **Insight 4.** Tesla's scale and the fragmented long tail. |
| V6 | Grouped bar chart | EVs per fast charger, IEA 2023 vs latest: Germany 119 → 71, France 79 → 46 (report figure; at least 50 on the dataset's BEV+PHEV basis) | **Insight 1.** Supply outpaced the fleet in the EU core. Definitions differ, so the chart shows direction, not exact size. |
| V7 | Paired horizontal bar charts | Top high-power operators: Germany (EnBW 6,005, end-2024) and France (May 2025). The German panel shows Ionity 5th, but EV Boosters has EWE Go (1,531) 5th and Ionity 8th. The French panel's Tesla 3,019 adds near-highway 2,453 and retail 566; added the same way, Powerdot (3,485) is larger and Izivia (1,548) edges TotalEnergies (1,543). Ionity and Fastned are highway-only counts, and Electra (1,504) is drawn above TotalEnergies. | **Insight 4.** Germany has one clear leader. France's leadership is split by segment; read it from the Insight 4 bullets, not the panel. |
| V8 | Table view (agent output) | The 2023 dataset baseline next to the latest research for all four markets, with charger definitions labelled. It is the agent's first version, and four cells carry errors: the UK utilisation cell (about 8%, all chargers) sits next to the US DC-only about 16% with no caveat (the R2 scope problem carried into the table); the UK BEV share shows "about 29.8% YTD" (R13, A14); the Germany and France utilisation cells show the EU report's "6–12 year payback" (R10, A13). | **Insights 1–3.** The side-by-side comparison, read with the corrections in Insights 2 and 3. The corrected table in `deliverables/agent_outputs/01_…docx` fixes the UK caveat but still shows the "29.8% YTD" share and the payback figure. |
| V9 | Grouped bar chart (agent, from dataset and research) | EVs per fast charger, 2023 dataset baseline vs latest: UK 158 → 66, US 112 → 101, Germany 119 → 70, France 79 → 46 | **Insight 1, direction only.** The agent plotted the UK and France report ratios (66, 46), its own Germany estimate (70; the report says 71) and, for the US, 101: the midpoint of the report's "96–106", which breaks its own no-averaging rule (A12). Recomputed, the ratios are about 73 (UK, new unit; about 90 on the old device basis), 115–119 (US, a fall of only about 6–9% like for like) and at least 50 (France). |
| V10 | Line chart (agent) | US DC fast ports: about 43,000 (2023, IEA chargers above 22 kW), 50,428 (2024), about 68,000 (2025) and 76,236 (Sep 2026), with the report's "30–35% a year" marked as true for 2024→2025 only | **Insight 1 and Section 7.** US build-out is slowing in 2026 to about 18–19% annualised. The last point is September 2026, although the chart title says "End-of-Year", and its label is clipped at the chart edge as generated (76,236 on 1 Sep 2026). Its 2023→2024 segment mixes the IEA count with AFDC ports (A5); like for like the rise was about +32% (38,271 → 50,428). |

## 6. Confidence Assessment

| Insight | Source quality | Consistency across sources | Timeliness | Confidence |
|---|---|---|---|---|
| 1. The 2023 gap has closed in Germany and France, narrowed in the UK | High: IEA, DfT, Bundesnetzagentur, AFDC, Avere-France | Direction agrees for Germany and France. The UK like-for-like ratio fell only from about 97–100 to about 90; the fall to about 73 relies on DfT's new counting unit. US like-for-like: about 126 → 115–119. Magnitudes are not comparable across markets (above 22 kW vs 50 kW+ vs 150 kW+; BEV-only vs BEV+PHEV). The reports' UK 66 and US 96–106 could not be reproduced. The UK "doubled" claim is wrong (+58%). | Baseline 2023; charger counts Jul–Sep 2026 (France Feb 2025); Germany ratio mid-2025 | **Medium.** Direction is High for Germany and France. |
| 2. Policy-driven, diverging demand | High: SMMT, ACEA, EIA, NADA, gov.uk | Sources agree on direction. The UK report's "29.8% YTD" is August's single-month share; SMMT gives 25.6% for January–August. The US "−31% registrations" figure comes from a single press source. | Full years 2023–2025; 2026 year to date through August | **Medium.** Direction is High; 2026 magnitudes are Medium. |
| 3. Utilisation and grid cost bind | Mixed: Zapmap, Paren and theevreport.com (trackers); Osprey (an operator with an interest); RMI; Ofgem | Utilisation figures cover different scopes (UK all chargers vs US DC only). The UK report's revenue estimate uses about 2 rapid sessions a day against Zapmap's about 4. No EU utilisation or payback data. The grid-connection gap predates the queue reform. | Utilisation 2025–26; standing charges 2022–2024; connection gap July 2024; RMI guidance older | **Low.** Grid-cost direction is Medium; utilisation magnitudes are Low. |
| 4. Competitive structure | Medium: industry trackers (self-reported counts), press, and two Wikipedia citations in the US report (neither relied on) | Operator rankings differ by source and date. The research reports misranked Germany's top 5, mixed France's location segments, gave IONNA's target in sites instead of charging bays, and dropped Blink and EV Connect from the US ranking. All four are corrected here. | US Sep 2026; UK Jul 2025 to Jul 2026; France May 2025; Germany end-2024 | **Medium** |
| 5. Time-bound but contested windows | High for the dated catalysts (CMA/gov.uk, DfT, FHWA, Avere-France, IEA policy database, CEC/NYSERDA, French government); Medium for the site-owner moves (Zapmap, The Fast Charge, electrive) and the ADVENIR 2030 amount (AEF info, les-energies-renouvelables.eu) | ADVENIR's end date conflicts (end-2027 in the report vs 2030), and the new 2030 money favours heavy-vehicle and residential charging. The France 2030 call has closed. New York's round is federal, not state money. No source confirms that freed motorway sites will be tendered to third parties. The NEVI amount was confirmed from search results only. | CMA commitments 2022; New York round Dec 2024; France 2030 call closed end-2024; everything else 2025–26 | **Medium** |

**Overall confidence level: Medium.** The direction of Insights 1, 2 and 5 (supply, demand and policy) is supported by official statistics. Insights 3 and 4 (utilisation and competition) rest mainly on industry trackers, operator statements and press. Three things reduce precision:

1. **Charger definitions** differ across sources. That includes DfT's own change of counting unit in January 2026.
2. **Utilisation data** is thin, with none at all for Germany or France.
3. **32 errors in AI-generated material were found** during review (Appendix E): 18 in the Quick Research reports and 14 in the agent's outputs.
    - None is used in this brief's analysis.
    - Some remain visible in the embedded images V5, V7, V8, V9 and V10, whose rows in Section 5 say so.
    - The agent corrected two of its own errors (A1 and A2) when they were pointed out.
    - The two flawed agent charts are excluded from the Visual Evidence.

## 7. Limitations and Risks

- **Missing data:**
    - No German or French utilisation data, and no EU-specific payback data.
    - No verified rapid-only UK utilisation percentage. Zapmap's rapid session data (about 4 a day of about 38 minutes) implies roughly 10–11%, but it was read from search results only. Search results also cite 12.8% for 150 kW+ chargers in Q4 2025; this was not verified and is not used.
    - No site-level traffic, grid-capacity or land-cost data. No post-reform UK grid-connection times.
    - No DfT device count for 50 kW+ chargers after October 2025. The mid-2026 like-for-like UK ratio is an estimate.
    - No price elasticity.
    - The internal dataset stops at 2023. Its 2025/2030 values are IEA scenario projections published in April 2024, before the US credit expired and before Germany's 2026 grant.
- **Conflicting signals:**
    - The UK "doubled" claim vs the arithmetic (+58%).
    - US port growth of "30–35% a year" (2024→25) vs about 18–19% annualised from 1 January to 1 September 2026, in the same report.
    - The UK ratio on DfT's new unit (about 73) vs the old device basis (about 90).
    - ADVENIR: end-2027 (report) vs 2030 (July 2026 announcement).
    - UK public funding: "over £1 billion" (UK report; £1.08 B in the agent's briefs) vs the £400 M Spending Review money, the only new money aimed at the strategic network. LEVI's £381 M funds mostly slow on-street chargers, and Ofgem's £300 M was past grid upgrades.
- **Potential bias or ambiguity:**
    - Operator-authored sources have an interest in the story. Osprey says costs are high, and tracker counts are self-reported.
    - USDOT's 84% unobligated figure was issued during its own review of the programme.
    - One US demand figure (−31%) comes from a single press article with no URL.
    - The US report cites Wikipedia twice, including for the Tesla cost-per-stall claim; neither is used here.
    - Thirty-two AI errors were found (Appendix E), which shows that model outputs need human arithmetic and source checks.
    - Comparisons of EVs per charger across markets mix BEV-only and BEV+PHEV fleets and different kW thresholds.
- **Assumptions:**
    - A mid-size operator can win motorway site access against the service-area operators' own networks, and can finance 150 kW+ hubs.
    - Policy stays roughly as legislated through 2028.
    - The UK's pre-reform 5.5-year connection gap (July 2024, connecting customers in a queue dominated by generation and storage) is taken as indicative for charging sites; the reform's effect on demand connections is unknown.

## 8. Strategic Implications

**What decisions could this inform?**

- **Market sequencing:** Commit 2026–2027 development resources to the UK and keep France as a phase-two option. Move the US to monitor-only until a federal purchase incentive returns.
- **UK site strategy:**
    - Approach Moto, Roadchef and Extra for motorway site access as exclusivity ends after November 2026, expecting competition from their own networks and existing partners.
    - Favour sites with existing grid capacity, and check each one against the 37 motorway service areas with Green Recovery Scheme upgrades. No source links those 37 to the freed sites, so this is an assumption to test.
    - Also screen underserved regions: Northern Ireland, London (rapid chargers), Yorkshire and the Humber, and the North East.
    - Avoid greenfield sites that need a new grid connection.
- **Diligence to fund now:**
    - Grid-capacity feasibility on a UK shortlist.
    - Utilisation data by charger speed for the UK (Zapmap) and France (a source still to be found).
    - ADVENIR eligibility for public 150 kW+ car charging.

**Impact vs effort of recommended actions (with confidence)**

| Action | Impact | Effort | Confidence behind it |
|---|---|---|---|
| Grid-capacity check on 20–30 shortlisted UK sites | High | Low–Medium | Medium (grid cost matters; the delay data is pre-reform) |
| Buy UK utilisation data by charger speed (Zapmap) and find a French source | High | Low | High (largest data gap) |
| Approach Moto, Roadchef and Extra for motorway site access after November 2026 | High | Medium | Low–Medium (the 2022 commitments need a recheck, and the owners are building their own networks or expanding with partners) |
| France phase-two scoping, including ADVENIR eligibility for public 150 kW+ car charging | Medium | Medium | Medium |
| Watch Germany's Deutschlandnetz concessions for partnership entry | Low–Medium | Low | Medium |
| US: monitor-only; revisit if a federal purchase incentive returns | Low (for now) | Low | Medium |

**What should not be concluded from this research?**

- **Do not conclude any market is undersupplied from national ratios of EVs per charger.** The ratios use different charger definitions. Like for like, the gap has closed in Germany and France and narrowed modestly in the UK and US. White space exists only at site and region level.
- **Do not conclude the UK is profitable, or unprofitable.** No payback, NPV or IRR was modelled, and the about 8% utilisation figure covers all public chargers, not rapid ones.
- **Do not conclude the US is permanently unattractive.** The weakness is policy-driven, and the US remains the largest absolute market.
- **Do not treat IEA 2025/2030 projections as forecasts, or the UK mandate as a guaranteed sales level.** The US is running at roughly half the STEPS 2025 sales-share projection. UK manufacturers met the 2024 target through flexibilities while sales ran 2.4 points below it.
- **Do not rank Germany against France on EVs per charger.** France's latest count is 150 kW+ only; Germany's covers all DC fast chargers.

## 9. Summary for Leadership

**Executive Summary:**

1. The 2023 dataset's picture of a widening charging shortfall is out of date: fast-charger build-out has clearly outpaced the fleet in Germany and France, while like for like the UK ratio has narrowed only modestly (about 97–100 BEVs per 50 kW+ device through October 2025, about 90 in mid-2026) and the US ratio is only about 6–9% below 2023.
2. Returns now depend on winning well-connected sites and on utilisation, not on a national charger shortage.
3. Demand is driven largely by policy: UK BEV sales run below the ZEV mandate targets (52% for 2028) and manufacturers met the 2024 target through flexibilities, France is accelerating (BEV registrations up 62.9% in H1 2026), and US BEV share fell below 6% after the federal credit ended.
4. The UK is the recommended first market because exclusivity at about two-thirds of motorway service areas ends after November 2026, regions such as Northern Ireland have few rapid chargers (19.3 per 100,000 people vs a 41.7 UK average) and UK supply has overtaken the fleet less than in the EU core; France is phase two and the US is deferred.
5. Overall confidence is Medium: the supply, demand and policy findings rest on official statistics, but utilisation and competition rest on industry trackers, the service-area operators are building their own networks or expanding with existing partners, and 32 errors in AI-generated research and agent outputs were found and kept out of the analysis.
6. The immediate next steps are grid-capacity checks on a UK site shortlist, site-access talks with the service-area operators, buying utilisation data by charger speed, and tracking the UK ZEV mandate consultation before any capital commitment.

---

## Appendix A. Research questions that produced the strongest evidence

These are paraphrased. Fragments of the requests are visible in screenshots 03 (the UK research objective), 07a, 11a, 14a–14c (the brief request, including the correction) and 16. Screenshot 13a shows the agent acknowledging that correction.

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
| Market Analysis - EV Fast Charging 2026-2028.docx (agent document) | `deliverables/agent_outputs/01_…docx`: the corrected version, regenerated after Brief v2. Screenshots 11a–11e show the first, pre-correction version. |
| Reliability Evaluation - EV Fast Charging 2026-2028.docx (agent document) | `deliverables/agent_outputs/02_…docx`: the corrected version. Screenshots 12a–12e show the first version. |
| Market Intelligence Brief (v1) and Market Intelligence Brief v2 (.docx, agent documents) | `deliverables/agent_outputs/03_…docx` and `04_…docx`; screenshots 13a–13d and 14a–14c |
| Combined Market Analysis and Reliability document with four agent charts (from the agent chat; not added to the Space) | `deliverables/agent_outputs/05_…docx` |
| Market_Intelligence_Research_Brief_FINAL.pdf (this brief) | `deliverables/Market_Intelligence_Research_Brief.*` |

The Space also holds an earlier draft of this brief (Market_Intelligence_Research_Brief.pdf, uploaded before the reviews); the FINAL file supersedes it.

## Appendix C. Key primary sources

- **Dataset:** IEA Global EV Data 2024 (Kaggle mirror `patricklford/global-ev-sales-2010-2024`, CC BY 4.0).
- **UK:**
    - DfT EV charging infrastructure statistics (1 Jul 2026, published 27 Aug 2026).
    - SMMT full-year 2025 release (6 Jan 2026) and August 2026 registrations (4 Sep 2026).
    - CMA motorway charging commitments (8 Mar 2022).
    - VETS Order 2023 (gov.uk).
    - 2025 Spending Review charging allocation and the Strategic Charging Infrastructure consultation (gov.uk).
    - Zapmap utilisation and network statistics.
    - Ofgem connections blog (17 Jul 2024) and the DESNZ/Ofgem letter (Apr 2026).
    - Moto Charge launch (Zapmap, Dec 2025); Roadchef M6 hub (The Fast Charge, 6 Aug 2026); Extra with Ionity (electrive, Aug 2025).
- **US:**
    - EIA Today in Energy 67144 (9 Feb 2026) and 67885.
    - NADA Dec 2025 Market Beat.
    - AFDC/NREL charging infrastructure trends, Q4 2023.
    - evchargingstations.com, DC fast charging Sep 2026 (3 Sep 2026).
    - FHWA Notice N 4510.913 (12 Mar 2026).
    - Paren Q1 2025 industry report; theevreport.com.
    - RMI rate-design guidance.
    - IONNA announcement (ionna.com).
    - CEC Fast Charge California (5 Aug 2025) and FY2026–27 ZEV infrastructure plan (18 Aug 2026); NYSERDA corridor round (Dec 2024).
- **EU core:**
    - ACEA H1 2026 registrations (23 Jul 2026).
    - Bundesnetzagentur figures via heise (4 Feb and 31 Jul 2026) and electrive (4 Feb 2026).
    - Avere-France barometers and ADVENIR page.
    - French government electrification plan (ecologie.gouv.fr, 23 Apr 2026) and the ADVENIR extension announcement (7 Jul 2026).
    - IEA policy database (France 2030).
    - EU AFIR summary (EUR-Lex).
    - EV Boosters operator rankings.

## Appendix D. Primary-source spot-check log (26 September 2026)

| # | Figure checked | Result | Note |
|---|---|---|---|
| 1 | UK 50 kW+ chargers 28,887 (1 Jul 2026); regional density NI 19.3, London 27.9, UK 41.7 | Verified | DfT statistics, published 27 Aug 2026 |
| 2 | UK BEV 381,970 (19.6%) in 2024 and 473,348 (23.4%) in 2025 | Verified; citation corrected | The figures are in SMMT's 6 Jan 2026 full-year release, not the page the report cites |
| 3 | Gridserve's exclusive motorway rights end November 2026 | Verified | CMA commitments of 8 Mar 2022: exclusive rights not enforced after Nov 2026, covering about two-thirds of motorway service areas |
| 4 | Tesla 37,995 of 76,236 US DC ports (49.8%); "Other" up 44% | Verified | evchargingstations.com, 3 Sep 2026 |
| 5 | US credit expired 30 Sep 2025; BEV share 12% in September, below 6% in Q4 2025 | Verified | EIA, 9 Feb 2026 |
| 6 | $503.8 M of NEVI funds repurposed in March 2026 | Verified (search-result text; the page itself returned 403) | Exact figure $503,756,000, repurposed rather than rescinded |
| 7 | Germany DC fast points 54,341 (Jul 2026) and 48,729 (Jan 2026) | Verified | heise, 31 Jul 2026 and 4 Feb 2026 (the report's own references); electrive, 4 Feb 2026, reports the same January figure |
| 8 | ADVENIR extended to end-2027 with €200 M more (about €520 M total) | Amount verified; end date out of date | The government's electrification plan (23 Apr 2026) gave ADVENIR visibility to 2030, and on 7 Jul 2026 it announced about €400 M more; Avere-France's own ADVENIR page still shows end-2027 |
| 9 | France H1 2026 BEV registrations +62.9% | Verified | ACEA, 23 Jul 2026 |
| 10 | UK rapid utilisation about 8% (about 2 hours a day) | Wrong scope (search-result text; the page itself returned 403) | The figure is Zapmap's average for all public chargers, not rapid chargers |

## Appendix E. Errors found in AI-generated material

None of these errors is used in this brief's analysis. The embedded images V5, V7, V8, V9 and V10 still show some of them as produced, as their rows in Section 5 note.

| ID | Where | Error | Correct figure or handling |
|---|---|---|---|
| R1 | UK Quick Research report | BEV fleet "doubled" from about 1.33 M to about 2.1 M (summary, body and conclusion) | +58% |
| R2 | UK report | Summary and conclusion apply the about 8% all-charger utilisation to rapid chargers | The body labels it correctly; the brief uses the all-charger scope |
| R3 | UK report | "Over £1 billion" of funding counts the £400 M twice (as SCI and as the Spending Review) | Itemised in Section 7 |
| R4 | US report | "30–35% a year" growth in DC ports, against its own later figures | True for 2024→25; about 18–19% annualised from 1 Jan 2026 (67,916) to 1 Sep 2026 (243 days) |
| R5 | US report | "96–106 EVs per port" | Cannot be reproduced (96 is the 2023 fleet divided by December 2024 ports); like for like, about 115–119 in 2025–26 |
| R6 | US report | IONNA "targets 30,000 sites" | The target is at least 30,000 charging bays across North America |
| R7 | US report | New York's $28.5 M described as a state programme | It is a round of federal NEVI money |
| R8 | EU report | Germany's top 5 lists Ionity 5th | EWE Go (1,531) is 5th; Ionity (1,084) is 8th |
| R9 | EU report | France's top 5 mixes location segments | Reported by segment |
| R10 | EU report | "6–12 year payback" for Germany and France | Taken from a global review of solar-powered charging; not used |
| R11 | EU report | ADVENIR "extended to end-2027" | Extended to 2030 (announced 7 Jul 2026) |
| R12 | EU report | France 2030's €300 M presented as current support | The call closed at end-2024 |
| R13 | UK report | "YTD share of approximately 29.8%" through August 2026 | 29.8% is August's single-month share; January–August is 25.6% (SMMT) |
| R14 | US report | Ranks IONNA straight after Red E Charge, leaving out Blink (2,059) and EV Connect (1,731) | IONNA is 8th of the top 10 |
| R15 | UK report | Calls DfT's new counting unit "EVSE connectors" | DfT counts EV chargers (EVSEs); a connector is a different unit |
| R16 | UK report | Revenue estimate assumes about 2 sessions a day, citing a Zapmap page that gives about 4 | Not used |
| R17 | UK report | Presents Ofgem's pre-reform 5.5-year connection gap as the position after the 2026 reform | Dated July 2024 and flagged as pre-reform |
| R18 | EU report | Says Germany's top 5 hold "a substantial majority" of fast-charging capacity | About 40% of DC fast points |
| A1 | Agent reliability table (first version) | UK 2023 EV sales share given as 22.3%, with a "dip" to 19.6% | The dataset says 24% (BEV+PHEV), which is not comparable with a BEV-only share; corrected by the agent before Brief v1 |
| A2 | Agent Brief v1 | Scotland and Wales listed as underserved | Scotland is best served (59.1); corrected by the agent in Brief v2 |
| A3 | Agent Briefs v1 and v2 | UK ranked first partly on ">£1B" / "£1.08B" of public funding | Adds LEVI (mostly slow on-street) and Ofgem's past grid upgrades to the £400 M; see Section 7 |
| A4 | Agent Market Analysis | France's HPC-only count means "the true DC fast ratio is higher" | Backwards: counting all DC chargers lowers the ratio |
| A5 | Agent Reliability Evaluation (the second part is repeated in Briefs v1 and v2 and the combined document; screenshot 12d; the first part is plotted in chart V10) | US port growth 2023→24 of "+17.3%", mixing IEA chargers above 22 kW with DC ports; and end-2025 → Sep 2026 annualised at "about 16.5%" over an assumed 9 months | Like-for-like AFDC counts give about +32% for 2023→24 (38,271 → 50,428); the 243-day period gives about 18–19% annualised |
| A6 | Agent Reliability Evaluation | Says the UK report's body text is "more careful" than its summary | The body also says "doubled" |
| A7 | Agent Reliability Evaluation | France's +62.9% called an EU-wide ACEA figure | It is France-specific |
| A8 | Agent documents (corrected versions) | "ADVENIR runs to 2030" cited to the EU report | The 2030 date came from the primary-source check (Appendix D) |
| A9 | Agent Briefs v1 and v2 | About 920 words of prose against the agent's own 600-word limit | Noted; this brief is the leadership deliverable |
| A10 | Agent chart (excluded) | US operator pie shows Tesla at 54.2% | It divides by 70,095 listed ports instead of the 76,236 total; the correct share is 49.8% |
| A11 | Agent chart (excluded) | BEV-share bar chart compares France's single-month 38.8% with full-year and year-to-date shares elsewhere | Excluded |
| A12 | Agent chart V9 | US "latest" value of 101 is the midpoint of the report's 96–106, which breaks the agent's no-averaging rule; Germany's 70 is its own estimate, not the report's 71 | Annotated in Section 5; the recomputed US ratio is about 115–119 |
| A13 | Agent Market Analysis (both versions), Brief v1 and combined document | Repeats R10's "6–12 year payback" for Germany and France | Not used; visible only in the V8 screenshot |
| A14 | Agent Market Analysis, combined document and V8 table | Repeats R13's "29.8% YTD" | SMMT gives 25.6% for January–August |

The agent's Market Analysis (both versions) and combined document also repeat R6, R8, R9 and R18 in their competitor tables. These repeats are not counted separately, and none is used here.
