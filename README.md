# **pands-project**

This repository stores the Pands project assigned as part of the Pands module.

The Pands module was undertaken in the first semester of Higher Diploma in Science in Computing in Data Analytics.

## **Table of Contents**

- [Introduction](#introduction)
- [Discussion of Previous Analyses](#discussion-of-previous-analyses)
- [My Analysis](#my-analysis---what-it-entails-how-python-is-used-to-do-it-how-to-run-the-python-code)
    - [Modules Imported](#modules-imported)
    - [Summary File](#summary-file)
         - [Distribution Line Plots](#distribution-line-plots)
         - [Histograms](#histograms)
         - [Scatter Plots](#scatter-plots)
         - [Pairplots](#pairplots)
    - [Graphs/Plots](#graphsplots)

- [References](#references)

## **Introduction** ##

The Iris dataset is one of the most well-known data sets in relation to pattern recognition.

The dataset was created in 1936 by R.A Fisher. It contains 3 classes, with each class referencing a type of iris plant. There are 50 instances of each class, with 150 instances in total.

Each class has 4 attributes, or variables, which are:

- Sepal length in centimetres
- Sepal width in centimetres
- Petal length in centimetres
- Petal width in centimetres

One class (Iris-setosa) is linearly separable from the other two, while the latter (Iris-versicolor and Iris-virginica) are not linearly separable from each other. [[1]](#1)

An image of the three Iris plant species referred to in the dataset can be seen below:

![Iris Plants](https://github.com/rachel-king4/pands-project/blob/main/Iris%20plants.jpg)

## **Discussion of Previous Analyses** ##

The Iris data set is one of the most analysed data sets available on the internet. As it is a simple dataset, with four variables of three species of Iris plant, with each species having 50 instances each, much of the previous analyses are similar in nature.

Most analysis of the data uses scatter plots and pair plots to show that the species Iris-setosa is linearly separable from the other two species (Iris-virginica and Iris-versicolor).
From the scatter plots comparing sepal length and sepal width, it is clear that the Iris-setosa species is separable from the other two species as it has smaller sepal lengths and larger sepal widths than the other two species. The Iris-virginica and Iris-versicolor data is not distinguishable from each other. [[2]](#2) [[3]](#3)

In particular, pair plots which show relationships between two variables [[4]](#4) are used to display trends and show this linear separability of the Iris-setosa species from Iris-virginica and Iris-versiscolor, while also showing that the virginica and versicolor species are not linearly separable from each other. [[5]](#5)
Linear separability exists if there is at least one line in the plane which separates datapoints of one class from datapoints of the other class. [[6]](#6)

Box plots and violin plots are also often used to show distribution and outliers. From the box plots, it is clear that Iris-setosa has the smallest features, with the lowest mean and quite little distribution for petal length, petal width and sepal length. [[7]](#7) [[8]](#8)
Violin plots also show distribution, whereby the fatter part of the plot show highly dense amount of data while the thinner plot represents less dense or low amount of datapoints. 
From the violin plots, it is clear that Iris-setosa has low distribution of data for features petal length and petal width, with the plots appearing quite wide in nature. In contrast to this, Iris-versicolor has long and narrow violin plots for features petal width and sepal length, representing data which is widely distributed. [[3]](#3)


One particular analysis used correlation plots which show which variables display good correlation and which have no correlation. Petal length and petal width have extremely high correlation, with results of 0.96 (1 being 100% correlation). Sepal and petal length also show very good correlation, with a result of 0.87. [[9]](#9)

Another interesting type of analysis focused on predictive analysis which can give predictions on the species for a given value of a variable. i.e. if petal length is < 2.1, the species is highly likely to be Iris-setosa, if petal length is > 4.8 it's highly likely to be Iris-virginica.
From the pairplots, it is clear petal length displays the clearest differentiation between the three species types. Therefore, petal length is a good variable to choose when performing this analysis. [[3]](#3)
Scikit-learn is used to perform predictive analysis also, again where the species type can be predicted when values for each variable are chosen. [[10]](#10)


## **My Analysis** ##

Performing exploratory data analysis means to analyse data using visual techniques. Python can be used to do this as it enables trends/patterns to be identified.

### **Modules Imported** ###

A number of modules were imported to aid in the analysis and visualisation of the data:

- Pandas (a Python library used for working with datasets and is used to analyse, explore and manipulate data) [[11]](#11)
- Numpy (a Python library used for working with arrays) [[12]](#12)
- Matplotlib (a Python library used for plotting data and for visualisation) [[13]](#13)
- Tabulate (a Python package used to print tabular data in nicely formatted tables) [[14]](#14)
- Seaborn (a Python library used for data visualisation - provides informative statistical graphics) [[15]](#15)
- Sys (a Python module that provides functions and variables that are used to manipulate parts of the Python runtime environment) [[16]](#16)

These modules are very useful as they enable data to be analysed, structured into readable and well-formatted tables & graphs and provide control over the input and output of the program.
This is very important when trying to create a clear picture of the story of the data and what it represents.

The dataset is imported into the workspace directly from its URL. [[17]](#17)
It is then stored as a variable *iris* so it can be called to analyse and visualise the data it contains.

```
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_url, names = col_names)
```

### **Summary File** ###

A summary file was created which displays a number of tables.
The first table displays a table of statistics of the dataset as a whole, while the remaining four tables display statistics such as mean, min and max for each of the 4 variables when grouped together by class. [[24]](#24)

sys.stdout was used to output the print commands to the txt file. [[18]](#18) (Note: I initially used f.write for this part of the program but I couldn't get satisfactory results to output the tables to the txt file, so from research of how to write a table to a file using print I discovered sys.stout)

```
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
    print(tabulate(table_of_data, headers = ["Class", "Mean (cm)", "Min (cm)", "Max (cm)"], tablefmt='grid', stralign='center'), file=f)
    print('\n')
```

A lot of inference can be made about the data from these tables alone. In particular, that the Iris-setosa species/class is the smallest of the three, as it has the lowest mean for 3 of the 4 characteristics of the plant represented in the dataset. In contrast to this, Iris-virginica is, generally speaking, the largest species/class, as it has the highest mean for 3 of the 4 characteristics.

### **Graphs/Plots** ###

To visualise the data, a variety of graphs and plots were created using the Python modules outlined above. These provide great insight into the data and what it represents in relation to the three species of Iris plant.

These plots were all created as functions, so they could be called together at the end of the code. In my opinion, this makes the code neater and easier to read/follow.
When the program is run, the last 4 lines of code (lines 222-225) call the code written inside the functions for each of the plots/graphs for which code was written for in the program.

#### **Line Plots** ####

Line plots were created which display the mean of each of the four variables when the data is grouped by species/class. [[20]](#20)

```
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
```

The code above is used to generate a line plot for the variable Sepal Length. The output is saved as a png file which can be seen below.

![Sepal Length LP output](https://github.com/rachel-king4/pands-project/blob/main/Sepal%20Length%20LP.png)

The line represents the mean for each of the three Iris plant species, while the shaded region shows the distribution of data from the minimum to the maximum data point for each species.


#### **Histograms** ####

Histograms were created for each of the four variables. Histograms display the distribution of the data points of each variable as a series of bars.

Four histograms were created, one for each variable. The Iris species were overlapped on each histogram [[19]](#19) to allow comparison of the data and good visualisation of the similarities and differences in each Iris plant species.

The histograms were also stacked as subplots in a 2x2 format for a cleaner display of the data. [[21]](#21)

Part of the code is seen below ([0,0] is the subplot that be displayed in the first row, first column; [0,1] is first row, second column; etc.):

```
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
```

![Histograms output](https://github.com/rachel-king4/pands-project/blob/main/Histograms.png)

#### **Scatter Plots** ####

Scatter plots were created for each pair of variables (Sepal Length vs Sepal Width and Petal Length vs Petal Width). Scatter plots show the relationship between two variables, which allow viewers to easily identify any trends. [[22]](#22)

Two scatter plots were created for each of the pairs of variables [[23]](#23)

```
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
```

![Petal Length vs Width Scatter Output](https://github.com/rachel-king4/pands-project/blob/main/Petal%20Length%20vs%20Petal%20Width.png)

This particular plot indicates there is very good correlation between these two variables (petal length and petal width). Perfect correlation (R-squared = 1) is outlined by a diagonal straight line from the point 0,0 on the scatter plot (the intersection of the x and y axes).

It's also clear from these scatter plots, that the Iris-setosa species is linearly separable from the other two species.


#### **Pairplots** ####

Pairplots were created to, again, show the relationship between the variables and display trends.

Pairplots were created using the Seaborn module. As there are four variables in the Iris dataset, three scatter plots are created for each variable (12 in total) and one distribution plot for each variable (4 in total). Overall, 16 plots were created and displayed as subplots in a 4x4 format. [[3]](#3)

```
sns.pairplot(iris, hue = "Class", height=4, palette=['blue', 'purple', 'blueviolet'])
    plt.savefig("Pairplot")
```

![Pairplot Output](https://github.com/rachel-king4/pands-project/blob/main/Pairplot.png)

The pairplots provide a very nice visualisation of the data. It is very clear from these plots that the Iris-setosa is the smallest of the Iris plant species and is clearly independent of the other two species. 

## **References**

<a id="1">[1]</a>
(Angela1c [2021](https://www.angela1c.com/projects/iris_project/the-iris-dataset/))

<a id="2">[2]</a>
(GeeksforGeeks [n.d](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/))

<a id="3">[3]</a>
(Medium.com [2021](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202))

<a id="4">[4]</a>
(Towardsdatascience.com [2018](https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166))

<a id="5">[5]</a>
(Scaler.com [2023](https://www.scaler.com/topics/machine-learning/iris-dataset-project/))

<a id="6">[6]</a>
(mylearningsinaiml [ n.d.](https://mylearningsinaiml.wordpress.com/concepts/linearly-separable-data/))

<a id="7">[7]</a>
(Medium.com [2021](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202))

<a id="8">[8]</a>
(Level Up Coding [2016](https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d))

<a id="9">[9]</a>
(Kaggle.com [2018](https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis))

<a id="10">[10]</a>
(Scaler.com [2023](https://www.scaler.com/topics/machine-learning/iris-dataset-project/))

<a id="11">[11]</a>
(W3schools.com [ n.d.](https://www.w3schools.com/python/pandas/pandas_intro.asp))

<a id="12">[12]</a>
(W3schools.com [ n.d.](https://www.w3schools.com/python/numpy/numpy_intro.asp))

<a id="13">[13]</a>
(W3schools.com [ n.d.](https://www.w3schools.com/python/matplotlib_intro.asp))

<a id="14">[14]</a>
(Analytics India Mag [2020](https://analyticsindiamag.com/beginners-guide-to-tabulate-python-tool-for-creating-nicely-formatted-tables/#:~:text=Tabulate%20is%20an%20open%2Dsource,downloaded%20in%20multiple%20output%20formats))

<a id="15">[15]</a>
(Seaborn.pydata.org [2012](https://seaborn.pydata.org/))

<a id="16">[16]</a>
(GeeksForGeeks.com [ n.d.](https://www.geeksforgeeks.org/python-sys-module/))

<a id="17">[17]</a>
(Angela1c [2021](https://www.angela1c.com/projects/iris_project/the-iris-dataset/))

<a id="18">[18]</a>
(Stackoverflow.com [2011](https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file))

<a id="19">[19]</a>
(Datavizpyr.com [2020](https://datavizpyr.com/overlapping-histograms-with-matplotlib-in-python/))

<a id="20">[20]</a>
(Stackoverflow.com [2022](https://stackoverflow.com/questions/74171240/python-linear-chart-with-min-max-and-avg))

<a id="21">[21]</a>
(Matplotlib.org [ n.d.](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html))

<a id="22">[22]</a>
(tibco.com [ n.d.](https://www.tibco.com/reference-center/what-is-a-scatter-chart#:~:text=A%20scatter%20chart%2C%20also%20called,in%20almost%20any%20other%20form))

<a id="23">[23]</a>
(GeeksForGeeks.com [ n.d.](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/))

<a id="24">[24]</a>
(Jamesrledoux.com [2019](https://jamesrledoux.com/code/group-by-aggregate-pandas))
