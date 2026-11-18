import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Python': [85, 90, 75, 80],
    'Java': [75, 80, 70, 85],
    'DBMS': [90, 85, 80, 95]
}

df = pd.DataFrame(data)

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

plt.title("Subject Marks Correlation")
plt.show()