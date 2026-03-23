#!/usr/bin/env python3
"""Generate academic CV PDF for Wookyoung Kim."""

from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os

PHOTO_PATH = "/Users/wookyoungkim/WookyoungWoody.github.io/assets/img/prof_pic.jpg"
OUTPUT_PATH = "/Users/wookyoungkim/WookyoungWoody.github.io/assets/pdf/cv_wookyoung_kim.pdf"

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)


class CV(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(left=25, top=20, right=25)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

    def header(self):
        pass  # no automatic header

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", size=9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, str(self.page_no()), align="C")
        self.set_text_color(0, 0, 0)

    # ------------------------------------------------------------------ helpers
    def section_title(self, title):
        """Print a section header (ALL CAPS, bold, 12pt, underlined)."""
        self.ln(4)
        self.set_font("Helvetica", style="B", size=12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # underline
        x1 = self.get_x()
        y = self.get_y()
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.4)
        self.line(x1, y, x1 + self.epw, y)
        self.ln(2)

    def body_text(self, txt, bold_tokens=None, italic=False, indent=0, size=10):
        """Print a line of body text with optional bold tokens."""
        if bold_tokens is None:
            bold_tokens = []
        if not bold_tokens and not italic:
            self.set_font("Times", style="I" if italic else "", size=size)
            self.set_x(self.l_margin + indent)
            self.multi_cell(0, 5, txt, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            return
        # split text into tokens and print with mixed styles
        self.set_x(self.l_margin + indent)
        remaining = txt
        while remaining:
            matched = False
            for token in bold_tokens:
                idx = remaining.find(token)
                if idx == 0:
                    self.set_font("Times", style="B", size=size)
                    self.write(5, token)
                    remaining = remaining[len(token):]
                    matched = True
                    break
                elif idx > 0:
                    before = remaining[:idx]
                    self.set_font("Times", style="I" if italic else "", size=size)
                    self.write(5, before)
                    self.set_font("Times", style="B", size=size)
                    self.write(5, token)
                    remaining = remaining[idx + len(token):]
                    matched = True
                    break
            if not matched:
                self.set_font("Times", style="I" if italic else "", size=size)
                self.write(5, remaining)
                remaining = ""
        self.ln()

    def kv_line(self, key, value, key_width=40):
        """Print a key: value line."""
        self.set_font("Times", style="B", size=10)
        self.cell(key_width, 5, key)
        self.set_font("Times", size=10)
        self.multi_cell(0, 5, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def kv_continuation(self, value, key_width=40):
        """Print continuation line for multi-line value."""
        self.set_font("Times", size=10)
        self.set_x(self.l_margin + key_width)
        self.multi_cell(0, 5, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def build_cv():
    pdf = CV()

    # ============================================================ TITLE
    pdf.set_font("Helvetica", style="B", size=20)
    pdf.cell(0, 12, "CURRICULUM VITAE", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    # ============================================================ PERSONAL INFORMATION + PHOTO
    pdf.section_title("PERSONAL INFORMATION")

    # Save position before personal info text
    text_start_y = pdf.get_y()
    text_start_x = pdf.l_margin
    photo_w = 30
    photo_h = 40
    page_w = pdf.w - pdf.l_margin - pdf.r_margin
    photo_x = pdf.l_margin + page_w - photo_w
    photo_y = text_start_y

    # Print personal info in left column (reserve space for photo)
    text_col_w = page_w - photo_w - 5

    def kv_narrow(key, value, key_w=38):
        pdf.set_font("Times", style="B", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.cell(key_w, 5, key)
        pdf.set_font("Times", size=10)
        pdf.multi_cell(text_col_w - key_w, 5, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    kv_narrow("NAME:", "Wookyoung Kim")
    kv_narrow("DATE OF BIRTH:", "September 27, 1993")
    kv_narrow("NATIONALITY:", "Korea")
    kv_narrow("AFFILIATION:", "Korea Institute of Machinery and Materials (KIMM),\nHeat Pump Research Center")
    kv_narrow("POSITION:", "Senior Researcher")
    kv_narrow("CONTACT:", "Heat Pump Research Center")
    pdf.set_font("Times", size=10)
    pdf.set_x(pdf.l_margin + 38)
    pdf.multi_cell(text_col_w - 38, 5,
                   "Korea Institute of Machinery and Materials (KIMM)\n"
                   "156 Gajeongbuk-ro, Yuseong-gu, Daejeon 34103, Korea\n"
                   "(TEL) +82-42-868-7619\n"
                   "(E-MAIL) wookyoung@kimm.re.kr",
                   new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Insert photo
    if os.path.exists(PHOTO_PATH):
        pdf.image(PHOTO_PATH, x=photo_x, y=photo_y, w=photo_w, h=photo_h)

    pdf.ln(2)

    # ============================================================ EDUCATION
    pdf.section_title("EDUCATION")

    # Table header
    col_w = [15, 32, 80, 40]
    pdf.set_font("Helvetica", style="B", size=10)
    pdf.cell(col_w[0], 6, "Degree")
    pdf.cell(col_w[1], 6, "University")
    pdf.cell(col_w[2], 6, "Department")
    pdf.cell(col_w[3], 6, "Date")
    pdf.ln()
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin + sum(col_w), pdf.get_y())
    pdf.ln(1)

    rows = [
        ("B.S.", "KAIST", "Department of Mechanical Engineering", "February, 2015", None, None),
        ("M.S.", "KAIST", "Department of Mechanical Engineering", "February, 2017",
         "\"Effect of artificial cavities on the thermal performance of pulsating heat pipes\"",
         "Sung Jin Kim"),
        ("Ph.D.", "KAIST", "Department of Mechanical Engineering", "February, 2021",
         "\"Study on a Thermal Network-based Model for Predicting the Thermal Resistance of Pulsating Heat Pipes\"",
         "Sung Jin Kim"),
    ]

    thesis_labels = {"M.S.": "Thesis:", "Ph.D.": "Dissertation:"}

    for deg, univ, dept, date, thesis, advisor in rows:
        pdf.set_font("Times", size=10)
        pdf.cell(col_w[0], 5, deg)
        pdf.cell(col_w[1], 5, univ)
        pdf.cell(col_w[2], 5, dept)
        pdf.cell(col_w[3], 5, date)
        pdf.ln()
        if thesis:
            label = thesis_labels.get(deg, "Thesis:")
            indent = col_w[0] + 4
            pdf.set_x(pdf.l_margin + indent)
            pdf.set_font("Times", style="B", size=10)
            pdf.write(5, label + " ")
            pdf.set_font("Times", style="I", size=10)
            pdf.write(5, thesis)
            pdf.ln()
            pdf.set_x(pdf.l_margin + indent)
            pdf.set_font("Times", style="B", size=10)
            pdf.write(5, "Advisor: ")
            pdf.set_font("Times", size=10)
            pdf.write(5, advisor)
            pdf.ln(6)

    # ============================================================ RESEARCH INTERESTS
    pdf.section_title("RESEARCH INTERESTS")
    interests = [
        "(1) Data center cooling (immersion cooling, direct liquid cooling, jet-impingement cooling)",
        "(2) High-heat-flux electronics cooling (CPU/GPU cold plate design)",
        "(3) Heat exchangers (PCHE for cryogenic liquid hydrogen, compact heat exchanger design)",
        "(4) Heat pump systems (chemisorption/adsorption heat pumps, high-temperature heat pumps)",
        "(5) Low GWP refrigerant systems (next-gen eco-friendly refrigerants, VLE measurement)",
        "(6) Two-phase heat transfer (boiling, evaporation, pulsating heat pipes, vapor chambers)",
        "(7) Cryogenic heat transfer (liquid hydrogen vaporizer, supercritical fluid heat transfer)",
    ]
    for line in interests:
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    # ============================================================ PUBLICATIONS
    pdf.section_title("PUBLICATIONS")

    def pub_subsection(title):
        pdf.set_font("Helvetica", style="B", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1)

    def pub_entry(number, text, bold_tokens=None):
        if bold_tokens is None:
            bold_tokens = ["W. Kim"]
        prefix = f"({number}) "
        indent_mm = 8
        # print prefix
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.cell(indent_mm, 5, prefix)
        # print rest with bold tokens
        pdf.set_x(pdf.l_margin + indent_mm)
        # Parse and write mixed style
        remaining = text
        while remaining:
            matched = False
            for token in bold_tokens:
                idx = remaining.find(token)
                if idx == 0:
                    pdf.set_font("Times", style="B", size=10)
                    pdf.write(5, token)
                    remaining = remaining[len(token):]
                    matched = True
                    break
                elif idx > 0:
                    before = remaining[:idx]
                    pdf.set_font("Times", size=10)
                    pdf.write(5, before)
                    pdf.set_font("Times", style="B", size=10)
                    pdf.write(5, token)
                    remaining = remaining[idx + len(token):]
                    matched = True
                    break
            if not matched:
                pdf.set_font("Times", size=10)
                pdf.write(5, remaining)
                remaining = ""
        pdf.ln()
        pdf.ln(1)

    # SCI/SCIE
    pub_subsection("SCI/SCIE Journal Papers")
    sci_papers = [
        ('W. Kim', ' et al., "Experimental and Theoretical Investigation of Freezing Phenomenon in Printed Circuit Heat Exchanger for Cryogenic Liquid Hydrogen Vaporizer", ', 'International Journal of Heat and Mass Transfer', ' (2025).'),
        ('J. Kim, C.G. Kim, H.S. Kim, W. Kim', ', D.H. Kim, "Characterization of liquid behavior in distributor of falling-film evaporator", ', 'Physics of Fluids', ' 35(6), 067124 (2023).'),
        ('W. Kim', ' et al., "Experimental studies on the VLE of R-32/R-125 and verification of experimental setup" (2024).'),
        ('H.S. Kim, J.H. Kim, J.S. Kim, W. Kim', ', Y. Kim, "A numerical study on the performance of chemisorption heat pump according to various design conditions", ', 'Applied Thermal Engineering', ' (2024).'),
        ('J.S. Kim, W. Kim', ', H.S. Kim, Y. Kim, "Pool boiling heat transfer of ammonia outside enhanced tubes with various fin structures", ', 'Applied Thermal Engineering', ' 247, 122986 (2024).'),
        ('H.S. Kim, J.H. Kim, J.S. Kim, W. Kim', ', Y. Kim, "Experimental study of a chemisorption heat pump under different operation conditions", ', 'Applied Thermal Engineering', ' 240, 122274 (2024).'),
        ('J.S. Kim, W. Kim', ', H.S. Kim, Y. Kim, "Pool boiling heat transfer of ammonia outside a single tube with fin structures: Hysteresis phenomena and boiling enhancement", ', 'International Communications in Heat and Mass Transfer', ' 149, 107157 (2023).'),
        ('W. Kim', ' and S.J. Kim, "Fundamental issues and technical problems about pulsating heat pipes", ', 'Journal of Heat Transfer - Transactions of the ASME', ' 143, 4051465 (2021).'),
        ('W. Kim', ' and S.J. Kim, "Effect of a flow behavior on the thermal performance of closed-loop and closed-end pulsating heat pipes", ', 'International Journal of Heat and Mass Transfer', ' 149, 119251 (2020).'),
        ('W. Kim', ' and S.J. Kim, "Effect of reentrant cavities on the thermal performance of a pulsating heat pipe", ', 'Applied Thermal Engineering', ' 133, 61-69 (2018).'),
    ]

    for i, parts in enumerate(sci_papers, 1):
        prefix = f"({i}) "
        indent_mm = 8
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.cell(indent_mm, 5, prefix)
        pdf.set_x(pdf.l_margin + indent_mm)

        for j, part in enumerate(parts):
            # Italic for journal name (even index 2 in 4-tuple, index 2 in 3-tuple)
            is_journal = (len(parts) == 4 and j == 2) or (len(parts) == 3 and j == 1 and False)
            # Bold for W. Kim occurrences in author field
            if "W. Kim" in part:
                # Mixed bold
                remaining = part
                while remaining:
                    idx = remaining.find("W. Kim")
                    if idx < 0:
                        pdf.set_font("Times", style="I" if is_journal else "", size=10)
                        pdf.write(5, remaining)
                        remaining = ""
                    elif idx == 0:
                        pdf.set_font("Times", style="B", size=10)
                        pdf.write(5, "W. Kim")
                        remaining = remaining[6:]
                    else:
                        pdf.set_font("Times", style="I" if is_journal else "", size=10)
                        pdf.write(5, remaining[:idx])
                        pdf.set_font("Times", style="B", size=10)
                        pdf.write(5, "W. Kim")
                        remaining = remaining[idx + 6:]
            elif is_journal:
                pdf.set_font("Times", style="I", size=10)
                pdf.write(5, part)
            else:
                pdf.set_font("Times", size=10)
                pdf.write(5, part)
        pdf.ln()
        pdf.ln(1)

    # KCI
    pub_subsection("KCI Journal Papers")
    kci_papers = [
        ('W. Kim', ', B. Kim, S. Sohn, K.H. Lee, J. Kim, "Experimental Investigation on the Freezing Condition of PCHE for Cryogenic Liquid Hydrogen Vaporizer", ', 'Journal of Hydrogen and New Energy', ' 35(2), 240-248 (2024).'),
        ('W. Kim', ', H.S. Kim, J. Kim, D.H. Kim, "An Experimental Study on The Thermal Performance Measurement and Flow Visualization of Falling Film Evaporator Using R-1233ZD(E) Refrigerant", ', 'Korean Journal of Air-Conditioning and Refrigeration Engineering', ' 36(1), 9-17 (2024).'),
        ('S. Sohn, W. Kim', ', "A Study on Anti-Icing Design by Conjugate Heat Transfer Analysis in a Lab-Scale PCHE for Supply of Cryogenic High Pressure Liquid Hydrogen", ', 'Transactions of the Korean Hydrogen and New Energy Society', ' 33(5), 541-549 (2022).'),
        ('D.H. Kim, H.S. Kim, J. Kim, W. Kim', ', "An Experimental Study on the Performance Characteristics of a Falling Film Evaporator for R-1234ze(E) Refrigerant", ', 'Korean Journal of Air-Conditioning and Refrigeration Engineering', ' 35(7), 363-370 (2023).'),
        ('J.S. Kim, S.A. Kim, D.H. Shin, W. Kim', ', S. Moon, Y. Chung, S. Sohn, "Comparative Study of Air Cooling and Immersion Cooling for the Thermal Management of a Cylindrical Battery Pack", ', 'Transactions of the KSME B', ' 47(10), 543-550 (2023).'),
        ('H.S. Kim, W. Kim', ', K.H. Lee, D.H. Kim, "Numerical Study on the Performance of Hybrid Falling Film Evaporator", ', 'Korean Journal of Air-Conditioning and Refrigeration Engineering', ' 34(8), 371-379 (2022).'),
        ('K.H. Lee, D.H. Kim, W. Kim', ', J.S. Kim, Y. Kim, J.W. Yoo, "Selection of the Equation of State for Thermodynamic Properties in the Low GWP Mixture Refrigerants", ', 'Transactions of the KSME B', ' 46(10), 563-571 (2022).'),
    ]

    for i, parts in enumerate(kci_papers, 1):
        prefix = f"({i}) "
        indent_mm = 8
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.cell(indent_mm, 5, prefix)
        pdf.set_x(pdf.l_margin + indent_mm)

        for j, part in enumerate(parts):
            is_journal = (len(parts) == 4 and j == 2)
            if "W. Kim" in part:
                remaining = part
                while remaining:
                    idx = remaining.find("W. Kim")
                    if idx < 0:
                        pdf.set_font("Times", style="I" if is_journal else "", size=10)
                        pdf.write(5, remaining)
                        remaining = ""
                    elif idx == 0:
                        pdf.set_font("Times", style="B", size=10)
                        pdf.write(5, "W. Kim")
                        remaining = remaining[6:]
                    else:
                        pdf.set_font("Times", style="I" if is_journal else "", size=10)
                        pdf.write(5, remaining[:idx])
                        pdf.set_font("Times", style="B", size=10)
                        pdf.write(5, "W. Kim")
                        remaining = remaining[idx + 6:]
            elif is_journal:
                pdf.set_font("Times", style="I", size=10)
                pdf.write(5, part)
            else:
                pdf.set_font("Times", size=10)
                pdf.write(5, part)
        pdf.ln()
        pdf.ln(1)

    # Conference proceedings
    pub_subsection("International Conference Proceedings")
    conf_papers = [
        "2024, \"Experimental and theoretical investigation on avoiding freezing phenomena of PCHE for cryogenic liquid hydrogen vaporizer\", 29th ICEC",
        "2024, \"Understanding the thermal characteristics of falling film evaporation of R-1233ZD(E) refrigerant using flow visualization and heat transfer measurement\", 11th ACRA",
        "2023, \"Experimental investigation on the flow and thermal characteristics of falling film evaporator using R-1233ZD(E) refrigerant\", 11th ICBCHT",
        "2019, \"Comparison of thermal performance between CEPHP and CLPHP\", 4th TFEC",
        "2018, \"Experimental investigation on the thermal performance of double-condenser pulsating heat pipes\", 10th ICBCHT",
        "2017, \"Experimental investigation of artificial cavities on the thermal performance of a pulsating heat pipe\", InterPACK 2017",
    ]
    for i, text in enumerate(conf_papers, 1):
        prefix = f"({i}) "
        indent_mm = 8
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        pdf.cell(indent_mm, 5, prefix)
        pdf.set_x(pdf.l_margin + indent_mm)
        pdf.multi_cell(0, 5, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1)

    # ============================================================ PATENTS
    pdf.section_title("PATENTS")
    pdf.set_font("Times", style="I", size=10)
    pdf.cell(0, 5, "Domestic Patents (17)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    patents = [
        ("Heat exchanger with anti-freezing capability (1)", "2023.03.27"),
        ("Heat exchanger with anti-freezing capability (2)", "2023.03.27"),
        ("Modular fin-tube reactor", "2024.11.04"),
        ("Fin-tube type reactor", "2024.11.04"),
        ("Tray structure for heat exchanger", "2022.10.13"),
        ("Oil recovery system for refrigeration systems (1)", "2022.10.13"),
        ("Oil recovery system for refrigeration systems (2)", "2022.10.13"),
        ("Micro-channel reactor", "2023.04.19"),
        ("Immersion cooling device", "2024.10.25"),
        ("Geothermal heat supply device and heating system", "2023.10.17"),
        ("Heat exchanger thermal performance testing apparatus", "2023.06.16"),
        ("Ternary refrigerant composition and heat pump system", "2022.10.24"),
        ("Display device", "2023.10.20"),
        ("Duct assembly and combustor", "2022.03.30"),
        ("Immersion cooling HVAC system and method", "2022.12.22"),
        ("Heat pipe integrated reactor for adsorption heat pump", "2022.04.06"),
        ("Adsorption heat pump evaporator and system", "2023.03.31"),
    ]
    for i, (name, date) in enumerate(patents, 1):
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        prefix = f"({i}) "
        indent_mm = 8
        pdf.cell(indent_mm, 5, prefix)
        pdf.set_x(pdf.l_margin + indent_mm)
        pdf.write(5, name)
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, f"  [{date}]")
        pdf.ln()
        pdf.ln(1)

    # ============================================================ SOFTWARE REGISTRATIONS
    pdf.section_title("SOFTWARE REGISTRATIONS")
    software = [
        ("PCHE thickness design program", "C-2024-052179", "2024.12.11"),
        ("High-temperature heat pump cycle design program", "C-2024-038691", "2024.10.22"),
        ("Heat exchanger HTC uncertainty analysis program", "C-2023-059071", "2023.12.12"),
        ("Lab-scale heat exchanger analysis program", "C-2023-056463", "2023.11.30"),
        ("100 kg/hr hydrogen PCHE design program", "C-2025-056891", "2025.12.11"),
        ("Adsorption cooling simulation program", "C-2025-034652", "2025.09.03"),
        ("Vapor chamber performance analysis program", "C-2024-041200", "2024.11.04"),
        ("Fin-tube heat exchanger design program", "C-2024-038692", "2024.10.22"),
    ]
    for i, (name, reg_num, date) in enumerate(software, 1):
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        prefix = f"({i}) "
        indent_mm = 8
        pdf.cell(indent_mm, 5, prefix)
        pdf.set_x(pdf.l_margin + indent_mm)
        pdf.write(5, name + " ")
        pdf.set_font("Times", style="B", size=10)
        pdf.write(5, f"({reg_num})")
        pdf.set_font("Times", size=10)
        pdf.write(5, f"  [{date}]")
        pdf.ln()
        pdf.ln(1)

    # ============================================================ TECHNOLOGY TRANSFERS
    pdf.section_title("TECHNOLOGY TRANSFERS")
    transfers = [
        "Heat pipe and vapor chamber structural design for electronics cooling",
        "Micro-channel bonding and fabrication techniques for heat exchangers",
        "Low dew-point dehumidifier development technology",
        "Ultra-thin vapor chamber for next-generation semiconductor cooling",
        "Compact inverter compressor-based dress care system development",
    ]
    for i, text in enumerate(transfers, 1):
        pdf.set_font("Times", size=10)
        pdf.set_x(pdf.l_margin)
        prefix = f"({i}) "
        indent_mm = 8
        pdf.cell(indent_mm, 5, prefix)
        pdf.set_x(pdf.l_margin + indent_mm)
        pdf.multi_cell(0, 5, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1)

    pdf.output(OUTPUT_PATH)
    print(f"PDF generated: {OUTPUT_PATH}")
    import os as _os
    size = _os.path.getsize(OUTPUT_PATH)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")


if __name__ == "__main__":
    build_cv()
