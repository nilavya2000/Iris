#import the modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import the dataset
data=pd.read_csv('data/Iris.csv')  #import the data
print("\n",data.head())  #print the data
print("\n",data.describe().T)    #it shows all the details of the data(mean, no_of_data, min,..etc)
print("\n",data.isnull().sum())  #check if there is any null value or not


#visualise the data
sns.pairplot(data, hue='Species')   #Clasify the data w.r.t to Species
plt.show()
