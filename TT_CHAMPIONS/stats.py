import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv('log.csv')

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create a scatterplot with line that shows the change in average score over time for each player
# Group by name and timestamp, and calculate the average score for each group
df = df.groupby(['name', pd.Grouper(key='timestamp', freq='1D')])['score'].mean().reset_index()

# Pivot the dataframe so that each player is a column
df = df.pivot(index='timestamp', columns='name', values='score')

# Plot the dataframe
df.plot(marker='o')

# Rotate x-axis label by 45 degrees
plt.xticks(rotation=45)

plt.legend()
plt.title("Average Score Over Time")
plt.xlabel("Date")
plt.ylabel("Average Score")
plt.savefig("average_score_over_time.png")
plt.show()
