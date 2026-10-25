"""Fetch recent news about a topic from NewsAPI and email a digest.

Usage:
    python newsemail.py                # topic defaults to "tesla"
    python newsemail.py "electric cars"

Requires NEWS_API_KEY (and the email variables used by send_email.py) in the
environment or in a ``.env`` file. Get a free key at https://newsapi.org.
"""

import argparse
import os
from datetime import date, timedelta

import requests
from dotenv import load_dotenv

from send_email import send_email

load_dotenv()

NEWS_URL = "https://newsapi.org/v2/everything"
MAX_ARTICLES = 20


def fetch_articles(topic, api_key, days_back=1):
    """Return a list of articles about ``topic`` published in the last ``days_back`` days."""
    params = {
        "q": topic,
        "from": (date.today() - timedelta(days=days_back)).isoformat(),
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": api_key,
    }
    response = requests.get(NEWS_URL, params=params, timeout=30)
    response.raise_for_status()  # fail loudly on 4xx/5xx instead of sending an empty email
    return response.json().get("articles", [])[:MAX_ARTICLES]


def build_digest(articles):
    """Format articles as plain text: title, description and link, separated by blank lines."""
    entries = []
    for article in articles:
        title = article.get("title") or "No title"
        description = article.get("description") or "No description"
        link = article.get("url") or "No URL"
        entries.append(f"{title}\n{description}\n{link}")
    return "\n\n".join(entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("topic", nargs="?", default="tesla", help="search topic")
    args = parser.parse_args()

    api_key = os.environ.get("NEWS_API_KEY")
    if not api_key:
        raise SystemExit("NEWS_API_KEY is not set. See .env.example.")

    articles = fetch_articles(args.topic, api_key)
    if not articles:
        print(f"No articles found for '{args.topic}'; no email sent.")
        return

    send_email(subject=f"Today's news: {args.topic}", body=build_digest(articles))
    print(f"Sent a digest of {len(articles)} articles about '{args.topic}'.")


if __name__ == "__main__":
    main()
