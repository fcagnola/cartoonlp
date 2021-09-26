import pandas as pd
import pickle
from pprint import pprint

with open("texts.pickle", "rb") as fp:
    data = pickle.load(fp)

df = pd.DataFrame.from_dict(data, orient='index', columns=["Year", "Text"])

print(df.head(59))