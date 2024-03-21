import requests
import os

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&" \
      f"from=2024-02-21&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.text
print(content)
