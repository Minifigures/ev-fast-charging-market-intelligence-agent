#!/usr/bin/env python3
"""
Build the Research Brief deliverables from the Markdown source.

  deliverables/Market_Intelligence_Research_Brief.md   (source of truth)
    -> deliverables/Market_Intelligence_Research_Brief.docx  (Udacity template styles)
    -> deliverables/Market_Intelligence_Research_Brief.html  (for PDF printing)

The DOCX starts from the course Research Brief template so its heading styles
carry over; the body is replaced with the Markdown content, and the charts
referenced in the Visual Evidence section are embedded at the end.

Requires: python-docx, markdown   (pip install python-docx markdown)
Usage:    python tools/build_brief.py <path-to-template.docx>
"""

import os
import re
import sys

import markdown
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "deliverables", "Market_Intelligence_Research_Brief.md")
OUT_DOCX = os.path.join(ROOT, "deliverables", "Market_Intelligence_Research_Brief.docx")
OUT_HTML = os.path.join(ROOT, "deliverables", "Market_Intelligence_Research_Brief.html")

# Visual Evidence images, in the order of the V1..V8 table rows.
VISUALS = [
    ("V1", "screenshots/visuals/v1_uk_bev_share_vs_zev_mandate_line.png", "UK BEV share vs ZEV mandate targets (Quick Research, UK report)"),
    ("V2", "screenshots/visuals/v2_uk_rapid_ultrarapid_charger_growth_stacked_bar.png", "UK rapid and ultra-rapid charger growth (Quick Research, UK report)"),
    ("V3", "screenshots/visuals/v3_uk_regional_rapid_density_bar.png", "UK regional rapid charger density (Quick Research, UK report)"),
    ("V4", "screenshots/visuals/v4_us_dc_ports_actual_vs_iea_steps_line.png", "US DC fast ports vs IEA STEPS (Quick Research, US report)"),
    ("V5", "screenshots/visuals/v5_us_networks_by_port_count_bar.png", "US DC fast networks by port count, Sep 2026 (Quick Research, US report)"),
    ("V6", "screenshots/visuals/v6_de_fr_evs_per_fast_charger_bar.png", "EVs per fast charger, Germany and France (Quick Research, EU report)"),
    ("V7", "screenshots/visuals/v7_de_fr_top_hpc_operators_bar.png", "Top HPC operators, Germany and France (Quick Research, EU report)"),
    ("V8", "screenshots/11b_market_analysis_comparison_table.png", "Market comparison table (Market Intelligence Agent)"),
    ("V9", "screenshots/visuals/v9_agent_evs_per_fast_charger_2023_vs_latest.png", "EVs per fast charger, 2023 vs latest (Market Intelligence Agent chart)"),
    ("V10", "screenshots/visuals/v10_agent_us_dc_port_growth_2023_2026.png", "US DC fast port growth 2023 to Sep 2026 (Market Intelligence Agent chart)"),
]

INLINE = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*)")


def add_runs(par, text):
    """Add text to a paragraph, honouring **bold**, *italic* and `code`."""
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            par.add_run(part[2:-2]).bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = par.add_run(part[1:-1])
            r.font.name = "Menlo"
            r.font.size = Pt(9)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            par.add_run(part[1:-1]).italic = True
        else:
            par.add_run(part)


def set_borders(table):
    """The template has no 'Table Grid' style, so draw single-line borders directly."""
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:color"), "BFC4C9")
        borders.append(el)
    tbl_pr.append(borders)


def add_table(doc, rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
    ncol = max(len(r) for r in cells)
    t = doc.add_table(rows=len(cells), cols=ncol)
    set_borders(t)
    for i, r in enumerate(cells):
        for j in range(ncol):
            txt = r[j] if j < len(r) else ""
            p = t.cell(i, j).paragraphs[0]
            add_runs(p, txt)
            for run in p.runs:
                run.font.size = Pt(8.5)
                if i == 0:
                    run.bold = True
    doc.add_paragraph()


def build_docx(template):
    doc = Document(template)
    body = doc.element.body
    for el in list(body):
        if not el.tag.endswith("sectPr"):
            body.remove(el)

    lines = open(SRC, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped or stripped == "---":
            i += 1
            continue
        if stripped.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            add_table(doc, block)
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            doc.add_heading(m.group(2), level=level)
        elif re.match(r"^\s*[-*]\s+", line):
            # the template has no list styles: indent and prefix a bullet instead
            indent = len(line) - len(line.lstrip())
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25 + 0.25 * (indent // 4))
            p.paragraph_format.first_line_indent = Inches(-0.15)
            p.add_run("• ")
            add_runs(p, re.sub(r"^\s*[-*]\s+", "", line))
        elif re.match(r"^\d+\.\s+", stripped):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.first_line_indent = Inches(-0.2)
            num, rest = stripped.split(".", 1)
            p.add_run(f"{num}. ")
            add_runs(p, rest.strip())
        else:
            p = doc.add_paragraph()
            add_runs(p, stripped)
        i += 1

    doc.add_page_break()
    doc.add_heading("Visual Evidence: images", level=2)
    for tag, rel, caption in VISUALS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        doc.add_picture(path, width=Inches(6.2))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = cap.add_run(f"{tag}. {caption}")
        r.italic = True
        r.font.size = Pt(9)
    props = doc.core_properties
    props.author = props.last_modified_by = "Marco Ayuste"
    props.title = "Market Intelligence Research Brief"
    doc.save(OUT_DOCX)


CSS = """
body { font-family: -apple-system, Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; max-width: 7.2in; margin: 0 auto; }
h1 { font-size: 20pt; margin-bottom: 4pt; color: #232f3e; }
h2 { font-size: 14pt; border-bottom: 1.5px solid #ff9900; padding-bottom: 2pt; margin-top: 18pt; color: #232f3e; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin-top: 12pt; color: #232f3e; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 8.8pt; page-break-inside: avoid; }
th, td { border: 1px solid #c8ccd0; padding: 4pt 5pt; vertical-align: top; text-align: left; }
th { background: #f2f4f6; }
code { font-family: Menlo, monospace; font-size: 8.5pt; background: #f4f4f4; padding: 0 2pt; }
ul, ol { padding-left: 18pt; }
li { margin: 2pt 0; }
figure { margin: 10pt 0 14pt; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; border: 1px solid #ddd; }
figcaption { font-size: 8.5pt; font-style: italic; color: #555; }
hr { border: 0; border-top: 1px solid #ddd; }
"""


def build_html():
    md = open(SRC, encoding="utf-8").read()
    html = markdown.markdown(md, extensions=["tables", "sane_lists"])
    figs = ['<h2 style="page-break-before: always">Visual Evidence: images</h2>']
    for tag, rel, caption in VISUALS:
        if os.path.exists(os.path.join(ROOT, rel)):
            figs.append(f'<figure><img src="../{rel}"><figcaption>{tag}. {caption}</figcaption></figure>')
    page = ("<!doctype html><html><head><meta charset='utf-8'><title>Market Intelligence Research Brief</title>"
            f"<style>{CSS}</style></head><body>{html}{''.join(figs)}</body></html>")
    open(OUT_HTML, "w", encoding="utf-8").write(page)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build_docx(sys.argv[1])
    build_html()
    print("wrote", OUT_DOCX)
    print("wrote", OUT_HTML)
