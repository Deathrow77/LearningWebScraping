from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getData(url):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find('p').get_text())
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print(e)

    for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('\n'*3)
                print(newPage)
                pages.add(newPage)
                getData(newPage)

getData('')
