#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
scores = soup.find_all(name="span", class_="score")
article_texts = [text.getText() for text in articles]
article_links = [link.get("href") for link in articles]
article_scores = [int(score.getText().split()[0]) for score in scores]
max_index = article_scores.index(max(article_scores))

print(article_texts[max_index + 1])
print(article_links[max_index + 1])
print(article_scores[max_index])

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
# heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)
