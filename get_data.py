
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://www.rbi.org.in/Scripts/ATMView.aspx")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    if link.get('href') is None:
        continue
    if 'XLSX' in link.get('href') :
        links.append(link.get('href'))

month_names = []
for name in soup.findAll('b'):
    month_names.append(name.text)

print(month_names)
print(links)
