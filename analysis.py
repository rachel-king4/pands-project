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


'''counts = iris["Class"].value_counts()
plt.bar(counts.index, counts.values, color=['blue', 'purple', 'indigo'])
plt.legend()
plt.show()'''

# Summary of each Variable
# Summary of Sepal Length
lines = ['Sepal Length is the first variable we are going to summarise.',
         'From the Histogram.png file, the top left histogram displays the number of occurrences for each sepal length.',
         'The majority of sepal lengths fall in the 5.0-6.5 cm region.',
         'There are few sepal lengths greater than 7.0cm.',
         '',
         'From the scatter plot of sepal length vs sepal width, it is clear that the species "Iris-setosa" has the smallest sepal lengths of all the species.'
         'The species "Iris-virginica" has mostly larger sepal lengths, while the species "Iris-versicolor" falls somewhere in the middle']

with open('summary.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')



# histograms for each variable

fig, axes = plt.subplots(2,2, figsize = (15,15))

# sepal length histogram 
axes[0,0].set_title("Sepal Length", fontweight='bold')
axes[0,0].set(xlabel='Sepal Length')
axes[0,0].hist(iris['Sepal_Length'], bins=7)
 
# sepal width histogram 
axes[0,1].set_title("Sepal Width", fontweight='bold')
axes[0,1].set(xlabel='Sepal Width')
axes[0,1].hist(iris['Sepal_Width'], bins=5);

# petal length histogram 
axes[1,0].set_title("Petal Length", fontweight='bold')
axes[1,0].set(xlabel='Petal Length')
axes[1,0].hist(iris['Petal_Length'], bins=6);

# petal width histogram 
axes[1,1].set_title("Petal Width", fontweight='bold')
axes[1,1].set(xlabel='Petal Width')
axes[1,1].hist(iris['Petal_Width'], bins=6);

for ax in axes.flat:
    ax.set(ylabel='No. of Occurrences')   # as y label is the same for all histograms

fig.savefig('Histograms.png')


# scatter plots of each pair of variables
# sepal length vs width
fig, ax = plt.subplots()
colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'purple' , 
          'Iris-virginica': 'indigo'}

grouped = iris.groupby('Class')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Sepal_Length', y='Sepal_Width', label=key, color=colors[key])

plt.legend(bbox_to_anchor=(1, 1), loc=2)   # places legend outside the plot
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()


# petal length vs width
fig, ax = plt.subplots()
colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'purple' , 
          'Iris-virginica': 'indigo'}

grouped = iris.groupby('Class')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Petal_Length', y='Petal_Width', label=key, color=colors[key])

plt.legend(bbox_to_anchor=(1, 1), loc=2)   # places legend outside the plot
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.show()
