import requests
import send_email


# api key
api_key = "your api key"
topic = "tesla"
lang = "en"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      f"sortBy=publishedAt&apiKey={api_key}&language={lang}"

request = requests.get(url)
content = request.json()

user_email = "adeel.nariai96@gmail.com"

body = ""

for article in content["articles"][:20]:
    title = article["title"] or "No Title"
    description = article["description"] or "No Description"
    news_url = article["url"] or "No url"
    body += "Subject: Today`s news" + "\n" + title + "\n" + description + "\n\n" + news_url + "\n\n"


body = body.encode("utf-8")
send_email.send_email(user_email,body)
