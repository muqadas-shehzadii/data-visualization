import matplotlib.pyplot as plt
import seaborn as sns
df_iris = sns.load_dataset('iris')
print(df_iris.head())
fig ,axes = plt.subplots(nrows = 2, ncols = 2)
axes[0][0].plot(df_iris.index,df_iris['sepal_length'],color = 'r')
axes[0][0].grid(True)
axes[0][1].scatter(df_iris.index,df_iris['sepal_length'],color = 'r')
axes[0][1].grid(True)
axes[1][0].bar(df_iris.index,df_iris['sepal_length'],color = 'r')
axes[1][0].grid(True)
axes[1][1].hist(df_iris['sepal_length'], bins=20, density=True, color='r')
axes[1][1].grid(True)

plt.show()