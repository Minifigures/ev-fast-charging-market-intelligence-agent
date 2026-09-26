#!/usr/bin/env python3
"""
EV fast-charging gap analysis on the IEA Global EV Data 2024 (Kaggle mirror).

Computes, for each candidate market, the internal-dataset signals used in the
Market Intelligence Brief: EV car stock and sales, BEV share of sales, public
fast and slow charging points, EVs per public fast charger, and the IEA STEPS
2030 projection for the car EV stock.

Usage:  python3 analysis/ev_charging_gap.py
Output: analysis/ev_charging_gap.json and analysis/ev_charging_gap.md
"""

import csv
import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "IEA Global EV Data 2024.csv")

MARKETS = ["USA", "Canada", "United Kingdom", "EU27", "Germany", "France",
           "Netherlands", "Norway", "China", "World"]

rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))

# index: (region, category, parameter, mode, powertrain, year) -> value
V = {}
for r in rows:
    V[(r["region"], r["category"], r["parameter"], r["mode"], r["powertrain"],
       int(r["year"]))] = float(r["value"])


def get(region, parameter, mode, powertrain, year, category="Historical"):
    return V.get((region, category, parameter, mode, powertrain, year))


def car_ev(region, parameter, year, category="Historical"):
    """BEV + PHEV (+ FCEV where present) for passenger cars."""
    total, seen = 0.0, False
    for pt in ("BEV", "PHEV", "FCEV"):
        v = get(region, parameter, "Cars", pt, year, category)
        if v is not None:
            total += v
            seen = True
    return total if seen else None


def pct(a, b):
    return None if (a is None or b in (None, 0)) else round(100.0 * (a - b) / b, 1)


out = {}
for m in MARKETS:
    stock23 = car_ev(m, "EV stock", 2023)
    stock22 = car_ev(m, "EV stock", 2022)
    sales23 = car_ev(m, "EV sales", 2023)
    sales22 = car_ev(m, "EV sales", 2022)
    bev23 = get(m, "EV sales", "Cars", "BEV", 2023)
    share23 = get(m, "EV sales share", "Cars", "EV", 2023)
    share22 = get(m, "EV sales share", "Cars", "EV", 2022)
    fast23 = get(m, "EV charging points", "EV", "Publicly available fast", 2023)
    fast22 = get(m, "EV charging points", "EV", "Publicly available fast", 2022)
    slow23 = get(m, "EV charging points", "EV", "Publicly available slow", 2023)
    steps30 = car_ev(m, "EV stock", 2030, "Projection-STEPS")
    aps30 = car_ev(m, "EV stock", 2030, "Projection-APS")
    out[m] = {
        "car_ev_stock_2023": stock23,
        "car_ev_stock_growth_2022_23_pct": pct(stock23, stock22),
        "car_ev_sales_2023": sales23,
        "car_ev_sales_growth_2022_23_pct": pct(sales23, sales22),
        "bev_share_of_car_ev_sales_2023_pct": round(100 * bev23 / sales23, 1) if bev23 and sales23 else None,
        "car_ev_sales_share_2023_pct": share23,
        "car_ev_sales_share_2022_pct": share22,
        "public_fast_chargers_2023": fast23,
        "public_fast_chargers_growth_2022_23_pct": pct(fast23, fast22),
        "public_slow_chargers_2023": slow23,
        "car_evs_per_fast_charger_2023": round(stock23 / fast23, 1) if stock23 and fast23 else None,
        "car_evs_per_public_charger_2023": round(stock23 / (fast23 + slow23), 1) if stock23 and fast23 and slow23 else None,
        "steps_car_ev_stock_2030": steps30,
        "aps_car_ev_stock_2030": aps30,
        "steps_stock_multiple_2023_to_2030": round(steps30 / stock23, 2) if steps30 and stock23 else None,
    }

# fast-charger trajectory for the three candidate markets
traj = {}
for m in ("USA", "EU27", "United Kingdom", "Canada"):
    traj[m] = {y: {"fast": get(m, "EV charging points", "EV", "Publicly available fast", y),
                   "car_ev_stock": car_ev(m, "EV stock", y)}
               for y in range(2018, 2024)}

json.dump({"markets": out, "trajectory": traj}, open(os.path.join(ROOT, "analysis", "ev_charging_gap.json"), "w"), indent=2)


def f(x, d=0):
    if x is None:
        return "n/a"
    return f"{x:,.{d}f}"


L = ["# EV fast-charging gap — IEA Global EV Data 2024 (passenger cars)\n",
     "Source: IEA Global EV Data 2024, via Kaggle `patricklford/global-ev-sales-2010-2024` (CC BY 4.0).",
     "Historical values are 2010–2023; 2030 values are IEA projections (STEPS = stated policies, APS = announced pledges).\n",
     "| Market | EV car stock 2023 | Stock growth 22→23 | EV car sales 2023 | Sales growth 22→23 | EV sales share 2023 | BEV share of EV sales | Public fast chargers 2023 | Fast-charger growth 22→23 | EVs per fast charger | STEPS stock 2030 | 2030 ÷ 2023 |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for m, d in out.items():
    L.append(f"| {m} | {f(d['car_ev_stock_2023'])} | {f(d['car_ev_stock_growth_2022_23_pct'],1)}% | "
             f"{f(d['car_ev_sales_2023'])} | {f(d['car_ev_sales_growth_2022_23_pct'],1)}% | "
             f"{f(d['car_ev_sales_share_2023_pct'],1)}% | {f(d['bev_share_of_car_ev_sales_2023_pct'],1)}% | "
             f"{f(d['public_fast_chargers_2023'])} | {f(d['public_fast_chargers_growth_2022_23_pct'],1)}% | "
             f"{f(d['car_evs_per_fast_charger_2023'],1)} | {f(d['steps_car_ev_stock_2030'])} | "
             f"{f(d['steps_stock_multiple_2023_to_2030'],2)}× |")
L.append("\n## Fast-charger build-out vs EV car stock, 2018–2023\n")
L.append("| Market | Year | Public fast chargers | EV car stock | EVs per fast charger |")
L.append("|---|---|---|---|---|")
for m, ys in traj.items():
    for y, d in ys.items():
        ratio = d["car_ev_stock"] / d["fast"] if d["fast"] and d["car_ev_stock"] else None
        L.append(f"| {m} | {y} | {f(d['fast'])} | {f(d['car_ev_stock'])} | {f(ratio,1)} |")
open(os.path.join(ROOT, "analysis", "ev_charging_gap.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
