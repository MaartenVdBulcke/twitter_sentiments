import streamlit as st
import pandas as pd
import twint
import os
import asyncio


def load_tweet(hashtag):
  result_loc = 'tweets.csv'
  c = twint.Config()
  c.Search = hashtag
  c.Limit = 1000
  c.Lang = 'en'
  c.Output = result_loc
  c.Store_csv = True
  asyncio.set_event_loop(asyncio.new_event_loop())
  twint.run.Search(c)
  st.write('after search load')
  df = pd.read_csv(result_loc)
  os.remove(result_loc)
  return df


def scrape_twitter_for_hashtag(hashtag):
    c = twint.Config()
    c.Search = hashtag
    c.Lang = 'en'
    c.Limit = 5000
    c.Pandas = True
    # c.Store_csv = True
    # c.Output = 'tweets.csv'
    # c.Hide_output = True
    # nest_asyncio.apply()
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # asyncio.set_event_loop(asyncio.new_event_loop())
    # st.write('before search')
    # twint.run.Search(c)
    # st.write('after search')
    # tweet_list = c.search_tweet_list
    scraped_tweets = twint.storage.panda.Tweets_df
    # st.write(scraped_tweets)
    scraped_tweets = scraped_tweets[scraped_tweets.language == 'en']
    scraped_tweets.reset_index(drop=True, inplace=True)
    # scraped_tweets = pd.DataFrame({'tweet':tweet_list})
    st.write('after reset_index')
    return scraped_tweets