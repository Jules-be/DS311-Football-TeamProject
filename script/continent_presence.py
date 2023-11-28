
## Question: Which continent is most present during the competition ?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "data/fifa_world_cup.csv"
df = pd.read_csv(file)

all_cont = pd.concat([df['home_team_continent'], df['away_team_continent']], ignore_index=True)
cont_counts = all_cont.value_counts()
most_prst_cont = cont_counts.idxmax()
participation_counter = cont_counts.max()
top_5 = cont_counts.head(5)

print(f"The continent most present during the FIFA World Cup is: {most_prst_cont} with {participation_counter} participations. \n")

print("Leaderboard - Top 5 Continents:")
for i, (continent, count) in enumerate(top_5.items(), start=1):
    print(f"{i}. {continent} with {count} participations")

plt.figure(figsize=(10, 6))
top_5.plot(kind='bar', color='skyblue')
plt.title('Top 5 Continents in FIFA World Cup Participation')
plt.xlabel('Continents')
plt.ylabel('Number of Participations')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()