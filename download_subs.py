#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections.abc import Mapping
import json
import os
import pprint

import requests
from urllib.parse import quote_plus

API_KEY = os.environ["OPENSUBTITLES_API_KEY"]
BASE = "https://api.opensubtitles.com"
SEARCH = "/api/v1/subtitles?type=movie&languages=en&ai_translated=exclude&hearing_impaired=exclude&query="

# Authentication
header = {"Api-Key": API_KEY}

# Step 1: search for subs via API /api/v1/subtitles

def get_list_tuples_titles():
    with open("disney_titles.json", "r") as fp:
        titles = json.load(fp)

        # list of tuples (title, year)
        titles = [(title, titles[title]['year']) for title in titles]

        return titles

def get_download_link(title):
    assert isinstance(title, tuple)

    title, year = title

    encoded_title = quote_plus(title)
    uri = BASE+SEARCH+encoded_title+"&year="+str(year)
    response = requests.get(uri, headers=header)

    if response.status_code >= 200:

        # Check if it behaves like a dict() through collections.abc abstract base class
        if isinstance(response.json(), Mapping):
            pprint.pprint(response.json())

        elif isinstance(response.json(), str):
            data = json.loads(response.json())
            pprint.pprint(data)

        else:
            print(type(response.json()))

    else:
        print(response.status_code, response.json())
