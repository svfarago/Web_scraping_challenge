# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import time
import pandas as pd
from splinter import Browser
from selenium import webdriver


def init_browser():
#Define path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_all():
    mars_data={}
    browser = init_browser()


## ---------Latest News
#----Visit Mars News site to retrieve latest news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

# URL of page to scrape 
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    time.sleep(4)
    soup = BeautifulSoup(html, "html.parser") 

# Scrape the container that has info
    results_head = soup.find_all("div", class_="content_title")
    results_title = results_head[1].text
    latest_news_title = results_title
    results_body = soup.find("div", class_="article_teaser_body")
    results_detail= results_body.text
    latest_news_detail = results_detail

## ---------Featured Space Image
# Open browser with JPL Featured Space Image url through splinter module
    url_spaceimage = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_spaceimage)
    time.sleep(4)
    browser.find_by_css("img.BaseImage").click()    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    feature_image_url = soup.find("a", class_="BaseButton")["href"]
    feature_image_url


## ---------Mars Facts
    url = "http://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_facts_df = tables[2]
    mars_facts_df.columns = ["Description", "Value"]
    mars_html_table = mars_facts_df.to_html()
    mars_html_table.replace('\n', '')


##---------Mars Hemispheres 4 Images
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

# Scrape all 4 items from page containing Mars hemispheres info. This creates 4 image URLs.
    result=soup.find_all("div", class_="item")

# Create empty list to store image titles and urls
    image_urls=[]
    base_url="https://astrogeology.usgs.gov"

# Go through above scrape and refine/clean further using the for loop
    for item in result:
    
    # Get image titles, remove (strip) "enhanced" from the end of each title
        titles=item.find("h3").text
        titles=titles.strip("Enhanced")
    
    # Get relative links of images 
        link=item.find("a", class_="itemLink product-item")["href"]
    
    # Get absolute links of images 
        image_link=base_url+link
    
    # Browse to page with link for full image; this opens a new tab for each image
        browser.visit(image_link)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        records = soup.find("div", class_="downloads")
    
    # Get links of full-sized images
        image_url = records.find("a")["href"]
    
    # Append results into a list of dictionaries
        image_urls.append({"title": titles, "image_url": image_url})


    # Store data in a dictionary to be used in Mongo database
    mars_data = {
        "latest_news": latest_news_title,
        "latest_news_detail": latest_news_detail,
        "feature_image_url": feature_image_url,
        "mars_html_table": mars_html_table,
        "image_urls": image_urls
    }

        
 # Close the browser after scraping
    browser.quit()
    # Return results
    return mars_data

if __name__ == "__main__":
        scrape_all()

