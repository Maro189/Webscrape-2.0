#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing Libraries
import time
import pandas as pd    
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Chrome Driver
path = r'driver file location'
driver = webdriver.Chrome(path)  

# Maximize Window
driver.maximize_window() 
driver.minimize_window()  
driver.maximize_window()  
driver.switch_to.window(driver.current_window_handle)
driver.implicitly_wait(10)

# Enter to the site
driver.get('https://www.linkedin.com/login');
time.sleep(2)

#  Accepting cookies
driver.find_element_by_xpath("/html/body/div/main/div[1]/div/section/div/div[2]/button[2]").click()

# Credentials
user_name = 'enter email here'
password = 'enter password here'
driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_name)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
time.sleep(1)

# Login
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
driver.implicitly_wait(30)

# Get job page URL
url1 = 'enter url here'
driver.get(url1)
time.sleep(1)

links = []
# Navigate through pages
print('Collecting Links. ')
try: 
    for page in range(2,12):
        time.sleep(2)
        jobs_block = driver.find_element_by_class_name('jobs-search-results-list')
        jobs_list= jobs_block.find_elements(By.CSS_SELECTOR, '.job-card-list')
    
        for job in jobs_list:
            all_links = job.find_elements_by_tag_name('a')
            for a in all_links:
                if str(a.get_attribute('href')).startswith('https://www.linkedin.com/jobs/view') and a.get_attribute('href') not in links: 
                    links.append(a.get_attribute('href'))
                else:
                    pass
            # scroll down for each job element
            driver.execute_script('arguments[0].scrollIntoView();', job)
        
        print(f'Collecting link in page: {page-1}')
        # iterrating through pages
        driver.find_element_by_xpath(f"//button[@aria-label='Page {page}']").click()
        time.sleep(3)
except:
    pass
print('Found ' + str(len(links)) + ' links for job offers')


# Empty list to iterate to
job_titles = []
company_names = []
company_locations = []
work_methods = []
post_dates = []
work_times = [] 
job_desc = []

i = 0
j = 1
# Visiting job links to extract informationn
print('Visiting links to collect information. ')
for i in range(len(links)):
    try:
        driver.get(links[i])
        i=i+1
        time.sleep(2)
        driver.find_element_by_class_name("artdeco-card__actions").click()
        time.sleep(2)
    except:
        pass
    
    # Scraping job information
    contents = driver.find_elements_by_class_name('p5')
    for content in contents:
        try:
            job_titles.append(content.find_element_by_tag_name('h1').text)
            company_names.append(content.find_element_by_class_name('jobs-unified-top-card__company-name').text)
            company_locations.append(content.find_element_by_class_name('jobs-unified-top-card__bullet').text)
            work_methods.append(content.find_element_by_class_name('jobs-unified-top-card__workplace-type').text)
            post_dates.append(content.find_element_by_class_name('jobs-unified-top-card__posted-date').text)
            work_times.append(content.find_element_by_class_name('jobs-unified-top-card__job-insight').text)
            print(f'Scraping the Job Offer {j} DONE.')
            j+= 1
            
        except:
            pass
        time.sleep(2)
        
        # Scraping job description
    job_description = driver.find_elements_by_class_name('jobs-description__content')
    for description in job_description:
        job_text = description.find_element_by_class_name('jobs-box__html-content').text
        job_desc.append(job_text)
        print(f'Scraping Job Offer {j}')
        time.sleep(2)  
        

df = pd.DataFrame(list(zip(job_titles,company_names,
                    company_locations,work_methods,
                    post_dates,work_times)),
                    columns =['job_title', 'company_name',
                           'company_location','work_method',
                           'post_date','work_time'])

# Saving df to csv file
df.to_csv('job_offers.csv', index=False)

# printing job descriptions to text
with open('job_descriptions.txt', 'w',encoding="utf-8") as f:
    for line in job_desc:
        f.write(line)
        f.write('\n')

