import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy import stats


path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(path)

print("Let's see if different types of 'drive-wheels' impact 'price', we group the data\n")
grouped_test2=df[['drive-wheels', 'price']].groupby(['drive-wheels'])
print(grouped_test2.head(2))

print("obtain the values of the method group using the method 'get_group'\n")
print(grouped_test2.get_group(('4wd',))['price'])

print("Using the function 'f_oneway' in the module 'stats' to obtain the F-test score and P-value\n")
f_val, p_val = stats.f_oneway(
    grouped_test2.get_group(('fwd',))['price'],
    grouped_test2.get_group(('rwd',))['price'],
    grouped_test2.get_group(('4wd',))['price']
)
print("ANOVA values are:\n")
print("F-Score:",f_val)
print("P-Score:",p_val)

print("Let's examine them separatel\n")
print("fwd and rwd")
f_val1, p_val1 = stats.f_oneway(
    grouped_test2.get_group(('fwd',))['price'],
    grouped_test2.get_group(('rwd',))['price']
)
print("ANOVA values are:\n")
print("F-Score:",f_val1)
print("P-Score:",p_val1)

print("4wd and rwd")
f_val2, p_val2 = stats.f_oneway(
    grouped_test2.get_group(('4wd',))['price'],
    grouped_test2.get_group(('rwd',))['price']
)
print("ANOVA values are:\n")
print("F-Score:",f_val2)
print("P-Score:",p_val2)

print("4wd and fwd")
f_val3, p_val3 = stats.f_oneway(
    grouped_test2.get_group(('4wd',))['price'],
    grouped_test2.get_group(('fwd',))['price']
)
print("ANOVA values are:\n")
print("F-Score:",f_val3)
print("P-Score:",p_val3)

