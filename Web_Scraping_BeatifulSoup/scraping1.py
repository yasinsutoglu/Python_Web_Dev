# Web Scraping : Grabbing Data From a Website such as Amazon, AirBnb etc.
# https://medium.com/@Excellarate/web-scraping-introduction-applications-and-best-practices-c7e5eb06c07e
# https://medium.com/@jugalsolanki1072/the-complete-guide-to-web-scraping-with-python-a2b55757e40c
# Download a webpage, grab the data, clean it up, then use this cleaned data.
# After opening the website, "View the page source" with mouse right click --> this html source will be used.
# Because, all of the info is included in here.

# https://www.airbnb.ca/robots.txt -->  "robots.txt": By this txt file, examine what things you are allowed to
# scrape from this webapp.
# https://www.udemy.com/robots.txt; https://www.amazon.com/robots.txt

# Useful Extension: https://webscraper.io/web-scraper-first-time-install

# Some websites open their APIs to public in JSON format, they can be used to scrape data.
# For training, you can use https://swapi.co
# ---------------------------------------------------------
import requests # used to download initially that html.
from bs4 import BeautifulSoup # allows us to use the html and grab different data.
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res) #<Response [200]>
print(res.text) # all contents of the html file in txt format
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')





