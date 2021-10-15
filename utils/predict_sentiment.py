from textblob import TextBlob


def predict_textblob(tweet):
    polarity = TextBlob(tweet).sentiment.polarity
    if polarity > 0:
        return 1
    else:
        return 0
