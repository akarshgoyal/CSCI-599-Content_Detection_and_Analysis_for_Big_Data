
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


get_ipython().system('ls')


# In[3]:


csv = pd.read_csv("flare_city_pop.csv")


# In[12]:


reqd = csv.sort_values(by = ["value"], ascending = False).drop_duplicates().head(250)


# In[14]:


reqd.to_csv("flare_city_pop_top250.csv")


# In[15]:


csv


# In[16]:


get_ipython().system('ls')


# In[17]:


json_data = pd.read_json("output_array_json.json")


# In[18]:


json_data


# In[22]:


json_data.reported_time.to_csv("date_only.csv")


# In[29]:


date_movie_influence = json_data.reported_time , json_data.movie_influence


# In[31]:


date_movie_influence = pd.DataFrame({'Date': json_data.reported_time, 'movie_influence': json_data.movie_influence})


# In[33]:


date_movie_influence = date_movie_influence[1:]


# In[34]:


date_movie_influence

