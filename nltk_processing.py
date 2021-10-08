from nltk import tokenize
from nltk.tokenize import word_tokenize
import pandas as pd
import pickle
from pprint import pprint
from spacy.lang.en.stop_words import STOP_WORDS
# from spacytextblob.spacytextblob import SpacyTextBlob

with open("texts.pickle", "rb") as fp:
    data = pickle.load(fp)

df = pd.DataFrame.from_dict(data, orient='index', columns=["Year", "Text"])

def tokenize_and_remove_stopwords(txt):
    text = word_tokenize(txt)
    text = " ".join([word for word in text if word not in STOP_WORDS])
    return text
df['tokenized'] = df['Text'].apply(lambda x: tokenize_and_remove_stopwords(x))

print(df.head(59))