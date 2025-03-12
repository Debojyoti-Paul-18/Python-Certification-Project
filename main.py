import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("sentimentdataset.csv")

# Task 1: Data Cleaning
# Checking for missing values
df.dropna(inplace=True)

# Converting Timestamp to datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df.set_index("Timestamp", inplace=True)

# Task 2: Analyze User Engagement Trends
# Aggregating likes and retweets over time
engagement_trends = df.resample("D")[["Likes", "Retweets"]].sum()

# Task 3: Identify Key Influencers and Popular Content
# Identifying influencers based on total engagement
influencers = df.groupby("User")[["Likes", "Retweets"]].sum()
influencers["Total Engagement"] = influencers["Likes"] + influencers["Retweets"]
influencers = influencers.sort_values(by="Total Engagement", ascending=False).head(10)

# Identifying top 5 most engaged posts
popular_content = df.sort_values(by=["Likes", "Retweets"], ascending=False).head(5)[["User", "Text", "Likes", "Retweets"]]

# Task 4: Create Visualizations
sns.set_theme(style="darkgrid")

# Engagement Trends Over Time
plt.figure(figsize=(12, 6))
plt.plot(engagement_trends.index, engagement_trends["Likes"], marker="o", label="Likes")
plt.plot(engagement_trends.index, engagement_trends["Retweets"], marker="s", label="Retweets")
plt.xlabel("Time")
plt.ylabel("Engagement Count")
plt.title("User Engagement Trends Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Sentiment Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sentiment", palette="coolwarm")
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

# Task 5: Present Findings in a Report
print("\n--- Social Media Engagement Analysis Report ---\n")
print("1. User Engagement Trends:\n")
print(engagement_trends.tail())
print("\n2. Sentiment Distribution:\n")
print(df["Sentiment"].value_counts())
print("\n3. Key Influencers:\n")
print(influencers)
print("\n4. Top 5 Most Engaged Posts:\n")
print(popular_content)