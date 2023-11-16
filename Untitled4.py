#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
import datetime


# In[48]:


orders = pd.read_csv('kz.csv')


# In[49]:


orders.head(10)


# In[50]:


orders.describe().apply(lambda s: s.apply('{0:.5f}'.format))


# In[51]:


orders.dtypes


# In[52]:


orders.isna().sum()/orders.shape[0]*100


# In[53]:


orders.loc[orders['category_id'].isna(),:]


# looks like we have some price data in category_code, and user_id data in brand column. 

# In[54]:


orders.price.fillna(orders.category_code, inplace=True)
orders.price.fillna(0, inplace=True)
orders.user_id.fillna(orders.brand, inplace=True)
orders.user_id.fillna(0, inplace=True)


# In[55]:


orders.category_id.fillna(0, inplace=True)


# In[56]:


orders.isna().sum()/orders.shape[0]*100


# In[58]:


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def reject_float(value):
    if value is None:
        return np.NaN
    if is_float(value):
        return np.NaN
    else:
        return value
    
orders.category_code = orders.category_code.apply(reject_float)
orders.category_code.fillna('unknown', inplace=True)

invalid_category_rate = orders[orders.category_code =='unknown'].shape[0] / orders['category_code'].shape[0]

print('Invalid category rate is {:.2%}'.format(invalid_category_rate))


# In[62]:


orders.brand = orders.brand.apply(reject_float)
orders.brand.fillna('unknown', inplace=True)


# In[63]:


invalid_brand_rate = orders[orders.brand =='unknown'].shape[0] / orders['brand'].shape[0]

print('Invalid brand rate is {:.2%}'.format(invalid_brand_rate))


# In[64]:


orders.category_id = orders.category_id.apply(lambda x: 0 if pd.isna(x) else x)


# In[ ]:




