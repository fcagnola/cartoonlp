#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple
import json
import subprocess


def get_list_tuples_titles(path: str) -> List[Tuple[str, str]]:
    with open(path, "r") as fp:
        titles = json.load(fp)

        # list of tuples (title, year)
        titles = [(title, titles[title]['year']) for title in titles]

        return titles


if __name__ == '__main__':
    ls = get_list_tuples_titles('disney_titles.json')
    for t in ls:
        filetitle = "_".join(t[0].split(" ")) + f"_{t[1]}"
        print(f"Writing {filetitle} to /titles")
        with open(f"titles/{filetitle}.txt", "w+") as f:
            f.write("")
        
    print("Done.")
        