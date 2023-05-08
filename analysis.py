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
import seaborn as sns
import sys

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# using the attribute information as the column names
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_url, names = col_names)

# Summary of each Variable
def summary():
    f = open('summary.txt', 'w')
    sys.stdout = f
    print("A table of statistics for each variable can be seen below.")
    print("The first table displays statistics of the data set as a whole, while Tables 2,3,4 and 5")
    print("display statistics such as mean, min and max for each of the 4 variables when grouped together by class.\n")

    print("Table 1 - Iris Dataset Statistics")
    iris_stats = iris.agg({'Sepal_Length': ['mean', 'min', 'max', 'std'],
                           'Sepal_Width': ['mean', 'min', 'max', 'std'],
                           'Petal_Length': ['mean', 'min', 'max', 'std'],
                           'Petal_Width': ['mean', 'min', 'max', 'std']})
    print(tabulate(iris_stats, headers = ["Stat", "Sepal_Length (cm)", "Sepal_Width (cm)", "Petal_Length (cm)", "Petal_Width (cm)"], tablefmt='grid', stralign='center'), file=f)
    print('\n')

    # Sepal Length Statistics
    print("Table 2 - Iris Dataset Sepal Length Statistics")
    table_of_data = iris.groupby('Class').agg({'Sepal_Length': ['mean', 'min', 'max']})
    table_of_data.reset_index(inplace=False)
    #with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean (cm)", "Min (cm)", "Max (cm)"], tablefmt='grid', stralign='center'), file=f)
    print('\n')

    # Sepal Width Statistics
    print("Table 3 - Iris Dataset Sepal Width Statistics")
    table_of_data = iris.groupby('Class').agg({'Sepal_Width': ['mean', 'min', 'max']})
    table_of_data.reset_index(inplace=False)
    #with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean (cm)", "Min (cm)", "Max (cm)"], tablefmt='grid', stralign='center'), file=f)
    print('\n')

    # Petal Length Statistics
    print("Table 4 - Iris Dataset Petal Length Statistics")
    table_of_data = iris.groupby('Class').agg({'Petal_Length': ['mean', 'min', 'max']})
    table_of_data.reset_index(inplace=False)
    #with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean (cm)", "Min (cm)", "Max (cm)"], tablefmt='grid', stralign='center'), file=f)
    print('\n')

    # Petal Width Statistics
    print("Table 5 - Iris Dataset Petal Width Statistics")
    table_of_data = iris.groupby('Class').agg({'Petal_Width': ['mean', 'min', 'max']})
    table_of_data.reset_index(inplace=False)
    #with open('summary.txt', 'a') as f:
    print(tabulate(table_of_data, headers = ["Class", "Mean (cm)", "Min (cm)", "Max (cm)"], tablefmt='grid', stralign='center'), file=f)
    print("\n")

    print("Sepal Length is the largest variable, with a mean of 5.8, while Petal Width is the smallest with a mean of 1.2.")
    print("The largest Sepal Lengths occur in the Iris virginica species while the smallest occur in the Iris setosa.")
    print("However, Iris setosa represents the largest Sepal Widths. \n\n")
    print("For the petal characteristics then, Petal Length and Petal Width are both largest in the Iris virginica species, and smallest in the Iris setosa species.")
    print("Petal Length is the variable with the widest spread of data, with a standard deviation of 1.7 and a range from a minimum of 1 to a maximum of 6.9.")
    print("Sepal Width then is the variable with the smallest spread of data, as all three species of Iris plant have similar sepal widths.")
    f.close()

summary()

# Distribution Line Plots
def distributionlineplots():
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
    plt.savefig('Sepal Length DLP.png')


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
    plt.savefig('Sepal Width DLP.png')


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
    plt.savefig('Petal Width DLP.png')


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
    plt.savefig('Petal Length DLP.png')


# histograms for each variable
def hist():
    fig, axes = plt.subplots(2,2, figsize = (15,15))
    setosa = iris[iris.Class == "Iris-setosa"]
    versicolor = iris[iris.Class == "Iris-versicolor"]
    virginica = iris[iris.Class == "Iris-virginica"]

    # sepal length histogram 
    axes[0,0].set_title("Sepal Length", fontweight='bold')
    axes[0,0].set(xlabel='Sepal Length')
    axes[0,0].hist(setosa['Sepal_Length'], bins=7, alpha=0.5, label="Iris-setosa", color='blue')
    axes[0,0].hist(versicolor['Sepal_Length'], bins=7, alpha=0.5, label="Iris-versicolor", color='purple')
    axes[0,0].hist(virginica['Sepal_Length'], bins=7, alpha=0.5, label="Iris-virginica", color='indigo')
    axes[0,0].legend(loc='upper right')
    
    # sepal width histogram 
    axes[0,1].set_title("Sepal Width", fontweight='bold')
    axes[0,1].set(xlabel='Sepal Width')
    axes[0,1].hist(setosa['Sepal_Width'], bins=5, alpha=0.5, label="Iris-setosa", color='blue')
    axes[0,1].hist(versicolor['Sepal_Width'], bins=5, alpha=0.5, label="Iris-versicolor", color='purple')
    axes[0,1].hist(virginica['Sepal_Width'], bins=5, alpha=0.5, label="Iris-virginica", color='indigo')
    axes[0,1].legend(loc='upper right');

    # petal length histogram 
    axes[1,0].set_title("Petal Length", fontweight='bold')
    axes[1,0].set(xlabel='Petal Length')
    axes[1,0].hist(setosa['Petal_Length'], bins=6, alpha=0.5, label="Iris-setosa", color='blue')
    axes[1,0].hist(versicolor['Petal_Length'], bins=6, alpha=0.5, label="Iris-versicolor", color='purple')
    axes[1,0].hist(virginica['Petal_Length'], bins=6, alpha=0.5, label="Iris-virginica", color='indigo')
    axes[1,0].legend(loc='upper right');

    # petal width histogram 
    axes[1,1].set_title("Petal Width", fontweight='bold')
    axes[1,1].set(xlabel='Petal Width')
    axes[1,1].hist(setosa['Petal_Width'], bins=6, alpha=0.5, label="Iris-setosa", color='blue')
    axes[1,1].hist(versicolor['Petal_Width'], bins=6, alpha=0.5, label="Iris-versicolor", color='purple')
    axes[1,1].hist(virginica['Petal_Width'], bins=6, alpha=0.5, label="Iris-virginica", color='indigo')
    axes[1,1].legend(loc='upper right');

    for ax in axes.flat:
        ax.set(ylabel='No. of Occurrences')   # as y label is the same for all histograms

    fig.savefig('Histograms.png')

# scatter plots of each pair of variables
def scatter():
    # sepal length vs width
    fig, ax = plt.subplots()
    colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'purple' , 
            'Iris-virginica': 'indigo'}

    grouped = iris.groupby('Class')
    for key, group in grouped:
        group.plot(ax=ax, kind='scatter', x='Sepal_Length', y='Sepal_Width', label=key, color=colors[key])

    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.savefig('Sepal Length vs Sepal Width.png')


    # petal length vs width
    fig, ax = plt.subplots()
    colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'purple' , 
            'Iris-virginica': 'indigo'}

    grouped = iris.groupby('Class')
    for key, group in grouped:
        group.plot(ax=ax, kind='scatter', x='Petal_Length', y='Petal_Width', label=key, color=colors[key])

    plt.legend()
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.savefig('Petal Length vs Petal Width.png')

def pair():
    sns.pairplot(iris, hue = "Class", height=4, palette=['blue', 'purple', 'blueviolet'])
    plt.savefig("Pairplot")


distributionlineplots()
hist()
scatter()
pair()