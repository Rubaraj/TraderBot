from NSETraderBot import MoneyControlScrapper,Helper

getnsesite = Helper.NSEHelper()

all_stock_name = getnsesite.getallNSEStockName()
del all_stock_name['SYMBOL']



for stock in all_stock_name:
    print(f"------------------start stock : {stock}")
    bselive = MoneyControlScrapper.get_stock_detail('nse',stock.upper())['data']
    nselive = MoneyControlScrapper.get_stock_detail('nse',stock.upper())['data']

    if bselive == None and nselive == None:
        print(f"No data found for the stock {stock}")
    else:
        if bselive != None:
            print(f"BSE Live for {stock} : {bselive['pricecurrent']}")
        if nselive != None:
            print(f"NSE Live for {stock}: {nselive['pricecurrent']}")
    print(f"------------------end stock : {stock}")