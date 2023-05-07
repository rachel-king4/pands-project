# **pands-project**

## **Table of Contents**

- [Introduction](#introduction)
- [Discussion of Previous Analyses](#discussion-of-previous-analyses)
- [My Analysis](#my-analysis---what-it-entails-how-python-is-used-to-do-it-how-to-run-the-python-code)
- [References](#references)

## **Introduction** ##

The Iris dataset is one of the most well-known data sets in relation to pattern recognition.

It contains 3 classes, with each class referencing a type of iris plant. There are 50 instances of each class, with 150 instances in total.

Each class has 4 attributes, or variables, which are:

- Sepal length in centimetres
- Sepal width in centimetres
- Petal length in centimetres
- Petal width in centimetres

One class (Iris-setosa) is linearly separable from the other two, while the latter (Iris-versicolor and Iris-virginica) are not linearly separable from each other.

 

## **Discussion of Previous Analyses** ##

The Iris data set is one of the most analysed data sets available on the internet. As it is a simple dataset, with four variables of three species of Iris plant, with each species having 50 instances each, much of the previous analyses are similar in nature.

Most analysis of the data uses scatter plots and pair plots to show that the species Iris-setosa is linearly separable from the other two species (Iris-virginica and Iris-versicolor).
From the scatter plots comparing sepal length and sepal width, it is clear that the Iris-setosa species is separable from the other two species as it has smaller sepal lengths and larger sepal widths than the other two species. The Iris-virginica and Iris-versicolor data is not distinguishable from each other. [a] [b]

In particular, pair plots which show relationships between two variables [c] are used to display trends and show this linear separability of the Iris-setosa species from Iris-virginica and Iris-versiscolor, while also showing that the virginica and versicolor species are not linearly separable from each other. [d]
Linear separability exists if there is at least one line in the plane which separates datapoints of one class from datapoints of the other class. [e]

Box plots and violin plots are also often used to show distribution and outliers. From the box plots, it is clear that Iris-setosa has the smallest features, with the lowest mean and quite little distribution for petal length, petal width and sepal length. [f] [g]
Violin plots also show distribution, whereby the fatter part of the plot show highly dense amount of data while the thinner plot represents less dense or low amount of datapoints. 
From the violin plots, it is clear that Iris-setosa has low distribution of data for features petal length and petal width, with the plots appearing quite wide in nature. In contrast to this, Iris-versicolor has long and narrow violin plots for features petal width and sepal length, representing data which is widely distributed. [b]


One particular analysis used correlation plots which show which variables display good correlation and which have no correlation. Petal length and petal width have extremely high correlation, with results of 0.96 (1 being 100% correlation). Sepal and petal length also show very good correlation, with a result of 0.87. [h]

Another interesting type of anlaysis focused on predictive analysis which can give predictions on the species for a given value of a variable. i.e. if petal length is < 2.1, the species is highly likely to be Iris-setosa, if opetal length is > 4.8 it's highly likely to be Iris-virginica.
From the pairplots, it is clear petal length displays the clearest differentiation between the three species types. Therefore, petal length is a good variable to choose when perfomring this analysis. [b]
Scikit-learn is used to perform predictive analysis also, again where the species type can be predicted when values for each variable are chosen. [i]





## **My Analysis - what it entails, how Python is used to do it, how to run the Python code, what the code does** ##

Performing exploratory data analysis means to analyse data using visual techniques. Python can be used to do this. It enables trends/patterns to be identified.


Numpy, matplotlib, sys, tabulate etc - what they are and why they're useful for this
My analysis shows basic statistics in relation to mean, median, min and max.
Summary of each variable and what the data shows
Summary - put a few summary tables (count, descrivbe,info etc). Then put the stats table for each variable and write to the summary.txt file.
Remove the discussion of the variables and add it to the summary above

Histogram shows the distribution as well as the line plot with shading which shows a good visual on the distribution of data for each species for each of the 4 variables.
Scatter plots show the relationship between sepal length & width and petal length & width

## **References**

[a] https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
[b] https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202.1%2C%20then,then%20species%20is%20Iris%20Virginica
[c] https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
[d] https://www.scaler.com/topics/machine-learning/iris-dataset-project/
[e] https://mylearningsinaiml.wordpress.com/concepts/linearly-separable-data/
[f] https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202.1%2C%20then,then%20species%20is%20Iris%20Virginica
[g] https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d
[h] https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis
[i] https://www.scaler.com/topics/machine-learning/iris-dataset-project/


https://www.angela1c.com/projects/iris_project/downloading-iris/  - reference for reading in the file from a URL

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ - reference for some of the data plots by Class

https://stackoverflow.com/questions/74171240/python-linear-chart-with-min-max-and-avg - graph the mean with min and max shaded

https://jamesrledoux.com/code/group-by-aggregate-pandas - table of mean, min and max data

https://datavizpyr.com/overlapping-histograms-with-matplotlib-in-python/ - overlapping histograms

https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html - stacking the histograms as subplots 2 x 2

https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file - to write a table to a file. tried to do this
using f.write but i couldnt get it to work, so i researched how to write a table to a file using print and i discovered sys.stdout
