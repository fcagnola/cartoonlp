from typing import List
from bs4 import BeautifulSoup, PageElement
import json
import requests

DISNEY_URI = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films"

response = requests.get(DISNEY_URI)
if response.status_code >= 200:
    with open("disney_titles.html", "r") as fp:
        data = fp.read()
        soup = BeautifulSoup(data, features="lxml")
        rows: List[PageElement] = soup.find_all("tr")
        disney_movies = dict()
        for row in rows:
            disney_movies[row.find_all("td")[0].text.strip("\n")] = {"release_date": row.find_all("td")[1].text.strip("\n").replace(" ", " ")}
        with open("disney_titles.json", "w") as outfile:
            json.dump(disney_movies, outfile)
