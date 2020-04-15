#Class name will be the type of stratergy
from NSETraderBot import NSEScrapper,Utility

nseData = NSEScrapper.NSEStockSite()
sendmail = Utility.GeneralUtility()

class OpenHighOpenLow:

    def getopenhighopenlow(self):
        nifty50_json_obj = nseData.getnify50Stock()['data']
        return nifty50_json_obj


    def sendgetopenhighopenlowmaail(self):
        try:
            nify50_json_obj = self.getopenhighopenlow()
            nify50_json_obj = sorted(nify50_json_obj, key=lambda x: x['symbol'], reverse=False)
            mail_htmlcontent = """
            <!DOCTYPE html> <html> <head> 
            <style> table, th, td {   border: 1px solid black; border-collapse: collapse; } th, td {   padding: 5px;   text-align: left; } th {background-color: #4CAF50;color: white;}</style>
            </head> <body> <h2>Eligible list of Open High and Open Low</h2>
            <table style="width:100%"> <tr> <th>SYMBOL</th> <th> LAST TRADED PRICE </th> <th>OPEN</th> <th>HIGH</th> <th>LOW</th> <th> VOLATILITY VALUE (Rs) </th> <th> MAX REACH </th> <th>BUY/SELL</th>"""

            noteligiblecound = 0
            eligibletobuy = 0
            eligibletosell = 0

            for value in nify50_json_obj:
                if value['open'] == value['high'] or value['open'] == value['low']:
                    stockderivativedetail = nseData.getOtherInformationNSEDerivative(value['symbol'])[0];
                    stock_open = value['open'].replace(',','')
                    volatilitycal = (float(stockderivativedetail['dailyVolatility']) / 100) * float(stock_open)
                    mail_htmlcontent += f"""<tr>
                    <td>{value['symbol']}</td>
                    <td>{value['ltP']}</td>
                    <td>{value['open']}</td>
                    <td>{value['high']}</td>
                    <td>{value['low']}</td>
                    <td>{round(volatilitycal,2)}</td>"""

                    if value['open'] == value['high']:
                        eligibledown = float(stock_open) - round(volatilitycal,2)
                        print(f"Need to sell {value['symbol']}")
                        mail_htmlcontent += f"<td>{round(eligibledown,2)}</td>"
                        mail_htmlcontent += "<td>SELL</td>"
                        eligibletosell += 1
                    if value['open'] == value['low']:
                        eligibleup = float(stock_open) + round(volatilitycal,2)
                        print(f"Need to buy {value['symbol']}")
                        mail_htmlcontent += f"<td>{round(eligibleup,2)}</td>"
                        mail_htmlcontent += "<td>BUY</td>"
                        eligibletobuy += 1

                    mail_htmlcontent += "</tr>"

                else:
                    noteligiblecound += 1

            mail_htmlcontent += """</table><br>"""
            mail_htmlcontent += f"No of Stock Eligible for Buying : {eligibletobuy} <br> No of Stock Eligible for Selling : {eligibletosell} <br> No of Stock Not Eligible : {noteligiblecound} <br>"
            mail_htmlcontent += "</body></html>"
            sendmailTo = ['rubarajankcs@hotmail.com']
            subject = "Equity Manager : Open High & Open Low Intraday Strategy"
            sendmail.sendmailutility(sendmailTo, subject, mail_htmlcontent, argattachmentfiles=None, argMailType=None)
        except Exception as ex:
            print(f"Something wrong in sendgetopenhighopenlowmaail Exception: {ex}" )