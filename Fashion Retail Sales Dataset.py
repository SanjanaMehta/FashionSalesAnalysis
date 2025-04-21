#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv(r"C:\Users\Sanjana\Downloads\archive (2)\Fashion_Retail_Sales.csv")


# In[4]:


df.head()


# In[13]:


df1=df.dropna()


# In[14]:


df1.info()


# In[8]:


df.describe()


# In[15]:


import matplotlib.pyplot as plt


# In[20]:


df1.boxplot(column='Purchase Amount (USD)')
plt.show


# In[21]:


df1.to_excel('fashion forecasting.xlsx')


# In[22]:


from IPython.display import FileLink

# This will generate a clickable link
FileLink('fashion forecasting.xlsx')


# In[ ]:




