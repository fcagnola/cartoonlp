from typing import List
from bs4 import BeautifulSoup, PageElement
import json
import requests

# Wikipedia page for "Disney Movies"
DISNEY_URI = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films"

# Retrieve the webpage in HTML format
response = requests.get(DISNEY_URI)

if response.status_code >= 200:
    with open("disney_titles.html", "r") as fp:
        data = fp.read()
        # Turn html string into Soup object
        soup = BeautifulSoup(data, features="lxml")
        # retrieve all table rows containing movie titles
        rows: List[PageElement] = soup.find_all("tr")

        disney_movies = dict()
        # Find first td element (title) and second td element (year) and aggregate in dict object
        for row in rows:
            disney_movies[row.find_all("td")[0].text.strip("\n")] = {"release_date": row.find_all("td")[1].text.strip("\n").replace(" ", " ")}
        
        # Save dict as disney_titles.json
        with open("disney_titles.json", "w") as outfile:
            json.dump(disney_movies, outfile)
