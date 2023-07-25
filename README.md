#  Linear Regression Using Least Squares **LLS** 

# **abalone** 

![image](lls.png)



## In the csv file of the [abalone](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset), we are looking to predict its height by receiving the length of the abalone


## plot 


### Display the Pairs plot (pairwise plot) in seaborn 

![Alt text](image.png)


###  Display the confusion matrix diagram with matplotlib


![Alt text](image-1.png)


###  Display the slope of a line  with matplotlib

![Alt text](image-2.png)

----


# **Students Performance (Regression)**

## Generate continuous random dataset for the problem of X = study hours and Y = grade of students (if you study more, you will get a higher grade)


![Alt text](image-3.png)



----

## Draw some wrong red lines with a random slope


![Alt text](image-4.png)



## Draw the correct blue line using your Object Oriented Linear Least Squares (LLS) method

![Alt text](image-5.png)



## Draw a green line using linregress from scipy library. Compare your result with scipy's result.


![Alt text](image-6.png)

-----


# **Boston house-prices (Regression)**


![Alt text](image-11.png)



###  Display the confusion matrix diagram with matplotlib



![Alt text](image-7.png)


----


### Display the Pairs plot (pairwise plot) in seaborn 

![Alt text](image-8.png)

----

## Exploratory Data Analysis
Exploratory Data Analysis is a very important step before training the model. In this section, we will use some visualizations to understand the relationship of the target variable with other features.

Let’s first plot the distribution of the target variable price. We will use the distplot function from the seaborn library.


![Alt text](image-9.png)


----

### This dataset has 13 features for each house. According to data correlation and your analysis, choose 2 features for X, for example:
**X = area and age**
### and choose 1 target for Y:

**Y = price**


![Alt text](image-10.png)
