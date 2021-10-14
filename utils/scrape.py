import pandas as pd
import twint
import nest_asyncio
import asyncio

def scrape_twitter_for_hashtag(hashtag):
    c = twint.Config()
    c.Lang = 'en'
    c.Limit = 50
    c.Search = hashtag
    c.Pandas = True
    c.Hide_output = True
    # nest_asyncio.apply()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print('before search')
    twint.run.Search(c)
    print('after search')
    # tweet_list = c.search_tweet_list
    scraped_tweets = twint.storage.panda.Tweets_df
    scraped_tweets = scraped_tweets[scraped_tweets.language == 'en']
    scraped_tweets.reset_index(drop=True, inplace=True)
    # scraped_tweets = pd.DataFrame({'tweet':tweet_list})
    print('after reset_index')
    return scraped_tweets