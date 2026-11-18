import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Student dataset
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Priya'],
    'Python': [85, 90, 75, 95, 80],
    'Java': [80, 85, 70, 90, 75],
    'DBMS': [90, 95, 80, 85, 90]
}

df = pd.DataFrame(data)

# Calculate total and average
subjects = ['Python', 'Java', 'DBMS']

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)

# Display student data
print("STUDENT PERFORMANCE ANALYSIS")
print(df)

# Calculate statistics
print("\nClass Average:", np.mean(df['Average']))
print("Highest Average:", df['Average'].max())
print("Lowest Average:", df['Average'].min())

# Find topper
topper = df.loc[df['Average'].idxmax(), 'Name']
print("Top Performing Student:", topper)

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Average'])

plt.title("Student Average Performance")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.savefig("student_performance.png")
plt.show()

# Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[subjects].corr(), annot=True, cmap='coolwarm')

plt.title("Subject Correlation")
plt.savefig("subject_correlation.png")
plt.show()