import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Do teams with stronger offense players score more goals? And do teams with stronger goalkeepers receive fewer goals? (suggested question)

df = pd.read_csv('data/fifa_world_cup.csv')

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

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Home Teams
# Scatter plot with a color gradient based on team strength
scatter1 = axs[0].scatter(df['home_team_mean_offense_score'], df['home_team_score'], 
                          c=df['home_team_mean_offense_score'], cmap='coolwarm')
plt.colorbar(scatter1, ax=axs[0], label='Home Team Strength')
# Regression line
sns.regplot(x='home_team_mean_offense_score', y='home_team_score', data=df, ax=axs[0], scatter=False, color='blue')
axs[0].set_xlabel('Home Team Offensive Strength')
axs[0].set_ylabel('Goals Scored by Home Team')
axs[0].set_title('Home Team Offensive Strength vs Goals Scored')

# Away Teams
# Scatter plot with a color gradient based on team strength
scatter2 = axs[1].scatter(df['away_team_mean_offense_score'], df['away_team_score'], 
                          c=df['away_team_mean_offense_score'], cmap='coolwarm')
plt.colorbar(scatter2, ax=axs[1], label='Away Team Strength')
# Regression line
sns.regplot(x='away_team_mean_offense_score', y='away_team_score', data=df, ax=axs[1], scatter=False, color='blue')
axs[1].set_xlabel('Away Team Offensive Strength')
axs[1].set_ylabel('Goals Scored by Away Team')
axs[1].set_title('Away Team Offensive Strength vs Goals Scored')

plt.tight_layout()
plt.show()

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 10))  # 2 rows, 1 column

# Home Team Goalkeepers
# Scatter plot with a color gradient based on goalkeeper strength
scatter1 = axs[0].scatter(df['home_team_goalkeeper_score'], df['away_team_score'], 
                          c=df['home_team_goalkeeper_score'], cmap='coolwarm')
plt.colorbar(scatter1, ax=axs[0], label='Home Team Goalkeeper Strength')
# Regression line
sns.regplot(x='home_team_goalkeeper_score', y='away_team_score', data=df, ax=axs[0], scatter=False, color='red')
axs[0].set_xlabel('Home Team Goalkeeper Strength')
axs[0].set_ylabel('Goals Conceded by Home Team')
axs[0].set_title('Home Team Goalkeeper Strength vs Goals Conceded')

# Away Team Goalkeepers
# Scatter plot with a color gradient based on goalkeeper strength
scatter2 = axs[1].scatter(df['away_team_goalkeeper_score'], df['home_team_score'], 
                          c=df['away_team_goalkeeper_score'], cmap='coolwarm')
plt.colorbar(scatter2, ax=axs[1], label='Away Team Goalkeeper Strength')
# Regression line
sns.regplot(x='away_team_goalkeeper_score', y='home_team_score', data=df, ax=axs[1], scatter=False, color='red')
axs[1].set_xlabel('Away Team Goalkeeper Strength')
axs[1].set_ylabel('Goals Conceded by Away Team')
axs[1].set_title('Away Team Goalkeeper Strength vs Goals Conceded')

plt.tight_layout()
plt.show()

