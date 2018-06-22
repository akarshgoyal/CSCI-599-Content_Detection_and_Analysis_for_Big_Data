
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv = pd.read_csv("military.csv")


# In[7]:


csv = csv.sort_values('ST_NAME')


# In[9]:


csv.to_csv("military.csv")

