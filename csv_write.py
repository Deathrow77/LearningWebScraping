from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs = BeautifulSoup(html, 'html.parser')

csvFile = open('edit.csv', 'wt+')

table = bs.findAll("table", {'class':'wikitable'})[0]
rows = table.findAll('tr')

writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRows =[]
        for cell in row.findAll(['td', 'th']):
            csvRows.append(cell.get_text())
            writer.writerow(csvRows)

finally:
    csvFile.close()
