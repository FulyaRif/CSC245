#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
#import csv
path_to_folder= ('C:/Users/fulya/Downloads/')
file_name='titanic.csv'
titanic_df=pd.read_csv(path_to_folder+file_name)

print(titanic_df.info())


# In[7]:


print("Column Labels:")
print(titanic_df.columns)

print("\nShape:")
print(titanic_df.shape)

print("\nData Types:")
print(titanic_df.dtypes)


# In[9]:


#create pivot table
pivot_table = titanic_df.pivot_table(index=['sex', 'pclass'])
print(pivot_table)


# In[12]:


pivot_table = titanic_df.pivot_table(index='sex', values='survived', aggfunc='mean')
print(pivot_table)


# In[10]:


pivot_table = titanic_df.pivot_table(index='sex', columns='pclass', values='survived', aggfunc='mean')
print(pivot_table)


# In[13]:


pivot_table = titanic_df.pivot_table(index=['sex', pd.cut(titanic_df['age'], [0, 10, 30, 60, 80])], columns='pclass', values='survived', aggfunc='mean')
print(pivot_table)


# In[14]:


age_categories = pd.cut(titanic_df['age'], bins=[0, 10, 30, 60, 80])
print(age_categories)


# In[16]:


pivot_table = titanic_df.pivot_table(index=['sex', age_categories], columns='pclass', values='survived', aggfunc='count')
print(pivot_table)


# In[17]:


pivot_table = titanic_df.pivot_table(index=['sex', age_categories], columns='pclass', values='survived', aggfunc='mean')
print(pivot_table)


# In[18]:


fare_categories = pd.qcut(titanic_df['fare'], q=2)
pivot_table = titanic_df.pivot_table(index=['sex', age_categories], columns=['pclass', fare_categories], values='survived', aggfunc='mean')
print(pivot_table)


# In[ ]:




