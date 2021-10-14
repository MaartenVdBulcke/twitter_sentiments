import streamlit as st
import nltk

pagetitle = 'hashtag sentiment analysis'

st.set_page_config(page_title=pagetitle, layout="centered")
@st.cache
def download_nltk():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')
download_nltk()

header = 'SENTIMENT ANALYSIS ON TWITTER HASHTAGS'
subheader = 'Analyse the sentiment of the hashtag of your interest.'

error_message_hashtag_format_one = 'You call this a hashtag?! Try to start with \'#\' and put some letters after...'

error_message_hashtag_format_two = 'write a hashtag that starts with \'#\' and contains only letters and numbers.' \
                                   ' No blanks allowed...'

waiting_message= 'NLP is short for Natural Language Processing. It is a extremly powerful tool' \
                 ' with which we can estimate the feelings a twitterer had when writing a tweet.' \
                 ' While we analyse the Twitter sentiment of your hashtag, we recommend you to' \
                 ' grab a drink, come sit by our side and let the world slip. Because this can take' \
                 ' a while. And you shall never be younger.'