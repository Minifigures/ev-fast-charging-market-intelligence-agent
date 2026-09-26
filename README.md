# EV Fast-Charging Market Intelligence Agent (Amazon Quick Suite)

A no-code market intelligence workflow built in **Amazon Quick Suite**. It answers one question for a mid-size public DC fast-charging operator: **which market should it prioritise for its 2026–2028 expansion — the United Kingdom, the United States, or the EU core (Germany and France)?**

The workflow combines an internal dataset (IEA Global EV Data 2024, from Kaggle) with three Quick Research reports. A custom chat agent turns them into a Market Analysis, a Reliability Evaluation and a leadership brief. Ten headline figures were spot-checked against their primary sources, and the final brief went through three line-by-line reviews against the reports, the dataset and the agent's documents.

**Recommendation:** prioritise the **UK** with a site-led entry. Gridserve's exclusive rights at about two-thirds of motorway service areas stop being enforced after November 2026, although Moto and Roadchef are building their own networks and Extra is expanding with Ionity. Several regions remain underserved, and UK supply has overtaken the fleet less than in the EU core. Scope **France** as phase two, and **defer the US** (monitor only) until a federal purchase incentive returns. **Overall confidence: Medium.**

➡️ **Read the brief:** [`deliverables/Market_Intelligence_Research_Brief.pdf`](deliverables/Market_Intelligence_Research_Brief.pdf) (also as [`.docx`](deliverables/Market_Intelligence_Research_Brief.docx) and [`.md`](deliverables/Market_Intelligence_Research_Brief.md))

---

## Key findings

| # | Insight | Confidence |
|---|---|---|
| 1 | **The 2023 "charging gap" has closed in Germany and France and narrowed in the UK.** In the dataset, the UK had 158 EVs per public fast charger in 2023. UK 50 kW+ chargers went from 10,118 (Jan 2024) to 28,887 (Jul 2026), but DfT switched from counting charging devices to counting EV chargers (EVSEs) in January 2026. Like for like, UK BEVs per 50 kW+ device held at about 97–100 through October 2025 and are about 90 in mid-2026. On a consistent DC-port count, the US ratio is only about 6–9% below 2023. | Medium |
| 2 | **Demand is driven largely by policy.** UK BEV sales run below the ZEV mandate targets (52% for 2028); manufacturers met the 2024 target through compliance flexibilities. UK BEV share was 25.6% for January–August 2026 (SMMT). French BEV registrations are up 62.9% year on year (H1 2026, ACEA). US BEV share fell below 6% after the federal credit expired in September 2025. | Medium |
| 3 | **Utilisation and grid cost are the binding constraints.** UK public chargers average about 8% utilisation (all speeds). The US DC figure is about 16%, against a roughly 15% breakeven. Grid standing charges for a typical UK ultra-rapid hub rose from £99 to £8,600 a year between 2022 and 2024 (example from the operator Osprey). Ofgem's pre-reform data (July 2024) showed a 5.5-year gap between requested and offered connection dates. | Low |
| 4 | **Competition is concentrated in the US and moderately concentrated in Germany; it is fragmented in the UK and France.** Tesla holds 49.8% of US DC ports. In Germany, EnBW holds about 16% of fast points and the top 5 about 40%, with the subsidised Deutschlandnetz rollout as the bigger barrier. The UK has 100–150 operators consolidating toward 5–6; France is fragmented and split by location type. | Medium |
| 5 | **The entry windows are time-bound but contested.** Gridserve's motorway exclusivity (about two-thirds of service areas) ends after November 2026, but Moto and Roadchef are building their own networks and Extra is expanding with Ionity. France's ADVENIR runs to 2030, but its new money favours heavy-vehicle and residential charging. $503.8 M of US federal NEVI charging funds was repurposed in March 2026. | Medium |

## What was built in Quick Suite

```
Kaggle dataset ──► Space "EV Fast-Charging Market Intelligence 2026-2028"
                     │   IEA Global EV Data 2024 + focus-market filter + DATASET_REFERENCE.md
                     │
Quick Research ──────┤   UK (Deep) · US (Fast) · Germany/France (Fast)
 (Space attached     │   preferred sites: gov.uk, Zapmap, SMMT, Ofgem, AFDC, FHWA, IEA, ACEA,
  as a Quick asset)  │   Bundesnetzagentur, KBA, Avere-France · avoided: reddit, quora, medium, social
                     │   → exported to the Space and to PDF
                     ▼
Chat agent "Market Intelligence Agent – EV Fast Charging" (knowledge = the Space)
   1. Market Analysis        comparison table · competitive landscape · trends · opportunities and risks
   2. Reliability Evaluation 5 insights × evidence / gaps / source quality / consistency / timeliness / confidence
                             + arithmetic checks on 3 research claims
   3. Leadership Brief v1 → human fact-check → Leadership Brief v2 (corrected)
                     ▼
Research Brief (this repo)   9-section course template + decision dashboard, freshness notes,
                             "what would change our mind", impact-vs-effort matrix
```

### Agent configuration

The agent's instructions, summarised. The full text is visible in screenshots 04–05, and the details panel with its knowledge source (the Space) is in 06:

- **Purpose:** analyse the dataset and external market signals to produce a market analysis and a brief leadership can act on.
- **Scope:** a mid-size DC fast-charging operator; the UK, US and EU core; 2026–2028; public DC fast charging for passenger cars.
- **Knowledge:** the Space. It reads `DATASET_REFERENCE.md` first and labels every figure `[Dataset, year]` or `[Research: source, date]`.
- **Behaviour rules:**
  - Say "not in my sources" rather than guess.
  - Where sources conflict, show both figures and never average them.
  - Treat IEA values for 2025 onward as scenarios, not forecasts.
  - Keep a confidence rating unless new evidence justifies changing it.
