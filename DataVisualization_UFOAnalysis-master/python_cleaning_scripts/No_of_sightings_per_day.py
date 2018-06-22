
# coding: utf-8

# In[1]:


import pandas as pd


# In[69]:


from datetime import datetime


# In[3]:


csv = pd.read_csv("final.csv")


# In[58]:





# In[81]:


csv1 = csv[['sight_time','location', 'shape_x','duration', 'population']]


# In[82]:


csv1.columns = ['Date', 'Location', 'Shape', 'Duration', 'Population']


# In[83]:


csv1['Count'] = csv1.groupby('Date')['Date'].transform('count')


# In[84]:


csv1 = csv1.drop_duplicates(subset='Date',keep='last')


# In[85]:


csv1['Count'].unique()


# In[86]:


csv1


# # 

# In[87]:


def lam(x):
    try:
        ret = datetime.strptime(x, '%Y-%m-%d')
    except:
        ret = datetime.strptime(x, '%m/%d/%y')
    return ret
csv1['Date'] = csv1['Date'].map(lam)


# In[91]:


csv1 = csv1.sort_values('Date')


# In[94]:


csv1 = csv1.head(6400)


# In[95]:


csv1


# In[96]:


csv1.to_csv("data.csv")

