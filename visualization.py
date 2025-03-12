import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="darkgrid")

# Engagement Trends Over Time
plt.figure(figsize=(12, 6))
df_cleaned.groupby("Timestamp")["Likes"].sum().plot(label="Likes", marker="o")
df_cleaned.groupby("Timestamp")["Retweets"].sum().plot(label="Retweets", marker="s")
plt.xlabel("Time")
plt.ylabel("Engagement Count")
plt.title("User Engagement Trends Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Sentiment Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df_cleaned, x="Sentiment", palette="coolwarm")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Top Influencers
plt.figure(figsize=(10, 5))
sns.barplot(x=influencers.index, y=influencers["Total Engagement"], palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("User")
plt.ylabel("Total Engagement")
plt.title("Top 10 Influencers Based on Engagement")
plt.show()
