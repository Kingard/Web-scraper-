#!/usr/bin/env python
# coding: utf-8

# In[20]:


from bs4 import BeautifulSoup as bs
import requests
import csv

# Parsing the html content and extracting the text
source = requests.get('http://www.coreyms.com').text
web_page = bs(source,'html.parser')

# Identifying the block that contains all the required fields 
container = web_page.find('article')

# Obtaining the first required field "Headline"
headline = container.h2.a.text

# Obtaining the summary field
summary = container.find('div',class_='entry-content').p.text

# Obtaining the video link and intergrating with the video ID
vid_link = container.find('iframe',class_='youtube-player')['src']
vid_id = vid_link.split('/')
vid_id = vid_id[4].split('?')
vid_id = vid_id[0]
yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)


# In[21]:


# INTEGRATION OF THE EXTRACTED FIELDS AND LOOPING THROUGH EACH FIELD TO OBTAIN ALL THE FIELDS FOR EACH BLOCK (CONTAINER) ON THE 
# WEB PAGE 

#containers = web_page.find_all('article')

from bs4 import BeautifulSoup as bs
import requests
import csv

source = requests.get('http://www.coreyms.com').text
web_page = bs(source,'html.parser')
container = web_page.find('article')

scraper_file = open('scraper.csv','w') 
csv_writer = csv.writer(scraper_file)
csv_writer.writerow(['Headline','Summary','Video link'])

for container in web_page.findAll('article'):
    headline = container.h2.a.text
    print(headline)
    
    summary = container.find('div',class_='entry-content').p.text
    print(summary)
    

    
    try:
        vid_link = container.find('iframe',class_='youtube-player')['src']
        vid_id = vid_link.split('/')
        vid_id = vid_id[4].split('?')
        vid_id = vid_id[0]
        yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)
        
    except Exception as e:
        yt_link = None
        
    print(yt_link)
    
    print()
    
    csv_writer.writerow([headline, summary, yt_link])
    
scraper_file.close()
    
    


# In[2]:


''' YO BBB'''


# In[ ]:




