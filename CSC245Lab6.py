#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


path_to_folder= ('C:/Users/fulya/Downloads/')
file_name='company_sales_data.csv'
df=pd.read_csv(path_to_folder+file_name)


# In[20]:


# Exercise 1: Read Total profit of all months and show it using a line plot
plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_profit'], marker='o')
plt.xticks(np.arange(1, 13))
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Profit')
plt.show()


# In[21]:


#Exercise 2: Get total profit of all months and show line plot with specific style properties
plt.figure(figsize=(10, 6))
plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_profit'], linestyle='--', color='red', marker='o', linewidth=3, label='Total Profit')
plt.xticks(np.arange(1, 13))
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Company Sales Data Last Year')
plt.legend(loc='lower right')
plt.show()


# In[25]:


# Exercise 3: Read all product sales data and show it using a multiline plot
plt.figure(figsize=(8, 5))
for product in df.columns[1:6]:
    plt.plot(df['month_number'], df[product], marker='o', label=product+' Sales Data')
plt.xticks(np.arange(1, 13))
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Sales Data')
plt.legend()
plt.show()


# In[27]:


# Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['month_number'], df['toothpaste'], marker='o')
plt.xticks(np.arange(1, 13))
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales Data')
plt.grid(True, linestyle='--')
plt.show()


# In[37]:


# Exercise 5: Read face cream and facewash product sales data and show it using a bar chart
plt.figure(figsize=(8, 5))
bar_width = 0.3
bar_positions = df['month_number']
plt.bar(bar_positions - bar_width/2, df['facecream'], bar_width, label='Face Cream')
plt.bar(bar_positions + bar_width/2, df['facewash'], bar_width, label='Face Wash')
plt.xticks(np.arange(1, 13))
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Numbers')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--')
plt.show()


# In[41]:


# Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['month_number'], df['bathingsoap'])
plt.xticks(np.arange(1, 13))
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Numbers')
plt.title('Bathing Soap Sales Data')
plt.grid(True, linestyle='--')
plt.savefig('bathing_soap_sales.png')
plt.show()


# In[48]:


# Exercise 7: Read the total profit of each month and show it using a histogram
plt.figure(figsize=(8, 5))
plt.hist(df['total_profit'])
plt.xlabel('Profit Range in Dollar')
plt.ylabel('Actual Profit in Dollar')
plt.title('Profit Data')
plt.show()


# In[61]:


# Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart
total_sales = df.iloc[:, 1:6].sum()
plt.figure(figsize=(6, 6))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=10)
plt.title(' Sales Data')
plt.axis('equal')
plt.legend(loc='lower right')
plt.show()


# In[76]:


#Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 5))

axes[0].plot(df['month_number'], df['bathingsoap'], marker='o', color='black')
axes[0].set_title('Bathing Soap Sales')
axes[0].set_xlabel('Month Number')
plt.xticks(np.arange(1, 13))
axes[0].set_ylabel('Sales Unit in Number')


axes[1].plot(df['month_number'], df['facewash'], marker='o', color='red')
axes[1].set_title('Facewash Sales')
axes[1].set_xlabel('Month Number')
plt.xticks(np.arange(1, 13))
axes[1].set_ylabel('Sales unit in number')

plt.tight_layout()
plt.show()


# In[66]:


# Exercise 10: Read all product sales data and show it using the stack plot
plt.figure(figsize=(8, 5))
plt.stackplot(df['month_number'], df.iloc[:, 1:6].T, labels=df.columns[1:6])
plt.xlabel('Month Number')
plt.ylabel('Sales Unit in Numer')
plt.title('Product Sales Data Using Stack Plot)')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()


# In[ ]:




