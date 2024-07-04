import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

pdf_dir = Path("PDFs")
pdf_dir.mkdir(parents=True, exist_ok=True)

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt="Invoice nr. {invoice_nr}")
    output_path = pdf_dir / f"{filename}.pdf"
    pdf.output(str(output_path))

print("PDF generation completed.")