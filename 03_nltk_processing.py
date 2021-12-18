from string import punctuation
from typing import List

from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import pickle
from pprint import pprint
from spacy.lang.en.stop_words import STOP_WORDS
from spacytextblob.spacytextblob import SpacyTextBlob

with open("02_out_texts.pickle", "rb") as fp:
    data = pickle.load(fp)

df = pd.DataFrame.from_dict(data, orient='index', columns=["Year", "Text"])
# Dataframe: 
# title - year - text


def sentence_tokenize(txt: str) -> List[str]:
    """Tokenize sentences: split text into sentences"""
    text = sent_tokenize(txt)
    return text

def tokenize_and_remove_stopwords(txt: str):
    """Basic tokenisation function with stopwords removal"""
    tokenized = word_tokenize(txt)
    stripped_lower = [word.lower() for word in tokenized if word not in STOP_WORDS and word not in punctuation]
    return stripped_lower

df['Sentence_Tokenized'] = df['Text'].apply(lambda x: sent_tokenize(x))
df['Tokenized'] = df['Text'].apply(lambda x: tokenize_and_remove_stopwords(x))
# Dataframe: 
# title - year - text - sentence tokenized - tokenized


#print(df.head(59))
#df.to_pickle("03_out_dataframe.pickle")
df.to_csv("03_out_dataframe.csv")

# print(df['Tokenized'].iloc[1])
# print(df['Sentence_Tokenized'])
# df['length'] = df["Sentence_Tokenized"].apply(lambda x: len(x))
# print(df['length'])
