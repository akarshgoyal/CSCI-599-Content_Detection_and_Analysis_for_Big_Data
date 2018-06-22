
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv = pd.read_csv("final.csv")


# In[3]:


csv


# In[13]:


lat_lng = csv[["lng_y","lat_y"]]
lat_lng


# In[15]:


lat_lng.to_json("sightings_lat_lng.json")

