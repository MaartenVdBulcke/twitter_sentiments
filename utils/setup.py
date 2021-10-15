import spacy


def nlp_setup():
    nlp = spacy.load('en_core_web_md')
    all_stopwords = nlp.Defaults.stop_words
    return nlp, all_stopwords

