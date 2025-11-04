import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(path)

print("let's group by the variable 'drive-wheels'")
print(df['drive-wheels'].unique())

print("We can then calculate the average price for each of the different categories of data")
df_group_one = df[['drive-wheels','body-style','price']]
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean(numeric_only=True)
print(df_group_one)

print("let's group by both 'drive-wheels' and 'body-style'")
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean(numeric_only=True)
print(grouped_test1)

print("we will leave the drive-wheels variable as the rows of the table")
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print(grouped_pivot)

print("We can fill these missing cells with the value 0")
grouped_pivot = grouped_pivot.fillna(0)
print(grouped_pivot)

print("the average 'price' of each car based on 'body-style'")
df_gptest2 = df[['body-style','price']]
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean()
print(grouped_test_bodystyle)

print("Let's use a heat map to visualize the relationship between Body Style vs Price")
plt.title("Body Style vs Price")
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

print("we can use the 'drive-wheels' and 'body-style' to the 'price' columns as the x and y axis")
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

fig.colorbar(im)
plt.title("Body Style & Drive Wheels vs Price")
plt.show()