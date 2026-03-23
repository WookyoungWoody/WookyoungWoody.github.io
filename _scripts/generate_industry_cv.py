#!/usr/bin/env python3
"""Generate industry-focused CV PDF using fpdf2."""

import warnings
warnings.filterwarnings("ignore")

from fpdf import FPDF

OUTPUT = "/Users/wookyoungkim/WookyoungWoody.github.io/assets/pdf/cv_industry.pdf"

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


def build_pdf():
    pdf = IndustryCVPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(18, 12, 18)
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    cw = pdf.w - pdf.l_margin - pdf.r_margin  # ~174mm

    # ------------------------------------------------------------------ HEADER
    photo_path = "/Users/wookyoungkim/WookyoungWoody.github.io/assets/img/prof_pic.jpg"
    photo_size = 22
    photo_x = pdf.w - pdf.r_margin - photo_size
    photo_y = pdf.t_margin

    text_w = cw - photo_size - 4
    pdf.set_font("Helvetica", "B", 15)
    pdf.set_text_color(*BLACK)
    pdf.cell(text_w, 7, "WOOKYOUNG KIM, Ph.D.", ln=True)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*ACCENT)
    pdf.cell(text_w, 5, "Senior Researcher  |  Thermal-Fluid Engineering", ln=True)

    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(*MED_GRAY)
    contact = (
        "wookyoung@kimm.re.kr  |  github.com/WookyoungWoody  |  "
        "linkedin.com/in/wookyoungwoody  |  Daejeon, Korea"
    )
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
        "Track record: 17+ journal papers, 17 patents, 8 registered software programs, 5 technology transfers to industry."
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

    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 4.5, "Senior Researcher  |  KIMM (Korea Institute of Machinery and Materials)  |  Mar 2021 - Present", ln=True)
    pdf.set_font("Helvetica", "I", 7.5)
    pdf.set_text_color(*MED_GRAY)
    pdf.cell(0, 3.5, "Korea's national research institute for machinery and materials engineering", ln=True)
    pdf.ln(0.5)

    bullets_exp = [
        "PI: Jet-enhanced immersion cooling for next-gen AI data center servers",
        "PI: Cross-platform thermophysical property app (iOS/Android, React Native + FastAPI)",
        "Lead: PCHE design for liquid hydrogen vaporizers (-220\u00b0C, 100 MPa class)",
        "Lead: Immersion cooling waste heat utilization and thermal management systems",
        "Delivered 5 technology transfers to industry partners",
        "Developed 8 registered engineering software programs (Korea Copyright Commission)",
    ]
    for b in bullets_exp:
        pdf.bullet(b, size=8)

    # --------------------------------------------------------- EDUCATION
    pdf.section_header("EDUCATION")

    edu = [
        ("Ph.D.", "Mechanical Engineering", "KAIST", "2017 - 2021"),
        ("M.S.", "Mechanical Engineering", "KAIST", "2015 - 2017"),
        ("B.S.", "Mechanical Engineering", "KAIST", "2011 - 2015"),
    ]
    for deg, field, inst, yr in edu:
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*BLACK)
        pdf.cell(12, 4.5, deg, ln=False)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(65, 4.5, field, ln=False)
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*ACCENT)
        pdf.cell(50, 4.5, inst, ln=False)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*MED_GRAY)
        pdf.cell(0, 4.5, yr, ln=True)

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
        ("17+", "Journal Papers (10 SCI + 7 KCI)"),
        ("17", "Domestic Patents"),
        ("8", "Registered Software Programs"),
        ("5", "Technology Transfers to Industry"),
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
        ("W. Kim", ' et al., "Freezing Phenomenon in PCHE for Cryogenic LH2 Vaporizer," Int. J. Heat Mass Transfer (2025)'),
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
                        "2-phase flow & heat transfer measurement, High-pressure testing (2000 bar), Flow visualization"),
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
