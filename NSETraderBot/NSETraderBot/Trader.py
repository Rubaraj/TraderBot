from NSETraderBot import Helper

nseHelper = Helper.NSEHelper()


all_nse_stocks = nseHelper.getallNSEStockName()
all_nse_stocks = list(all_nse_stocks.items())
all_nse_stocks.pop(0)

start_count = 0
per_thrd_count = int(len(all_nse_stocks) / 5)
end_count = per_thrd_count


v = all_nse_stocks[start_count:end_count]
start_count = end_count
end_count += per_thrd_count
w = all_nse_stocks[start_count:end_count]
start_count = end_count
end_count += per_thrd_count
x = all_nse_stocks[start_count:end_count]
start_count = end_count
end_count += per_thrd_count
y = all_nse_stocks[start_count:end_count]
start_count = end_count
z = all_nse_stocks[start_count:]




for stock_symbol in all_nse_stocks:
    print(f" the stock symbol is {stock_symbol} and the company is {stock_symbol[:]}")
    if stock_symbol.upper() != "SYMBOL":
        print(stock_symbol)
        print(nseHelper.get_stock_detail(stock_symbol.upper()))
