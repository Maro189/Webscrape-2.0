#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# opening text file
f = open("job_descriptions.txt", "r", encoding = 'UTF-8').read()

# converting all to lowercase
f2 = f.lower()

# counting words
python_count = f2.count('python')

sql_count = f2.count('sql')

bi_count = f2.count('power bi')

exl_count = f2.count('excel')

tblu_count = f2.count('tableau')

mtlab_count = f2.count('matlab')

spss_count = f2.count('spss')

java_count = f2.count('javascript')

c_count = f2.count('c++')

# creating dataframe
df = pd.DataFrame({'Python': python_count,
     'SQL': sql_count,
     'Power BI': bi_count,
     'Excel': exl_count,
     'Tableau': tblu_count,
     'Matlab': mtlab_count,
     'SPSS': spss_count,
     'Javascript': java_count,
     'C++': c_count}, index = [0])

# reordering columns
df = df[['Excel', 'SQL', 'Python', 'Power BI', 'Tableau', 'SPSS', 'Javascript', 'Matlab', 'C++']]

# creating bar plot
ax = df.plot(kind = 'bar', figsize = (20, 20), legend = True, fontsize = 15)
plt.title('Required Skills for Data Analyst Position', fontsize = 26)
ax.set_xlabel("Skill", fontsize = 25)
ax.set_ylabel("Count", fontsize = 25)
plt.rc('legend', fontsize = 30)
plt.show()

