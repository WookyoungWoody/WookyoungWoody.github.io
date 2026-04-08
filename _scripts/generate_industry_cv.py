#!/usr/bin/env python3
"""Generate industry-focused CV PDF using fpdf2."""

import json
import os
import warnings

warnings.filterwarnings("ignore")

from fpdf import FPDF

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.join(_SCRIPT_DIR, "..")

OUTPUT = os.path.join(_REPO_ROOT, "assets", "pdf", "cv_industry.pdf")

# Colors
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
MED_GRAY = (100, 100, 100)
LIGHTER_GRAY = (245, 245, 245)
ACCENT = (30, 80, 150)  # deep blue accent
ACHIEVEMENT_BG = (240, 245, 255)  # light blue tint


class IndustryCVPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-10)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*MED_GRAY)
        self.cell(0, 4, f"Page {self.page_no()}", align="C")

    def section_header(self, title, spacing_before=2.5):
        """Draw section header with accent line."""
        self.ln(spacing_before)
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(*ACCENT)
        self.cell(0, 5, title, ln=False)
        y = self.get_y() + 4
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.4)
        self.line(self.l_margin, y + 1, self.w - self.r_margin, y + 1)
        self.ln(6)
        self.set_text_color(*BLACK)
        self.set_draw_color(*BLACK)

    def bullet(self, text, indent=4, size=8.5):
        """Render a bullet point."""
        self.set_font("Helvetica", "", size)
        self.set_text_color(*DARK_GRAY)
        self.set_x(self.l_margin + indent)
        self.cell(4, 4.5, chr(149), ln=False)
        self.set_x(self.l_margin + indent + 4)
        self.multi_cell(0, 4.5, text)


def _load_data():
    resume_path = os.path.join(_REPO_ROOT, "assets", "json", "resume.json")
    with open(resume_path, "r") as f:
        return json.load(f)


def _compute_counts(data):
    all_pubs = data.get("publications", [])
    journal_papers = [p for p in all_pubs if "Proceedings" not in p.get("publisher", "")]
    patents = [c for c in data["certificates"] if c["issuer"] == "Korean Intellectual Property Office"]
    software = [c for c in data["certificates"] if c["issuer"] == "Korea Copyright Commission"]
    transfers = data.get("volunteer", [])
    return journal_papers, patents, software, transfers


def _year(date_str):
    """Extract year from a date string like '2017-03-01'."""
    return date_str[:4] if date_str else ""


