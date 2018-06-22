
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ufo = pd.read_csv('ufo_awesome.tsv', sep='\t',header=None, names=["sighted_at", "reported_at", "location", "shape", "duration", "description"])


# In[3]:


from geopy.geocoders import Nominatim, GoogleV3
from pygeocoder import Geocoder
geolocator = GoogleV3()


# In[4]:


location_series = ufo.loc[:, 'location']


# In[5]:


lat_list_coordinates = []
long_list_coordinates = []
# type(location_series.head())
# x = geolocator.geocode(location_series).latitude
# print(x)
for x, y in location_series.iteritems():
    if y != float('nan'):
        temp = Geocoder.geocode(y)
        lat_list_coordinates.append(temp.coordinates[0])
        long_list_coordinates.append(temp.coordinates[0])
    else:
        lat_list_coordinates.append(None)
        long_list_coordinates.append(None)
print(lat_list_coordinates[:5])
print(long_list_coordinates[:5])


# In[ ]:


# series_lat = pd.Series(lat_list_coordinates,ufo.index.values,dtype=None, name='lat_coordinates', copy=False)


# In[6]:


get_ipython().system('pip install pygeocoder')


# In[7]:


from pygeocoder import Geocoder


# In[8]:


import numpy as np


# In[9]:


results = Geocoder.geocode("Los angeles, CA")


# In[10]:


results.coordinates


# In[11]:


get_ipython().system('pip list')


# In[12]:


get_ipython().system('ls')


# In[13]:


cities_coord = pd.read_csv('uscitiesv.csv', header=0)


# In[14]:


cities_coord = cities_coord[['city','state_id','lat','lng']]
cities_coord


# In[15]:


cities_coord['location'] = cities_coord['city'] + ', ' + cities_coord['state_id']


# In[16]:


cities_coord


# In[17]:


del cities_coord['city']


# In[18]:


del cities_coord['state_id']


# In[19]:


cities_coord


# In[20]:


ufo


# In[21]:


ufo.set_index('location')


# In[22]:


cities_coord.set_index('location')


# In[23]:


ufo.reset_index()


# In[24]:


cities_coord.reset_index()


# In[25]:


cities_coord


# In[41]:


h = pd.DataFrame(list(zip(cities_coord.groupby('location')['lat'].mean(),
                          cities_coord.groupby('location')['lng'].mean())),
                 columns=['lat','lng'],
                 index=cities_coord.groupby('location')['lat'].mean().index)


# In[74]:


h


# In[66]:



h.to_csv('city_lat_long.csv')
h.loc['Kodiak, AK',:]


# In[44]:


ufo


# In[49]:


pop = pd.read_csv('populations_dataset.csv', header=0)
pop.shape


# In[50]:


pop


# In[67]:


pop.loc[:,:]


# In[59]:


pop['Place Type'].value_counts()


# In[69]:


pop = pop.loc[:,'CityST':'Name_2010']


# In[72]:


pop


# In[75]:


pop = pop.set_index('CityST')


# In[76]:


pop


# In[77]:


h


# In[87]:


h = h.reset_index()


# In[84]:


pop = pop.reset_index()


# In[106]:


pop.columns

pop = pop.loc[:,'CityST':'Name_2010']

pop = pop.drop(['ST','City'],axis=1)


# In[111]:


pop.columns


# In[112]:



pop


# In[113]:


result = h[].merge(pop,how='outer',left_on='location',right_on='CityST')


# In[115]:


result = result.dropna()


# In[116]:


result


# In[121]:


result = result.loc[:,'1880':]


# In[122]:


result


# In[124]:


result = h.merge(pop,how='outer',left_on='location',right_on='CityST')


# In[125]:


result


# In[126]:


result = result.dropna()


# In[127]:


result


# In[130]:


result = result.drop(['lat','lng'],axis=1)


# In[133]:


result = result.drop(['CityST'],axis=1)


# In[134]:


result


# In[135]:


result.columns


# In[136]:


result = result.drop(['1790', '1800', '1810', '1820', '1830', '1840', '1850',
       '1860', '1870'],axis=1)


# In[141]:


population = result
population


# In[142]:


lat_long = h
lat_long


# In[143]:


population_and_latlong = population.merge(lat_long, how='inner',left_on='location',right_on='location')


# In[144]:


population_and_latlong


# In[145]:


population_and_latlong.columns


# In[146]:


population_and_latlong.to_csv('population_and_latlong.csv')

