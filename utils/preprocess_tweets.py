import pandas as pd
import string
import re
from emot.emo_unicode import UNICODE_EMOJI
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet, stopwords
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def clean_stopwords(tweet):
    stopwords_list = stopwords.words('english')
    return ' '.join(word for word in tweet.split() if word not in stopwords_list)


def clean_url(tweet):
    return re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', ' ', tweet)


def clean_atsigns(tweet):
    return re.sub('@\S*\s?', ' ', tweet)


def clean_punctuation(tweet):
    punctuations_list = string.punctuation
    translator = str.maketrans('', '', punctuations_list)
    return tweet.translate(translator)


def clean_numbers(tweet):
    return re.sub('[0-9]+', '', tweet)


def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def pos_lemma_tweet(tweet):
    lemmatizer = nltk.stem.WordNetLemmatizer()

    tokens = word_tokenize(tweet)
    pos_tags = nltk.pos_tag(tokens)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), pos_tags)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            # if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            # else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return ' '.join(lemmatized_sentence)


pos_lemma_tweet('doing craziest I')


def remove_searched_hashtag(tweet, hashtag):
    return ' '.join(word for word in tweet.split() if word != hashtag[1:].lower())


def convert_emojis(tweet):
    for emot in UNICODE_EMOJI:
        tweet = tweet.replace(emot, " ".join(UNICODE_EMOJI[emot].replace(",", "").replace(":", "").split()))
    return tweet


def preprocess_pipeline(tweets: pd.Series, hashtag: str):
    tweets = tweets.str.lower()
    tweets = tweets.apply(lambda t: clean_stopwords(t))
    tweets = tweets.apply(lambda t: clean_url(t))
    tweets = tweets.apply(lambda t: clean_atsigns(t))
    tweets = tweets.apply(lambda t: clean_punctuation(t))
    tweets = tweets.apply(lambda t: clean_numbers(t))
    tweets = tweets.apply(lambda t: pos_lemma_tweet(t))
    tweets = tweets.apply(lambda t: remove_searched_hashtag(t, hashtag))
    tweets = tweets.apply(lambda t: convert_emojis(t))
    return tweets


def combine_all_tweets(df):
    return ' '.join(
        row.preprocessed_tweets + ' '
        for idx, row in df.iterrows()
    )
