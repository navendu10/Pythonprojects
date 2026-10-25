# PDF Generator

Builds a multi-page A4 PDF template from `topics.csv`: each topic gets a title page followed by
blank pages (the number is set in the `Pages` column), with the topic name as a footer on every page.

## Run

```bash
python pdf_generator/pdf.py
```

Output: `pdf_generator/output/output.pdf` (git-ignored).

## topics.csv format

```
Order,Topic,Pages
1,Variables,2
2,Lists,3
```
