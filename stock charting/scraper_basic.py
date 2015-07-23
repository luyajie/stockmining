__author__ = 'well'

from  selenium import webdriver

from bs4 import BeautifulSoup
import urllib2

#url = "http://basic.10jqka.com.cn/002271/finance.html"
url = "http://basic.10jqka.com.cn/300085/finance.html"

browser = webdriver.Firefox()
browser.get(url)
html_page = browser.page_source
browser.quit()
#r = requests.get(url)
#print r.content
#page = urllib2.urlopen(url).read()

soup = BeautifulSoup(html_page)
#print soup.prettify()

finance_table = soup.find("div",attrs={"id":"finance", "stat":"finance_finance"})
#print finance_table.prettify()

cwzbTable = finance_table.find_next("div", attrs={"id":"cwzbTable", "class":"cwzb_table"})
table_data = cwzbTable.find_next("div",class_="table_data")
#print table_data.prettify()

left_thread = table_data.div
finance_types = left_thread.find_all("tr")
finance_type_list = []
for ftype in finance_types:
	text = unicode(ftype.th.string)
	finance_type_list.append(text)
	#print text
#print finance_type_list

data_tbody = left_thread.find_next_sibling()
top_thread = data_tbody.table
season_dates = top_thread.find_all("th")
season_date_list = []
for sdate in season_dates:
	text = sdate.div.string
	season_date_list.append(text)
#print season_date_list

tbody_thread = top_thread.find_next_sibling()
table_rows = tbody_thread.tbody
table_body = {}
cn = 0
for trow in table_rows:
	row_list = []
	for td in trow.find_all("td"):
		row_list.append(td.string)
	table_body[finance_type_list[cn]] = row_list
	cn = cn + 1
	print finance_type_list[cn],":", ' '.join(row_list)

#print table_body




