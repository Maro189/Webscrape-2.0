#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import re
import nltk
from nltk.corpus import stopwords

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# file directory and change to lowercase
f = open("G:\Python projects\Final webscrape\Docs\job_descriptions.txt", 'r', encoding = 'UTF-8').read()
f2 = f.lower()

# tokenize
f_token = nltk.word_tokenize(f2)
f_dist = nltk.FreqDist()

# remove puncuation
punc = re.compile(r'[->?!,:;()|0-9#]')

post_punc = []

for words in f_token:
    word = punc.sub("", words)
    if len(word) > 0:
        post_punc.append(word)
        
# keyword search
keys = ['python', 'sql', 'mysql', 'jupyter', 'spss', 'c++', 'r', 'tableau',
        'powerbi','numpy', 'pandas', 'matplotlib', 'java', 'javascript', 'excel']

key_count = []

for word in post_punc:
    if word in keys:
        key_count.append(word)
freq = nltk.FreqDist(key_count)
freq


# In[24]:


freq2 = pd.Series(dict(freq))

fig, ax = plt.subplots(figsize = (15,15))

plot = sns.barplot(x = freq2.index, y = freq2.values, ax=ax, order = freq2.index)
plt.title('Required Skills for Data Analyst Position')
plt.xticks(rotation=30)


# In[ ]:




