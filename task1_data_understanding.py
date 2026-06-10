import pandas as pd

# Load the survey data I collected from Google Forms
df = pd.read_csv('survey.csv')

# Check how big this dataset actually is
print(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns")
print("\n")

# Look at each column and what type of data it stores
print("What's in each column:")
for column in df.columns:
    print(f"- {column}: {df[column].dtype}")

print("\n")
print("First 5 responses in the dataset:")
print(df.head())

print("\n")
print("What is this data about?")
print("I collected this data from Yango/InDrive users. Total 27 people responded.")
print("The columns capture things like age, how often they use the app,")
print("whether they feel safe, if they've had bad experiences with drivers,")
print("how the recent price hike affected them, and what matters most to them.")
