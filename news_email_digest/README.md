# News Email Digest

Fetches the latest news about a topic from [NewsAPI](https://newsapi.org) and emails you a plain-text digest
(title, description and link for up to 20 articles).

## Setup

1. Install dependencies from the repository root: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` in the repository root and set `NEWS_API_KEY`,
   `EMAIL_USERNAME`, `EMAIL_PASSWORD` (Gmail app password) and optionally `EMAIL_RECEIVER`.

## Run

```bash
python news_email_digest/newsemail.py            # default topic: tesla
python news_email_digest/newsemail.py "electric cars"
```

The script requests articles from the last day, sorted by newest first, in English.
No email is sent if nothing is found.

## Scheduling (optional)

Run it daily with cron (Linux/macOS) or Task Scheduler (Windows), e.g. every day at 8:00:

```
0 8 * * * cd /path/to/Pythonprojects && .venv/bin/python news_email_digest/newsemail.py
```

## Files

| File | Purpose |
|---|---|
| `newsemail.py` | Fetches articles, builds the digest and sends it |
| `send_email.py` | Gmail SMTP helper (credentials come from environment variables) |
