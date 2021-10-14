import flair


def predict_flair(tweet, flair_sentiment):
    s = flair.data.Sentence(tweet)
    flair_sentiment.predict(s)
    total_sentiment = s.labels
    if len(total_sentiment) < 1:
        return -1
    string_sentiment = str(total_sentiment[0])
    if string_sentiment.startswith('POSITIVE'):
        return 1
    else:
        return 0