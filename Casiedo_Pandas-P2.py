#!/usr/bin/env python
# coding: utf-8

# # Programming Assignment 3
# ## Casiedo, Jihan Harvey C.
# ### 2ECE-A
# ### Problem 2

# In[11]:


import pandas as pd #import to use pandas library


# In[13]:


cars = pd.read_csv('cars.csv') #This function loads the existing cars.csv located in the same file path of this code
cars #print the data frame


# In[15]:


cars.iloc[:5, ::2] #This function prints the first five cars and the odd columns of the data type


# In[17]:


cars.loc[cars['Model'] == 'Mazda RX4'] #This function prints the row of the Model 'Mazda RX4'


# In[19]:


cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']] #This function shows how many cyl the Model 'Camaro Z28' have


# In[21]:


cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L')|
         (cars['Model'] == 'Honda Civic') ,['Model','cyl','gear']] 
#This function shows how many cyl and what gear type the Models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have


# In[ ]:




