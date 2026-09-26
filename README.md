# EV Fast-Charging Market Intelligence Agent (Amazon Quick Suite)

A no-code market intelligence workflow built in **Amazon Quick Suite**. It answers one question for a mid-size public DC fast-charging operator: **which market should it prioritise for its 2026–2028 expansion — the United Kingdom, the United States, or the EU core (Germany and France)?**

The workflow combines an internal dataset (IEA Global EV Data 2024, from Kaggle) with three Quick Research reports. A custom chat agent turns them into a Market Analysis, a Reliability Evaluation and a leadership brief. Every headline figure was then checked against its primary source before the final brief was written.

**Recommendation:** prioritise the **UK** with a site-led entry. Motorway service areas open to competition from November 2026, and several regions remain underserved. Scope **France** as phase two, and **defer the US** until demand recovers. **Overall confidence: Medium.**

➡️ **Read the brief:** [`deliverables/Market_Intelligence_Research_Brief.pdf`](deliverables/Market_Intelligence_Research_Brief.pdf) (also as [`.docx`](deliverables/Market_Intelligence_Research_Brief.docx) and [`.md`](deliverables/Market_Intelligence_Research_Brief.md))

---

## Key findings

| # | Insight | Confidence |
|---|---|---|
| 1 | **The 2023 "charging gap" has largely closed.** In the dataset, the UK had 158 EVs per public fast charger in 2023. By July 2026 UK 50 kW+ chargers had nearly tripled (10,118 → 28,887). The build-out now outruns the fleet in all four markets. | Medium |
| 2 | **Demand follows policy.** The UK ZEV mandate sets a legal floor (52% of new-car sales by 2028), and France is up +62.9% (H1 2026). US BEV share fell below 6% after the federal credit expired in September 2025. | High (direction) |
| 3 | **Utilisation and grid cost are the binding constraints.** UK public chargers average about 8% utilisation (all speeds), against a US DC figure of about 16% and a roughly 15% breakeven. UK grid standing charges rose from £99 to £8,600 a year, and grid-connection queues average 5.5 years. | Medium-Low |
| 4 | **Competition is concentrated in the US and Germany, fragmented in the UK and France.** Tesla holds 49.8% of US DC ports; EnBW leads Germany. The UK has 100–150 operators consolidating toward 5–6. | Medium |
| 5 | **The entry windows are time-bound.** The UK motorway opening starts November 2026 (CMA). France's ADVENIR subsidy programme runs to 2030. $503.8 M of US federal NEVI charging funds was repurposed in March 2026. | Medium |

## What was built in Quick Suite

```
Kaggle dataset ──► Space "EV Fast-Charging Market Intelligence 2026-2028"
                     │   IEA Global EV Data 2024 + focus-market filter + DATASET_REFERENCE.md
                     │
Quick Research ──────┤   UK (Deep) · US (Fast) · Germany/France (Fast)
 (Space attached     │   preferred sites: gov.uk/DfT, SMMT, Ofgem, AFDC, FHWA, EIA, ACEA,
  as a Quick asset)  │   Bundesnetzagentur, Avere-France · avoided: reddit, quora, medium, social
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

The agent's instructions, summarised; the full text is visible in screenshots 04–05:

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

- **Dataset recomputed independently.** `analysis/ev_charging_gap.py` (Python standard library only) re-derives every dataset metric the agent used: EV car stock, public fast chargers, EVs per fast charger and STEPS projections. The agent's comparison table matches it to rounding; the agent shows the US 9.5% share as 10%.
- **Arithmetic checks inside Quick.** The agent tested three claims from the research reports and found two problems:
  - The UK report's claim that the BEV fleet "doubled" is actually +58%.
  - The US report cites "30–35% a year" growth in DC ports, but its own figures imply about 16.5% annualised in 2026.
- **Primary-source spot-check of 10 headline figures.** Six were verified as written and two were verified with a corrected citation. One end date was out of date: ADVENIR runs to 2030, not end-2027. One had the wrong scope: the ~8% UK utilisation figure covers all chargers, not rapid chargers only.
- **Four AI errors caught and corrected before Brief v2:**
  - The UK research report's "doubled" claim.
  - The US report's inconsistent growth rate.
  - The agent citing a UK 2023 share of 22.3% (the dataset says 24%).
  - The agent listing Scotland, the best-served UK region, as underserved.

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
screenshots/
  01–07   Space, Quick Research set-up, agent configuration, first agent test
  08–10   Quick Research reports (UK, US, EU core)
  11a–11e Market Analysis (agent)
  12a–12e Reliability Evaluation (agent)
  13a–13d Leadership Brief v1 (agent)
  14a–14c Leadership Brief v2 after fact-check (agent)
  15a     Space contents (11 items: dataset, research, analysis, reliability, briefs)
  16      agent scope test (refuses IRR, stock picks, post-2030 forecasts)
  visuals/ charts from the Quick Research reports, used as Visual Evidence
tools/
  build_brief.py                                    builds the .docx/.html from the Markdown brief
```

## Reproduce

```bash
python3 analysis/ev_charging_gap.py
```

That regenerates `analysis/ev_charging_gap.{md,json}` from the CSV using only the standard library.

To rebuild the brief, install `python-docx` and `markdown` in a virtual environment, then run:

```bash
python tools/build_brief.py path/to/research-brief-template.docx
```

That writes the `.docx` and an `.html`. The PDF is printed from the HTML.

## Data and sources

- **Internal dataset:** IEA *Global EV Outlook 2024* data via Kaggle [`patricklford/global-ev-sales-2010-2024`](https://www.kaggle.com/datasets/patricklford/global-ev-sales-2010-2024), licensed CC BY 4.0. Historical data ends in 2023; values for 2025 onward are IEA scenario projections.
- **External research:** generated with Amazon Quick Research on 26 September 2026. Every claim in the reports links to its source, and the reference lists are in the PDFs. The primary sources behind the brief are listed in its Appendix C.

## Context

Built for the Udacity **AWS AI & ML Scholars** programme, course *Building No-Code AI Agents with Amazon Quick*, project *Building a Market Research Agent*. The scenario (a mid-size charging operator) is illustrative; nothing here is investment advice.

**Author:** Marco Ayuste
