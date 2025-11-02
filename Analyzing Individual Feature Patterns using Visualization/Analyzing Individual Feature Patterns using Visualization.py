import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(path)
print("first five rows of the dataframe\n")
print(df.head())

print("list the data types for each column\n")
print(df.dtypes)

print("data type of 'peak-rpm' column\n")
print(df["peak-rpm"].dtypes)

print("correlation matrix for Data between int64 and float64 \n")
numeric_df = df.select_dtypes(include=["number"])
df[numeric_df.columns] = df[numeric_df.columns].apply(pd.to_numeric, errors="coerce")
df_encoded = pd.get_dummies(df, drop_first=True)
print(df_encoded.corr())

print(
    "correlation values between 'bore', 'stroke', 'compression-ratio', 'horsepower'\n"
)
print(df[["bore", "stroke", "compression-ratio", "horsepower"]].corr())
print("Numerical Variables____________________")

print("\tPositive & Negative Linear Relationship\n")

print("We can examine the correlation & Scatter plot between 'engine-size' and 'price'")
print(df[["engine-size", "price"]].corr())
sns.regplot(x="engine-size", y="price", data=df)
plt.show()

print("We can examine the correlation & Scatter plot between 'highway-mpg' and 'price'")
print(df[["highway-mpg", "price"]].corr())
sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()

print("We can examine the correlation & Scatter plot between 'peak-rpm' and 'price'")
print(df[["peak-rpm", "price"]].corr())
sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()

print("We can examine the correlation & Scatter plot between 'stroke' and 'price'")
print(df[["stroke", "price"]].corr())
sns.regplot(x="stroke", y="price", data=df)
plt.show()
print("Categorical Variables____________________")
# this part needs encoding for getting dummies or label encoding or one hot encoding for applying Corr().( sklearn.preprocessing )
print("We can examine the Box plot between 'body-style' and 'price'")
sns.boxplot(x="body-style", y="price", data=df)
plt.show()

print("We can examine the Box plot between 'engine-location' and 'price'")
sns.boxplot(x="engine-location", y="price", data=df)
plt.show()

print("We can examine the Box plot between 'drive-wheels' and 'price'")
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.show()
