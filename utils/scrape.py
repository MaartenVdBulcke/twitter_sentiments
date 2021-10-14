import pandas as pd
import twint
import asyncio

async def test():
    await asyncio.sleep(1)

asyncio.set_event_loop(None)      # Clear the main loop.
loop = asyncio.new_event_loop()   # Create a new loop.
loop.run_until_complete(test())


def scrape_twitter_for_hashtag(hashtag):
    c = twint.Config()
    c.Lang = 'en'
    c.Limit = 50
    c.Search = hashtag
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)
    # tweet_list = c.search_tweet_list
    scraped_tweets = twint.storage.panda.Tweets_df
    scraped_tweets = scraped_tweets[scraped_tweets.language == 'en']
    scraped_tweets.reset_index(drop=True, inplace=True)
    # scraped_tweets = pd.DataFrame({'tweet':tweet_list})
    return scraped_tweets