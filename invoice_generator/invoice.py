"""Turn Excel invoices into PDF invoices.

Each ``sample_invoices/<invoice_nr>-<date>.xlsx`` file (sheet "Sheet 1") becomes
``output/<invoice_nr>-<date>.pdf``.

Run from anywhere:  python invoice_generator/invoice.py
"""

from pathlib import Path

import pandas as pd
from fpdf import FPDF

BASE_DIR = Path(__file__).parent
INVOICES_DIR = BASE_DIR / "sample_invoices"
OUTPUT_DIR = BASE_DIR / "output"
LOGO = BASE_DIR / "pythonhow.png"

# Table layout: (column name in the Excel sheet, cell width in mm)
COLUMNS = [
    ("product_id", 30),
    ("product_name", 70),
    ("amount_purchased", 30),
    ("price_per_unit", 30),
    ("total_price", 30),
]
GREY = (80, 80, 80)


def _cell(pdf, width, text, bold=False, border=1, end_line=False):
    """Draw one table cell in the standard invoice style."""
    pdf.set_font("Times", size=10, style="B" if bold else "")
    pdf.set_text_color(*GREY)
    pdf.cell(
        w=width,
        h=8,
        text=str(text),
        border=border,
        new_x="LMARGIN" if end_line else "RIGHT",
        new_y="NEXT" if end_line else "TOP",
    )


def build_invoice_pdf(filepath):
    """Read one Excel invoice and return the finished FPDF document."""
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    invoice_nr, invoice_date = Path(filepath).stem.split("-", 1)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Invoice number and date
    pdf.set_font("Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=f"Invoice nr. {invoice_nr}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=50, h=8, text=f"Date: {invoice_date}", new_x="LMARGIN", new_y="NEXT")

    # Table header: "product_id" -> "Product Id"
    for index, (column, width) in enumerate(COLUMNS):
        title = column.replace("_", " ").title()
        _cell(pdf, width, title, bold=True, end_line=index == len(COLUMNS) - 1)

    # One table row per product
    for _, row in df.iterrows():
        for index, (column, width) in enumerate(COLUMNS):
            _cell(pdf, width, row[column], end_line=index == len(COLUMNS) - 1)

    # Totals row (only the last column is filled) and a summary line
    total_sum = df["total_price"].sum()
    for index, (_, width) in enumerate(COLUMNS):
        is_last = index == len(COLUMNS) - 1
        _cell(pdf, width, total_sum if is_last else "", end_line=is_last)

    pdf.set_font("Times", size=10, style="B")
    pdf.cell(w=20, h=8, text=f"The total price is {total_sum}", new_x="LMARGIN", new_y="NEXT")

    # Branding
    pdf.set_font("Times", size=16, style="B")
    pdf.cell(w=30, h=8, text="PythonHow")
    pdf.image(str(LOGO), w=10)
    return pdf


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    invoices = sorted(INVOICES_DIR.glob("*.xlsx"))
    if not invoices:
        raise SystemExit(f"No .xlsx invoices found in {INVOICES_DIR}")

    # Note: saving happens *inside* the loop so every invoice gets its own PDF.
    for filepath in invoices:
        pdf = build_invoice_pdf(filepath)
        output_path = OUTPUT_DIR / f"{filepath.stem}.pdf"
        pdf.output(str(output_path))
        print(f"Created {output_path}")

    print("PDF generation completed.")


if __name__ == "__main__":
    main()
