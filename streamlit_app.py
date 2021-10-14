import streamlit as st
from utils import variables, run, setup

st.set_page_config(page_title=variables.pagetitle, layout="centered")
hide_st_style = """ <style> footer {visibility: hidden;} </style> """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header(variables.header)
st.subheader(variables.subheader)

nlp, all_stopwords, flair_sentiment = setup.nlp_setup()    # setup spacy and flair

user_input = st.text_input("", '#')

if user_input is not None:
    if user_input =='#':
        pass
    elif user_input=='' or len(user_input)==1:
        st.write(variables.error_message_hashtag_format_one)
    else:
        hashtag = user_input.strip()
        if not hashtag[1:].isalnum():
            st.write(variables.error_message_hashtag_format_two)
        else:
            run.sentiment_analysis(hashtag, all_stopwords, flair_sentiment)
