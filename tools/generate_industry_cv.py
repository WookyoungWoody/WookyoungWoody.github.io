#!/usr/bin/env python3
"""Generate industry-focused CV PDF using fpdf2.  2-page version."""

import yaml
import os
import re
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

# Typography constants — bumped up from the cramped 1-page version
BODY_SIZE = 9.0       # general body text
BULLET_SIZE = 9.0     # bullet point text
SMALL_SIZE = 8.0      # secondary lines, footnotes
TINY_SIZE = 7.5       # column headers inside boxes
LINE_H = 5.0          # standard line height
BULLET_H = 5.0        # bullet line height

# Trailing glyph marking a live hyperlink. Must stay latin-1: the core
# Helvetica font cannot encode arrows like U+2197.
LINK_MARKER = chr(187)  # >>
LINK_PAD = 0.7          # mm of extra click area around hyperlink text

# App store URLs are duplicated from _projects/software.md (the KIMMPROP
# section); everything else resolves from _data/. Keep the two in sync.
KIMMPROP_IOS = "https://apps.apple.com/kr/app/kimmprop/id6745596456"
KIMMPROP_ANDROID = "https://play.google.com/store/apps/details?id=com.kimmprop_v03"
SOFTWARE_PROJECT_PAGE = "https://wookyoungwoody.github.io/projects/software/"


class IndustryCVPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-10)
        # Legend telling the reader the blue underlined text is live. Both
        # pages carry links, so it runs on both.
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "I", 6.5)
        self.set_text_color(*MED_GRAY)
        self.cell(70, 4, f"Blue underlined text is clickable {LINK_MARKER}", ln=False)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*MED_GRAY)
        self.cell(0, 4, f"Page {self.page_no()}", align="C")

    def linked_cell(self, text, url, h, w=None):
        """Draw text and register a padded click area over it.

        cell(link=...) sizes the hotspot to the glyph box only (~3mm tall),
        which is a fussy target. Registering the rect separately lets the
        hotspot cover the full line height plus a small margin.
        """
        if w is None:
            w = self.get_string_width(text)
        x0, y0 = self.get_x(), self.get_y()
        self.cell(w, h, text, ln=False)
        # cell() insets its text by c_margin, so the glyphs start there, not
        # at the cell edge; without this the hotspot sits a millimetre left.
        self.link(x0 + self.c_margin - LINK_PAD, y0 - LINK_PAD, w + 2 * LINK_PAD, h + 2 * LINK_PAD, url)
        return w

    def link_chip(self, label, url, size=None):
        """Inline hyperlink chip: accent + underline + trailing marker.

        Returns the width consumed so callers can width-check a line.
        """
        if size is None:
            size = SMALL_SIZE
        text = f"{label} {LINK_MARKER}"
        self.set_font("Helvetica", "U", size)
        self.set_text_color(*ACCENT)
        w = self.linked_cell(text, url, BULLET_H)
        self.set_font("Helvetica", "", size)
        self.set_text_color(*DARK_GRAY)
        return w

    def bullet_with_links(self, text, links, indent=4, size=None):
        """Bullet whose trailing chips hyperlink out. Must stay on one line."""
        if size is None:
            size = BULLET_SIZE
        self.set_x(self.l_margin + indent)
        self.set_font("Helvetica", "", size)
        self.set_text_color(*DARK_GRAY)
        self.cell(4, BULLET_H, chr(149), ln=False)
        self.set_x(self.l_margin + indent + 4)
        self.cell(self.get_string_width(text) + 2, BULLET_H, text, ln=False)
        for label, url in links:
            self.link_chip(label, url, size)
            self.cell(2, BULLET_H, "", ln=False)
        self.ln(BULLET_H)

    def section_header(self, title, spacing_before=3):
        """Draw section header with accent underline rule."""
        self.ln(spacing_before)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*ACCENT)
        self.cell(0, 5, title, ln=False)
        y = self.get_y() + 4
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.4)
        self.line(self.l_margin, y + 1, self.w - self.r_margin, y + 1)
        self.ln(6.5)
        self.set_text_color(*BLACK)
        self.set_draw_color(*BLACK)

    def bullet(self, text, indent=4, size=None):
        """Render a bullet point with hanging indent."""
        if size is None:
            size = BULLET_SIZE
        self.set_font("Helvetica", "", size)
        self.set_text_color(*DARK_GRAY)
        self.set_x(self.l_margin + indent)
        self.cell(4, BULLET_H, chr(149), ln=False)
        self.set_x(self.l_margin + indent + 4)
        self.multi_cell(0, BULLET_H, text)

    def sub_label_bullet(self, label, text, indent=4):
        """Bold sub-label followed by normal text on same line."""
        self.set_x(self.l_margin + indent)
        self.set_font("Helvetica", "", BULLET_SIZE)
        self.set_text_color(*DARK_GRAY)
        self.cell(4, BULLET_H, chr(149), ln=False)
        self.set_x(self.l_margin + indent + 4)
        self.set_font("Helvetica", "B", BULLET_SIZE)
        self.set_text_color(*BLACK)
        lw = self.get_string_width(label)
        self.cell(lw + 1, BULLET_H, label, ln=False)
        self.set_font("Helvetica", "", BULLET_SIZE)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(0, BULLET_H, text)

    def role_tag(self, tag):
        """Render a small inline role tag (PI / Lead / Participant)."""
        self.set_font("Helvetica", "I", SMALL_SIZE - 0.5)
        self.set_text_color(*ACCENT)
        return f"[{tag}]"


def _load_data():
    resume_path = os.path.join(_REPO_ROOT, "_data", "resume.yml")
    with open(resume_path, "r") as f:
        return yaml.safe_load(f)


def _scholar_url():
    """Google Scholar profile URL, built from the id in _data/socials.yml."""
    socials_path = os.path.join(_REPO_ROOT, "_data", "socials.yml")
    with open(socials_path, "r") as f:
        socials = yaml.safe_load(f) or {}
    uid = socials.get("scholar_userid", "")
    return f"https://scholar.google.com/citations?user={uid}" if uid else ""


def _profile_url(data, network):
    for prof in data["basics"].get("profiles", []):
        if prof.get("network", "").lower() == network.lower():
            return prof.get("url", "")
    return ""


def _compute_counts(data):
    all_pubs = data.get("publications", [])
    journal_papers = [p for p in all_pubs if "Proceedings" not in p.get("publisher", "")]
    patents = [c for c in data["certificates"] if c["issuer"] == "Korean Intellectual Property Office"]
    us_patents = [c for c in data["certificates"] if c["issuer"] == "United States Patent and Trademark Office"]
    software = [c for c in data["certificates"] if c["issuer"] == "Korea Copyright Commission"]
    transfers = data.get("volunteer", [])
    return journal_papers, patents, us_patents, software, transfers


def _year(date_str):
    """Extract year from a date string like '2017-03-01'."""
    return date_str[:4] if date_str else ""


def build_pdf():
    data = _load_data()
    journal_papers, patents, us_patents, software, transfers = _compute_counts(data)

    # Counts for summary / achievements
    n_journal = len(journal_papers)
    n_patents = len(patents)
    n_us = len(us_patents)
    n_software = len(software)
    n_transfers = len(transfers)

    # SCI vs KCI breakdown
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
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.add_page()

    cw = pdf.w - pdf.l_margin - pdf.r_margin  # ~174mm

    # ------------------------------------------------------------------ HEADER
    basics = data["basics"]
    name = basics["name"].upper()
    label = basics.get("label", "")
    email = basics.get("email", "")
    city = basics.get("location", {}).get("city", "")
    location_str = f"{city}, Korea" if city else ""

    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 8, f"{name}, Ph.D.", ln=True)

    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 5, f"{label}  |  Thermal Engineer", ln=True)

    # Single contact line tuned to fit the page width (must stay 1 line to
    # preserve the precise 2-page layout). Scholar shown as a short label
    # ("Google Scholar") rather than the full citations URL to make room.
    # Each entry is a live hyperlink; no LINK_MARKER here because the line
    # already runs at ~171mm of the 174mm content width.
    site_url = basics.get("url", "")
    contact_links = [
        (email, f"mailto:{email}"),
        ("Google Scholar", _scholar_url()),
        ("linkedin.com/in/wookyoungwoody", _profile_url(data, "LinkedIn")),
        ("wookyoungwoody.github.io", site_url),
    ]
    sep = "  |  "
    pdf.set_font("Helvetica", "", 8.5)
    sep_w = pdf.get_string_width(sep)
    line_w = sum(pdf.get_string_width(t) for t, _ in contact_links) + len(contact_links) * sep_w
    line_w += pdf.get_string_width(location_str)
    if line_w > cw:
        print(f"WARNING: contact line is {line_w:.1f}mm wide, exceeds {cw:.1f}mm -- it will wrap")

    for text, url in contact_links:
        pdf.set_font("Helvetica", "U", 8.5)
        pdf.set_text_color(*ACCENT)
        pdf.linked_cell(text, url, 5)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*MED_GRAY)
        pdf.cell(sep_w, 5, sep, ln=False)
    pdf.cell(0, 5, location_str, ln=True)

    # Horizontal rule
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.6)
    rule_y = pdf.get_y() + 1.5
    pdf.line(pdf.l_margin, rule_y, pdf.w - pdf.r_margin, rule_y)
    pdf.set_y(rule_y + 2)

    # --------------------------------------------------------- PROFESSIONAL SUMMARY
    pdf.section_header("PROFESSIONAL SUMMARY", spacing_before=1.5)
    pdf.set_font("Helvetica", "", BODY_SIZE)
    pdf.set_text_color(*DARK_GRAY)
    # NOTE: keep this text within ~5 rendered lines (~550 chars). The fixed-
    # position KEY ACHIEVEMENTS box at the bottom of page 1 breaks across
    # pages (2 -> 7 page blowup) if the summary grows by even one line.
    summary = (
        "Ph.D. thermal engineer with 10+ years in electronics cooling and two-phase heat transfer, from "
        "pulsating heat pipes (KAIST) to AI data center cooling (DLC, immersion, jet impingement) "
        "as PI/project lead at Korea's national research institute (KIMM). Combines hands-on experimental "
        "expertise (-220°C / 100 MPa testing, hydrogen heat exchangers, heat pumps) with "
        "production-grade software development (Python / FastAPI / React Native). Lab-to-market record: "
        f"{n_transfers} technology transfers, {n_patents} domestic + {n_us} U.S. patents, "
        f"{n_journal} journal papers ({n_sci} SCI + {n_kci} KCI), {n_software} registered design programs."
    )
    pdf.multi_cell(0, LINE_H, summary)

    # --------------------------------------------------------- CORE COMPETENCIES
    pdf.section_header("CORE COMPETENCIES")

    box_y = pdf.get_y()
    box_h = 27
    pdf.set_fill_color(*LIGHTER_GRAY)
    pdf.rect(pdf.l_margin, box_y, cw, box_h, style="F")
    pdf.set_y(box_y + 2.5)

    cols = [
        ("Thermal Management", [
            "Data center cooling (ILC/DLC)",
            "Immersion / Jet impingement",
            "Electronics thermal design",
        ]),
        ("Energy Systems", [
            "Heat pump (vapor./ads.)",
            "Liquid hydrogen vaporizer",
            "Low-GWP refrigerant R&D",
        ]),
        ("System Design & Testing", [
            "Heat exchanger (PCHE/S&T)",
            "Thermal loop construction",
            "High-pressure / cryogenic sys.",
        ]),
        ("Software & Analysis", [
            "Python / FastAPI / React Native",
            "2-phase HT measurement",
            "VLE measurement & EOS",
        ]),
    ]
    col_w = cw / 4

    for i, (title, items) in enumerate(cols):
        x = pdf.l_margin + i * col_w
        pdf.set_xy(x, box_y + 2.5)
        pdf.set_font("Helvetica", "B", TINY_SIZE)
        pdf.set_text_color(*ACCENT)
        pdf.cell(col_w, 5, title, ln=False)
        for j, item in enumerate(items):
            pdf.set_xy(x, box_y + 8.5 + j * 5.5)
            pdf.set_font("Helvetica", "", TINY_SIZE)
            pdf.set_text_color(*DARK_GRAY)
            pdf.cell(col_w, 5, item, ln=False)

    pdf.set_y(box_y + box_h + 2)

    # --------------------------------------------------------- EXPERIENCE
    pdf.section_header("EXPERIENCE")

    work = data["work"][0]
    position = work.get("position", "")
    company = work.get("name", "")
    start_year = _year(work.get("startDate", ""))
    end_date = work.get("endDate", "")
    end_str = _year(end_date) if end_date else "Present"
    date_range = f"Jun {start_year} - {end_str}"

    pdf.set_font("Helvetica", "B", BODY_SIZE + 0.5)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, LINE_H, f"{position}  |  {company}", ln=True)
    pdf.set_font("Helvetica", "", SMALL_SIZE)
    pdf.set_text_color(*MED_GRAY)
    pdf.cell(0, 4, f"{date_range}  --  Korea's national research institute for machinery and materials", ln=True)
    pdf.ln(1)

    # Thematic stream groupings
    streams = [
        (
            "Data Center Thermal Management",
            [
                "Jet-enhanced immersion cooling for next-gen high-heat-density servers [PI, 2025]",
                "Immersion cooling waste heat utilization and active thermal management [Lead, 2024-2028]",
                "Direct liquid cooling (DLC) system for data center power-consumption reduction [Lead, 2026-2029]",
            ],
        ),
        (
            "Cryogenic / Hydrogen Heat Exchangers",
            [
                "PCHE design & testing for liquid-hydrogen vaporizers: cryogenic testing to -220°C / 100 MPa [Lead, 2021-2026]",
                "Anti-freezing PCHE design; CFD conjugate heat transfer analysis; freezing condition experimental mapping [Lead]",
                "Compact PCHE development for below -200°C, 100 MPa-class hydrogen supply system [Lead, 2022-2026]",
            ],
        ),
        (
            "Heat Pumps & Refrigerants",
            [
                "300°C-class high-temperature heat pump system for fossil fuel replacement [Participant, 2023-2028]",
                "Chemisorption heat pump with electrochemical compressor; experimental characterization [Participant, 2021-2025]",
                "Low-GWP refrigerant VLE measurement (R-32/R-125, R-1233ZD(E)) and equation-of-state development [Participant]",
            ],
        ),
        (
            "Engineering Software & Apps",
            [
                "AI-based automated design tool for data center DLC cooling systems [PI, 2026]",
                # Shipped app -- link straight to both stores so a recruiter can
                # open it. Text trimmed ("cross-platform" is implied by
                # iOS/Android) to leave room for the two chips on one line.
                (
                    "KIMMPROP: iOS/Android thermophysical-property app (CoolProp/REFPROP via WASM) [PI, 2025]",
                    [("App Store", KIMMPROP_IOS), ("Google Play", KIMMPROP_ANDROID)],
                ),
                (
                    f"{n_software} registered engineering design programs (PCHE, heat-pump cycle, vapor chamber, etc.) [Lead]",
                    [("Details", SOFTWARE_PROJECT_PAGE)],
                ),
            ],
        ),
    ]

    # Advisory drift check: every curated Experience bullet should trace back
    # to a project in resume.yml (this section is hand-tuned to fit 2 pages,
    # so bullets stay curated -- but a bullet describing work that is not in
    # resume.yml is a red flag; see cv-manager notes on a past incident).
    def _tokens(text):
        return {t for t in re.findall(r"[a-z0-9]+", str(text).lower()) if len(t) > 3}

    def _bullet_text(b):
        """A stream bullet is either plain text or (text, [(label, url), ...])."""
        return b[0] if isinstance(b, tuple) else b

    project_token_sets = [_tokens(p) for p in data.get("projects", []) + data.get("publications", [])]
    for _, stream_bullets in streams:
        for b in stream_bullets:
            bt = _tokens(_bullet_text(b).split("[")[0])
            best = max((len(bt & pt) / len(bt) for pt in project_token_sets), default=0)
            if bt and best < 0.3:
                print(f"WARNING: Experience bullet not traceable to resume.yml projects: {_bullet_text(b)!r}")

    # A linked bullet is drawn as inline cells, so unlike bullet() it cannot
    # wrap -- overflow would silently run past the right margin.
    bullet_avail = cw - 6 - 4
    for _, stream_bullets in streams:
        for b in stream_bullets:
            if not isinstance(b, tuple):
                continue
            text, links = b
            pdf.set_font("Helvetica", "", SMALL_SIZE)
            w = pdf.get_string_width(text) + 2
            pdf.set_font("Helvetica", "U", SMALL_SIZE)
            w += sum(pdf.get_string_width(f"{label} {LINK_MARKER}") + 2 for label, _ in links)
            if w > bullet_avail:
                print(f"WARNING: linked bullet is {w:.1f}mm, exceeds {bullet_avail:.1f}mm: {text!r}")

    for stream_title, stream_bullets in streams:
        # Stream label
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "B", BODY_SIZE)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(0, LINE_H, stream_title, ln=True)
        for b in stream_bullets:
            if isinstance(b, tuple):
                pdf.bullet_with_links(b[0], b[1], indent=6, size=SMALL_SIZE)
            else:
                pdf.bullet(b, indent=6, size=SMALL_SIZE)
        pdf.ln(1)

    # Quantified impact line
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "I", SMALL_SIZE)
    pdf.set_text_color(*ACCENT)
    pdf.cell(
        0, LINE_H,
        f"Impact: {n_journal} journal papers ({n_sci} SCI + {n_kci} KCI) | {n_patents} domestic patents + {n_us} U.S. patent | {n_software} registered software | {n_transfers} technology transfers",
        ln=True,
    )

    # --------------------------------------------------------- EDUCATION
    pdf.section_header("EDUCATION")

    for edu_entry in data["education"]:
        study_type = edu_entry.get("studyType", "")
        area = edu_entry.get("area", "")
        institution = edu_entry.get("institution", "")
        inst_display = institution.split("(")[0].strip()
        start_yr = _year(edu_entry.get("startDate", ""))
        end_yr = _year(edu_entry.get("endDate", ""))
        yr_range = f"{start_yr} - {end_yr}" if start_yr and end_yr else start_yr or end_yr

        pdf.set_font("Helvetica", "B", BODY_SIZE)
        pdf.set_text_color(*BLACK)
        pdf.cell(12, LINE_H, study_type, ln=False)
        pdf.set_font("Helvetica", "", BODY_SIZE)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(65, LINE_H, area, ln=False)
        pdf.set_font("Helvetica", "B", BODY_SIZE)
        pdf.set_text_color(*ACCENT)
        pdf.cell(50, LINE_H, inst_display, ln=False)
        pdf.set_font("Helvetica", "", BODY_SIZE)
        pdf.set_text_color(*MED_GRAY)
        pdf.cell(0, LINE_H, yr_range, ln=True)

        courses = edu_entry.get("courses", [])
        dissertation_line = next((c for c in courses if c.startswith("Dissertation:") or c.startswith("Thesis:")), None)
        advisor_line = next((c for c in courses if c.startswith("Advisor:")), None)

        if dissertation_line:
            pdf.set_x(pdf.l_margin + 12)
            pdf.set_font("Helvetica", "I", SMALL_SIZE)
            pdf.set_text_color(*MED_GRAY)
            pdf.multi_cell(0, 4.5, dissertation_line)
        if advisor_line:
            pdf.set_x(pdf.l_margin + 12)
            pdf.set_font("Helvetica", "I", SMALL_SIZE)
            pdf.set_text_color(*MED_GRAY)
            pdf.cell(0, 4.5, advisor_line, ln=True)

    # --------------------------------------------------------- KEY ACHIEVEMENTS
    pdf.section_header("KEY ACHIEVEMENTS")

    ach_y = pdf.get_y()
    ach_h = 16
    pdf.set_fill_color(*ACHIEVEMENT_BG)
    pdf.rect(pdf.l_margin, ach_y, cw, ach_h, style="F")
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.2)
    pdf.rect(pdf.l_margin, ach_y, cw, ach_h, style="D")

    achievements = [
        (f"{n_journal}", f"Journal Papers\n({n_sci} SCI + {n_kci} KCI)"),
        (str(n_patents), "Domestic\nPatents"),
        (str(n_us), "U.S.\nPatents"),
        (str(n_software), "Registered\nSoftware"),
        (str(n_transfers), "Tech\nTransfers"),
    ]
    ach_col_w = cw / 5
    for i, (num, desc) in enumerate(achievements):
        x = pdf.l_margin + i * ach_col_w
        pdf.set_xy(x, ach_y + 2)
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(*ACCENT)
        pdf.cell(ach_col_w, 6, num, align="C", ln=False)
        pdf.set_xy(x, ach_y + 8.5)
        pdf.set_font("Helvetica", "", 6.0)
        pdf.set_text_color(*DARK_GRAY)
        # multi-line desc: split on \n
        lines = desc.split("\n")
        for li, line_text in enumerate(lines):
            pdf.set_xy(x, ach_y + 8.5 + li * 3.5)
            pdf.cell(ach_col_w, 3.5, line_text, align="C", ln=False)

    pdf.set_y(ach_y + ach_h + 2)

    # ========================================================= PAGE 2 STARTS HERE
    # (auto_page_break handles it; we proceed with content)

    # --------------------------------------------------------- SELECTED PUBLICATIONS
    pdf.section_header("SELECTED PUBLICATIONS")

    # 9 representative publications: W. Kim first-author / lead works + key co-author
    selected_pubs = [
        # W. Kim first-author — KIMM era
        ("W. Kim", ' et al., "Freezing Phenomenon in PCHE for Cryogenic LH2 Vaporizer," Appl. Therm. Eng. 273 (2025)'),
        ("W. Kim", ' et al., "Freezing Condition of PCHE for LH2 Vaporizer," J. Hydrogen New Energy 35(2) (2024)'),
        ("W. Kim", ' et al., "Falling Film Evaporation of R-1233ZD(E): Flow & Thermal Characteristics," Korean J. ACRE 36(1) (2024)'),
        # co-author — KIMM era
        ("J.S. Kim, W. Kim", ' et al., "Pool boiling of ammonia outside enhanced tubes," Appl. Therm. Eng. 247 (2024)'),
        ("H.S. Kim, W. Kim", ' et al., "Chemisorption heat pump performance under various conditions," Appl. Therm. Eng. (2024)'),
        ("D.H. Kim, W. Kim", ' et al., "VLE of R-32/R-125: experiment and EOS verification," J. Mech. Sci. Technol. (2024)'),
        ("J. Kim, W. Kim", ' et al., "Liquid behavior in falling-film evaporator distributor," Physics of Fluids 35 (2023)'),
        # W. Kim first-author — KAIST era (Ph.D. core work)
        ("W. Kim", ' and S.J. Kim, "Fundamental issues about pulsating heat pipes," J. Heat Transfer - ASME 143 (2021)'),
        ("W. Kim", ' and S.J. Kim, "Flow behavior effect on pulsating heat pipes," Int. J. Heat Mass Transfer 149 (2020)'),
    ]

    for idx, (bold_part, rest) in enumerate(selected_pubs, 1):
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", SMALL_SIZE)
        pdf.set_text_color(*MED_GRAY)
        num_w = pdf.get_string_width(f"({idx}) ") + 1
        pdf.cell(num_w, LINE_H, f"({idx})", ln=False)
        pdf.set_font("Helvetica", "B", SMALL_SIZE)
        pdf.set_text_color(*BLACK)
        bw = pdf.get_string_width(bold_part)
        pdf.cell(bw + 1, LINE_H, bold_part, ln=False)
        pdf.set_font("Helvetica", "", SMALL_SIZE)
        pdf.set_text_color(*DARK_GRAY)
        pdf.multi_cell(0, LINE_H, rest)

    # --------------------------------------------------------- SELECTED PATENTS
    pdf.section_header("SELECTED PATENTS")

    # 8 representative patents drawn from resume.yml certificates (KIPO)
    # Sorted to highlight most relevant to current research themes
    selected_patent_names = [
        "Immersion cooling device",
        "Immersion cooling HVAC system and method",
        "Heat exchanger with anti-freezing capability (1)",
        "Micro-channel reactor",
        "Ternary refrigerant composition and heat pump system",
        "Adsorption heat pump evaporator and system",
        "Heat pipe integrated reactor for adsorption heat pump",
        "Geothermal heat supply device and heating system",
    ]

    kipo_patents = [c for c in data["certificates"] if c["issuer"] == "Korean Intellectual Property Office"]
    patent_map = {c["name"]: c for c in kipo_patents}

    pdf.set_font("Helvetica", "I", SMALL_SIZE - 0.5)
    pdf.set_text_color(*MED_GRAY)
    pdf.cell(0, 4.5, f"Showing 8 of {n_patents} domestic patents (Korean Intellectual Property Office)", ln=True)
    pdf.ln(0.5)

    shown = 0
    for pname in selected_patent_names:
        if pname in patent_map:
            c = patent_map[pname]
            year = c["date"][:4] if c.get("date") else ""
            display_name = pname.replace(" (1)", "").replace(" (2)", "")
            pdf.set_x(pdf.l_margin)
            pdf.set_font("Helvetica", "", SMALL_SIZE)
            pdf.set_text_color(*DARK_GRAY)
            pdf.cell(4, LINE_H, chr(149), ln=False)
            pdf.set_x(pdf.l_margin + 4)
            pdf.set_font("Helvetica", "", SMALL_SIZE)
            pdf.set_text_color(*DARK_GRAY)
            # Name takes remaining width; year right-aligned
            name_w = cw - 4 - 12
            pdf.cell(name_w, LINE_H, display_name, ln=False)
            pdf.set_font("Helvetica", "", SMALL_SIZE)
            pdf.set_text_color(*MED_GRAY)
            pdf.cell(12, LINE_H, year, align="R", ln=True)
            shown += 1

    # --------------------------------------------------------- REGISTERED SOFTWARE
    pdf.section_header("REGISTERED SOFTWARE PROGRAMS")

    kcc_sw = [c for c in data["certificates"] if c["issuer"] == "Korea Copyright Commission"]
    # Sort by date
    kcc_sw_sorted = sorted(kcc_sw, key=lambda c: c.get("date", ""), reverse=True)

    pdf.set_font("Helvetica", "I", SMALL_SIZE - 0.5)
    pdf.set_text_color(*MED_GRAY)
    note = f"All {n_software} programs registered with Korea Copyright Commission"
    pdf.cell(pdf.get_string_width(note) + 3, 4.5, note, ln=False)
    pdf.link_chip("Project page", SOFTWARE_PROJECT_PAGE, SMALL_SIZE - 0.5)
    pdf.ln(4.5)
    pdf.ln(0.5)

    for c in kcc_sw_sorted:
        year = c["date"][:4] if c.get("date") else ""
        # Strip registration number from name for cleaner display
        raw_name = c["name"]
        display_name = raw_name.split(" (C-")[0] if " (C-" in raw_name else raw_name
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", SMALL_SIZE)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(4, LINE_H, chr(149), ln=False)
        pdf.set_x(pdf.l_margin + 4)
        name_w = cw - 4 - 12
        pdf.cell(name_w, LINE_H, display_name, ln=False)
        pdf.set_font("Helvetica", "", SMALL_SIZE)
        pdf.set_text_color(*MED_GRAY)
        pdf.cell(12, LINE_H, year, align="R", ln=True)

    # --------------------------------------------------------- TECHNOLOGY TRANSFERS
    pdf.section_header("TECHNOLOGY TRANSFERS")

    pdf.set_font("Helvetica", "I", SMALL_SIZE - 0.5)
    pdf.set_text_color(*MED_GRAY)
    pdf.cell(0, 4.5, f"{n_transfers} transfers to industry partners", ln=True)
    pdf.ln(0.5)

    for t in transfers:
        pos = t.get("position", "")
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", SMALL_SIZE)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(4, LINE_H, chr(149), ln=False)
        pdf.set_x(pdf.l_margin + 4)
        pdf.multi_cell(0, LINE_H, pos)

    # --------------------------------------------------------- TECHNICAL SKILLS
    pdf.section_header("TECHNICAL SKILLS")

    skills = [
        ("Experimental:", "Thermal loop design & construction (1-/2-phase) · Low-GWP refrigerant systems · "
                          "2-phase flow & heat-transfer measurement · High-pressure testing (100 MPa) · "
                          "Cryogenic systems (-220°C) · Flow visualization"),
        ("Analytical & Computational:", "Thermal network modeling · Heat exchanger design (PCHE, S&T, PHE) · "
                          "CFD (ANSYS FLUENT, COMSOL) · CAD (SOLIDWORKS, INVENTOR) · "
                          "Surrogate modeling & design optimization · "
                          "CoolProp/REFPROP"),
        ("Software Development:", "Python · JavaScript/TypeScript · C/C++ · FastAPI · React / React Native · "
                          "Git · Docker · Linux"),
    ]

    for skill_label, val in skills:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "B", SMALL_SIZE)
        pdf.set_text_color(*BLACK)
        lw = pdf.get_string_width(skill_label) + 2
        pdf.cell(lw, LINE_H, skill_label, ln=False)
        pdf.set_font("Helvetica", "", SMALL_SIZE)
        pdf.set_text_color(*DARK_GRAY)
        pdf.multi_cell(0, LINE_H, val)

    # --------------------------------------------------------- PROFESSIONAL ACTIVITIES
    affiliations = data.get("affiliations", [])
    if affiliations:
        pdf.section_header("PROFESSIONAL ACTIVITIES")

        def _aff_period(start, end):
            if not start and not end:
                return ""
            if start and not end:
                return f"{start.replace('-', '.')} - Present"
            return f"{start.replace('-', '.')} - {end.replace('-', '.')}"

        for aff in affiliations:
            org = aff.get("organization", "")
            aff_position = aff.get("position", "")
            period = _aff_period(aff.get("startDate", ""), aff.get("endDate", ""))

            # NOTE: uses TINY_SIZE (not SMALL_SIZE) so long organization names
            # (e.g. "SAREK Data Center Facility Technology Division Committee")
            # stay on one line. A one-line wrap here previously pushed the last
            # bullet onto a spurious 3rd page (2026-07 regression when the SAREK
            # committee was renamed/promoted). Keep at TINY_SIZE unless width is
            # re-verified with get_string_width.
            pdf.set_x(pdf.l_margin)
            pdf.set_font("Helvetica", "", TINY_SIZE)
            pdf.set_text_color(*DARK_GRAY)
            pdf.cell(3.5, LINE_H, chr(149), ln=False)
            pdf.set_font("Helvetica", "B", TINY_SIZE)
            pdf.set_text_color(*BLACK)
            pos_w = pdf.get_string_width(aff_position)
            pdf.cell(pos_w, LINE_H, aff_position, ln=False)
            pdf.set_font("Helvetica", "", TINY_SIZE)
            pdf.set_text_color(*DARK_GRAY)
            tail = f", {org}"
            if period:
                tail += f"  [{period}]"
            pdf.multi_cell(0, LINE_H, tail)

    pdf.output(OUTPUT)
    print(f"Generated: {OUTPUT}")
    print(f"Pages: {pdf.page}")


if __name__ == "__main__":
    build_pdf()
