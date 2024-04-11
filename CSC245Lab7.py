#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np

import pandas as pd 

from sklearn import datasets

from sklearn.datasets import load_breast_cancer 
cancer = load_breast_cancer() 

print(cancer.DESCR) 


# In[41]:


print(cancer.keys())


# In[42]:


#0 How many features does the breast cancer dataset have? This function should return an integer.
def how_many_features():
    return len(cancer.feature_names)
    
how_many_features()


# In[43]:


#question 1

def dataFrame_convert():
    data = numpy.c_[cancer.data,cancer.target] 
    columns = numpy.append(cancer.feature_names, ["target"]) 
     
    return pd.DataFrame(data, columns=columns) 
    
dataFrame_convert()



# In[45]:


# 2 What is the class distribution? (i.e. how many instances of malignant (encoded 0) and how many benign (encoded 1)?) 
#This function should return a Series named target of length 2 with integer values and index = ['malignant', 'benign']
""""def class_distribution():
    cancer_df = pd.DataFrame(data=np.c_[cancer.data, cancer.target], columns=np.append(cancer.feature_names, ['target']))
    target_distribution = cancer_df['target'].value_counts()
    target_distribution.index = ['malignant', 'benign']
    return target_distribution
class_distribution()"""


# In[54]:


# ANSWER 2
def class_distribution(): 
    
    cancerdf = dataFrame_convert()
    counts = cancerdf.target.value_counts(ascending=True) 
    counts.index = "malignant benign".split() 
    return counts 
 
class_distribution()


# In[47]:


#ANSWER 3
#Split the DataFrame into X (the data) and y (the labels). This function should return a tuple of length 2: 
#(X, y), where X, a pandas DataFrame, has shape (569, 30) y, a pandas Series, has shape (569,)
def split_dataFrame():
    cancer_df = pd.DataFrame(data=np.c_[cancer.data, cancer.target], columns=np.append(cancer.feature_names, ['target']))
    X = cancer_df[cancer.feature_names]
    Y = cancer_df['target']
    return X, Y
split_dataFrame()


# In[48]:


#ANSWER 4
#Using train_test_split, split X and y into training and test sets (X_train, X_test, y_train, and y_test).
from sklearn.model_selection import train_test_split 
 
def test_split(): 
    X, Y = split_dataFrame() 
    return train_test_split(X, Y, train_size=426, test_size=143, random_state=0) 
test_split()


# In[49]:


#ANSWER 5
#Using KNeighborsClassifier, fit a k-nearest neighbors (knn) classifier with X_train, y_train and using one nearest neighbor
#(n_neighbors = 1). This function should return a sklearn.neighbors.classification.KNeighborsClassifier.

from sklearn.neighbors import KNeighborsClassifier
def knn_model(): 
    X_train, X_test, Y_train, Y_test =test_split () 
    model = KNeighborsClassifier(n_neighbors=1) 
    model.fit(X_train, Y_train) 
    return model 
knn_model() 


# In[50]:


#ANSWER 6
def class_label(): 

    cancerdf = dataFrame_convert() 
    means = cancerdf.mean()[:-1].values.reshape(1, -1) 
    model = knn_model() 
    return model.predict(means) 
class_label()


# In[57]:


#ANSWER 7
#Using your knn classifier, predict the class labels for the test set X_test.
def class_label_2(): 
    X_train, X_test, Y_train, Y_test =test_split()  
    knn = knn_model()
    return knn.predict(X_test)
class_label_2()


# In[60]:


def answer_eight(): 
 
    X_train, X_test, Y_train, Y_test =test_split () 
    knn = knn_model() 
    return knn.score(X_test, Y_test) 
answer_eight() 
 
 
 


# In[ ]:




