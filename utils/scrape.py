import twint


def scrape_twitter_for_hashtag(hashtag):
    c = twint.Config()
    c.Lang = 'en'
    c.Limit = 50
    c.Search = hashtag
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)
    scraped_tweets = twint.storage.panda.Tweets_df
    scraped_tweets = scraped_tweets[scraped_tweets.language == 'en']
    scraped_tweets.reset_index(drop=True, inplace=True)
    return scraped_tweets