- **Formats:** a six-section Market Analysis and a Leadership Brief of at most 600 words that opens with a one-sentence answer.
- **Limits:** no investment, legal or financial advice; no payback, NPV or IRR; no companies that are not in its sources; no predictions beyond 2030.

## Validation: how the numbers were checked

- **Dataset recomputed independently.** `analysis/ev_charging_gap.py` (Python standard library only) re-derives the 2023 dataset metrics (EV car stock, public fast chargers, EVs per fast charger, sales share). The IEA projection values quoted in the brief were read directly from the CSV. The agent's first dataset test (screenshots 07a–07b) and its comparison table match it to rounding; the agent shows the US 9.5% share as 10%.
- **Arithmetic checks inside Quick.** The agent tested three claims from the research reports and found two problems:
  - The UK report's claim that the BEV fleet "doubled" is actually +58%.
  - The US report cites "30–35% a year" growth in DC ports. The agent showed this holds only for 2024→2025, and put 2026 at about 16.5% annualised over an assumed 9 months (screenshot 12d). Over the actual 243 days from 1 January to 1 September 2026 it is about 18–19%, the figure the brief uses.
- **Primary-source spot-check of 10 headline figures.** Seven were verified as written and one was verified with a corrected citation. One end date was out of date: ADVENIR runs to 2030, not end-2027. One had the wrong scope: the ~8% UK utilisation figure covers all chargers, not rapid chargers only.
- **Three line-by-line reviews of the brief** against the reports, the dataset and the agent's documents. Together with the checks above they found 32 errors in AI-generated material: 18 in the Quick Research reports and 14 in the agent's outputs. They are listed in the brief's Appendix E, and none is used in the brief's analysis; the embedded V5 and V7–V10 images still show a few, and their Section 5 rows flag them. Examples:
  - The UK report says the BEV fleet "doubled"; it grew 58%.
  - The US report gives "96–106 EVs per port", which cannot be reproduced. Recomputed on a consistent DC-port count, the ratio is about 115–119, only 6–9% below 2023.
  - The UK report's "29.8% year to date" BEV share is August's single-month share; SMMT gives 25.6% for January–August.
  - The EU report lists Ionity as Germany's 5th-largest fast-charging network; it is 8th.
  - An agent chart shows Tesla at 54.2% of US DC ports; the correct share is 49.8%. That chart and one other flawed chart are kept out of the Visual Evidence.

## Repository layout

```
data/
  IEA Global EV Data 2024.csv                       full Kaggle file (CC BY 4.0), 12,654 rows × 8 columns
  iea_ev_cars_and_charging_focus_markets_2018_2030.csv   695-row filter uploaded alongside it
  DATASET_REFERENCE.md                              columns, units, how to read the file
analysis/
  ev_charging_gap.py                                recomputes the dataset metrics
  ev_charging_gap.md / .json                        its output
deliverables/
  Market_Intelligence_Research_Brief.{pdf,docx,md}  the submission brief (9 template sections + extras)
  quick_research_reports/                           the three Quick Research reports (PDF)
  agent_outputs/                                    the agent's documents (01–04 from the Space, 05 from the agent chat):
                                                    01 Market Analysis · 02 Reliability Evaluation ·
                                                    03 Brief v1 · 04 Brief v2 · 05 combined doc with 4 agent charts
screenshots/
  01      Space with the dataset uploaded
  02–03   UK Quick Research set-up (preferred sites), Deep run in progress (02b) and revised plan
  04–06   agent configuration (instructions, scope limits) and knowledge source (the Space)
  07a–07b first agent test: 2023 dataset table matching the recomputation
  08      UK research report · 09a–09b US report and its materials · 10a–10b EU core report and its materials
  11a–11e Market Analysis (agent)
  12a–12e Reliability Evaluation (agent)
  13a–13d Leadership Brief v1 (agent)
  14a–14c Leadership Brief v2 after fact-check (agent)
  15a–15b Space contents (dataset, research reports, analysis, reliability, both agent briefs, this brief)
  16      agent scope test (refuses IRR, stock picks, post-2030 forecasts)
  visuals/ v1–v7 charts from the Quick Research reports; v9–v10 charts generated by the agent;
           excluded_flawed_agent_charts/ two agent charts with errors, kept as a record
tools/
  build_brief.py                                    builds the .docx/.html from the Markdown brief
```

## Reproduce

```bash
python3 analysis/ev_charging_gap.py
```

That regenerates `analysis/ev_charging_gap.{md,json}` from the CSV using only the standard library.

To rebuild the brief, install `python-docx` and `markdown` in a virtual environment, then run the command below. It needs the course's Research Brief template (.docx), which is not redistributed here.

```bash
python tools/build_brief.py path/to/research-brief-template.docx
```

That writes the `.docx` and an `.html`. The PDF is printed from the HTML.

## Data and sources

- **Internal dataset:** IEA *Global EV Outlook 2024* data via Kaggle [`patricklford/global-ev-sales-2010-2024`](https://www.kaggle.com/datasets/patricklford/global-ev-sales-2010-2024), licensed CC BY 4.0. Historical data ends in 2023; values for 2025 onward are IEA scenario projections.
- **External research:** generated with Amazon Quick Research on 26 September 2026. Most claims in the reports are linked to a numbered reference; a few references have no URL or point to the private lab Space. The reference lists are in the PDFs. The primary sources behind the brief are listed in its Appendix C.

## Context

Built for the Udacity **AWS AI & ML Scholars** programme, course *Building No-Code AI Agents with Amazon Quick*, project *Building a Market Research Agent*. The scenario (a mid-size charging operator) is illustrative; nothing here is investment advice.

**Author:** Marco Ayuste
