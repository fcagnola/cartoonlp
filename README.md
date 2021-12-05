# CartooNLP

_Introduction_

The reason behind the choice of our subject is a deep fascination for the imaginary worlds crafted by Disney Pixar and for the language used in the company's motion pictures. Since these movies, ranging from classic to contemporary, span almost a hundred years, it was also the perfect opportunity to study chilren-centric language from a **diachronic** point of view. The challenge mainly consisted in the normalization and treatment of such orally-bound and children-specific language in such a way that could allow us to gather meaningful insight.

_Scope_

When we took up the project we chose to include in the study any and all motion pictures from Disney Pixar studios up until that moment. When this choice was made, 59 movies had been created and distributed, and were therefore included, from 1937 to 2021.

_Methodology_

1.  Data gathering:
    file: titles_scraper.py
    We scraped the movie titles from the wikipedia page using BeautifulSoup for Python. With this data we generated a json file for easier handling in the format
    '''{"Title": {"year": YYYY}, ...}'''
    In order to download the english subtitles for the movies we had listed we turned to an existing project called OpenSubtitlesDownload https://github.com/emericg/OpenSubtitlesDownload. Since the script runs in a folder and looks for video files, we generated dummy files with the name of the movie and the extension .mp4. After running the script and inserting opensubtitles credentials, our folder was populated with the desired english subtitle files, which are stored in the /subs folder in this repository.

2.  Data cleaning
    file: first_clean.py
    Removed "html-like" tags, parsed .srt files and removed noise, created object containing all movies and texts in format
    {"movie_name_YEAR": ["text"], ...}
    output was pickled for easier processing and saved as texts.pickle

3.  Tokenization and Dataframe
    file: nltk*processing.py
    We imported the pickled texts, built a pandas dataframe to benefit from vectorized operations in the format:
    \_Title - Year - Text*
    Through pandas' apply function we created a new column of the tokenized text for all movies, and while applying nltk's tokenizer we also filtered out all stopwords.
    The final output of this step is a new dataframe in the format:
    _Title - Year - Text - Tokenized_
