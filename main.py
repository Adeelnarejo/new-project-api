import requests


# api key
api_key = "c25984fdf8c340b3b2c773ecb9dcffff"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-05-27&sortBy=publishedAt&apiKey"
       "=c25984fdf8c340b3b2c773ecb9dcffff")

request = requests.get(url)
content = request.json()


for article in content["articles"]:
    print(article["title"])
    print(article["description"])
