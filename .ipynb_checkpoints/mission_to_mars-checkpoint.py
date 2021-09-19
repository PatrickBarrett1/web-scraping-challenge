#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pandas as pd


# In[15]:


filepath = os.path.join('NewsMarsExplorationProgram.html')
with open(filepath, encoding='utf-8') as file:
    html = file.read()


# In[17]:


chrome_driver = "/Users/patba/Desktop/ChromeDriver/chromedriver"
executable_path = {'executable_path': chrome_driver}
browser = Browser('chrome', **executable_path, headless=False)


# In[18]:


mars_url = 'https://redplanetscience.com/'
browser.visit(mars_url)


# In[19]:


mars_html = browser.html
mars_soup = bs(mars_html, 'html.parser')


# In[20]:


# get latest news title
news_title = mars_soup.find('div', class_='content_title').get_text()
print('The latest news title is: ' + news_title)


# In[21]:


# get paragraph text from the latest news article
news_p = mars_soup.find('div', class_='article_teaser_body').get_text()
print(news_p)


# In[22]:


browser.quit()


# In[23]:


# SPACE IMAGES FROM MARS
executable_path = {'executable_path': chrome_driver}
browser = Browser('chrome', **executable_path, headless=False)
space_url = 'https://spaceimages-mars.com'
browser.visit(space_url)


# In[24]:


space_html = browser.html
space_soup = bs(space_html, 'html.parser')


# In[25]:


# find featured image 
featured_img = space_soup.find('img', class_='headerimage fade-in').get('src')
print(featured_img)


# In[26]:


# assign featured img to url string
featured_img_url = f'{space_url + featured_img}'
featured_img_url


# In[27]:


browser.quit()


# In[28]:


# MARS FACTS
executable_path = {'executable_path': chrome_driver}
browser = Browser('chrome', **executable_path, headless=False)
mars_facts_url = 'https://galaxyfacts-mars.com/'
browser.visit(mars_facts_url)


# In[29]:


# 
mars_facts_html = browser.html
mars_facts_soup = bs(mars_facts_html, 'html.parser')


# In[30]:


# scrape mars facts table
planet_facts_dfs = pd.read_html(mars_facts_url)
planet_facts_dfs


# In[31]:


# mars facts dfs
mars_dfs = planet_facts_dfs[1]
mars_dfs.rename(columns={0 : "Properties", 1 : "Mars Facts"}).set_index("Properties")


# In[32]:


# mars earth comparison df
earth_dfs = planet_facts_dfs[0]
earth_dfs.rename(columns={0 : "Properties", 1 : "", 2 : ""}).set_index("Properties")


# In[33]:


browser.quit()


# In[35]:


# MARS HEMISPHERE
executable_path = {'executable_path': chrome_driver}
browser = Browser('chrome', **executable_path, headless=False)
mars_hemi_url = 'https://marshemispheres.com/'
browser.visit(mars_hemi_url)


# In[36]:


mars_hemi_html = browser.html
mars_hemi_soup = bs(mars_hemi_html, 'html.parser')


# In[37]:


# get links to enhanced images
links = []
for h in mars_hemi_soup.find_all('a', class_='itemLink product-item'):
    if h not in links:
        links.append(h.get('href'))


# In[38]:


# get titles of imgs
titles = []
for h in mars_hemi_soup.find_all('h3'):
    if h not in titles:
        titles.append(h.get_text())


# In[39]:


links[0]


# In[227]:


# hemisphere urls


# In[40]:


# assign featured img to url string
mars_img_A = f'{mars_hemi_url + links[0]}'
mars_img_B = f'{mars_hemi_url + links[2]}'
mars_img_C = f'{mars_hemi_url + links[4]}'
mars_img_D = f'{mars_hemi_url + links[6]}'

print(mars_img_A + "\n" + mars_img_B + "\n" + mars_img_C + "\n" + mars_img_D)


# In[41]:


mars_title_A = titles[0]
mars_title_B = titles[1]
mars_title_C = titles[2]
mars_title_D = titles[3]
print(mars_title_A + "\n" + mars_title_B + "\n" + mars_title_C + "\n" + mars_title_D)


# In[42]:


hemi_img_urls = [
    {"title": mars_title_A, "img_url": mars_img_A},
    {"title": mars_title_B, "img_url": mars_img_B},
    {"title": mars_title_C, "img_url": mars_img_C},
    {"title": mars_title_D, "img_url": mars_img_D}
]


# In[43]:


hemi_img_urls


# In[ ]:




