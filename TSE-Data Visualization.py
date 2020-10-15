#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[80]:


df_train = pd.read_csv('Dataset/train.csv')
df_test = pd.read_csv('Dataset/test.csv')


# In[82]:


df_train.info()


# In[83]:


df_train = df_train.dropna()


# In[81]:


df_test.info()


# In[87]:


df = df_train.append(df_test,'sort=False')


# In[89]:


df.info() #the column 'selected text' is only in training set  


# In[90]:


df.head(5)


# In[91]:


df.isnull().sum()


# In[92]:


sns.countplot('sentiment',data = df)


# In[99]:


df['text_length'] = df['text'].apply(len)


# In[102]:


sns.stripplot(x='sentiment', y='text_length', data=df)


# In[101]:


df.hist(column='text_length',by='sentiment', bins=50,figsize=(20,10))


# In[ ]:




