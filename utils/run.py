import streamlit as st

if __name__ != '__main__':
    from utils import variables, scrape, preprocess_tweets, predict_sentiment, plotting


def sentiment_analysis(hashtag, stopwords, flair_model):
    st.write(variables.waiting_message)

    scraped_tweets = scrape.scrape_twitter_for_hashtag(hashtag)
    scraped_tweets_df = scraped_tweets[['date', 'hashtags', 'tweet']]

    scraped_tweets_df['preprocessed_tweets'] = \
        preprocess_tweets.preprocess_pipeline(scraped_tweets_df.tweet, hashtag)
    scraped_tweets_df.drop_duplicates(subset='preprocessed_tweets', keep=False, inplace=True)

    scraped_tweets_df['predict_flair'] = \
        scraped_tweets_df.preprocessed_tweets. \
            apply(lambda t: predict_sentiment.predict_flair(t, flair_model))

    scraped_tweets_df = plotting.work_dates(scraped_tweets_df)
    fig_sentiment_distribution = plotting.plot_sentiment_distribution(scraped_tweets_df)
    # buf, col0, buff = st.columns((1, 4, 1))
    # col0.pyplot(fig_sentiment_distribution)
    st.pyplot(fig_sentiment_distribution)

    one_big_tweet = preprocess_tweets.combine_all_tweets(scraped_tweets_df)
    stopwords.update(hashtag[1:])
    fig_wordcloud = plotting.plot_wordcloud(stopwords, one_big_tweet)
    # col0.pyplot(fig_wordcloud)
    st.pyplot(fig_wordcloud)
