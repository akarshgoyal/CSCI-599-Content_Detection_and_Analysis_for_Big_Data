
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np
import re
import warnings
import math
from datetime import datetime, timedelta
warnings.filterwarnings('ignore')


# In[72]:


def print_series(x):
    print('length =', len(x))
    print('\n'.join(str(y) for y in x))
    
def print_multiple_series(x, y):
    print('length =', len(x))
    print('\n'.join(str(i) + ', ' + str(j) for i,j in zip(x,y)))    
    
def parse_city(raw_loc):
    splits = re.split('[^a-zA-Z\s.]', raw_loc)
    try:
        city = splits[0].strip()
        if 'St.' in city:
            city = city.split('St.')[-1]
            city = 'Saint ' + city.strip()
    except:
        city = 'None'
    return city

def parse_state(raw_loc):
    splits = re.split('[^a-zA-Z]', raw_loc)
    state = splits[-1]
    return state

def remove_apostrophe(x):
    x = x.replace('\'', '')
    return x


# In[73]:


keywords = pd.read_csv('data/movies/keywords.csv')

movies_metadata = pd.read_csv('data/movies/movies_metadata.csv')
# print('\',\n\''.join(movies_metadata.columns))

movies_metadata_features = [
    'genres',
    'id',
    'original_language',
    'overview',
    'popularity',
    'production_countries',
    'release_date',
    'revenue',
    'runtime',
    'title'
]

movies_metadata_selected = movies_metadata[movies_metadata_features]
print(movies_metadata_selected.shape)

movies_metadata_selected = movies_metadata_selected.dropna()
movies_metadata_selected.release_date = pd.to_datetime(movies_metadata_selected.release_date)

drop_these = movies_metadata_selected[movies_metadata_selected.id.str.contains(r'[^\d]')]

movies_metadata_selected = movies_metadata_selected.drop(drop_these.index)
print(movies_metadata_selected.shape)


# In[74]:


#print_multiple_series(keywords.id, movies_metadata.id)

# movies_metadata_selected = movies_metadata_selected.set_index(['id'])
# keywords = keywords.set_index(['id'])
print(keywords.columns)
print(movies_metadata_selected.columns)


# In[75]:


keywords.id.dtype


# In[76]:


movies_metadata_selected.id = movies_metadata_selected.id.astype('int64')
movies_metadata_selected.id.dtype


# In[77]:


movies_keywords = pd.merge(movies_metadata_selected, 
                  keywords, 
                  on='id')
movies_keywords.keywords = movies_keywords.keywords.astype(list)

movies = movies_keywords[movies_keywords.keywords.str.contains(r'\balien\b')]
movies.columns


# In[78]:


ufo_cities = pd.read_csv('data/ufo-sightings/merged_lat_long.csv')
ufo_cities = ufo_cities.rename(columns={'location_x': 'location'})
del ufo_cities['location_y']
ufo_cities.columns


# In[79]:


ufo_cities.location = ufo_cities.location.apply(str)

ufo_cities = ufo_cities[ufo_cities.reported_time != 0]
ufo_cities.reported_time.value_counts()


ufo_cities.reported_time = ufo_cities.reported_time.apply(str)
ufo_cities.reported_time = pd.to_datetime(ufo_cities.reported_time, 
                                          format="%Y%m%d",
                                         errors = "coerce")


# In[80]:


month = timedelta(days=30)

movies = movies.sort_values('release_date')
ufo_cities = ufo_cities.sort_values('reported_time')


# In[82]:


# def get_movie(sighting):
#     f = movies[sighting['reported_time'] > movies.release_date & 
#                sighting['reported_time'] <= movies.release_date + month]
#     if f:
#         return True
#     return False

def get_movie(sighting):
    f = movies[(sighting['reported_time'] > movies.release_date) & 
               (sighting['reported_time'] <= movies.release_date + month)]
    if not f.empty:
        movie = f.iloc[0]
        return (sighting['idx'],
                True,
                movie.title, 
                movie.popularity, 
                movie.revenue,
                None,None,None,None,None,None)
    return (sighting['idx'], False, None, None, None,None,None,None,None,None,None)

sightings_movies = ufo_cities.apply(get_movie, axis = 1)
sightings_movies.columns


# In[84]:


sightings_movies.tail()
select_cols = ['idx','sight_time' ,'reported_time','location', 'shape']

matched_movies = sightings_movies[select_cols]

rename_cols = {'sight_time':'movie_influence' ,
               'reported_time':'movie_title',
               'location':'movie_pop',
              'location':'movie_rev'}

matched_movies = matched_movies.rename(columns = rename_cols)
matched_movies


# In[86]:


ufo_cities_merged = pd.merge(ufo_cities, 
                  matched_movies, 
                  on='idx')
ufo_cities_merged.to_csv('movies_merged_final.csv')


# In[88]:


ufo_cities_merged.to_csv('data/movies/movies_merged_final.csv')

