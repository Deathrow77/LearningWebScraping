# Python Scraper to scrape the logo from https://www.pythonscraping.com
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com")
bs = BeautifulSoup(html, 'html.parser')
imageLoc = bs.find('a', {'id':'logo'}).find('img')['src']
urlretrieve(imageLoc, "logo.jpg")
