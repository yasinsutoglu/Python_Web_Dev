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

# USE SCRAPY framework if you want to scrape massive websites, massive amounts of data.!!!!!
# https://scrapy.org/
# ******************************************
# import requests # requests lib is used to download initially related html.
# from bs4 import BeautifulSoup # It's a LIB that allows us to use the html and grab different data.
# import pprint  # pretty print - used to print with appropriate spacing, for readability

# url = 'https://news.ycombinator.com/'
# res = requests.get(url)

# print(res)    # Response 200 menas everything is good
# print(res.text)
# this will have the entire html data in it. Exactly the same thing which we get when we click 'View Page Source'

# soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)
# this will also have the exact same thing as res.text, but it will keep in html format, and not in string format,
# and it will be easier to manupulate it

# print(soup.body)
# print(soup.body.contents)    # result comes in a 'list' in this case. But not with the previous cases.

# print(soup.find_all('div'))
# print(soup.find_all('a'))    # find all the 'a' tags - all the links
# print(soup.title)
# print(soup.a)     # it finds the first a tag
# print(soup.find('a'))    # it finds the first a tag

# print(soup.find(id="score_24273602"))
# print(soup.select("#score_24273602"))   # outputs in a list
# select grabs the data using a CSS selector, where '.' means 'class', '#' means 'id', etc.

# print(soup.select('a')[0])
# grabs all the 'a' tags, and print only the first one, as this is a list, and we want the 0th item

# print(soup.select(".score")) # grabs all the class="score" tags

# links = soup.select(".storylink")
# <a class="storylink" href="https://www.bbc.com/news/world-africa-53887947">Africa declared free of wild polio</a>
# print(links[0].get('href'))

# voted_links = soup.select(".storylink").select('#vote')

# ---------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res) #<Response [200]>
# print(res.text) # all contents of the html file in txt format
soup = BeautifulSoup(res.text, 'html.parser') # Conversion from txt to real html object(suitable to scrap)
# print(soup)
# print(soup.title) # <title>Hacker News</title>
# print(soup.body)
# print(soup.body.form)
# print(soup.find_all('div')) # all divs in a list
# print(soup.find('a')) # finds the first a tag
# print(soup.find('a')['href']) # https://news.ycombinator.com
# print(soup.find(id='score_20514755')) # <span class='score' id="score_20514755"> 159 points </span>


res2 = requests.get('https://news.ycombinator.com/news?p=2') # scraping for page2
soup2 = BeautifulSoup(res2.text, 'html.parser')

# select(.titleline > a) => css selector baz alarak find() işlevini yapar
links = soup.select('.titleline')
# print("output:" , links[0])
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		# print(vote) # one of them: [<span class="score" id="score_42396372">183 points</span>]
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