def build_pdf():
    data = _load_data()
    journal_papers, patents, software, transfers = _compute_counts(data)

    # Counts for summary / achievements
    n_journal = len(journal_papers)
    n_patents = len(patents)
    n_software = len(software)
    n_transfers = len(transfers)

    # SCI vs KCI breakdown (SCI = international journals, KCI = Korean journals)
    # Approximate: publishers with Korean-language names or known Korean journals = KCI
    korean_publishers = {
        "Journal of Hydrogen and New Energy",
        "Korean Journal of Air-Conditioning and Refrigeration Engineering",
        "Transactions of the Korean Society of Mechanical Engineers B",
        "Transactions of the Korean Hydrogen and New Energy Society",
    }
    n_sci = len([p for p in journal_papers if p.get("publisher", "") not in korean_publishers])
    n_kci = n_journal - n_sci

    pdf = IndustryCVPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(18, 12, 18)
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    cw = pdf.w - pdf.l_margin - pdf.r_margin  # ~174mm

    # ------------------------------------------------------------------ HEADER
    basics = data["basics"]
    name = basics["name"].upper()
    label = basics.get("label", "")
    email = basics.get("email", "")
    city = basics.get("location", {}).get("city", "")
    country_code = basics.get("location", {}).get("countryCode", "")
    location_str = f"{city}, Korea" if city else ""

    github_username = ""
    for profile in basics.get("profiles", []):
        if profile.get("network", "").lower() == "github":
            github_username = profile.get("username", "")

    photo_path = os.path.join(_REPO_ROOT, "assets", "img", "prof_pic.jpg")
    photo_size = 22
    photo_x = pdf.w - pdf.r_margin - photo_size
    photo_y = pdf.t_margin

    text_w = cw - photo_size - 4
    pdf.set_font("Helvetica", "B", 15)
    pdf.set_text_color(*BLACK)
    pdf.cell(text_w, 7, f"{name}, Ph.D.", ln=True)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*ACCENT)
    pdf.cell(text_w, 5, f"{label}  |  Thermal-Fluid Engineering", ln=True)

    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(*MED_GRAY)
    contact_parts = [email]
    if github_username:
        contact_parts.append(f"github.com/{github_username}")
    contact_parts.append("linkedin.com/in/wookyoungwoody")
    if location_str:
        contact_parts.append(location_str)
    contact = "  |  ".join(contact_parts)
    pdf.cell(text_w, 4.5, contact, ln=True)

    pdf.image(photo_path, x=photo_x, y=photo_y, w=photo_size, h=photo_size)

    # Horizontal rule
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.6)
    rule_y = max(pdf.get_y(), photo_y + photo_size) + 1
    pdf.line(pdf.l_margin, rule_y, pdf.w - pdf.r_margin, rule_y)
    pdf.set_y(rule_y + 1)

    # --------------------------------------------------------- PROFESSIONAL SUMMARY
    pdf.section_header("PROFESSIONAL SUMMARY", spacing_before=1)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(*DARK_GRAY)
    summary = (
        "Thermal-fluid engineer with 5+ years of R&D experience at Korea's national research institute (KIMM). "
        "Specialized in thermal management solutions for AI data centers, hydrogen energy systems, and heat pump technology. "
        "Extensive hands-on experience in thermal system design, experimental facility construction, performance testing, and data analysis. "
        "Spearheading development of multiple engineering software tools (Python/FastAPI/React Native). "
        f"Track record: {n_journal}+ journal papers, {n_patents} patents, {n_software} registered software programs, {n_transfers} technology transfers to industry."
    )
    pdf.multi_cell(0, 4.5, summary)

    # --------------------------------------------------------- CORE COMPETENCIES
    # Focused on DOMAIN expertise (no tool names — those go in Technical Skills)
    pdf.section_header("CORE COMPETENCIES")

    box_y = pdf.get_y()
    box_h = 25
    pdf.set_fill_color(*LIGHTER_GRAY)
    pdf.rect(pdf.l_margin, box_y, cw, box_h, style="F")
    pdf.set_y(box_y + 2)

    cols = [
        ("Thermal Management", [
            "Data center cooling",
            "Immersion / DLC / Jet cooling",
            "Electronics thermal design",
        ]),
        ("Energy Systems", [
            "Heat pump (vapor./ads.)",
            "Hydrogen vaporizer (PCHE)",
            "Low-GWP refrigerant R&D",
        ]),
        ("System Design", [
            "Heat exchanger design",
            "Thermal loop construction",
            "High-pressure cryogenic sys.",
        ]),
        ("Testing & Analysis", [
            "Performance testing",
            "2-phase flow visualization",
            "VLE measurement & EOS",
        ]),
    ]
    col_w = cw / 4

    for i, (title, items) in enumerate(cols):
        x = pdf.l_margin + i * col_w
        pdf.set_xy(x, box_y + 2)
        pdf.set_font("Helvetica", "B", 7.5)
        pdf.set_text_color(*ACCENT)
        pdf.cell(col_w, 4.5, title, ln=False)
        for j, item in enumerate(items):
            pdf.set_xy(x, box_y + 7.5 + j * 5)
            pdf.set_font("Helvetica", "", 7.5)
            pdf.set_text_color(*DARK_GRAY)
            pdf.cell(col_w, 4.5, item, ln=False)

    pdf.set_y(box_y + box_h + 1)

    # --------------------------------------------------------- EXPERIENCE
    pdf.section_header("EXPERIENCE")

    work = data["work"][0]
    position = work.get("position", "")
    company = work.get("name", "")
    start_year = _year(work.get("startDate", ""))
    end_date = work.get("endDate", "")
    end_str = _year(end_date) if end_date else "Present"
    date_range = f"Mar {start_year} - {end_str}"

    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 4.5, f"{position}  |  {company}  |  {date_range}", ln=True)
    pdf.set_font("Helvetica", "I", 7.5)
    pdf.set_text_color(*MED_GRAY)
    pdf.cell(0, 3.5, "Korea's national research institute for machinery and materials engineering", ln=True)
    pdf.ln(0.5)

    # Build experience bullets from highlights, replacing the summary highlight with computed bullets
    summary_highlight_keyword = "journal papers"
    bullets_exp = []
    for h in work.get("highlights", []):
        if summary_highlight_keyword in h.lower():
            # Replace with computed count bullets
            bullets_exp.append(f"Delivered {n_transfers} technology transfers to industry partners")
            bullets_exp.append(f"Developed {n_software} registered engineering software programs (Korea Copyright Commission)")
        else:
            bullets_exp.append(h)

    for b in bullets_exp:
        pdf.bullet(b, size=8)

    # --------------------------------------------------------- EDUCATION
    pdf.section_header("EDUCATION")

    for edu_entry in data["education"]:
        study_type = edu_entry.get("studyType", "")
        area = edu_entry.get("area", "")
        institution = edu_entry.get("institution", "")
        # Shorten "KAIST (Korea Advanced Institute...)" to "KAIST"
        inst_display = institution.split("(")[0].strip()
        start_yr = _year(edu_entry.get("startDate", ""))
        end_yr = _year(edu_entry.get("endDate", ""))
        yr_range = f"{start_yr} - {end_yr}" if start_yr and end_yr else start_yr or end_yr

        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*BLACK)
        pdf.cell(12, 4.5, study_type, ln=False)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(65, 4.5, area, ln=False)
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*ACCENT)
        pdf.cell(50, 4.5, inst_display, ln=False)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*MED_GRAY)
        pdf.cell(0, 4.5, yr_range, ln=True)

        courses = edu_entry.get("courses", [])
        dissertation_line = next((c for c in courses if c.startswith("Dissertation:")), None)
        advisor_line = next((c for c in courses if c.startswith("Advisor:")), None)

        if dissertation_line:
            pdf.set_x(pdf.l_margin + 12)
            pdf.set_font("Helvetica", "I", 7.5)
            pdf.set_text_color(*MED_GRAY)
            pdf.multi_cell(0, 4, dissertation_line)
        if advisor_line:
            pdf.set_x(pdf.l_margin + 12)
            pdf.set_font("Helvetica", "I", 7.5)
            pdf.set_text_color(*MED_GRAY)
            pdf.cell(0, 4, advisor_line, ln=True)

    # --------------------------------------------------------- KEY ACHIEVEMENTS
    # 2x2 grid inside a tinted box for visual emphasis
    pdf.section_header("KEY ACHIEVEMENTS")

    ach_y = pdf.get_y()
    ach_h = 14
    pdf.set_fill_color(*ACHIEVEMENT_BG)
    pdf.rect(pdf.l_margin, ach_y, cw, ach_h, style="F")
    # Draw thin border
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.2)
    pdf.rect(pdf.l_margin, ach_y, cw, ach_h, style="D")

    achievements = [
        (f"{n_journal}+", f"Journal Papers ({n_sci} SCI + {n_kci} KCI)"),
        (str(n_patents), "Domestic Patents"),
        (str(n_software), "Registered Software Programs"),
        (str(n_transfers), "Technology Transfers to Industry"),
    ]
    ach_col_w = cw / 4
    for i, (num, desc) in enumerate(achievements):
        x = pdf.l_margin + i * ach_col_w
        # Big number
        pdf.set_xy(x, ach_y + 1.5)
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(*ACCENT)
        pdf.cell(ach_col_w, 5, num, align="C", ln=False)
        # Description
        pdf.set_xy(x, ach_y + 7)
        pdf.set_font("Helvetica", "", 6.5)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(ach_col_w, 4, desc, align="C", ln=False)

    pdf.set_y(ach_y + ach_h + 1)

    # --------------------------------------------------------- SELECTED PUBLICATIONS
    pdf.section_header("SELECTED PUBLICATIONS")

    pubs = [
        ("W. Kim", ' et al., "Freezing Phenomenon in PCHE for Cryogenic LH2 Vaporizer," Appl. Therm. Eng. 273 (2025)'),
        ("W. Kim", ' and S.J. Kim, "Fundamental issues about pulsating heat pipes," J. Heat Transfer - ASME 143 (2021)'),
        ("W. Kim", ' and S.J. Kim, "Flow behavior effect on pulsating heat pipes," Int. J. Heat Mass Transfer 149 (2020)'),
        ("W. Kim", ' and S.J. Kim, "Reentrant cavities on pulsating heat pipe," Appl. Therm. Eng. 133 (2018)'),
        ("J.S. Kim, W. Kim", ' et al., "Pool boiling of ammonia outside enhanced tubes," Appl. Therm. Eng. 247 (2024)'),
    ]

    for idx, (bold_part, rest) in enumerate(pubs, 1):
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*MED_GRAY)
        num_w = pdf.get_string_width(f"({idx}) ") + 1
        pdf.cell(num_w, 4.5, f"({idx})", ln=False)
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(*BLACK)
        bw = pdf.get_string_width(bold_part)
        pdf.cell(bw + 1, 4.5, bold_part, ln=False)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*DARK_GRAY)
        pdf.multi_cell(0, 4.5, rest)

    # --------------------------------------------------------- TECHNICAL SKILLS
    # No overlap with Core Competencies — this section lists specific tools & methods
    pdf.section_header("TECHNICAL SKILLS")

    skills = [
        ("Software:", "Python, JavaScript/TypeScript, C/C++, FastAPI, React, React Native, Git, Docker, Linux"),
        ("CAD / CAE:", "INVENTOR, SOLIDWORKS, COMSOL Multiphysics, ANSYS FLUENT, CoolProp, REFPROP"),
        ("AI / ML:", "PyTorch, JAX, PINN"),
        ("Experiment:", "Thermal loop design & construction (1-phase / 2-phase), Low GWP Refrigerant system, "
                        "2-phase flow & heat transfer measurement, High-pressure testing (100 MPa), Flow visualization"),
    ]

    for label, val in skills:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "B", 7.5)
        pdf.set_text_color(*BLACK)
        lw = pdf.get_string_width(label) + 2
        pdf.cell(lw, 4.5, label, ln=False)
        pdf.set_font("Helvetica", "", 7.5)
        pdf.set_text_color(*DARK_GRAY)
        pdf.multi_cell(0, 4.5, val)

    pdf.output(OUTPUT)
    print(f"Generated: {OUTPUT}")
    print(f"Pages: {pdf.page}")


if __name__ == "__main__":
    build_pdf()
