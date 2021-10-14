# import flair
import spacy


def nlp_setup():
    nlp = spacy.load('en_core_web_md')
    all_stopwords = nlp.Defaults.stop_words
    # flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
    return nlp, all_stopwords  #, flair_sentiment

