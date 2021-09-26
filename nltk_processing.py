import pickle
from pprint import pprint

with open("texts.pickle", "rb") as fp:
    data = pickle.load(fp)

for key in data.keys():
    pprint(key)
print(len(data.keys()))