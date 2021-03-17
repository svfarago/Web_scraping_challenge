#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from splinter import Browser
from selenium import webdriver


# In[2]:


# Set up Chrome Web driver with Splinter (above)
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


# Initialize PyMongo to work with MongoDBs
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


# In[4]:


# Define database and collection
db = client.mars_db
collection = db.items


# ## NASA Mars News
# * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
# * Assign the text to variables that you can reference later.

# In[5]:


# URL of page to scrape
# Note: Run splinter line above to open up a browser window, otherwise code won't run
url = "https://mars.nasa.gov/news/"
browser.visit(url)
html = browser.html


# In[6]:


# Create BeautifulSoup object; parse with html.parser for html structure
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify())


# In[7]:


# Search for the div where the title is located
results = soup.find_all('div', class_="content_title")
latest_news_title = results[1].text
print(f"Title: {latest_news_title}")


# In[8]:


# Scrape html container that has info; using .text to convert html detail body to text
latest_news_detail = soup.find("div", class_="article_teaser_body").text
latest_news_detail


# In[9]:


# Scrape news title and content
print(f"----Latest News----")
print(f"Title: {latest_news_title}")
print(f"Paragraph: {latest_news_detail}")


# In[ ]:


# Note: browser.quit() will hang .py export and won't enable it to run correctly. So rem the line out on export.
# browser.quit()


# ## JPL Mars Space Images - Featured Image
# * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# * Make sure to find the image url to the full size `.jpg` image.
# * Make sure to save a complete url string for this image.
# 

# In[ ]:


# Reminder to run first row of code if browser.quit() is run above


# In[17]:


# Open browser with JPL Featured Space Image url through splinter module
url_spaceimage = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_spaceimage)


# In[18]:


# HTML Object
html = browser.html
soup = BeautifulSoup(html, "html.parser")
#soup = BeautifulSoup(img_html, "html.parser")


# In[22]:


# Featured image - pull first chunk of html code
results = soup.find("div", class_ = "sm:object-cover object-cover")
print(results)


# In[23]:


# Featured image - refine first chunk of html code from above
results2 = results.find("img")
print(results2)


# In[24]:


# Featured image - refine second chunk of html code from above pull out URL
# Note: Rerun 2 rows above if the URL does not display below
image = results.findAll("img")
for results in image:
    print (results["src"])


# In[25]:


# Display url of the full image
featured_image_url = f"Featured Image:{img_results}"
print("--JPL Featured Space Image----")
print (results["src"])


# In[ ]:


# Note: browser.quit() will hang .py export and won't enable it to run correctly. So rem the line out on export.
# browser.quit()


# ## Mars Facts
# * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# * Use Pandas to convert the data to a HTML table string.

# In[ ]:


# Reminder to run first row of code if browser.quit() is run above


# In[ ]:


# Open browser using Chromedriver through splinter module
#executable_path = {"executable_path": "chromedriver.exe"}
#browser = Browser("chrome", **executable_path, headless=False)


# In[26]:


url="https://space-facts.com/mars/"
browser.visit(url)
html = browser.html


# In[27]:


# Pull all Mars facts
facts=pd.read_html(url)
#facts


# In[28]:


# Put Mars facts into an indexed dataframe
mars_facts_df=facts[0]
mars_facts_df


# In[29]:


# Save dataframe to html
mars_facts_df.to_html()


# In[30]:


# Save html to table
html_table = mars_facts_df.to_html()

# Remove unwanted newlines to clean up the table
html_table.replace("\n", "")

# Save html table to folder Mission_to_Mars
mars_facts_df.to_html("mars_facts_data.html")


# In[ ]:


# Note: browser.quit() will hang .py export and won't enable it to run correctly. So rem the line out on export.
# browser.quit()


# ## Mars Hemispheres
# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# * Click each of the links to the hemispheres in order to find the image url to the full resolution image.
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# In[ ]:


# Reminder to run first row of code if browser.quit() is run above


# In[ ]:


# Open browser using Chromedriver through splinter module
#executable_path = {"executable_path": "chromedriver.exe"}
#browser = Browser("chrome", **executable_path, headless=False)


# In[31]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
html = browser.html


# In[32]:


# Create BeautifulSoup object; parse with html.parser for html structure
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())


# In[33]:


# Scrape all 4 items from page containing Mars hemispheres info. This creates 4 image URLs.
result=soup.find_all("div", class_="item")
#result

# Create empty list to store image titles and urls
image_urls=[]

# Assign base url for loop
base_url="https://astrogeology.usgs.gov"

# Go through above scrape and refine/clean further using for loop
for item in result:
    
    # Get image titles, strip "enhanced" from the end of each title
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

# Print title and image URL formatted
    print(titles)
    print(image_url)
    print("-----------")

# Or print url string outside of for loop
#print(image_urls)


# In[ ]:


# Note: browser.quit() will hang .py export and won't enable it to run correctly. So rem the line out on export.
# browser.quit()

