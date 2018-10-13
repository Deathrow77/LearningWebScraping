from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("URL ERROR :: \t" + e)
    try:
        bs = BeautifulSoup(html, 'lxml')
        return bs.body.h1
    except AttributeError as e:
        print(e)
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title==None:
    print("Page not found !!")
else:
    print(title)
