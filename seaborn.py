#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
data = data.pivot("month","year","passengers")
#Heatmap
sns.heatmap(data=data, annot=True,fmt="d",cmap="YlGnBu")
plt.show()


# In[4]:


data.info()


# In[9]:



sns.lineplot(data=data, x="year",y="passengers")
plt.show()


# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt 
data =sns.load_dataset("iris")
#swarn plot
sns.swarmplot(x = "species", y="petal_length",data=data)
plt.show()


# In[12]:


import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("titanic")
# bar plot
sns.countplot(data=data, x="class")
plt.show()


# 

# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
#scatter plot
sns.scatterplot(data=data, x ="total_bill",y="tip")


# In[ ]:




