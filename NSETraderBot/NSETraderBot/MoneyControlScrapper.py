from bs4 import BeautifulSoup
from NSETraderBot import ConstURLList
import requests

moneycontrolURl = ConstURLList.MoneyControlURLList()


def getallequityURL():
    rtnstockdetailslist = []
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
                    rtnstockdetailslist.append([stocklistlinktd, stocklistcpyname])
            except:
                stocklistlinktd = None
                stocklistcpyname = None
    except requests.exceptions.ConnectionError:
        print("Unable to connect the URL")
        rtnstockdetailslist = None
    except:
        print("Unknown Error in getallequityURL()")
    return rtnstockdetailslist


def get_stock_detail(arg_stock_type, arg_stock_symbol):
    try:
        if arg_stock_type.upper() == "BSE":
            res = requests.get(moneycontrolURl.getbseStockdetails + arg_stock_symbol, timeout=3)
        elif arg_stock_type.upper() == "NSE":
            res = requests.get(moneycontrolURl.getnseStockdetails + arg_stock_symbol, timeout=3)
        rtnstockdetails = res.json()
    except Exception as ex:
        print("Unkown Error : " + str(ex))
        rtnstockdetails = None
    return rtnstockdetails
