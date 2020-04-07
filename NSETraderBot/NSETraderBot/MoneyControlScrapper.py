from bs4 import BeautifulSoup
from NSETraderBot import ConstURLList
import requests


moneycontrolURl = ConstURLList.MoneyControlURLList()


def getallequityURL():
    rtnstockdetailslist = {}
    try:
        source = requests.get(moneycontrolURl.getallStockURL).text
        soup = BeautifulSoup(source, 'lxml')
        stocklist_table = soup.find('table', class_='pcq_tbl MT10')
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
                    rtnstockdetailslist.update({stocklistcpyname:stocklistlinktd})
            except:
                stocklistlinktd = None
                stocklistcpyname = None
    except requests.exceptions.ConnectionError:
        print("Unable to connect the URL")
        rtnstockdetailslist = None
    except:
        print("Unknown Error in getallequityURL()")
    if rtnstockdetailslist != None:
        del rtnstockdetailslist['']
    return rtnstockdetailslist

testlist = getallequityURL()
print(testlist)