import matplotlib.pyplot as plt
import seaborn as sns
df_cc = sns.load_dataset('car_crashes')
print(df_cc.head())
import matplotlib.pyplot as plt
import seaborn as sns

df_cc = sns.load_dataset('car_crashes')

print(df_cc.head())
totals = df_cc[['speeding', 'alcohol']].sum()

plt.figure(figsize=(6, 4))
sns.barplot(x=totals.index, y=totals.values)

plt.title('Total Speeding vs Alcohol-related Crashes')
plt.ylabel('Total Percentage')
plt.xlabel('Crash Cause')
plt.show()
