#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[2]:


import mysql.connector as connection
import pandas as pd


# In[3]:


sql = "SELECT * FROM student ;"


# In[ ]:





# In[4]:


#db = connection.connect(host="localhost", database="my_db", user="root", password="Root@123",  use_pure=True) 
db = connection.connect(host='127.0.0.1', user="User_name",   password ="db_password", database="databse_name" , auth_plugin='mysql_native_password')


# In[5]:


df = pd.read_sql(sql, db)


# In[6]:


df.head()


# In[7]:


df.to_excel("mysql_date.xlsx", index=False)


# In[ ]:




