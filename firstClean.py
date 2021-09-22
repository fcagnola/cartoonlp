import pysrt
import pickle
import re
import os
import string

#print(string.punctuation)

allowed_char = string.ascii_letters + string.digits + " " + "'"
# path = "subs/"
# for filename in os.listdir(os.curdir):
#     print(filename)
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
    """ 
    Turn subtitle files in object:
    {"movie_name_YEAR": ["text"], ...}
    """
    subs_directory = "subs/"
    final_object = {}
    for file in os.listdir("./subs")[:1]:

        # Parse .srt file for easier handling
        srt  = pysrt.open(subs_directory + file)

        # Remove html tags, dashes (dialogues), returns and punctuation
        remove_html = re.sub(re.compile("<[\/]?\w*>"), " ", srt.text)
        remove_dashes = re.sub(re.compile("-\s"), " ", remove_html)
        remove_returns = re.sub(re.compile("[\r\t\n]"), " ", remove_dashes)
        allowed_chars = string.ascii_letters + " " + "'" + "-"
        remove_punctuation = "".join([char for char in remove_returns if char in allowed_chars])
        remove_double_spaces = re.sub(re.compile("\s+"), " ", remove_punctuation)
        print(remove_double_spaces)
        
        # Turn all words to lowercase

        # Make the whole script a long string by stripping \n \t 



if __name__=='__main__':
    parse_subs()