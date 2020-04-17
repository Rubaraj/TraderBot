from NSETraderBot import MoneyControlScrapper,Helper,Tradingstrategy,Utility,NSEScrapper

tradingstrategy= Tradingstrategy.OpenHighOpenLow()
nsescra = NSEScrapper.NSEStockSite()

# nsescra.getOtherInformationNSEDerivative('CIPLA')
# nify50_json_obj = tradingstrategy.getopenhighopenlow()

# print(nify50_json_obj)

#> sorted(lst, key=lambda x: x[1], reverse=True)

# nify50_json_obj = sorted(nify50_json_obj,key=lambda  x:x['symbol'],reverse=False)

# print (nify50_json_obj)

tradingstrategy.sendgetopenhighopenlowmaail()

#nsescrap = NSEScrapper.NSEStockSite()

#stock_data = nsescrap.getOtherInformationNSEDerivative('TCS')[0]

# print(type(stock_data))

# print(stock_data['dailyVolatility'])

#tradingstrategy.sendgetopenhighopenlowmaail()