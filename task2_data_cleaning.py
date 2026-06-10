import pandas as pd

# Load the messy data
df = pd.read_csv('survey.csv')

# Make a copy so I don't mess up the original
df_clean = df.copy()

# First, let's see what's missing
print("Missing values before I fix anything:")
print(df_clean.isnull().sum())
print("\n")

# Some people didn't mention their age. I'll fill with the most common age group
most_common_age = df_clean['What is your age group?'].mode()[0]
df_clean['What is your age group?'] = df_clean['What is your age group?'].fillna(most_common_age)

# For night rides question, if left blank I'll mark as 'Not specified'
df_clean['Have you ever booked these rides during night time? If not, why?'] = df_clean['Have you ever booked these rides during night time? If not, why?'].fillna('Not specified')

# Same for cancellation question
df_clean['Have you ever canceled a ride because of driver behavior or price?'] = df_clean['Have you ever canceled a ride because of driver behavior or price?'].fillna('No')

# Check if missing values are gone
print("Missing values after cleaning:")
print(df_clean.isnull().sum())
print("\n")

# Remove any duplicate rows if they exist
before_count = len(df_clean)
df_clean = df_clean.drop_duplicates()
after_count = len(df_clean)
print(f"Found and removed {before_count - after_count} duplicate rows")
print("\n")

# Some people wrote 'Yes, alot' and others wrote 'Yes, a lot' - need to make these consistent
df_clean['Did the recent price increase affect how often you use these apps?'] = df_clean['Did the recent price increase affect how often you use these apps?'].replace({
    'Yes, alot': 'Yes, a lot',
    'I use it less now': 'Use less often',
    'I use local transport now': 'Switched to local transport'
})

# A couple of responses in the priority column were 'Option 5' and 'Option 6' - renaming these to 'Other'
df_clean['What matters most to you when choosing a ride-hailing app?'] = df_clean['What matters most to you when choosing a ride-hailing app?'].replace({
    'Option 5': 'Other',
    'Option 6': 'Other'
})

print("Data cleaning is done. Final dataset is ready for analysis.")
print(f"Final shape: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns")
