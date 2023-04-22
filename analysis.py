# analysis.py
# this program outputs a summary of each variable to a single text file
# and saves a histogram of each variable to png files
# and outputs a scatter plot of each pair of variables

# Author: Rachel King

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from tabulate import tabulate

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
         'The species "Iris-virginica" has mostly larger sepal lengths, while the species "Iris-versicolor" falls somewhere in the middle.',
         '',
         'A table of some Sepal Length statistics can be seen below:'
         '']

with open('summary.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# Sepal Length Statistics
table_of_data = iris.groupby('Class').agg({'Sepal_Length': ['mean', 'min', 'max']})
table_of_data.reset_index(inplace=False)
#print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'))
with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'), file=f)

sepal_length = iris.groupby(["Class"],as_index=False).agg(
    min=pd.NamedAgg(column="Sepal_Length", aggfunc="min"),
    max=pd.NamedAgg(column="Sepal_Length", aggfunc="max"),
    mean=pd.NamedAgg(column="Sepal_Length", aggfunc=np.mean))
sepal_length.reset_index(inplace=True)


ax = sepal_length.plot(x='Class', y='mean', c='brown')
ax.fill_between(x='Class', y1='min', y2='max', data=sepal_length,
                color=mpl.colors.to_rgba('brown', 0.15))
plt.ylim(3,9)
plt.title("Sepal Length", fontweight='bold')
plt.ylabel("Data for Sepal Length (cm)")
plt.savefig('Sepal Length Statistics.png')

lines2 = ['From the Sepal Length Statistics plot, we can see the range of data for min, max and mean for all three classes of Iris plants.',
         'The line represents the mean for all three classes, while the shaded region represents the spread of data from minimum to maximum.']

with open('summary.txt', 'a') as f:
    for line in lines2:
        f.write(line)
        f.write('\n')


# Sepal Width Statistics
table_of_data = iris.groupby('Class').agg({'Sepal_Width': ['mean', 'min', 'max']})
table_of_data.reset_index(inplace=False)
#print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'))
with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'), file=f)

sepal_width = iris.groupby(["Class"],as_index=False).agg(
    min=pd.NamedAgg(column="Sepal_Width", aggfunc="min"),
    max=pd.NamedAgg(column="Sepal_Width", aggfunc="max"),
    mean=pd.NamedAgg(column="Sepal_Width", aggfunc=np.mean))
sepal_width.reset_index(inplace=True)


ax = sepal_width.plot(x='Class', y='mean', c='green')
ax.fill_between(x='Class', y1='min', y2='max', data=sepal_width,
                color=mpl.colors.to_rgba('green', 0.15))
plt.ylim(1,5)
plt.title("Sepal Width", fontweight='bold')
plt.ylabel("Data for Sepal Width (cm)")
plt.savefig('Sepal Width Statistics.png')

# Petal Length Statistics
table_of_data = iris.groupby('Class').agg({'Petal_Length': ['mean', 'min', 'max']})
table_of_data.reset_index(inplace=False)
#print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'))
with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'), file=f)

petal_length = iris.groupby(["Class"],as_index=False).agg(
    min=pd.NamedAgg(column="Petal_Length", aggfunc="min"),
    max=pd.NamedAgg(column="Petal_Length", aggfunc="max"),
    mean=pd.NamedAgg(column="Petal_Length", aggfunc=np.mean))
petal_length.reset_index(inplace=True)


ax = petal_length.plot(x='Class', y='mean', c='brown')
ax.fill_between(x='Class', y1='min', y2='max', data=petal_length,
                color=mpl.colors.to_rgba('brown', 0.15))
plt.ylim(0,8)
plt.title("Petal Length", fontweight='bold')
plt.ylabel("Data for Petal Length (cm)")
plt.savefig('Petal Length Statistics.png')

# Petal Width Statistics
table_of_data = iris.groupby('Class').agg({'Petal_Width': ['mean', 'min', 'max']})
table_of_data.reset_index(inplace=False)
#print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'))
with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean", "Min", "Max"], tablefmt='grid', stralign='center'), file=f)

petal_width = iris.groupby(["Class"],as_index=False).agg(
    min=pd.NamedAgg(column="Petal_Width", aggfunc="min"),
    max=pd.NamedAgg(column="Petal_Width", aggfunc="max"),
    mean=pd.NamedAgg(column="Petal_Width", aggfunc=np.mean))
petal_width.reset_index(inplace=True)


ax = petal_width.plot(x='Class', y='mean', c='green')
ax.fill_between(x='Class', y1='min', y2='max', data=petal_width,
                color=mpl.colors.to_rgba('green', 0.15))
plt.ylim(0,3)
plt.title("Petal Width", fontweight='bold')
plt.ylabel("Data for Petal Width (cm)")
plt.savefig('Petal Width Statistics.png')



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


# min, max and mean of each variable

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