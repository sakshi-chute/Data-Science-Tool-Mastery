import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Sneha'],
    'Marks': [85, 90, 75, 95],
    'City': ['Nagpur', 'Pune', 'Mumbai', 'Yavatmal']
}

df = pd.DataFrame(data)

print(df)