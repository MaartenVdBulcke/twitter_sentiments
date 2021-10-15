import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


def get_labels(unique_labels: list) -> list:
    if len(unique_labels)==3:
        return ['unknown', 'negative', 'positive']
    elif len(unique_labels)==2:
        return ['negative', 'positive']


def plot_sentiment_distribution(scraped_tweets_df):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.title.set_fontsize(35)
    ax.title.set_color('white')
    ax.spines[['top', 'right', ]].set_visible(False)
    ax.spines[['left', 'bottom']].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    fig.patch.set_alpha(1.0)
    fig.set_facecolor('#1DA1F2')
    ax.set_facecolor('#E1E8ED')
    ax.patch.set_alpha(1.0)

    y_axis = [pd.to_datetime(day).date() for day in scraped_tweets_df.date.unique()]
    sp = sns.countplot(y='date', data=scraped_tweets_df,
                       hue='predict_textblob',
                       palette='Set1',
                       orient='horizontal'
                       )
    labels = get_labels(scraped_tweets_df.predict_textblob.unique())

    leg = plt.legend(title='Sentiment', loc='lower right', bbox_to_anchor=[1.3,-.1],
               labels=labels, facecolor='#1DA1F2')
    for text in leg.get_texts():
        text.set_color('white')
    plt.setp(leg.get_title(), color='white')
    plt.title('SENTIMENT DISTRIBUTION BY DAY', fontsize=30)
    ax.set_ylabel('')
    ax.set_xlabel('count', fontsize=13, color='white')
    sp.set_yticklabels(y_axis, fontsize=13)
    return fig


def work_dates(df):
    df['date'] = df['date'].astype('datetime64[D]')
    return df


def plot_wordcloud(stopwords, text):
    wordcloud = WordCloud(width=400, height=100, margin=1,
                          min_word_length=5, background_color="white",
                          stopwords=stopwords, max_words=50, colormap='Set1')\
                .generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return fig
