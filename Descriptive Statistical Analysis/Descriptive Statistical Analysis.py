import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(path)

print("apply the method 'describe'\n")
print(df.describe())

print("apply the method 'describe' on the variables of type 'object'\n")
print(df.describe(include=['object']))

print("value counts for the column 'drive-wheels'\n")
print(df['drive-wheels'].value_counts())

print("convert the series to a dataframe\n")
print(df['drive-wheels'].value_counts().to_frame())

print("rename the column 'drive-wheels' to 'value_counts'\n")
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
print(drive_wheels_counts)

print("set the index name to 'drive-wheels'\n")
drive_wheels_counts.index.name = 'drive-wheels'
print(drive_wheels_counts)

print("value counts for the column 'engine-location'\n")
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts.head(10))