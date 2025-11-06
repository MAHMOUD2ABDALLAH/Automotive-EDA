import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy import stats


path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(path)

print(df.corr(numeric_only=True))

def Pearson_Detection(pearson_coef):
    if(pearson_coef>0 and pearson_coef<=1):
        print("Perfect positive linear correlation\n")
    elif(pearson_coef<0 and pearson_coef>=-1):
        print("Perfect negative linear correlation\n")
    elif(pearson_coef==0):
        print("No linear correlation\n")

def Pvalue_Detection(p_value):
    if p_value < 0.001:
        print("there is strong evidence that the correlation is significant.\n")
    elif p_value< 0.05:
        print("there is moderate evidence that the correlation is significant.\n")
    elif p_value< 0.1:
        print("there is weak evidence that the correlation is significant.\n")
    elif p_value> 0.1:
        print("there is no evidence that the correlation is significant.\n")




print("Let's calculate the Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price\n")
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print("Let's calculate the  Pearson Correlation Coefficient and P-value of 'horsepower' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print("Let's calculate the Pearson Correlation Coefficient and P-value of 'length' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print("Let's calculate the Pearson Correlation Coefficient and P-value of 'width' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print("Let's calculate the Pearson Correlation Coefficient and P-value of 'curb-weight' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print(" Let's calculate the  Pearson Correlation Coefficient and P-value of 'bore' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print(" Let's calculate the  Pearson Correlation Coefficient and P-value of 'city-mpg' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)


print(" Let's calculate the  Pearson Correlation Coefficient and P-value of 'highway-mpg' and 'price'\n")
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print("The Pearson Correlation Coefficient is =", pearson_coef)
Pearson_Detection(pearson_coef)
print("P-value of P =", p_value)
Pvalue_Detection(p_value)

