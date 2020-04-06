from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.moneycontrol.com/india/stockpricequote/').text

soup = BeautifulSoup(source,'lxml')

# stocklist_table = soup.find('table',class_='pcq_tbl MT10')
# print(stocklist_table.prettify())

stocklist_table = soup.find('table',class_='pcq_tbl MT10')

for stocklinktr in stocklist_table.find_all('tr'):
    stocklistlinktd = None
    stocklistcpyname = None
    try:
        for stocklisttd in stocklinktr.find_all('td'):
            try:
                stocklistlinktd = stocklisttd.a['href']
                stocklistcpyname = stocklisttd.a['title']
            except:
                stocklistlinktd = None
                stocklistcpyname = None
            print(stocklistlinktd, stocklistcpyname)
    except:
        stocklistlinktd = None
        stocklistcpyname = None


# print(stocklinktr.prettify())

# print(soup.prettify())

