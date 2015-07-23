__author__ = 'well'

from bs4 import BeautifulSoup


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')

tag = soup.b
print tag.name, tag['class'],
