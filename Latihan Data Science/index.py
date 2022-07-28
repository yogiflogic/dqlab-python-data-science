from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

bacadata = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
bacadatamv = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
print(bacadata.head())
print(bacadata.describe(exclude=['O']))

print(bacadata.isnull().values.any())
print(bacadatamv.isnull().values.any())

print(bacadata.mean())

bacadata2 = bacadata.fillna(bacadata.mean())
print("Dataset yang sudah diproses Handling Missing Values dengan Mean :")
print(bacadata.head(10))

plt.plot([1,2,3,4,5,6,7], [2,6,1,4,8,10,9])
plt.xlabel('label X')
plt.ylabel('label Y')
plt.show()
