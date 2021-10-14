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
    c.Limit = 10000
    c.Pandas = True
    scraped_tweets = twint.storage.panda.Tweets_df
    scraped_tweets = scraped_tweets[scraped_tweets.language == 'en']
    scraped_tweets.reset_index(drop=True, inplace=True)
    st.write('after reset_index')
    return scraped_tweets