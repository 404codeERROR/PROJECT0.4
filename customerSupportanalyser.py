import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Fake support ticket data
data = {
    'ticket_id': [1, 2, 3, 4, 5],
    'issue': [
        'Login problem',
        'Payment failed',
        'Login problem',
        'App crash',
        'Payment failed'
    ],
    'resolution_time_hours': [5, 12, 4, 24, 10]
}

df = pd.DataFrame(data)

# 🔍 Most common issues
issue_counts = df['issue'].value_counts()

# 🧠 Average resolution time per issue
avg_resolution = df.groupby('issue')['resolution_time_hours'].mean()

# 📊 Plot it
plt.figure(figsize=(10,4))
sns.barplot(x=avg_resolution.index, y=avg_resolution.values)
plt.title("Avg Resolution Time by Issue")
plt.ylabel("Hours")
plt.xlabel("Issue Type")
plt.show()

print("Top issues:")
print(issue_counts)
print("\nAvg resolution time:")
print(avg_resolution)