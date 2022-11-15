#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing packages
from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import pandas as pd 
import os
--------------
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# going to webpage
url1 = 'https://www.linkedin.com/uas/login'
time.sleep(5)

driver = webdriver.Chrome(executable_path = 'driver location')
driver.get(url1)

# user credentials 
username = driver.find_element_by_id("username")
username.send_keys("user email")
psword = driver.find_element_by_id("password")
psword.send_keys("user password")
driver.find_element_by_xpath("//button[@type='submit']").click()

# job page url
url2 = 'https://www.linkedin.com/jobs/'
driver.get(url2)

url3 ='jobs link'
driver.get(url3)

# finding job title
job = driver.find_elements_by_class_name('job-card-list__title')
job_list = []
for i in job:
    job_list.append(i.text)


job_title = []
for i in range(len(job_list)):
    job_title.append(job_list[i].strip())
    job_title
    
print(job_title)
print()
print(len(job_title))

# company name
company = driver.find_elements_by_class_name('job-card-container__company-name')
comp_name = []
for i in company:
    comp_name.append(i.text)

print(comp_name)
print()
print(len(comp_name))

# job location
location = driver.find_elements_by_class_name('job-card-container__metadata-item')
loc = []

for i in location:
    loc.append(i.text)

print(loc)
print()
print(len(loc))

# job type - remote/onsite
remote_onsite = driver.find_elements_by_class_name('job-card-container__metadata-item--workplace-type')
type_ = []

for i in remote_onsite:
    type_.append(i.text)
    
print(type_)
print()
print(len(type_))

# job descriptions
desc = driver.find_elements_by_class_name('jobs-description-content__text')
jdesc = []

for i in desc:
    jdesc.append(i.text)
    
print(jdesc)
print()
print(len(jdesc))


