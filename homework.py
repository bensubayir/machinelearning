#!/usr/bin/env python
# coding: utf-8

# In[1]:


var = 10  
var2 = 15
gun ="pazartesi"
print(var)


# In[2]:


#list
var1 = 10
var2 = 20
var3 = 30 
list_int =[10,20,30]
type(list_int)


# In[3]:


list_int[0]


# In[4]:


list_int[-1]


# In[5]:


list_int[0:3]


# In[6]:


list_int.append(7)
print(list_int)


# In[10]:


list_int.remove(7)


# In[9]:


list_int.reverse
print(list_int)


# In[11]:


list_int.sort
print(list_int)


# In[15]:


for each in range (1,11):    
    print(each)


# In[20]:


minimum = 10
for each in list_int:
        if(each>minimum):
            minimum = each
        else:
                    continue
print(minimum)


# In[23]:


i=0
while (i<4):
    print(i)
    i = i+1
    


# In[26]:


def cember_cevre(r,pi=3.14):
    output =2*pi*r
    return output
cember_cevre(2)


# In[27]:


def hesapla(x)
    output =x*x
    return output
sonuc= hesapla(2)
print(sonuc)
sonuc2= lambda x:x*x
print (sonuc2(2))


# In[28]:


dictionary = {"bensu":21,"asuman":22,"beyza":22}
print(dictionary)


# In[29]:


type(dictionary)


# In[30]:


dictionary.keys()


# In[31]:


dictionary.values()


# In[32]:


keys = dictionary.keys()
if "bensu" in keys:
    print("yes")
else:
    print("no")


# In[ ]:




