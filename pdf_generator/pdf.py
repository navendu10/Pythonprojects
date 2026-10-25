"""Generate a PDF template with one section per topic in ``topics.csv``.

For every topic a title page is created, followed by empty pages up to the
number given in the "Pages" column. Every page gets the topic name as a footer.

Run from anywhere:  python pdf_generator/pdf.py
"""

from pathlib import Path

import pandas as pd
from fpdf import FPDF

BASE_DIR = Path(__file__).parent
TOPICS_FILE = BASE_DIR / "topics.csv"
OUTPUT_FILE = BASE_DIR / "output" / "output.pdf"

FOOTER_Y = 277  # mm from the top of the A4 page


def add_title(pdf, topic):
    """Write the topic as a blue heading with a line underneath (first page of a topic)."""
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, text=topic, align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.line(10, 21, 200, 21)


def add_footer(pdf, topic):
    """Write the topic in small grey italics at the bottom right of the page."""
    pdf.set_y(FOOTER_Y)
    pdf.set_font("Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, text=topic, align="R")


def main():
    df = pd.read_csv(TOPICS_FILE)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)  # we place footers ourselves

    for _, row in df.iterrows():
        for page_number in range(int(row["Pages"])):
            pdf.add_page()
            if page_number == 0:
                add_title(pdf, row["Topic"])
            add_footer(pdf, row["Topic"])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUTPUT_FILE))
    print(f"Created {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
