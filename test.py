#import the modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
Iris = pd.read_csv("data/Iris.csv")

# Identify the number of NA values for each column
print(Iris.isnull().sum())
