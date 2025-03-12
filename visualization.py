import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "C:/Users/Debojyoti/Py Certification Project/sentimentdataset.csv"  # Change path if needed
df = pd.read_csv(file_path)

# Data Cleaning
df_cleaned = df.copy()

# Check if necessary columns exist
required_columns = ["Timestamp", "Likes", "Retweets", "User", "Sentiment"]
missing_columns = [col for col in required_columns if col not in df_cleaned.columns]

if missing_columns:
    print(f"Error: Missing columns - {missing_columns}")
else:
    # Convert Timestamp to datetime format
    df_cleaned["Timestamp"] = pd.to_datetime(df_cleaned["Timestamp"], errors="coerce")

    # Remove rows where Timestamp is NaT
    df_cleaned = df_cleaned.dropna(subset=["Timestamp"])

    # Set Timestamp as index
    df_cleaned.set_index("Timestamp", inplace=True)

    # Set Seaborn style
    sns.set_theme(style="darkgrid")

    # Engagement Trends Over Time
    plt.figure(figsize=(12, 6))
    df_cleaned["Likes"].resample("D").sum().plot(label="Likes", marker="o")
    df_cleaned["Retweets"].resample("D").sum().plot(label="Retweets", marker="s")
    plt.xlabel("Time")
    plt.ylabel("Engagement Count")
    plt.title("User Engagement Trends Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

    # Sentiment Distribution
    if "Sentiment" in df_cleaned.columns:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df_cleaned, x="Sentiment", palette="coolwarm")
        plt.title("Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.show()
    else:
        print("Error: 'Sentiment' column not found in dataset.")

    # Identifying Key Influencers
    if "User" in df_cleaned.columns and "Likes" in df_cleaned.columns and "Retweets" in df_cleaned.columns:
        influencers = df_cleaned.groupby("User")[["Likes", "Retweets"]].sum()
        influencers["Total Engagement"] = influencers["Likes"] + influencers["Retweets"]
        influencers = influencers.sort_values(by="Total Engagement", ascending=False).head(10)

        # Reset index for Seaborn
        influencers = influencers.reset_index()

        # Top Influencers Plot
        plt.figure(figsize=(10, 5))
        sns.barplot(x="User", y="Total Engagement", data=influencers, palette="viridis")
        plt.xticks(rotation=45)
        plt.xlabel("User")
        plt.ylabel("Total Engagement")
        plt.title("Top 10 Influencers Based on Engagement")
        plt.show()
    else:
        print("Error: Columns 'User', 'Likes', or 'Retweets' not found in dataset.")
