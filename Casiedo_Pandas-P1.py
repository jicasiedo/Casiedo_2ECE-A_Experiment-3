#!/usr/bin/env python
# coding: utf-8

# # Programming Assignment 3
# ## Casiedo, Jihan Harvey C.
# ### 2ECE-A
# ### Problem 1

# In[ ]:


import pandas as pd #import to use pandas library


# In[27]:


cars = pd.read_csv('cars.csv') #This function loads the existing cars.csv located in the same file path of this code
cars #print the data frame


# In[29]:


cars.head() #This function shows the first five rows of the data frame cars.csv


# In[21]:


cars.tail() #This function shows the last five rows of the data frame cars.csv

