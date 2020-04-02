from NSETraderBot import Helper

nseHelper = Helper.NSEHelper()

all_nse_stocks = nseHelper.getallNSEStockName()


# print(all_nse_stocks)


for stock_symbol in all_nse_stocks:
    print(f" the stock symbol is {stock_symbol} and the company is {stock_symbol[:]}")
    if stock_symbol.upper() != "SYMBOL":
        print(nseHelper.get_stock_detail(stock_symbol.upper()))
        break