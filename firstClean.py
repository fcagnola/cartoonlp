import pysrt
import pickle
import re
import os
import string

allowed_char = string.ascii_letters + string.digits + " " + "'"

def parse_subs() -> str:
    """ 
    Turn subtitle files in object:
    {"movie_name_YEAR": ["text"], ...}
    """
    subs_directory = "subs/"
    final_object = {}
    for file in os.listdir("./subs"):
        if file != ".DS_Store":
        # Parse .srt file for easier handling
            try:
                srt  = pysrt.open(subs_directory + file)
            except UnicodeDecodeError:
                print(f"Error handling file: {file}\nSkipping...")

            # Remove opensubtitles ads and intro:
            opensubs_ads = r"(Advertise your product or brand here)|(contact www\.OpenSubtitles\.org today)|(Support us and become VIP member )|(to remove all ads from www.OpenSubtitles.org)"
            remove_ads = re.sub(re.compile(opensubs_ads), "", srt.text)
            # Remove html tags, dashes (dialogues), returns and punctuation
            remove_html = re.sub(re.compile(r"<[\/]?\w*>"), " ", remove_ads)
            remove_dashes = re.sub(re.compile(r"-\s"), " ", remove_html)
            remove_returns = re.sub(re.compile(r"[\r\t\n]"), " ", remove_dashes)
            allowed_chars = string.ascii_letters + " " + "'" + "-"
            remove_punctuation_lowercase = "".join([char.lower() for char in remove_returns if char in allowed_chars])
            remove_double_spaces = re.sub(re.compile(r"\\s+"), " ", remove_punctuation_lowercase)
            
            final_object[file] = remove_double_spaces

    return final_object 



if __name__=='__main__':
    data = parse_subs()
    with open("texts.pickle", "wb") as f:
        pickle.dump(data, f)
