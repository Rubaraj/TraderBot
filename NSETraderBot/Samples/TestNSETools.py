from nsetools import Nse

nse = Nse()

allsocks = nse.get_stock_codes()

# print(len(allsocks))
stock_item = nse.get_quote('infy', as_json=False)

print(type(stock_item))