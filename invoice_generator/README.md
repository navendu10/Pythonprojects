# Invoice Generator

Converts Excel invoices into PDF invoices, one PDF per spreadsheet.

## Input format

Put `.xlsx` files in `sample_invoices/`, named `<invoice_nr>-<date>.xlsx` (e.g. `10001-2023.1.18.xlsx`).
Each file needs a sheet called **Sheet 1** with these columns:

`product_id`, `product_name`, `amount_purchased`, `price_per_unit`, `total_price`

## Run

From the repository root (after `pip install -r requirements.txt`):

```bash
python invoice_generator/invoice.py
```

PDFs are written to `invoice_generator/output/` (git-ignored).

## Files

| File | Purpose |
|---|---|
| `invoice.py` | Reads each Excel file and builds the PDF |
| `sample_invoices/` | Example input spreadsheets |
| `pythonhow.png` | Logo drawn at the bottom of each invoice |
