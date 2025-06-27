import requests
import send_email


# api key
api_key = "c25984fdf8c340b3b2c773ecb9dcffff"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-05-27&sortBy=publishedAt&apiKey"
       "=c25984fdf8c340b3b2c773ecb9dcffff")

request = requests.get(url)
content = request.json()

user_email = "adeel.nariai96@gmail.com"

body = ""

for article in content["articles"]:
    title = article["title"] or "No Title"
    description = article["description"] or "No Description"
    body += title + "\n" + description + "\n\n"


body = body.encode("utf-8")
send_email.send_email(user_email,body)
