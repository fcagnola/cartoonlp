import pysrt
import re
import os
import string

#print(string.punctuation)

allowed_char = string.ascii_letters + string.digits + " " + "'"
path = "subs/"
for filename in os.listdir(os.curdir):
    print(filename)
    # if re.match(".*"+".srt", filename):
    #     print(filename)
    #
    #     subs = pysrt.open(path+filename)
    #     document = []
    #     for sub in subs:
    #         raw_string = sub.text
    #         clean = re.sub("<.*>","", raw_string)
    #         #print(clean)
    #         for c in clean:
    #             if c not in allowed_char:
    #                 clean = clean.replace( c , "" )
    #         #print(raw_string)
    #         words_list= clean.split(" ")
    #         #print(words_list)
    #         for w in words_list:
    #             w = w.lower()
    #             if (w != ''):
    #         #print(raw_string)
    #                 document.append(w)

        #print(filename, document)


def parse_subs() -> str:
    subs_directory= "subs/"
    for file in os.listdir("/subs"):
         = pysrt.open(subs_directory + filename)

    print(file)