import requests
from send_email import send_email

api_key = "3cbcc2cd668142f6bad98be3164b47a1"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-18&sortBy=publishedAt&apiKey=3cbcc2cd668142f6bad98be3164b47a1"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles title and description
body = ""
for article in (content["articles"]):
    title = article.get("title", "No title")
    description = article.get("description", "No description")
    body += f"{title}\n{description}\n\n"

body = body.encode("utf-8")
send_email(message=body)