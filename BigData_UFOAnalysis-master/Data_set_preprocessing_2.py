
# coding: utf-8

# In[1]:


get_ipython().system('ls')


# In[2]:


get_ipython().system('pip list')


# In[3]:


import pandas as pd


# In[4]:


ufo = pd.read_csv('ufo_awesome.tsv',
                  sep='\t',
                  names=["sighted_at", "reported_at", "location", "shape", "duration", "description"])


# In[5]:


ufo


# In[6]:


airports = pd.read_csv('airport.csv')


# In[ ]:


airports


# In[ ]:


airports = airports.loc[:,['ident','name','coordinates','iso_region']]


# In[ ]:


airports


# In[ ]:


ufo


# In[ ]:


airports


# In[ ]:


airports['coordinates'].str.split(',')


# In[ ]:


airports


# In[ ]:


f = lambda x: [float(y) for y in x.split(',')]
coor = airports['coordinates'].apply(f)


# In[ ]:


coor


# In[ ]:


airports


# In[ ]:


# airports.to_csv('airports.csv')
airports


# In[ ]:


get_ipython().system('pip install haversine')


# In[ ]:


from haversine import haversine


# In[ ]:


lyon = [float(x) for x in '74.93360137939453, 40.07080078125'.split(',')]
paris = [float(x) for x in '87.47419738769531, 43.907100677490234'.split(',')]
haversine(lyon, paris)


# In[ ]:


ufo.head()


# In[ ]:


airports.head()
# def find_nearest_airport(sighting):


# In[ ]:


def lat(x):
    y = [float(a) for a in x.split(',')]
    return y[1]
def lng(x):
    y = [float(a) for a in x.split(',')]
    return y[1]
lat = airports['coordinates'].apply(lat)
lng = airports['coordinates'].apply(lng)
airports['lat'] = lat
airports['lng'] = lng


# In[ ]:


del airports['coordinates']


# In[ ]:


airports


# In[ ]:


ufo


# In[ ]:


airports


# In[ ]:


ufo


# In[ ]:


cities_lat_long = pd.read_csv('merged_lat_long_city.csv')


# In[ ]:


cities_lat_long


# In[ ]:


ufo = cities_lat_long
ufo.head()


# In[ ]:


ufo.head()


# In[ ]:


airports


# In[ ]:


ufo.head()


# In[ ]:


import sys
def distance_to_nearest_airport(sighting):
    minn = sys.maxsize
    for index, row in airports.iterrows():
        dist = haversine([([sighting['lat'],sighting['lng']]),([[row['lat'], row['long']]])])
        print(dist)
        minn = min(minn, dist)
    return minn
ufo['dist_to_airport'] = ufo.apply(distance_to_nearest_airport)


# In[ ]:


import sys

def distance_to_nearest_airport(sighting):
    a = tuple()
    def lat_long_dist(p1):
        return haversine(p1, p2, miles=True) <= 25
    print(sighting)
#     result = airports.select(lat_long_dist((sighting['lat'],sighting['lng']),
#                                 (airports['lat'], airports['lng'])))
    result = airports.apply()
    if not result.empty:
        return True
    return False
ufo['dist_to_airport'] = ufo.apply(distance_to_nearest_airport, axis=1)


# In[ ]:


airports['lat_long'] = list(zip(airports['lat'],airports['lng']))


# In[ ]:


airports


# In[ ]:


# del airports['lat']
del airports['lng']


# In[ ]:


airports['lat_long'] = list(zip(airports['lat'],airports['lng']))


# In[ ]:


airports


# In[ ]:


airports.to_csv('airports_lat_long.csv')
airports

