import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Do teams with stronger offense players score more goals? And do teams with stronger goalkeepers receive fewer goals? (suggested question)

df = pd.read_csv('data/fifa_world_cup.csv')
df = df.dropna()

# Calculate correlation between home/away team's offensive strength and goals scored
home_offense_corr = df['home_team_mean_offense_score'].corr(df['home_team_score'])
away_offense_corr = df['away_team_mean_offense_score'].corr(df['away_team_score'])

print(f"Home Team Offense to Goals Scored Correlation: {home_offense_corr:.4f}")
print(f"Away Team Offense to Goals Scored Correlation: {away_offense_corr:.4f}")
print("We can notice a POSITIVE correlation, which means teams with stronger offensive players score MORE goals.\n")

# Calculate correlation between home/away team's goalkeeper strength and goals conceded
home_gk_corr = df['home_team_goalkeeper_score'].corr(df['away_team_score'])
away_gk_corr = df['away_team_goalkeeper_score'].corr(df['home_team_score'])

print(f"Home Team Goalkeeper to Goals Conceded Correlation: {home_gk_corr:.4f}")
print(f"Away Team Goalkeeper to Goals Conceded Correlation: {away_gk_corr:.4f}")
print("We can notice a NEGATIVE correlation, which means teams with stronger goalkeepers receive FEWER goals.")

# Create a figure with 2 rows and 2 columns of subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Home Team Offensive Strength vs Goals Scored
scatter1 = axs[0, 0].scatter(df['home_team_mean_offense_score'], df['home_team_score'], 
                             c=df['home_team_mean_offense_score'], cmap='Oranges')
plt.colorbar(scatter1, ax=axs[0, 0], label='Home Team Offensive Score')
sns.regplot(x='home_team_mean_offense_score', y='home_team_score', data=df, ax=axs[0, 0], scatter=False, color='darkblue')
axs[0, 0].set_xlabel('Home Team Mean Offense Score')
axs[0, 0].set_ylabel('Home Team Score')
axs[0, 0].set_title('Home Team Offensive Strength vs Goals Scored')

# Away Team Offensive Strength vs Goals Scored
scatter2 = axs[0, 1].scatter(df['away_team_mean_offense_score'], df['away_team_score'], 
                             c=df['away_team_mean_offense_score'], cmap='Oranges')
plt.colorbar(scatter2, ax=axs[0, 1], label='Away Team Offensive Score')
sns.regplot(x='away_team_mean_offense_score', y='away_team_score', data=df, ax=axs[0, 1], scatter=False, color='darkblue')
axs[0, 1].set_xlabel('Away Team Mean Offense Score')
axs[0, 1].set_ylabel('Away Team Score')
axs[0, 1].set_title('Away Team Offensive Strength vs Goals Scored')

# Home Team Goalkeeper Strength vs Goals Conceded
scatter3 = axs[1, 0].scatter(df['home_team_goalkeeper_score'], df['away_team_score'], 
                             c=df['home_team_goalkeeper_score'], cmap='Greens')
plt.colorbar(scatter3, ax=axs[1, 0], label='Home Team Goalkeeper Score')
sns.regplot(x='home_team_goalkeeper_score', y='away_team_score', data=df, ax=axs[1, 0], scatter=False, color='darkred')
axs[1, 0].set_xlabel('Home Team Goalkeeper Score')
axs[1, 0].set_ylabel('Away Team Score')
axs[1, 0].set_title('Home Team Goalkeeper Strength vs Goals Conceded')

# Away Team Goalkeeper Strength vs Goals Conceded
scatter4 = axs[1, 1].scatter(df['away_team_goalkeeper_score'], df['home_team_score'], 
                             c=df['away_team_goalkeeper_score'], cmap='Greens')
plt.colorbar(scatter4, ax=axs[1, 1], label='Away Team Goalkeeper Score')
sns.regplot(x='away_team_goalkeeper_score', y='home_team_score', data=df, ax=axs[1, 1], scatter=False, color='darkred')
axs[1, 1].set_xlabel('Away Goalkeeper Score')
axs[1, 1].set_ylabel('Home Team Score')
axs[1, 1].set_title('Away Team Goalkeeper Strength vs Goals Conceded')

plt.tight_layout()
plt.show()