# Webscrape-2.0
Webscraping LinkedIn jobs 
<!--  -->
This is my second time trying to webscrape. My first project was websraping Indeed.com jobs - this time I decided to scrape LinkedIn.
WebScrape 1.0 was my first attempt at doing this however, there was an issue with scraping job descriptions as I could only do it for the selected job.
The final webscrape fixes this by iterating through 'x' amount of pages and picking out links for the various jobs on different pages then saving job details to a csv file and the job description for each job in a single text file.
Job descriptions were then subbject to word count to see the required skills for data analyst positions in my location.

EDIT 7/12/2022
First iteration of looking at the skills was implementing a simple word count on keywords which are associated with data analyst postions
This update I decided to do the same thing except using NLP through nltk which is a much better version of the code I had perviously


<!--  -->
Code Insprired from - https://medium.com/@kurumert/web-scraping-linkedin-job-page-with-selenium-python-e0b6183a5954

