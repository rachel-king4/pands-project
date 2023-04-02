# analysis.py
# this program outputs a summary of each variable to a single text file
# and saves a histogram of each variable to png files
# and outputs a scatter plot of each pair of variables

# Author: Rachel King

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# using the attribute information as the column names
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_url, names = col_names)

#print(iris.head())
'''print(iris.tail())
print(iris.dtypes)
print(iris.describe())'''



counts = iris["Class"].value_counts()
plt.bar(counts.index, counts.values, color=['blue', 'purple', 'indigo'])
plt.legend()
plt.show()

fig, ax = plt.subplots()

colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'purple' , 
          'Iris-virginica': 'indigo'}

grouped = iris.groupby('Class')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Sepal_Length', y='Sepal_Width', label=key, color=colors[key])

plt.legend()
plt.show()

