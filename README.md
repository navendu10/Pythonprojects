# Python Projects

A collection of small Python apps and scripts, including a Streamlit portfolio site that showcases them.

## Projects

| Folder | What it does | How to run |
|---|---|---|
| `Home.py` + `pages/` | Streamlit **portfolio website** with a contact form | `streamlit run Home.py` |
| [`company_website/`](company_website/) | Streamlit **company site demo** with a team directory and contact form | `streamlit run company_website/app.py` |
| [`invoice_generator/`](invoice_generator/) | Converts Excel invoices into PDF invoices | `python invoice_generator/invoice.py` |
| [`news_email_digest/`](news_email_digest/) | Fetches news about a topic and emails a digest | `python news_email_digest/newsemail.py "topic"` |
| [`pdf_generator/`](pdf_generator/) | Builds a multi-page PDF template from a CSV of topics | `python pdf_generator/pdf.py` |
| [`scratch/`](scratch/) | Small practice scripts | `python scratch/word_frequency.py` |

## Getting started

```bash
# 1. Clone and enter the repo
git clone https://github.com/navendu10/Pythonprojects.git
cd Pythonprojects

# 2. Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure secrets (only needed for the contact forms and the news digest)
cp .env.example .env             # then edit .env with your own values
```

### Configuration

Secrets are read from environment variables, loaded from a local `.env` file.
**Never commit `.env`** (it is git-ignored).

| Variable | Used by | Description |
|---|---|---|
| `EMAIL_USERNAME` | contact forms, news digest | Gmail address that sends the email |
| `EMAIL_PASSWORD` | contact forms, news digest | Gmail [app password](https://myaccount.google.com/apppasswords) (not your normal password) |
| `EMAIL_RECEIVER` | contact forms, news digest | Who receives the email (defaults to `EMAIL_USERNAME`) |
| `NEWS_API_KEY` | news digest | Free key from [newsapi.org](https://newsapi.org) |

The apps run without these; only sending email or fetching news needs them.

## Repository layout

```
.
├── Home.py                 # portfolio home page (Streamlit entry point)
├── pages/Contact_Us.py     # portfolio contact form
├── send_email.py           # email helper used by the portfolio
├── data.csv                # list of projects shown on the portfolio
├── images/                 # portfolio screenshots and photo
├── company_website/
├── invoice_generator/
├── news_email_digest/
├── pdf_generator/
├── scratch/
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

## License

[MIT](LICENSE)
