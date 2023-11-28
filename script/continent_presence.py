
## Question: Which continent is most present during the competition ?
## Answered by Mateo Deroche

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
file = "data/fifa_world_cup.csv"
df = pd.read_csv(file)

# Concatenate home_team_continent and away_team_continent columns for all matches
all_cont = pd.concat([df['home_team_continent'], df['away_team_continent']], ignore_index=True)

# Count the occurrences of each continent
cont_counts = all_cont.value_counts()

# Find the continent with the most participations
most_prst_cont = cont_counts.idxmax()
participation_counter = cont_counts.max()

# Get the top 5 continents
top_5 = cont_counts.head(5)

# Print the result for the most present continent
print(f"The continent most present during the FIFA World Cup is: {most_prst_cont} with {participation_counter} participations. \n")

# Print the leaderboard for the top 5 continents
print("Leaderboard - Top 5 Continents:")
for i, (continent, count) in enumerate(top_5.items(), start=1):
    print(f"{i}. {continent} with {count} participations")

# Visualize the result with a bar plot for the top 5 continents
plt.figure(figsize=(10, 6))
top_5.plot(kind='bar', color='skyblue')
plt.title('Top 5 Continents in FIFA World Cup Participation')

# Set labels and formatting for better readability
plt.xlabel('Continents')
plt.xticks(rotation=45, ha='right')

plt.ylabel('Number of Participations')

# Display the plot
plt.tight_layout()
plt.show()
