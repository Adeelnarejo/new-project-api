import requests

url = "https://api.nasa.gov/assets/img/general/apod.jpg"

response = requests.get(url)

with open("nasa.jpg", "wb") as file:
    file.write(response.content)

print("Image downloaded successfully!")
