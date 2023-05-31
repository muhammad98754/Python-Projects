"""Imagine you have a data series that represents the amount of precipitation each day for a year in a given city."""

import numpy as np
import pandas as pd

data = pd.read_csv("Seattle2014.csv")
print(data.head())

rainfall = data["PRCP"].values
inches = rainfall/254
print(inches.shape)

"""Before we go ahead with this task, let’s take a quick look at the rainy day histogram using matplotlib:"""

import matplotlib.pyplot as plt
import seaborn
seaborn.set()
plt.hist(inches, 40)
plt.show()

"""to perform the task of numerical computing in python we can easily perform our tasks using the NumPy package in Python. So let’s perform some necessary NumPy functions for numerical computing with Python.

Using the numerical calculation functions using NumPy, we could begin to answer the types of questions we receive about our precipitation data. Here are some examples of results we can calculate for counting rainy days using Python:"""

print("Number of days without rain: ", np.sum(inches == 0))
print("Number of days with rain: ", np.sum(inches != 0))
print("Number of days with rain more than 0.5 inches: ", np.sum(inches>0.5))
print("Number of days with rain < 0.2 inches: ", np.sum((inches > 0)& (inches < 0.2)))

