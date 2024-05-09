# -*- coding: utf-8 -*-
"""LVADSUSR139_IA2_Clustering_Abinaya_Anbu.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tNaOUbt5R4Kh4LhUUrx7qpIcsrZLS1YJ
"""

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

data=pd.read_csv('https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch5-Assessment/main/Mall_Customers.csv')

data.describe()

data.info()

data.isna().sum()

data.isnull().sum()

data.duplicated().sum()

for column in data.select_dtypes(include=['float64','int64']):
  sns.boxplot(data[column])
  plt.show()

for column in data.select_dtypes(include = "number"):
  q1 = data[column].quantile(0.25)
  q3 = data[column].quantile(0.75)
  iqr = q3-q1
  lower = q1 - 1.5*iqr
  upper = q3 + 1.5* iqr
  data[column] = data[column].clip(lower = lower, upper= upper)

for column in data.select_dtypes(include=['float64','int64']):
  sns.boxplot(data[column])
  plt.show()

#Feature encoding
len = LabelEncoder()
for column in data.select_dtypes(include = 'object'):
  data[column] = len.fit_transform(data[column])
data.head()

scaler = MinMaxScaler()
for column in data.select_dtypes(include=['float64','int64']):
  data[column] = scaler.fit_transform(data[[column]])

print(data.head())

data.columns

data.isna().sum()

data.dropna()



sse = [] # The sum of Squared Errors =SSE
k_rng = range(1,10)
for k in k_rng:
   km = KMeans(n_clusters=k)
   km.fit(data[['Age','Spending Score (1-100)']])
   sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)

km = KMeans(n_clusters=2)
y_predicted = km.fit(data[['Age','Spending Score (1-100)']])
y_predicted
data['cluster']=y_predicted
print(km.cluster_centers_)

df1 = data[data.cluster==0]
df2 = data[data.cluster==1]
df3 = data[data.cluster==2]

plt.scatter(df1['Spending Score (1-100)'],df1['Age'],color='green')
plt.scatter(df2['Spending Score (1-100)'],df2['Age'],color='red')
plt.scatter(df3['Spending Score (1-100)'],df3['Age'],color='black')
plt.scatter(km.cluster_centers_[:,0],
            km.cluster_centers_[:,1],
            color='purple',
            marker='*',
            label='centroid')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.legend()

silhouette_score(data, y_predicted)