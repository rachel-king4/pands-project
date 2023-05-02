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

Lots of analyses done on this data set.
Uses box plots, violin plots etc to show distribution and outliers. 
Correlation plots which show which variables display good correlation and which have no correlation
Petal length and width have the highest correlation - setosa has low petal length and width, versiscolor has medium and virginica has the largest
Sepal length and width - setosa has small length and large width. Versicolor is in the middle for both. Virginica has large length but medium widths.

Predictive analysis which can give predictions on the species for a given value for each variable is chosen. 
i.e if petal length is < 2.1, the species is highly likely to be Iris-setosa, if > 4.8 it's highly likely to be Iris-virginica





## **My Analysis - what it entails, how Python is used to do it, how to run the Python code, what the code does** ##

Performing exploratory data analysis means to analyse data using visual techniques. Python can be used to do this. It enables trends/patterns to be identified.

My analysis shows basic statistics in relation to mean, median, min and max.
Histogram shows the distribution as well as the line plot with shading which shows a good visual on the distribution of data for each species for each of the 4 variables.
Scatter plots show the relationship between sepal length & width and petal length & width



## **References**


https://www.angela1c.com/projects/iris_project/downloading-iris/  - reference for reading in the file from a URL

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ - reference for some of the data plots by Class

https://stackoverflow.com/questions/74171240/python-linear-chart-with-min-max-and-avg - graph the mean with min and max shaded

https://jamesrledoux.com/code/group-by-aggregate-pandas - table of mean, min and max data

