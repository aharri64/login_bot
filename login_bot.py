#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
import time, requests
from keys import username, password


# In[7]:


driver = webdriver.Chrome('/Users/amirharrison/downloads/chromedriver')


# In[8]:


driver.get('https://stackoverflow.com/')


# In[9]:


driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()


# In[10]:


driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="submit-button"]').click()


# In[14]:


text = driver.find_element_by_xpath('//*[@id="newuser-box"]/h4').text


# In[16]:


print(text)


# In[ ]:





# In[ ]:




