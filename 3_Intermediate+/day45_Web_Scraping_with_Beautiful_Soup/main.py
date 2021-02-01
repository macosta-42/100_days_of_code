#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
films = soup.find_all(name="h3", class_="title")
film_titles = [text.getText() for text in films]
with open("top_100.txt", "w") as file:
    for film in reversed(film_titles):
        file.write(f"{film}\n")
