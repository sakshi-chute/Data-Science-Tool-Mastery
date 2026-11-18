import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Amit'],
    'Marks': [85, None, 75, 85],
    'City': ['Nagpur', 'Pune', 'Mumbai', 'Nagpur']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)