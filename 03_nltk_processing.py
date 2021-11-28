from string import punctuation

from nltk import tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import pickle
from pprint import pprint
from spacy.lang.en.stop_words import STOP_WORDS
from typing import List
# from spacytextblob.spacytextblob import SpacyTextBlob

with open("texts.pickle", "rb") as fp:
    data = pickle.load(fp)

df = pd.DataFrame.from_dict(data, orient='index', columns=["Year", "Text"])
# Dataframe: 
# title - year - text

print(df.head(59))

def sentence_tokenize(txt: str) -> List[str]:
    """Tokenize sentences: split text into sentences"""
    text = sent_tokenize(txt)
    return text

def tokenize_and_remove_stopwords(txt: List[str]):
    """Basic tokenisation function with stopwords removal"""
    out = []
    for sentence in txt:
        tokenized = word_tokenize(sentence)
        sentence = [word for word in tokenized if word not in STOP_WORDS and word not in punctuation]
        out.append(sentence)
    return out

# df['Sentence_Tokenized'] = df['Text'].apply(lambda x: sent_tokenize(x))
# df['Tokenized'] = df['Sentence_Tokenized'].apply(lambda x: tokenize_and_remove_stopwords(x))
# Dataframe: 
# title - year - text - sentence tokenized - tokenized


# print(df.head(59))
# print(df['Tokenized'].iloc[1])
# print(df['Sentence_Tokenized'])
# df['length'] = df["Sentence_Tokenized"].apply(lambda x: len(x))
# print(df['length'])
