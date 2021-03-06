from twitter import generate_tweets
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

WEEKLY_BASE_URL = 'C:/data_v2/weekly/2019/week{}.csv'

def generate_full_season_df():
    df = pd.DataFrame()
    for week in range(1, 18):
        weekly_df = pd.read_csv(WEEKLY_BASE_URL.format(week))
        weekly_df['Week'] = week
        df = pd.concat([df, weekly_df])

    return df

def get_top_n_names(pos, n=20):
    df = generate_full_season_df()
    df = df.loc[df['Pos'] == pos].groupby('Player').sum().sort_values(by='StandardFantasyPoints', ascending=False).head(n).reset_index()
    names = df['Player'].to_list()
    
    formatted_names = []

    for name in names:
        split_name = name.split(' ')
        name_one = name
        name_two = '. '.join([split_name[0][0], split_name[-1]]) #first initial, last name

        formatted_names.append(
            [name_one, name_two]
        )

    return formatted_names

def generate_sentiment_scores(pos, n=20):
    data = dict()
    top_players_at_pos = get_top_n_names(pos, n)
    for player in top_players_at_pos:
        data[player[0]] = {
            'pos': 0,
            'neg': 0,
            'neutral': 0,
            'num_tweets': 0
        }

        tweets = generate_tweets(player)
        sid = SentimentIntensityAnalyzer()
        for tweet in tweets:
            polarity_score = sid.polarity_scores(tweet)
            data[player[0]]['pos'] += polarity_score.get('pos', 0)
            data[player[0]]['neg'] += polarity_score.get('neg', 0)
            data[player[0]]['neutral'] += polarity_score.get('neutral', 0)
            data[player[0]]['num_tweets'] += 1

    return data

print(
    get_top_n_names('QB')
)