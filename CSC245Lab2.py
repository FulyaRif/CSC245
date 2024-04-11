#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
#Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
data = pd.Series([1, 2, 3, 4, 5])
print("Pandas Series:")
print(data)


# In[2]:


#Write a Pandas program to convert a Panda module Series to Python list and it's type
data_list = data.tolist()
print("Converted Python list:", data_list)
print("Type of converted list:", type(data_list))


# In[3]:


#Write a Pandas program to add, subtract, multiple and divide two Pandas Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])
addition = series1 + series2

subtraction = series1 - series2

multiplication = series1 * series2

division = series1 / series2

# Display the results
print("Addition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)


# In[4]:


#Write a Pandas program to compare the elements of the two Pandas Series.
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
comparison_result = series1 == series2

print("Comparison Result:")
print(comparison_result)


# In[5]:


#Write a Pandas program to convert a dictionary to a Pandas series
original_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}


converted_series = pd.Series(original_dict)

print("Converted Series:")
print(converted_series)


# In[7]:


#Write a Pandas program to convert a NumPy array to a Pandas series. 
numpy_array = np.array([10, 20, 30, 40, 50])

converted_series = pd.Series(numpy_array)

print("Converted Pandas Series:")
print(converted_series)


# In[8]:


#Write a Pandas program to change the data type of given a column or a Series.
original_series = pd.Series(['100', '200', 'python', '300.12', '400'])

converted_series = pd.to_numeric(original_series, errors='coerce')

print("Changed Data Type Series:")
print(converted_series)


# In[9]:


#Write a Pandas program to convert the first column of a DataFrame as a Series
data = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}
df = pd.DataFrame(data)

first_column_series = df['col1']

print("1st column as a Series:")
print(first_column_series)

print(type(first_column_series))


# In[10]:


# Write a Pandas program to convert a given Series to an array.
data_series = pd.Series(['100', '200', 'python', '300.12', '400'])

array_from_series = data_series.values
print("Original Data Series:")
print(data_series)

print("Series to an array:")
print(array_from_series)

print(type(array_from_series))


# In[11]:


#Write a Pandas program to create a dataframe from a dictionary and display it.
data = {'X': [78, 85, 96, 80, 86],
        'Y': [84, 94, 89, 83, 86],
        'Z': [86, 97, 96, 72, 83]}


df = pd.DataFrame(data)

print(df)


# In[12]:


#Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from dictionary data with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print(df)


# In[13]:


#Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
print(df.info())


# In[14]:


#Print first 3 rows
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from dictionary data with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Get the first 3 rows of the DataFrame
first_three_rows = df.head(3)

# Display the first 3 rows
print("First 3 rows of the DataFrame:")
print(first_three_rows)


# In[15]:


#Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
selected_columns = df[['name', 'score']]

print("Select specific columns:")
print(selected_columns)


# In[16]:


selected_data = df.loc[['b', 'd', 'f', 'g'], ['score', 'qualify']]
print("Select specific columns and rows:")
print(selected_data)


# In[17]:


#print attempts greater than 2
selected_rows = df[df['attempts'] > 2]

print("Number of attempts in the examination is greater than 2:")
print(selected_rows)


# In[19]:


# Write a Pandas program to count the number of rows and columns of a DataFrame.
num_rows, num_columns = df.shape

# Display the number of rows and columns
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)


# In[20]:


# Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
missing_score_rows = df[df['score'].isna()]
print("Rows where the score is missing:")
print(missing_score_rows)


# In[21]:


#Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
selected_rows = df[(df['score'] >= 15) & (df['score'] <= 20)]

print("Rows where the score is between 15 and 20 (inclusive):")
print(selected_rows)


# In[ ]:




