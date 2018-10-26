import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

baseUrl = 'https://www.pythonscraping.com'

# Getting the absolute paths of every link with respect to the base url
def getAbsolutePath(baseUrl, source):
    if source.startswith('https://www.'):
        url = 'https://{}'.format(source[11:])
    elif source.startswith('https://'):
        url = source
    elif source.startswith('www.'):
        url = 'https://{}'.format(source[4:])
    else:
        url = "{}/{}".format(baseUrl, source)

    if baseUrl not in url:
        return None
    return url
