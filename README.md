# Web Scraping Challenge
* This project uses Beautiful Soup, Pymongo, Splinter, HTML, CSS, Bootstrap, Chromedriver.

## ReadMe File
* Updated: March 18 2021 | Created: March 2, 2021
* Copyright: open source

### License ===========================
* None. See Installation instructions below for a list of applications.


### Configuration Instructions ========
* None


### Installation Instructions ==========
Applications used:
- Beautiful Soup
- Pymongo
- Flask
- Splinter
- Google Chrome browser
- Visual Studio Code
- GitBash terminal
- Git Hub (to save versions and share code while in development)
- Image viewer such as Microsoft Photos or Microsoft Paint
* Similar applications may also work.


https://pypi.org/project/webdrivermanager/
pip install webdrivermanager

The above module is dependent on the following additional packages (install from commandline):
- pip install splinter
- pip install requests
- pip install tqdm
- pip install BeautifulSoup4
- pip install appdirs
- pip install flask-pymongo


### List of Files ====================
* \Web_scraping_challenge
*    \Mission_to_Mars
        app.py
        chromedriver.exe
        mars_facts_data.html
        scrape.py
        mission_to_mars.ipynb
        \.ipynb_checkpoints
                 mission_to_mars-checkpoint.ipynb
        \ __pycache__
                scrape_mars.cpython-38
        screen_database and website
                Mission to Mars_pdf of website.pdf
                MongoDB - mars_app.png
        templates
                index.html
*   README.md


### Operating Instructions =============
*All pages are designed to run and interact with one another on a local machine. Web pages are not hosted on a central server.
1. Open GitBash window in same directory as app.py.
2. Run at command "python app.py".
3. Open browswer and navigate to localhost:5000. This page will activate scripts to run to scrape websites.
4. Click the "Click to Scrape Top Mars Headline" button. Or navigate to localhost:5000/scrape and reload/refresh the page. This executes the scrape_mars.py script. Scraped web data will display in browser.
5. Open MongoDB and view scraped data in mars_app database.

* See also jupyter notebook for detailed notes on scripts and outputs.


### Data Set(s) =======================
* See also "List of Files" section above for files associated with this project.
* URLs used to scrape and pull data:
- https://space-facts.com/mars/
- https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
- https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars


### Additional Resources =======================
* None.


###  Data Alterations =======================
* None.


###  Known Bugs =====================
* CAUTION: If running scrape script with Chromedriver too frequenty (more than 3 times in 10-15 minutes) it may cause Windows to lock you out of your account for 10 min as a security precaution.


### Troubleshooting ===============
* Comments are used liberally throughout the code to run individual lines of code for additional testing/troubleshooting, and code notes/additional information.

* Resources used to build and troubleshoot this code are listed below, in addition to help and code peer review from students, instructor, and TA's.

* Web URLs:
- https://space-facts.com/mars/
- https://www.w3.org/TR/webdriver2/
- https://beautifytools.com/html-beautifier.php
- https://pypi.org/project/Flask-PyMongo/
- https://stackoverflow.com/questions/43982002/
- https://stackoverflow.com/questions/49788257/
- https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
- https://www.geeksforgeeks.org/extracting-an-attribute-value-with-beautifulsoup-in-python/
- https://www.knowledgehut.com/blog/programming/python-split-function
extract-src-attribute-from-img-tag-using-beautifulsoup/47166671 (For Texts with img tag)
- https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
what-is-default-location-of-chromedriver-and-for-installing-chrome-on-windows
* URLs last used: March 18, 2021


###  Contact Information ===============
Colorado   United States


### Random Notes ===============
This project uses Beautiful Soup, Pymongo, Splinter, HTML, CSS, Bootstrap, Chromedriver.
Time to complete: approximately 25 hours
