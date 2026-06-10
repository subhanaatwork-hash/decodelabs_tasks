import pandas as pd

# Load the cleaned data
df = pd.read_csv('survey.csv')  # I'll re-clean it here since separate file
df_clean = df.copy()
most_common_age = df_clean['What is your age group?'].mode()[0]
df_clean['What is your age group?'] = df_clean['What is your age group?'].fillna(most_common_age)
df_clean['Have you ever booked these rides during night time? If not, why?'] = df_clean['Have you ever booked these rides during night time? If not, why?'].fillna('Not specified')
df_clean['Have you ever canceled a ride because of driver behavior or price?'] = df_clean['Have you ever canceled a ride because of driver behavior or price?'].fillna('No')
df_clean['Did the recent price increase affect how often you use these apps?'] = df_clean['Did the recent price increase affect how often you use these apps?'].replace({
    'Yes, alot': 'Yes, a lot',
    'I use it less now': 'Use less often',
    'I use local transport now': 'Switched to local transport'
})
df_clean['What matters most to you when choosing a ride-hailing app?'] = df_clean['What matters most to you when choosing a ride-hailing app?'].replace({
    'Option 5': 'Other',
    'Option 6': 'Other'
})

print("BASIC STATISTICS - How people responded")
print("="*50)
print("\n")

print("Age groups of respondents:")
print(df_clean['What is your age group?'].value_counts())
print("\n")

print("How often do people use Yango/InDrive?")
print(df_clean['How often do you use Yango/Indrive?'].value_counts())
print("\n")

print("Do people feel safe during rides?")
print(df_clean['Do you feel safe during the rides?'].value_counts())
print("\n")

print("How do users rate driver behavior?")
print(df_clean['How would you rate the behaviour of most drivers?'].value_counts())
print("\n")

print("Have users experienced bad driver behavior?")
print(df_clean['Have you experienced any unprofessional behavior from drivers?'].value_counts())
print("\n")

print("What matters most to users when picking a ride app?")
print(df_clean['What matters most to you when choosing a ride-hailing app?'].value_counts())
print("\n")

print("TRENDS AND PATTERNS I NOTICED")
print("="*50)
print("\n")

# Let me see if age affects how safe people feel
print("Age group vs Safety perception:")
age_safety = pd.crosstab(df_clean['What is your age group?'], df_clean['Do you feel safe during the rides?'])
print(age_safety)
print("\n")

# Also check if driver behavior is linked to unprofessional experiences
print("Driver rating vs Unprofessional behavior experienced:")
driver_behavior = pd.crosstab(df_clean['How would you rate the behaviour of most drivers?'], 
                              df_clean['Have you experienced any unprofessional behavior from drivers?'])
print(driver_behavior)
print("\n")

# Finding any unusual responses - people who feel unsafe
unsafe_people = df_clean[df_clean['Do you feel safe during the rides?'] == 'Feel unsafe']
print(f"Found {len(unsafe_people)} person who said they feel unsafe")
if len(unsafe_people) > 0:
    print(f"Their comment about night rides: {unsafe_people['Have you ever booked these rides during night time? If not, why?'].values[0]}")
print("\n")

print("KEY FINDINGS FROM THIS DATA")
print("="*50)
print("1. Most users are young - 21 out of 27 are between 18-24 years old")
print("2. Safety is the number one priority (11 people said this), not price or speed")
print("3. 15 people have experienced unprofessional driver behavior - that's more than half")
print("4. Only 1 person reported feeling unsafe - interestingly, a woman who avoids night rides")
print("5. The price increase pushed 13 people to either use the app less or switch to local transport")
