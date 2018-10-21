from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(url):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')
                        
