from turtle import position
from sentiment import generate_sentiment_scores
import pandas as pd
from nltk_install import nltk_install

nltk_install()

positions = ['QB', 'RB', 'WR', 'TE']

df = pd.DataFrame()

for p in positions:
    data = generate_sentiment_scores(p, 20)
    pos_df = pd.DataFrame(data)
    pos_df = pos_df.transpose()
    pos_df['Pos'] = p

    df = pd.concat([df, pos_df])

df.to_csv('data/sentiment.csv')