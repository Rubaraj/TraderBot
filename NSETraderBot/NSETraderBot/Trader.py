from NSETraderBot import Helper
import _thread

nseHelper = Helper.NSEHelper()

all_nse_stocks = nseHelper.getallNSEStockName()

def getstockdetails (argthrdlist,argstrThrdname):
    for stock_symbol in argthrdlist:
        print(f" Thread Name: {argstrThrdname} the stock symbol is {stock_symbol[0]} and the company is {stock_symbol[1]}")
        print(stock_symbol[0])
        print(nseHelper.get_stock_detail(stock_symbol[0].upper()))

start_count = 0
per_thrd_count = int(len(all_nse_stocks) / 5)
end_count = per_thrd_count

first_thrd = list(all_nse_stocks.items())[start_count:end_count]
first_thrd.pop(0)
start_count = end_count
end_count += per_thrd_count
second_thrd = list(all_nse_stocks.items())[start_count:end_count]
start_count = end_count
end_count += per_thrd_count
third_thrd = list(all_nse_stocks.items())[start_count:end_count]
start_count = end_count
end_count += per_thrd_count
fourth_thrd = list(all_nse_stocks.items())[start_count:end_count]
start_count = end_count
fifth_thrd = list(all_nse_stocks.items())[start_count:end_count]

_thread.start_new_thread(getstockdetails,(first_thrd,"First Thread"))
_thread.start_new_thread(getstockdetails,(second_thrd,"second Thread"))
_thread.start_new_thread(getstockdetails,(third_thrd,"Third Thread"))
_thread.start_new_thread(getstockdetails,(fourth_thrd,"Fourth Thread"))
_thread.start_new_thread(getstockdetails,(fifth_thrd,"Fifth Thread"))

while 1:
    pass