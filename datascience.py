#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os


# In[8]:


titanic_train = pd.read_csv("C:/Users/bensu/Downloads/train.csv")


# In[9]:


titanic_train.shape


# In[10]:


titanic_train.head()


# In[11]:


del titanic_train["PassengerId"]


# In[12]:


titanic_train.head()


# In[13]:


new_Pclass = pd.Categorical(titanic_train["Pclass"],ordered = True)
new_Pclass = new_Pclass.rename_categories(["class1","class2","class3"])
new_Pclass.describe()


# In[14]:


titanic_train["Age"].describe()


# In[16]:


missing = np.where(titanic_train["Age"].isnull()== True)
missing


# In[17]:


len(missing[0])


# In[19]:


titanic_train.hist(column="Age",figsize=(9,6),bins=20)


# In[20]:


new_age = np.where(titanic_train["Age"].isnull(),28,titanic_train["Age"])
titanic_train["Age"] = new_age
titanic_train["Age"].describe()


# In[21]:


titanic_train.hist(column="Age",figsize=(9,6),bins=20)


# In[ ]:




