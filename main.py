import requests
import os

# API key from https://newsapi.org
api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&" \
      f"from=2024-02-21&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)

content = request.json()

for articles in content["articles"]:
    print(articles["title"])
    print(articles["description"])
    print(articles["url"])
