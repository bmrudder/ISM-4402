#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[7]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[11]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[12]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[139]:


import pandas as pd
import matplotlib.pyplot as plt


Names = ['Jada Walters','Nicole Henderson','Tanya Moore','Ronelle Jackson','Brad Sears']
Gender = ['F','F','F','F','M']
HoursWorked = [39,46,42,38,33]
SalesTraining = ['N','N','Y','Y','N']
YearsExperience = [3,3,4,5,4]
CarsSold = [2,6,6,3,2]
SalesList = zip(Names,CarsSold)

df = pd.DataFrame(data = SalesList, columns=['Names', 'Cars Sold'])

get_ipython().run_line_magic('matplotlib', 'inline')


# In[140]:


df2 = df.set_index(df['Names'])
df2.plot(kind="bar")

plt.title("Employee Sales")
plt.ylabel('Cars')
plt.xlabel('Names')


# In[148]:


import pandas as pd
import matplotlib.pyplot as plt

Names = ['Jada Walters','Nicole Henderson','Tanya Moore','Ronelle Jackson','Brad Sears']
Gender = ['F','F','F','F','M']
HoursWorked = [39,46,42,38,33]
SalesTraining = ['N','N','Y','Y','N']
YearsExperience = [3,3,4,5,4]
CarsSold = [2,6,6,3,2]

HoursWorkedList = zip(Names,CarsSold,HoursWorked)
df = pd.DataFrame(data = HoursWorkedList, columns=['Names', 'Cars Sold', 'Hours Worked'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind="bar")

plt.title("Employee Sales by Hours Worked")
plt.ylabel('Hours')
plt.xlabel('Cars')


# In[ ]:




