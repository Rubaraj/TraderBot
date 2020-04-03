from NSETraderBot import Helper


nseHelper = Helper.NSEHelper()

all_nse_stocks = nseHelper.getallNSEStockName()
nse_stock_count = len(all_nse_stocks)

sum = nse_stock_count / 5

x =  list(all_nse_stocks.items())[:30]

<<<<<<< HEAD
print(type(all_nse_stocks))

=======
# print(all_nse_stocks)
# Test_GitHub
>>>>>>> c49f7b7f5f590cefac677a15937792e91c40e101

# for stock_symbol in all_nse_stocks:
#     print(f" the stock symbol is {stock_symbol} and the company is {stock_symbol[:]}")
#     if stock_symbol.upper() != "SYMBOL":
#         print(stock_symbol)
#         print(nseHelper.get_stock_detail(stock_symbol.upper()))