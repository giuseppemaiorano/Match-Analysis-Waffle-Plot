#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install pywaffle


# In[54]:


import pandas as pd
from pywaffle import Waffle
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[55]:


df = pd.read_csv("tocchi.csv", encoding="unicode_escape", sep = ';')
df['Player'] = df['Player'].str.split('\\', expand=True)
df = df.sort_values(by=['Touches'], ascending=False)
df = df.drop(16)
df = df.drop(['Touches'], axis=1)
df = df.T
df.columns = df.iloc[0]
df = df.drop(['Player'])
my_list = df.columns.values.tolist()
df = pd.DataFrame(df, columns=my_list)


# In[56]:


df


# In[60]:


fig = plt.figure(FigureClass = Waffle, 
                 values = df.iloc[:, 0], 
                 labels = list(df.index), 
                 rows = 10,
                 title = {
                     'label' : my_list[0]
                 },
                 figsize = (6, 6)
                )


# In[66]:


fig = plt.figure(
                 FigureClass = Waffle, 
                 rows = 10, 
                 figsize = (10, 10),
                 plots = {
                     '331' : {
                         'values' : df.iloc[:, 0],
                         'title': {
                             'label' : my_list[0]
                         }
                     },
                                          '332' : {
                         'values' : df.iloc[:, 1],
                         'title': {
                             'label' : my_list[1]
                         }
                     },
                                          '333' : {
                         'values' : df.iloc[:, 2],
                         'title': {
                             'label' : my_list[2]
                         }
                     },
                                          '334' : {
                         'values' : df.iloc[:, 3],
                         'title': {
                             'label' : my_list[3]
                         }
                     },
                                          '335' : {
                         'values' : df.iloc[:, 4],
                         'title': {
                             'label' : my_list[4]
                         }
                     },
                                          '336' : {
                         'values' : df.iloc[:, 5],
                         'title': {
                             'label' : my_list[5]
                         }
                     },
                                          '337' : {
                         'values' : df.iloc[:, 6],
                         'title': {
                             'label' : my_list[6]
                         }
                     },
                                          '338' : {
                         'values' : df.iloc[:, 7],
                         'title': {
                             'label' : my_list[7]
                         }
                     },
                                          '339' : {
                         'values' : df.iloc[:, 8],
                         'title': {
                             'label' : my_list[8]
                         }
                     },
                 }
                )


# In[ ]:




