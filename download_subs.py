#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections.abc import Mapping
import json
import os
import pprint
import pickle
import random
from typing import Tuple, List

import requests
from urllib.parse import quote_plus

API_KEY = os.environ["OPENSUBTITLES_API_KEY"]
BASE = "https://api.opensubtitles.com"
SEARCH = "/api/v1/subtitles?type=movie&languages=en&ai_translated=exclude&hearing_impaired=exclude&query="

# Authentication

# Step 1: search for subs via API /api/v1/subtitles

def get_list_tuples_titles(path: str) -> List[ Tuple[str, str] ]:
    with open(path, "r") as fp:
        titles = json.load(fp)

        # list of tuples (title, year)
        titles = [(title, titles[title]['year']) for title in titles]

        return titles


def get_proxy() -> Tuple[str, str]:
    PATH = 'proxies.pickle'
    with open(PATH, "rb") as fp:
        obj = pickle.load(fp)
        proxy = random.choice(obj['proxies'])
        return proxy
        
def get_subtitles():
    titles: List = get_list_tuples_titles("disney_titles.json")

    # Loop through titles
    for title in titles:
        # use a new IP address each time to avoid API limiting
        ip, port = get_proxy()
        proxies = {"https": "http://"+ip+":"+port}
        # set the correct auth header
        # header = {"Api-Key": API_KEY}
        movie_title, year = title
        encoded_title = quote_plus(movie_title)
        uri = BASE+SEARCH+encoded_title+"&year="+str(year)
        response = requests.get(uri, proxies=proxies)

        if response.status_code == 200: # successful request
            # Check if it behaves like a dict() through collections.abc abstract base class
            print(f"Successful fetch: {movie_title}. [Proxy {ip}]")
            add_sub_to_json(response.json())

        else:  # failed request
            print(f"Failed fetch: {movie_title}. [Proxy {ip}]")
            print(response.status_code, response.json())


def add_sub_to_json(json: str):
    with open('opensubs_response.json', "a") as fp:
        json.dump(json, fp)
    




get_subtitles()