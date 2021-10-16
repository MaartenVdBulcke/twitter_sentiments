import streamlit as st
import twint


if __name__ != '__main__':
    from utils import variables, preprocess_tweets, predict_sentiment, plotting


def sentiment_analysis(hashtag, stopwords):
    with st.spinner(f"Searching Twitter for {hashtag}"):
        c = twint.Config()
        c.Search = hashtag
        c.Lang = 'en'
        c.Limit = 1000
        c.Pandas = True
        twint.run.Search(c)
        scraped_tweets = twint.storage.panda.Tweets_df
        if len(scraped_tweets)<25:
            st.write('Not enough tweets founds. Please try another hashtag')
        else:
            scraped_tweets_df = scraped_tweets[['date', 'hashtags', 'tweet']]
            scraped_tweets_df['preprocessed_tweets'] = \
                preprocess_tweets.preprocess_pipeline(scraped_tweets_df.tweet, hashtag)
            scraped_tweets_df.drop_duplicates(subset='preprocessed_tweets', keep=False, inplace=True)
            st.success('Finished searching!')

            with st.spinner('Analyzing tweets'):
                scraped_tweets_df['predict_textblob'] = \
                scraped_tweets_df.preprocessed_tweets. \
                    apply(lambda t: predict_sentiment.predict_textblob(t))
            st.success("Done analysing!")

            scraped_tweets_df = plotting.work_dates(scraped_tweets_df)
            st.write('Hover over a tweet to see the full tweet:')
            scraped_tweets_df['sentiment'] = scraped_tweets_df.predict_textblob.replace(variables.replace_dict)
            st.write(scraped_tweets_df[['preprocessed_tweets', 'sentiment']])
            fig_sentiment_distribution = plotting.plot_sentiment_distribution(scraped_tweets_df)
            st.pyplot(fig_sentiment_distribution)

            one_big_tweet = preprocess_tweets.combine_all_tweets(scraped_tweets_df)
            stopwords.update(hashtag[1:])
            fig_wordcloud = plotting.plot_wordcloud(stopwords, one_big_tweet)
            st.pyplot(fig_wordcloud)
