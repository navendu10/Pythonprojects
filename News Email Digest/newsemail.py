import requests
from send_email import send_email

topic = "tesla"
api_key = "3cbcc2cd668142f6bad98be3164b47a1"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2024-06-18&sortBy=publishedAt&apiKey=3cbcc2cd668142f6bad98be3164b47a1$language=en")
response = requests.get(url)

# Make request
request = requests.get(url)
body = "Subject: Today's news\n"
if response.status_code == 200:
    content = request.json()

    if 'articles' in content:

        for article in content["articles"][:20]:
            title = article["title"] if article["title"] is not None else "No title"
            description = article["description"] if article["description"] is not None else "No description"
            url = article["url"] if article["url"] is not None else "No URL"
            body += f"{title}\n{description}\n{url}\n\n"


body = body.encode("utf-8")
send_email(message=body)