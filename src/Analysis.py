import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("songs_normalize.csv")
df = pd.read_csv("../data/songs_normalize.csv")


df = df.dropna() 

df['duration_ms'] = (df['duration_ms'] / 60000).round()
df['song'] = df['song'].str.strip()

top_genres = df['genre'].value_counts().head(10)
print("\nTop 10 genre:\n", top_genres)

avg_duration = df.groupby('genre')['duration_ms'].mean().sort_values(ascending = True)
print("\nAverage Duration by Genre:\n", avg_duration.head(10))

print("\nSummary Statistics:\n")
print(df.describe())




plt.figure(figsize=(10,5))
top_genres.plot(kind='bar', color='skyblue')
plt.title("Top 10 Genres on Spotify")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")
plt.tight_layout()
plt.savefig("../data/songs_normalize.png")
plt.close()