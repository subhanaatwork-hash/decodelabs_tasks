import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data (same as before)
df = pd.read_csv('survey.csv')
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

# Setting up the style for all charts
sns.set_style("whitegrid")

# CHART 1: Age distribution - who is using these apps?
plt.figure(figsize=(8, 5))
age_counts = df_clean['What is your age group?'].value_counts()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = plt.bar(age_counts.index, age_counts.values, color=colors)
plt.title('Age Groups of Survey Respondents', fontsize=14, fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel('Number of People')
for bar, count in zip(bars, age_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(count), ha='center')
plt.tight_layout()
plt.show()

# CHART 2: What do users care about most? (pie chart shows percentages clearly)
plt.figure(figsize=(8, 8))
priorities = df_clean['What matters most to you when choosing a ride-hailing app?'].value_counts()
colors_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
plt.pie(priorities.values, labels=priorities.index, autopct='%1.1f%%', startangle=90, colors=colors_pie)
plt.title('Most Important Factor When Choosing a Ride App', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# CHART 3: How did the price increase affect usage?
plt.figure(figsize=(9, 5))
price_effect = df_clean['Did the recent price increase affect how often you use these apps?'].value_counts()
colors_bar = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
bars_h = plt.barh(price_effect.index, price_effect.values, color=colors_bar)
plt.title('Impact of Price Increase on App Usage', fontsize=14, fontweight='bold')
plt.xlabel('Number of Respondents')
for bar, val in zip(bars_h, price_effect.values):
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, str(val), va='center')
plt.tight_layout()
plt.show()

# CHART 4: Heatmap showing connection between driver behavior and safety
plt.figure(figsize=(8, 6))
driver_safety = pd.crosstab(df_clean['How would you rate the behaviour of most drivers?'], 
                            df_clean['Do you feel safe during the rides?'])
sns.heatmap(driver_safety, annot=True, fmt='d', cmap='YlOrRd', linewidths=1)
plt.title('Does Driver Behavior Affect How Safe People Feel?', fontsize=12, fontweight='bold')
plt.xlabel('Safety Perception')
plt.ylabel('Driver Behavior Rating')
plt.tight_layout()
plt.show()

# CHART 5: How many people have dealt with bad driver behavior?
plt.figure(figsize=(8, 5))
bad_behavior = df_clean['Have you experienced any unprofessional behavior from drivers?'].value_counts()
colors_last = ['#FF6B6B', '#4ECDC4', '#45B7D1']
bars_last = plt.bar(bad_behavior.index, bad_behavior.values, color=colors_last)
plt.title('Have You Experienced Unprofessional Driver Behavior?', fontsize=14, fontweight='bold')
plt.xlabel('Response')
plt.ylabel('Number of Respondents')
for bar, val in zip(bars_last, bad_behavior.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), ha='center')
plt.tight_layout()
plt.show()

print("All 5 charts have been generated. Close each chart window to continue.")
