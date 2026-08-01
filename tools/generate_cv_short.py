#!/usr/bin/env python3
"""Generate SHORT academic CV PDF for Wookyoung Kim (≤2 pages).

Compact 2-page CV: counts replace full lists for papers/patents/etc.
Source: assets/json/resume.json. Output: assets/pdf/cv_academic_short.pdf.
"""

import yaml
import os
import re

from fpdf import FPDF
from fpdf.enums import XPos, YPos

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
PHOTO_PATH = os.path.join(REPO_ROOT, "assets/img/prof_pic.jpg")
OUTPUT_PATH = os.path.join(REPO_ROOT, "assets/pdf/cv_academic_short.pdf")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

KOREAN_PUBLISHERS = {
    "Journal of Hydrogen and New Energy",
    "Korean Journal of Air-Conditioning and Refrigeration Engineering",
    "Transactions of the Korean Society of Mechanical Engineers B",
    "Transactions of the Korean Hydrogen and New Energy Society",
}


class ShortCV(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(left=20, top=14, right=20)
        self.set_auto_page_break(auto=True, margin=10)
        self.add_page()

    def footer(self):
        self.set_y(-9)
        self.set_font("Helvetica", size=8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 4, str(self.page_no()), align="C")
        self.set_text_color(0, 0, 0)

    def section_title(self, title):
        self.ln(2)
        self.set_font("Helvetica", style="B", size=11)
        self.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y = self.get_y()
        self.set_line_width(0.3)
        self.line(self.l_margin, y, self.l_margin + self.epw, y)
        self.ln(1)


def _period(sd, ed):
    if sd and ed and sd != ed:
        return f"{sd}-{ed}"
    if sd and not ed:
        return f"{sd}-Present"
    if sd == ed and sd:
        return sd
    return ""


def _aff_period(sd, ed):
    if sd and not ed:
        return f"{sd.replace('-', '.')}-Present"
    if sd and ed:
        return f"{sd.replace('-', '.')}-{ed.replace('-', '.')}"
    return ""


def build_short_cv():
    with open(os.path.join(REPO_ROOT, "_data/resume.yml"), "r") as f:
        data = yaml.safe_load(f)

    pdf = ShortCV()

    # ============================================================ TITLE
    pdf.set_font("Helvetica", style="B", size=17)
    pdf.cell(0, 9, "CURRICULUM VITAE", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    # ============================================================ PERSONAL INFORMATION (compact)
    basics = data["basics"]
    work = data["work"][0]
    department = work["summary"].split(",")[0].strip()
    location = basics["location"]
    address_line = f"{location['address']}, {location['city']} {location['postalCode']}, Korea"

    photo_w = 25
    photo_h = 32
    page_w = pdf.w - pdf.l_margin - pdf.r_margin
    photo_x = pdf.l_margin + page_w - photo_w
    photo_y = pdf.get_y()
    text_col_w = page_w - photo_w - 5

    pdf.set_font("Helvetica", style="B", size=14)
    pdf.set_x(pdf.l_margin)
    pdf.cell(text_col_w, 6, basics["name"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Times", size=10)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        text_col_w,
        4.8,
        f"{work['position']}, {department}\n"
        f"{work['name']}\n"
        f"{address_line}\n"
        f"TEL: {basics['phone']}  |  E-MAIL: {basics['email']}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    if os.path.exists(PHOTO_PATH):
        pdf.image(PHOTO_PATH, x=photo_x, y=photo_y, w=photo_w, h=photo_h)

    pdf.set_y(max(pdf.get_y(), photo_y + photo_h) + 1)

    # ============================================================ EDUCATION (compact, single line)
    pdf.section_title("EDUCATION")
    # JSON order is already reverse-chronological (Ph.D., M.S., B.S.) — display as-is
    edu_entries = list(data["education"])
    for edu in edu_entries:
        deg = edu["studyType"]
        univ = edu["institution"].split("(")[0].strip()
        dept = f"Department of {edu['area']}"
        end = edu.get("endDate", "")
        year = end[:4] if end else ""
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, f"{deg}  ")
        pdf.set_font("Times", size=10)
        pdf.write(5, f"{univ}, {dept}  ({year})")
        pdf.ln(5)
        # Advisor for PhD only
        if deg == "Ph.D.":
            for course in edu.get("courses", []):
                if course.startswith("Advisor:"):
                    advisor_name = course[len("Advisor:"):].strip().replace("Prof. ", "")
                    pdf.set_font("Times", style="I", size=9)
                    pdf.set_x(pdf.l_margin + 6)
                    pdf.cell(0, 4, f"Advisor: {advisor_name}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    break

    # ============================================================ RESEARCH INTERESTS (categorized list)
    pdf.section_title("RESEARCH INTERESTS")
    for interest in data.get("interests", []):
        category = interest.get("name", "")
        keywords = interest.get("keywords", [])
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", size=10)
        pdf.cell(4, 5, "-")
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, category)
        if keywords:
            pdf.set_font("Times", size=10)
            pdf.write(5, ":  ")
            pdf.write(5, " / ".join(keywords))
        pdf.ln(5)

    # ============================================================ RESEARCH OUTPUTS (counts only)
    pubs = data["publications"]
    journal_pubs = [p for p in pubs if "Proceedings" not in p.get("publisher", "")]
    n_sci = len([p for p in journal_pubs if p.get("publisher", "") not in KOREAN_PUBLISHERS])
    n_kci = len(journal_pubs) - n_sci
    n_conf = len([p for p in pubs if "Proceedings" in p.get("publisher", "")])
    n_patents = len([c for c in data["certificates"] if c["issuer"] == "Korean Intellectual Property Office"])
    n_us_patents = len([c for c in data["certificates"] if c["issuer"] == "United States Patent and Trademark Office"])
    n_software = len([c for c in data["certificates"] if c["issuer"] == "Korea Copyright Commission"])
    n_transfers = len(data.get("volunteer", []))
    n_projects = len(data.get("projects", []))
    pi_lead_projects = [
        p for p in data.get("projects", [])
        if "(PI)" in p.get("summary", "") or "(Lead)" in p.get("summary", "")
    ]

    pdf.section_title("RESEARCH OUTPUTS")
    outputs = [
        ("SCI/SCIE Journal Papers", n_sci),
        ("KCI Journal Papers", n_kci),
        ("Conference Presentations", n_conf),
        ("Domestic Patents (registered)", n_patents),
        ("U.S. Patents (registered)", n_us_patents),
        ("Registered Software Programs", n_software),
        ("Technology Transfers to Industry", n_transfers),
        ("Research Projects (PI/Lead / Total)", f"{len(pi_lead_projects)} / {n_projects}"),
    ]
    col_w = (pdf.epw - 6) / 2
    rows = (len(outputs) + 1) // 2
    start_y = pdf.get_y()
    pdf.set_font("Times", size=10)
    for i, (label, value) in enumerate(outputs):
        col = i // rows
        row = i % rows
        x = pdf.l_margin + col * (col_w + 6)
        y = start_y + row * 5
        pdf.set_xy(x, y)
        pdf.set_font("Times", size=10)
        pdf.write(5, "- ")
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, f"{label}: ")
        pdf.set_font("Times", size=10)
        pdf.write(5, str(value))
    pdf.set_y(start_y + rows * 5 + 1)

    # ============================================================ SELECTED PUBLICATIONS (top 5)
    pdf.section_title("SELECTED PUBLICATIONS")
    selected = [
        ('W. Kim', ' et al., "Freezing phenomenon in PCHE for cryogenic LH2 vaporizer," ', 'Appl. Therm. Eng.', ' 273 (2025).'),
        ('W. Kim', ' and S.J. Kim, "Fundamental issues about pulsating heat pipes," ', 'J. Heat Transfer - ASME', ' 143 (2021).'),
        ('W. Kim', ' and S.J. Kim, "Flow behavior effect on pulsating heat pipes," ', 'Int. J. Heat Mass Transfer', ' 149 (2020).'),
        ('W. Kim', ' and S.J. Kim, "Reentrant cavities on pulsating heat pipe," ', 'Appl. Therm. Eng.', ' 133 (2018).'),
        ('J.S. Kim, W. Kim', ' et al., "Pool boiling of ammonia outside enhanced tubes," ', 'Appl. Therm. Eng.', ' 247 (2024).'),
    ]
    for i, (authors, title, journal, vol) in enumerate(selected, 1):
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", size=10)
        pdf.cell(7, 5, f"({i})")
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, authors)
        pdf.set_font("Times", size=10)
        pdf.write(5, title)
        pdf.set_font("Times", style="I", size=10)
        pdf.write(5, journal)
        pdf.set_font("Times", size=10)
        pdf.write(5, vol)
        pdf.ln(5)

    # ============================================================ RESEARCH PROJECTS (PI/Lead highlights)
    pdf.section_title("RESEARCH PROJECTS (PI / Lead)")
    pdf.set_font("Times", style="I", size=9)
    pdf.cell(0, 4, f"Showing {len(pi_lead_projects)} of {n_projects} total projects (PI/Lead role).", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(0.5)

    for i, proj in enumerate(pi_lead_projects, 1):
        name = proj.get("name", "")
        summary = proj.get("summary", "")
        m = re.search(r"\((PI|Lead)\)", summary)
        role = m.group(1) if m else ""
        period = _period(proj.get("startDate", ""), proj.get("endDate", ""))

        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", size=10)
        pdf.cell(7, 5, f"({i})")
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, name)
        pdf.set_font("Times", size=10)
        if role:
            pdf.write(5, f"  ({role})")
        if period:
            pdf.write(5, f"  [{period}]")
        pdf.ln(5)

    # ============================================================ PROFESSIONAL ACTIVITIES
    pdf.section_title("PROFESSIONAL ACTIVITIES")
    for i, aff in enumerate(data.get("affiliations", []), 1):
        org = aff.get("organization", "")
        position = aff.get("position", "")
        period = _aff_period(aff.get("startDate", ""), aff.get("endDate", ""))

        pdf.set_x(pdf.l_margin)
        pdf.set_font("Times", size=10)
        pdf.cell(7, 5, f"({i})")
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, position)
        pdf.set_font("Times", size=10)
        pdf.write(5, f", {org}")
        if period:
            pdf.write(5, f"  [{period}]")
        pdf.ln(5)

    pdf.output(OUTPUT_PATH)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"Pages: {pdf.page}")
    size = os.path.getsize(OUTPUT_PATH)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")


if __name__ == "__main__":
    build_short_cv()
