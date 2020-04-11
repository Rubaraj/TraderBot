from NSETraderBot import MoneyControlScrapper,Helper,Tradingstrategy,Utility
tradingstrategy= Tradingstrategy.OpenHighOpenLow()
sendmail = Utility.GeneralUtility()


nify50_json_obj = tradingstrategy.getopenhighopenlow()
mail_htmlcontent = """
<!DOCTYPE html> <html> <head> 
<style> table, th, td {   border: 1px solid black; border-collapse: collapse; } th, td {   padding: 5px;   text-align: left; } th {background-color: #4CAF50;color: white;}</style>
</head> <body> <h2>Eligible list of Open High and Open Low</h2>
<table style="width:100%"> <tr> <th>SYMBOL</th> <th>OPEN</th> <th>HIGH</th> <th>LOW</th> <th>BUY/SELL</th> </tr>"""

noteligiblecound = 0
eligibletobuy =0
eligibletosell = 0

for value in nify50_json_obj:
    if value['open'] == value['high'] or value['open'] == value['low'] :

        mail_htmlcontent += f"""<tr>
        <td>{value['symbol']}</td>
        <td>{value['open']}</td>
        <td>{value['high']}</td>
        <td>{value['low']}</td>"""

        if value['open'] == value['high']:
            print(f"Need to sell {value['symbol']}")
            mail_htmlcontent += "<td>SELL</td>"
            eligibletosell += 1
        if value['open'] == value['low']:
            print(f"Need to buy {value['symbol']}")
            mail_htmlcontent += "<td>BUY</td>"
            eligibletobuy += 1

        mail_htmlcontent += "</tr>"

    else:
        noteligiblecound += 1

mail_htmlcontent += """</table><br>"""
mail_htmlcontent +=f"No of Stock Eligible for Buying : {eligibletobuy} <br> No of Stock Eligible for Selling : {eligibletosell} <br> No of Stock Not Eligible : {noteligiblecound} <br>"
mail_htmlcontent +="</body></html>"
# print(f"""\
# No of Stock Eligible for Buying : {eligibletobuy}
# No of Stock Eligible for Selling :{eligibletosell}
# No of Stock Not Eligible :{noteligiblecound}""")

sendmailTo = ['rubarajankcs@hotmail.com']
subject = "Equity Manager : Open High & Open Low Intraday Strategy"
sendmail.sendmailutility(sendmailTo,subject,mail_htmlcontent,argattachmentfiles=None,argMailType=None)


# getnsesite = Helper.NSEHelper()
#
# all_stock_name = getnsesite.getallNSEStockName()
# del all_stock_name['SYMBOL']



# for stock in all_stock_name:
#     print(f"------------------start stock : {stock}")
#     bselive = MoneyControlScrapper.get_stock_detail('nse',stock.upper())['data']
#     nselive = MoneyControlScrapper.get_stock_detail('nse',stock.upper())['data']
#
#     if bselive == None and nselive == None:
#         print(f"No data found for the stock {stock}")
#     else:
#         if bselive != None:
#             print(f"BSE Live for {stock} : {bselive['pricecurrent']}")
#         if nselive != None:
#             print(f"NSE Live for {stock}: {nselive['pricecurrent']}")
#     print(f"------------------end stock : {stock}")