import pandas as pd

# Load the dataset
file_path = "C:\\Users\\Debojyoti\\Py Certification Project\\sentimentdataset.csv"
df = pd.read_csv(file_path)

# Drop unnecessary columns
df_cleaned = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

# Convert Timestamp to datetime format
df_cleaned["Timestamp"] = pd.to_datetime(df_cleaned["Timestamp"])

# Ensure numerical columns are in the correct type
df_cleaned["Retweets"] = df_cleaned["Retweets"].astype(int)
df_cleaned["Likes"] = df_cleaned["Likes"].astype(int)

# Check for missing values
missing_values = df_cleaned.isnull().sum()

# Display cleaned dataset info and missing values
df_cleaned.info(), missing_values
