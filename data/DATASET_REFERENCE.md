# Dataset reference — IEA Global EV Data 2024

**Source:** International Energy Agency (IEA), *Global EV Data Explorer* / *Global EV Outlook 2024*.
**Retrieved from:** Kaggle — `patricklford/global-ev-sales-2010-2024`
(https://www.kaggle.com/datasets/patricklford/global-ev-sales-2010-2024), file `IEA Global EV Data 2024.csv`, version 1.
**Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0).
**Size:** 12,654 rows × 8 columns.

## Columns

| Column | Meaning |
|---|---|
| `region` | Country, bloc (`EU27`, `Europe`), or aggregate (`World`, `Rest of the world`). 54 values. |
| `category` | `Historical` (reported data, 2010–2023), `Projection-STEPS` (IEA Stated Policies Scenario), `Projection-APS` (IEA Announced Pledges Scenario). Projections cover 2025, 2030 and 2035. |
| `parameter` | `EV sales`, `EV stock`, `EV sales share`, `EV stock share`, `EV charging points`, `Electricity demand`, `Oil displacement Mbd`, `Oil displacement, million lge`. |
| `mode` | `Cars`, `Buses`, `Vans`, `Trucks`, or `EV` (used for charging points). |
| `powertrain` | `BEV` (battery electric), `PHEV` (plug-in hybrid), `FCEV` (fuel cell), `EV` (all electric), or for charging points `Publicly available fast` / `Publicly available slow`. |
| `year` | Calendar year. |
| `unit` | `Vehicles`, `percent`, `charging points`, `GWh`, `Milion barrels per day`, `Oil displacement, million lge`. |
| `value` | The measured or projected value in `unit`. |

## How to read it

- **EV car stock / sales** for a market = sum of `BEV` + `PHEV` (+ `FCEV` where present) rows with `mode = Cars`.
- **EV sales share** rows (`powertrain = EV`, `unit = percent`) are the share of all new cars sold that were electric, already in percent (e.g. `24` = 24%).
- **Public fast chargers** = `parameter = EV charging points`, `powertrain = Publicly available fast` (IEA: > 22 kW).
- **EVs per public fast charger** = EV car stock ÷ public fast chargers, same year.
- Historical data ends in **2023**. Anything for 2025 or later is an IEA scenario projection, not an observation, and predates policy changes made after the Global EV Outlook 2024 was published.

## Files in this Space

- `IEA Global EV Data 2024.csv` — the full, unmodified Kaggle file.
- `iea_ev_cars_and_charging_focus_markets_2018_2030.csv` — a 695-row filter of the same file (no values changed): 10 focus markets (USA, Canada, United Kingdom, EU27, Germany, France, Netherlands, Norway, China, World); parameters EV stock, EV sales, EV sales share and EV charging points; historical 2018–2023 plus 2025/2030 projections.
