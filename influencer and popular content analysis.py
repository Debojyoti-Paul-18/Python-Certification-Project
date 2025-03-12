import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Update the correct file path)
file_path = "C:/Users/Debojyoti/Py Certification Project/sentimentdataset.csv"
df = pd.read_csv(file_path)

# Data Cleaning
df_cleaned = df.copy()  # Work on a copy of the dataset
df_cleaned["Timestamp"] = pd.to_datetime(df_cleaned["Timestamp"], errors="coerce")  # Convert timestamp
df_cleaned = df_cleaned.dropna(subset=["Timestamp"])  # Drop missing timestamps
df_cleaned.set_index("Timestamp", inplace=True)  # Set timestamp as index

# Ensure correct column names
print("Columns in dataset:", df_cleaned.columns)

# Identifying Key Influencers
if "User" in df_cleaned.columns and "Likes" in df_cleaned.columns and "Retweets" in df_cleaned.columns:
    influencers = df_cleaned.groupby("User")[["Likes", "Retweets"]].sum()
    influencers["Total Engagement"] = influencers["Likes"] + influencers["Retweets"]
    influencers = influencers.sort_values(by="Total Engagement", ascending=False).head(10)

    # Reset index for plotting
    influencers = influencers.reset_index()

    # Plot top influencers
    plt.figure(figsize=(10, 5))
    sns.barplot(x="User", y="Total Engagement", data=influencers, palette="viridis")
    plt.xticks(rotation=45)
    plt.xlabel("User")
    plt.ylabel("Total Engagement")
    plt.title("Top 10 Influencers Based on Engagement")
    plt.show()
else:
    print("Error: Columns 'User', 'Likes', or 'Retweets' not found in dataset.")

# Most Popular Content
if "Text" in df_cleaned.columns:
    popular_content = df_cleaned.sort_values(by=["Likes", "Retweets"], ascending=False).head(5)[["Text", "Likes", "Retweets"]]
    print("\nMost Popular Content:")
    print(popular_content)
else:
    print("Error: Column 'Text' not found in dataset.")
