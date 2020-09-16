#import the modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
Iris = pd.read_csv("Iris.csv")
check = pd.isnull(Iris["SepalLengthCm"])
check = pd.isnull(Iris["SepalWidthCm"])
check = pd.isnull(Iris["PetalLengthCm"])
check = pd.isnull(Iris["PetalWidthCm"])
Iris[check]
