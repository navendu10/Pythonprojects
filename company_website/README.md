# Company Website (demo)

A small Streamlit site for a fictional company: a landing page with a team directory
and a contact form that emails the message to the site owner.

## Run

From the repository root (after `pip install -r requirements.txt`):

```bash
streamlit run company_website/app.py
```

The contact form needs the email variables from `.env` (see the root README); the rest works without them.

## Files

| File | Purpose |
|---|---|
| `app.py` | Landing page and team grid |
| `pages/Contact_Us.py` | Contact form with a topic dropdown |
| `pages/topics.csv` | Topics shown in the dropdown |
| `data.csv` | Team members (first name, last name, role, image) |
| `images/` | Team photos |
| `send_email.py` | Gmail SMTP helper |
