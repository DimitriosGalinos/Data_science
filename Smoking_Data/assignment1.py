# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:45:57 2020

@author: Dimitrios Galinos
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import t
from scipy.stats import pearsonr

############################### Exercise 1 ####################################

data = np.loadtxt('smoking.txt')

smokers=np.array([])
non_smokers=np.array([])

flag1=0
flag2=0

# Dividing the dataset into two numpy arrays
for x in range(len(data)):
    if data[x,4]==1:
        if flag1==0:
            flag1=1
            smokers=data[x]
        else:
            smokers=np.vstack((smokers, data[x]))
    else:
        if flag2==0:
            flag2=1
            non_smokers=data[x]
        else:
            non_smokers=np.vstack((non_smokers, data[x]))

# Finding the mean FEV1 for the two groups
avg_lng_smok=np.mean(smokers[:,1])
avg_lng_non_smok=np.mean(non_smokers[:,1])

print("The average lung function, measured in FEV1, among the smokers is "+
      str(avg_lng_smok)+" and among the non-smokers is "+str(avg_lng_non_smok))

############################### Exercise 2 ####################################

# Preparing the data for the boxplot
boxdata=[None]*2
boxdata[0]=non_smokers[:,1]
boxdata[1]=smokers[:,1]

# Making the boxplot
plt.boxplot(boxdata, labels=["Non-smokers", "Smokers"])
plt.title('Boxplot of the lung function, measured in FEV1, among '+
          "smokers and non-smokers")
plt.ylabel('Lung function, measured in FEV1')
plt.show()

############################### Exercise 3 ####################################

# Using scipy's ttest_ind just to check it out
ttest,pval = ttest_ind(smokers[:,1],non_smokers[:,1], equal_var = False)
print("\nThe p-value from ttest_ind is:",pval)

# Doing it on my own as requested
# Finding the sample variance and size of the groups
smok_var=np.var(smokers[:,1], ddof=1)
non_smok_var=np.var(non_smokers[:,1], ddof=1)
n_smok=len(smokers[:,1])
n_non_smok=len(non_smokers[:,1])

# Calculating the T-statistic
Taf=(avg_lng_smok-avg_lng_non_smok)/math.sqrt(smok_var/n_smok
                                         +non_smok_var/n_non_smok)

print("Our T-statistic is: "+str(Taf))

# Calculating the degrees of freedom
degreesoffreedom=((smok_var/n_smok+non_smok_var/n_non_smok)**2)/((smok_var**2)
     /((n_smok-1)*n_smok**2)+(non_smok_var**2)/((n_non_smok-1)*n_non_smok**2))
# and getting the rounded floor of it
degreesoffreedom=math.floor(degreesoffreedom)
print("Our degrees of freedom are :"+str(degreesoffreedom))

# Calculate the p-value
p=2*t.cdf(-Taf, degreesoffreedom)
print("Our p value is: "+str(p))

# Reject or accept the null-hypothesis
if p <0.05:
  print("we reject the null hypothesis")
else:
  print("we accept the null hypothesis")
  
############################### Exercise 4 ####################################
  
# I did a barplot because I think it looks the best
plt.bar(non_smokers[:,0], non_smokers[:,1], color="lightblue", 
        label="Non Smokers")
plt.bar(smokers[:,0], smokers[:,1], color="green", label="Smokers")
plt.legend()
plt.xlabel('Age')
plt.ylabel('Lung function, measured in FEV1')
plt.show()

# And I also did a scatter plot because somebody might prefer that
plt.scatter(non_smokers[:,0], non_smokers[:,1], color="lightblue", 
            label="Non Smokers")
plt.scatter(smokers[:,0], smokers[:,1], color="green", label="Smokers")
plt.legend()
plt.xlabel('Age')
plt.ylabel('Lung function, measured in FEV1')
plt.show()

# Calculate Pearson's correlation coefficient between age and FEV1 for the 
# whole dataset
Pear=pearsonr(data[:,0], data[:,1])
print("\nPearson's correlation coefficient between age and FEV1 for the whole"
      +" dataset is: "+str(Pear[0]))
############################### Exercise 5 ####################################

# I did a histogram with both groups combined because I think that makes more 
# sense than 2 different histograms of the two groups
plt.hist(non_smokers[:,0], color="orange", label='Non Smokers')
plt.hist(smokers[:,0], color='lightgreen', label='Smokers')
plt.xlabel('Ages')
plt.ylabel('Count')
plt.title('Histogram over the age of the subjects in each of the two groups')
plt.legend()
plt.show()

# I created the 2 histograms as requested by the exercise
plt.hist(non_smokers[:,0], color="orange", label='Non Smokers')
plt.xlabel('Ages of the Non Smoking group')
plt.ylabel('Count')
plt.title('Histogram over the age of the subjects in the Non Smoking group')
plt.legend()
plt.show()

plt.hist(smokers[:,0], color='lightgreen', label='Smokers')
plt.xlabel('Ages of the Smoker group')
plt.ylabel('Count')
plt.title('Histogram over the age of the subjects in the Smoker group')
plt.legend()
plt.show()
