class NSEURLList:

    def __init__(self):
        self.allNSEstockNameList = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"
        self.getparticularstockdetails = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?"
        self.getnsenifty50stock ="https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
        self.getnsederivativedetail = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp"


class MoneyControlURLList:

    def __init__(self):
        self.getallStockURL = "https://www.moneycontrol.com/india/stockpricequote/"
        self.getbseStockdetails = "https://priceapi-aws.moneycontrol.com/pricefeed/bse/equitycash/"
        self.getnseStockdetails = "https://priceapi-aws.moneycontrol.com/pricefeed/nse/equitycash/"

class GeneralURLList:

    def __init__(self):
        self.getGmailSMTP = "smtp.gmail.com"