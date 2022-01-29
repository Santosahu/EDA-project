#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df1=pd.read_csv("C:/Users/LENOVO/Desktop/Hotel Bookings.csv")


# In[3]:


df1.head(2)


# In[4]:


df1.shape


# In[5]:


df1.columns


# In[6]:


df1.describe()


# In[7]:


df1.info()


# In[8]:


#calculating percentage of null valus of each column
(df1.isnull().sum()/df1.shape[0])*100


# ##as we can see 94% of data is missing in 'company' column, so it is not much helpful for us to do the analysis.I am going to drop it, as well as  'Agent' column which signifies the id number of agent which is also not useful.

# In[9]:


df1=df1.drop(columns=['agent','company'])
df1.columns


# In[10]:


#filling country null values with unknown and children null values with zero

df1.fillna(value={"children":0,"country":"unknown"},inplace=True)


# In[11]:


# checking duplicate rows
df1[df1.duplicated()].index


# In[12]:


#droping duplicate rows
df1.drop(index=df1[df1.duplicated()].index, inplace=True)


# In[13]:


df1.shape


# In[14]:



df1["Total guests"]=df1['adults']+df1['children']+df1['babies']


# In[15]:


# Dropping rows where total number of guests is zero
y=df1[df1["Total guests"]==0].index
df1.drop(index=y,inplace=True)


# Now we have a cleaned dataset and good to go do the analysis

# 1) From where guests are from

# In[16]:


country_wise_guest=df1[df1['is_canceled'] == 0].groupby('country')['Total guests'].sum().sort_values(ascending=False).reset_index()
country_wise_guest.columns


# In[19]:


#creating pie chart
plt.pie(data=country_wise_guest,x='Total guests', labels = 'country', autopct='%.0f%%')
plt.show()


# 2) Top 10 countries having more visitors

# In[82]:


top_10_countries=df1[df1['is_canceled'] == 0].groupby('country')['Total guests'].sum().sort_values(ascending=False).head(10).plot(kind='bar',color='purple')


# 3)which hotel has more demand?

# In[114]:


sns.countplot(data=df1, x = 'hotel')


# In[ ]:





# 4)Busiest month for both the hotel

# In[119]:


resort_hotel_df1=df1[(df1['hotel']=='Resort Hotel')].groupby(['hotel','arrival_date_month'])['Total guests'].sum().reset_index()
resort_hotel_df1


# In[117]:


city_hotel_df1=df1[df1['hotel']=='City Hotel'].groupby(['hotel','arrival_date_month'])['Total guests'].sum().reset_index()
city_hotel_df1


# In[71]:


merged_df=pd.concat([resort_hotel_df1,city_hotel_df1],ignore_index=True)
merged_df


# In[81]:


plt.figure(figsize=(10,9))
sns.barplot(x="arrival_date_month",
           y="Total guests",

            hue="hotel",
           data=merged_df)


# 5) Having a glance of assigned and reserved room type

# In[92]:


pd.crosstab(df1['reserved_room_type'], df1['assigned_room_type'])


# 6)Distribution of meal

# In[95]:


df1.meal


# In[97]:


z=sns.countplot(x=df1['meal'])


# 7)Booking distribution of different medium

# In[104]:


df1.market_segment.value_counts()


# In[106]:


plt.figure(figsize=(8,8))

plt.pie(data=df1,x=df1.market_segment.value_counts().values, labels = df1.market_segment.value_counts().index, autopct='%.0f%%')
plt.show()


# In[ ]:


8)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




