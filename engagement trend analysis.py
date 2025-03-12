import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/Debojyoti/Py Certification Project/sentimentdataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Data Cleaning
df_cleaned = df.copy()  # Create a copy of the dataset to work with
df_cleaned["Timestamp"] = pd.to_datetime(df_cleaned["Timestamp"], errors="coerce")  # Handle invalid dates
df_cleaned = df_cleaned.dropna(subset=["Timestamp"])  # Remove rows with invalid/missing timestamps
df_cleaned.set_index("Timestamp", inplace=True)

# Set Seaborn style
sns.set_theme(style="darkgrid")

# Aggregate engagement trends over time
plt.figure(figsize=(12, 6))
df_cleaned["Likes"].resample("D").sum().plot(label="Likes", marker="o")  # 'D' for daily aggregation
df_cleaned["Retweets"].resample("D").sum().plot(label="Retweets", marker="s")
plt.xlabel("Time")
plt.ylabel("Engagement Count")
plt.title("User Engagement Trends Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()
