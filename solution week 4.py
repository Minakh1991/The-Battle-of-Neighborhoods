#!/usr/bin/env python
# coding: utf-8

# # Business Problem Introduction

# # The idea of this study is to help people planning to open a new restaurant in Toronto to chose the right location by providing data about the income and population of each neighborhood as well as the competitors already present on the same r regions.

# # Data Description

# # To provide the stakeholders the necessary information I'll be combining Toronto's 2016 Census that contains Population, Average income per Neighborhood with Foursquare API to collect competitors on the same neighborhoods.
# 
# Toronto's Census data in publicly available at this website: https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#8c732154-5012-9afe-d0cd-ba3ffc813d5a

# In[1]:


import numpy as np 

import pandas as pd 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

get_ipython().system('conda install -c conda-forge geopy --yes ')
from geopy.geocoders import Nominatim 

get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes ')
import folium 

print('Libraries imported.')


# In[2]:


csv_path='https://www.toronto.ca/ext/open_data/catalog/data_set_files/2016_neighbourhood_profiles.csv'
df = pd.read_csv(csv_path,encoding='latin1')
print('Data loaded')


# In[3]:


df.head()


# In[4]:


Neighbourhoods = list(df.columns.values)
Neighbourhoods = Neighbourhoods[5:]
print(Neighbourhoods)


# In[5]:


dfToronto = pd.DataFrame(index=Neighbourhoods, columns=["Population_2016","Income_2016"])
dfToronto.head()


# In[6]:


for index, row in dfToronto.iterrows():
    dfToronto.at[index, 'Population_2016'] = df[index][2]
    dfToronto.at[index, 'Income_2016'] = df[index][2264]
    

dfToronto.sort_values('Income_2016')


# # Methodology

# # For this report I used a few different maps that could help a new investor to decide the best neighborhood to open a restaurant in Toronto based on it's income, population and available competitors. In order to do that I've used the 2016 Census information combined with choropleth maps to visually display the wealthier and more populational neighborhoods and Foursquare data to display the current restaurants in each region.
# 
# 

# # Results

# # Comparing the maps we can notice the majority of the restaurants grouped on main streets and on the south of the city, although some of the welthiest neighborhoods are up to the north. Also, the areas with a dense population don't reflect on the number of restaurants.

# # Discussion

# # When I first decided to create this study I was expecting to find clusters of restaurants in certain regions and the final result didn't meet that expectation.

# # Conclusion

# # This report may be helpful for someone planning on opening a restaurant in Toronto, by comparing the current offers and neighborhoods profiles, however it may not cover all variables such as access to public transportation or even the restaurants profiles, so it shall not be used as a single decidion making tool.

# In[ ]:




