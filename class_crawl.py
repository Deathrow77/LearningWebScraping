import requests
from bs4 import BeautifulSoup
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.body = body
        self.title = title
def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYtimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find_all('p', {'class':'body-content'})
    body = '\n'.join([line.text for line in lines])
    return Content(url, title,body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class':'post-body'})
    return Content(url, title, body)
            
            
url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'

content = scrapeBrookings(url)
print('Title : {}'.format(content.title))
print('URL : {}'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/'
content = scrapeNYtimes(url)
print('Title : {}'.format(content.title))
print('URL : {}'.format(content.url))
print(content.body)
