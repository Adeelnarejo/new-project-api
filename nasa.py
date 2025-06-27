import requests
import streamlit as st


api_key = "38Xi1DQdWMEUYlOy6tQ7cYdEnTQ9Digdw49fZ9eM"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url).json()


st.title(response["title"])
st.image(response["hdurl"])
st.write(response["explanation"])

# image_file_path = "nasa_image.jpg"
# response2 = requests.get(response["hdurl"])
# with open(image_file_path, "wb") as f:
#     f.write(response2.content)
