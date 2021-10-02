from bs4 import BeautifulSoup as bs
from splinter import Browser, browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
#import pymongo

# mongo set up
#mongo_local_connection_string = "mongodb://localhost:27017"
#client = pymongo.MongoClient(mongo_local_connection_string)
#db = client.web_scraping
#collection = db.mars_data

# assign chromedriver to namespace
chrome_driver = "/Users/patba/Desktop/ChromeDriver/chromedriver"
executable_path = {'executable_path': chrome_driver}
browser = Browser('chrome', **executable_path, headless=False)


# MARS NEWS
def mars_news(browser):
    mars_url = 'https://redplanetscience.com/'
    browser.visit(mars_url)

    # parse html data using beautifulsoup
    mars_html = browser.html
    mars_soup = bs(mars_html, 'html.parser')

    # get latest news title
    news_title = mars_soup.find('div', class_='content_title').get_text()

    # get paragraph text from the latest news article
    news_p = mars_soup.find('div', class_='article_teaser_body').get_text()

    new_news_dict = {'title': [news_title],
                    'summary': [news_p]}

    return new_news_dict

# SPACE IMAGES from MARS - featured image
def featured_image(browser):
    space_url = 'https://spaceimages-mars.com'
    browser.visit(space_url)

    # parse html data using beautifulsoup
    space_html = browser.html
    space_soup = bs(space_html, 'html.parser')

    # get the featured image 
    featured_img = space_soup.find('img', class_='headerimage fade-in').get('src')

    # assign featured img to url string
    featured_img_url = f'{space_url + featured_img}'

    feature_img_dict = {"title": "Featured Mars Image",
                        "url": featured_img_url}

    return feature_img_dict


# MARS FACTS
def mars_facts(browser):
    mars_facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(mars_facts_url)

    # get mars facts table using pandas - returns table as list - iterate
    planet_facts_dfs = pd.read_html(mars_facts_url)

    # display mars facts df
    mars_df = planet_facts_dfs[1]
    mars_df.rename(columns={0 : "Properties", 1 : "Mars Facts"}).set_index("Properties")

    # mars earth comparison df
    earth_mars_df = planet_facts_dfs[0]
    earth_mars_df = earth_mars_df.rename(columns={0 : "Properties", 1 : "", 2 : ""}).set_index("Properties")

    earth_mars_dict = earth_mars_df.T.to_dict('list')

    return earth_mars_dict

# MARS hemisphere
def mars_hemi(browser):
    mars_hemi_url = 'https://marshemispheres.com/'
    browser.visit(mars_hemi_url)

    # parse html data with beautiful soup
    mars_hemi_html = browser.html
    mars_hemi_soup = bs(mars_hemi_html, 'html.parser')

    # create empty list and append links of enhanced mars hemisphere images to list
    links = []
    for h in mars_hemi_soup.find_all('a', class_='itemLink product-item'):
        if h not in links:
            links.append(h.get('href'))

    # create empty list and append enhanced mars hemisphere img titles to list
    titles = []
    for h in mars_hemi_soup.find_all('h3'):
        if h not in titles:
            titles.append(h.get_text())

    # hemisphere urls
    # assign namespace to mars hemisphere imgs to url string and get image titles
    mars_img_A = f'{mars_hemi_url + links[0]}'
    mars_img_B = f'{mars_hemi_url + links[2]}'
    mars_img_C = f'{mars_hemi_url + links[4]}'
    mars_img_D = f'{mars_hemi_url + links[6]}'

    # assign namespace to mars hemisphere img titles to
    mars_title_A = titles[0]
    mars_title_B = titles[1]
    mars_title_C = titles[2]
    mars_title_D = titles[3]

    # mars hemisphere img dictionary
    hemi_img_dict = {'title': [mars_title_A, mars_title_B, mars_title_C, mars_title_D],
                    'url': [mars_img_A, mars_img_B, mars_img_C, mars_img_D]}

    return hemi_img_dict


def scrape():
    new_news_dict = mars_news(browser)
    feature_img_dict = featured_image(browser)
    earth_mars_dict = mars_facts(browser)
    hemi_img_dict = mars_hemi(browser)

    mars_dict = {
        'news': new_news_dict,
        'feat_img': feature_img_dict,
        'mars_facts': earth_mars_dict,
        'hemi_img': hemi_img_dict
    }
    browser.quit()
    return mars_dict

#with open('mars.json', 'w') as outfile:
#    json.dump(scrape(), outfile, indent=4)

print(scrape())