import pysrt
import pickle
import re
import os
import string


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
            opensubs_ads = r'(Advertise your product or brand here)|(contact www\.OpenSubtitles\.(org|com) today)|(Support us and become VIP member)|(to remove all ads from www\.OpenSubtitles\.(org|com))|(-== \[ www\.OpenSubtitles\.(org|com) \] ==-)|((((Subtitles by )|(Sync by ))(.+))$)|(font color="(.+)?")|(Provided by(.+)$)|(^(https?):\/\/[^\s\/$.?#].[^\s]*$)'
            remove_ads = re.sub(re.compile(opensubs_ads), "", srt.text)
            # Remove html tags, dashes (dialogues), returns and punctuation
            remove_curly = re.sub(re.compile(r"\{.*?\}"), "", remove_ads)
            remove_html = re.sub(re.compile(r"((<[^>]+>)+)"), " ", remove_curly)
            remove_html_closing = re.sub(re.compile(r"((<\/[^>]+>)+)"), " ", remove_html)
            remove_dashes = re.sub(re.compile(r"-\s"), " ", remove_html_closing)
            remove_returns = re.sub(re.compile(r"[\r\t\n]"), " ", remove_dashes)
            # allowed_chars = string.ascii_letters + " " + "'" + "-" + "."
            # remove_punctuation_lowercase = "".join([char.lower() for char in remove_returns if char in allowed_chars])
            remove_double_spaces = re.sub(re.compile(r"(\s+)"), " ", remove_returns)
            remove_starting_spaces = re.sub(re.compile(r"(^\s)"), "", remove_double_spaces)
            year = file.split("_")[-1].strip(".srt")
            title = "_".join(file.split("_")[:-1])

            final_object[title] = [year, remove_starting_spaces]

    return final_object 



if __name__=='__main__':
    data = parse_subs()
    with open("texts.pickle", "wb") as f:
        pickle.dump(data, f)
