import requests

api_key = "3cbcc2cd668142f6bad98be3164b47a1"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-18&sortBy=publishedAt&apiKey=3cbcc2cd668142f6bad98be3164b47a1"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles title and description
for article in (content["articles"]):
    print(article["title"])
    print(article["Description"])