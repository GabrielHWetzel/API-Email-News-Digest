import requests
import os
import send_email

# API key from https://newsapi.org
api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&" \
      f"from=2024-02-21&sortBy=publishedAt&apiKey={api_key}"
# Content
request = requests.get(url)
content = request.json()
message = ""

for articles in content["articles"][11:15]:
    message = (message + f"""{articles['title']}
{articles['url']}
{articles['description']}\n\n""")

message = "Subject: Email digest\n" + message

send_email.send_email(message.encode('utf-8'))
