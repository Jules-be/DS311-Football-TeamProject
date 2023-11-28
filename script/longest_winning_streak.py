
## What team has the longest winning streak ?
## Asnwered by Mateo Deroche

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
file = "data/fifa_world_cup.csv"
df = pd.read_csv(file)

# Create list to store the winner of each match
df['winner'] = df.apply(lambda row: row['home_team'] if row['home_team_result'] == 'Win' else row['away_team'], axis=1)

# Initialize variables to track winning streaks
current_streak = 0
max_streak = 0
current_team = None
max_streak_teams = []
teams = []
streaks = []

# Iterate through the DataFrame to find the longest winning streaks
for index, row in df.iterrows():
    if row['winner'] == current_team:
        # Continue the current streak
        current_streak += 1
    else:
        # Start a new streak
        current_streak = 1
        current_team = row['winner']

    # Update the longest winning streak if needed
    if current_streak > max_streak:
        max_streak = current_streak
        max_streak_teams = [current_team]
    elif current_streak == max_streak and current_team not in max_streak_teams:
        max_streak_teams.append(current_team)

    # Store data for visualization
    teams.append(current_team)
    streaks.append(current_streak)

# Sort teams based on streaks in descending order
sorted_teams, sorted_streaks = zip(*sorted(zip(teams, streaks), key=lambda x: x[1], reverse=True))
num_teams_to_display = 10
teams_display = ', '.join(sorted_teams[:num_teams_to_display])

# Print the result for the top 10 teams
print(f"The top {num_teams_to_display} teams with the longest winning streaks are: {teams_display}")
print(f"The length of the streak is: {max_streak} matches")

# Visualize the result with a bar plot for the top 10 teams
plt.figure(figsize=(12, 6))
plt.bar(sorted_teams[:num_teams_to_display], sorted_streaks[:num_teams_to_display], color='green')
plt.title(f'Top {num_teams_to_display} Teams with Longest Winning Streaks in FIFA World Cup')

# Set labels and formatting for better readability
plt.xlabel('Team')
plt.xticks(rotation=45, ha='right')

plt.ylabel('Number of Consecutive Wins')
plt.yticks(range(max_streak + 1))

# Display the plot
plt.tight_layout()
plt.show()
