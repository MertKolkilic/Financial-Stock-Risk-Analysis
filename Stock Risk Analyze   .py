#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn
import numpy as np

from pandas import Series, DataFrame
from pylab import rcParams


# In[126]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = 15, 10
sb.set_style('darkgrid')


# In[139]:


stock = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'MSFT']
stocks = yf.download(stock, start = "2020-01-01", end = "2020-12-28")
data = stocks.loc[:,"Close"].copy()

stocks.head()


# In[140]:


data.plot()


# In[141]:


data.describe()


# In[142]:


data.info()


# In[ ]:


# Normalize Stock Data 


# In[143]:


norm = data.div(data.iloc[0]).mul(100)
norm.plot()


# In[144]:


data.pct_change()


# In[145]:


dataset = data.pct_change().dropna()
dataset.describe()


# In[146]:


X = dataset.describe().T.loc[:,["mean","std"]]
X


# In[147]:


X['mean'] = X['mean']*252
X['std'] = X['std']*np.sqrt(252)
X


# In[162]:


X.plot.scatter(x='std', y='mean', figsize = (15,10), fontsize = 10)
for i in X.index:
    plt.annotate(i, xy= (X.loc[i,'std']+0.002, X.loc[i,'mean']+0.002), size=15)


# In[ ]:





# In[ ]:




