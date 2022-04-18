from twitter import generate_tweets
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

WEEKLY_BASE_URL = '../data/weekly/2019/week{}.csv'

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


print(
    get_top_n_names('QB')
)