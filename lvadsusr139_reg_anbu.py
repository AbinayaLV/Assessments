# -*- coding: utf-8 -*-
"""lvadsusr139_Reg_Anbu.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oVikpdVgwCGZzBE8mpFTpo_LkvcKyJnP

Importing Libraries
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder

"""Reading Data"""

data=pd.read_csv('https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch5-Assessment/main/Fare%20prediction.csv')

"""Describe"""

data.describe(include='all')

"""Info"""

data.info()

"""Missing Values"""

data.isna().sum()#no null values

"""Duplicates"""

data.duplicated().sum()# no duplicates

"""Correlation Matrix"""

numerical_col= data.select_dtypes(include=['int','float'])
correl = numerical_col.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correl, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
print()

"""Outliers box plot and removal"""

plt.figure(figsize=(12, 6))
sns.boxplot(data=data)
plt.title("Boxplot of Variables")
plt.xticks(rotation=45)
plt.show()
print()# outliers on the data set

for col in data.select_dtypes(include=[np.number]).columns:
    ninety_fifth_percentile = data[col].quantile(0.95)
    data[col] = np.where(data[col] > ninety_fifth_percentile, ninety_fifth_percentile, data[col])

plt.figure(figsize=(12, 6))
sns.boxplot(data=data)
plt.title("Boxplot of Variables after Handling Outliers")
plt.xticks(rotation=45)
plt.show()

"""Scaling(normalization)"""

cat_colum = data.select_dtypes(include=['object'])
scaler = StandardScaler()
#ata[cat_colum]= scaler.fit_transform(data[cat_colum])

"""Data Processing"""

data.head()

data.columns

"""X, y splitting"""

X = data.drop('fare_amount', axis=1)
y = data['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_encoded = pd.get_dummies(X_train)
X_test_encoded = pd.get_dummies(X_test)

X_train_encoded, X_test_encoded = X_train_encoded.align(X_test_encoded, join='outer', axis=1, fill_value=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_encoded, y_train)

y_pred = model.predict(X_test_encoded)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

rmse = mean_squared_error(y_test, y_pred, squared=False)

print("Mean Squared Error:", mse)
print()
print("R-squared:", r2)
print()
print("Root Mean Squared Error (RMSE):", rmse)



"""Insights"""