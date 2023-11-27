import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Which teams are the best at shout outs? Do teams with stronger goalkeepers win more at shout outs? Are these teams amongst the best teams in general? (personal question)

df = pd.read_csv('data/fifa_world_cup.csv')
df = df.dropna()

# Extract games that went to shootout
shootout_df = df[df['shoot_out'] == 'Yes'].copy()

# Determine shootout winners and their FIFA ranks and goalkeeper scores
shootout_df['winning_team'] = shootout_df.apply(
    lambda row: row['home_team'] if row['home_team_score'] > row['away_team_score'] else row['away_team'], axis=1
)
shootout_df['fifa_score'] = shootout_df.apply(
    lambda row: row['home_team_fifa_rank'] if row['home_team_score'] > row['away_team_score'] else row['away_team_fifa_rank'], axis=1
)
shootout_df['gk_score'] = shootout_df.apply(
    lambda row: row['home_team_goalkeeper_score'] if row['winning_team'] == row['home_team'] else row['away_team_goalkeeper_score'], axis=1
)

# Calculate win counts for each team
shootout_wins = shootout_df['winning_team'].value_counts()

# Calculate average FIFA rank and goalkeeper score for each team
team_averages = shootout_df.groupby('winning_team').agg({'fifa_score': 'mean', 'gk_score': 'mean'}).reset_index()

# Merge win counts with averages
final_df = pd.merge(shootout_wins.reset_index().rename(columns={'index': 'winning_team', 'winning_team': 'win_count'}), team_averages, on='winning_team')

# Plotting the top 10 teams with most shootout wins
top_10_teams = final_df.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='winning_team', y='win_count', data=top_10_teams)
plt.xticks(rotation=45)
plt.title('Top 10 Teams with Most Shootout Wins')
plt.xlabel('Team')
plt.ylabel('Wins')
plt.show()

# Plotting the correlation between win counts and average goalkeeper scores
plt.figure(figsize=(10, 6))
sns.regplot(x='win_count', y='gk_score', data=final_df, scatter_kws={'s': 50})
plt.title('Correlation between Shootout Wins and Average Goalkeeper Scores')
plt.xlabel('Number of Shootout Wins')
plt.ylabel('Average Goalkeeper Score')
plt.show()

# Bar plot for the number of shootout wins
fig, ax1 = plt.subplots(figsize=(12, 8))
color = 'tab:blue'
ax1.set_xlabel('Team')
ax1.set_ylabel('Number of Shootout Wins', color=color)
ax1.bar(top_10_teams['winning_team'], top_10_teams['win_count'], color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=45)
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Average FIFA Ranking', color=color)  
ax2.plot(top_10_teams['winning_team'], top_10_teams['fifa_score'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)
ax2.invert_yaxis()
plt.title('Top 10 Teams: Shootout Wins vs Average FIFA Ranking')
plt.show()