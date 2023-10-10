import pandas as pd
import numpy as np

df = pd.read_csv('/Users/jules/Desktop/work/sfsu/DS311/DS311-Football-TeamProject/data/fifa_world_cup.csv')

array = np.unique(df[['home_team', 'away_team']].values)

print(f'There are {array.size} unique countries in the list.')


goal_sum = df['home_team_score'].sum() + df['away_team_score'].sum()

print(f'Total goal scored: {goal_sum}!')

average = goal_sum / 30

print(f'That is an average of {average} goals per year.')


df['date'] = pd.to_datetime(df['date'])

earliest = df['date'].min()

print(f'The first entry for the dataset is {earliest}.')