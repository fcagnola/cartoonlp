
from nltk.tokenize import word_tokenize
import spacy
import os.path 
import nltk
from nltk.stem import 	WordNetLemmatizer
import re


NER = spacy.load("en_core_web_sm")
path = "nn_txts/"
for file in os.listdir("./txts"):
    with open("./txts/"+file, "r")  as new_file:
        text = new_file.read()
        stripped_text = []
       # print(text) 
        parsed = NER(text)
        for word in parsed.ents:
            if word.label_ == "PERSON" or word.label_ == "ORG":
                text = text.replace(str(word), "")
        tokens = word_tokenize(text)
        
        tagged = nltk.pos_tag(tokens)
        for word, tag in tagged:
            
            if tag == 'NN' and len(word)>4:
                #print("log")
                #print(word, tag)
                stripped_text.append(word)

        #print(stripped_text)
        for word in stripped_text:
            #print('loop')
            if re.search(r"\w+[']\w+?",word):
                
                stripped_text.remove(str(word))
                print('removed')


        
        new_string=" ".join(str(x) for x in stripped_text)
       
        #print(lemma)
       
        out_file=open(path+file,"w")
        out_file.write(new_string)
        out_file.close()
        
        """ csvreader = csv.reader(file)
            for row in csvreader:
                text = row[2]
                
                title = row [0]
                print(title)

                parsed = NER(text)
                print(text)
                for word in parsed.ents:
                    if word.label_ == "PERSON" or word.label_ == "ORG":
                        text = text.replace(str(word), "")
                text = word_tokenize(text)


                out_file=open(path+title+".txt","w")
                out_file.write(text)
                out_file.close()  """

