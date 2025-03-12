# Identifying Key Influencers
influencers = df_cleaned.groupby("User")[["Likes", "Retweets"]].sum()
influencers["Total Engagement"] = influencers["Likes"] + influencers["Retweets"]
influencers = influencers.sort_values(by="Total Engagement", ascending=False).head(10)

# Plot top influencers
plt.figure(figsize=(10, 5))
sns.barplot(x=influencers.index, y=influencers["Total Engagement"], palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("User")
plt.ylabel("Total Engagement")
plt.title("Top 10 Influencers Based on Engagement")
plt.show()

# Most Popular Content
popular_content = df_cleaned.sort_values(by=["Likes", "Retweets"], ascending=False).head(5)[["Text", "Likes", "Retweets"]]
print("Most Popular Content:")
print(popular_content)
