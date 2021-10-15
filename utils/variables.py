import streamlit as st
import nltk

pagetitle = 'BLUE SENTIMENTS'
icon = 'blue_heart'
st.set_page_config(page_title=pagetitle, layout="centered", page_icon=icon)


@st.cache
def download_nltk():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')


download_nltk()

header = 'BLUE SENTIMENTS'
subheader = 'Twitter sentiment analysis'

error_message_hashtag_format_one = 'You call this a hashtag?! Try to start with \'#\' and put some letters after...'

error_message_hashtag_format_two = 'write a hashtag that starts with \'#\' and contains only letters and numbers.' \
                                   ' No blanks allowed...'

replace_dict = {0: 'negative', 1: 'positive'}