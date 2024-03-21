import requests
import os
import send_email

# API key from https://newsapi.org
api_key = os.getenv("NEWS_API_KEY")

# Search parameters
topic = "tesla"
date = "2024-02-21"
language = "en"
url = f"https://newsapi.org/v2/everything?"\
        f"q={topic}&" \
        f"from={date}&"\
        "sortBy=publishedAt&"\
        f"apiKey={api_key}&"\
        f"language={language}"

# Get Content
request = requests.get(url)
content = request.json()

# Create email message
message = ""
for articles in content["articles"][:20]:
    if all([articles['title'], articles['description'], articles['url']]):
        message = message + f"""Title: {articles['title']}
Description: {articles['description']}
See more at: {articles['url']}\n\n"""

message = "Subject: Email digest\n\n" + message

# Send Email
print(message)
send_email.send_email(message.encode('utf-8'))
