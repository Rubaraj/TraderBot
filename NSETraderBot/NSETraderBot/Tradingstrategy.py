#Class name will be the type of stratergy
from NSETraderBot import NSEScrapper,Utility

nseData = NSEScrapper.NSEStockSite()
sendmail = Utility.GeneralUtility()

class OpenHighOpenLow:

    def getopenhighopenlow(self):
        nifty50_json_obj = nseData.getnify50Stock()['data']
        return nifty50_json_obj


    def sendgetopenhighopenlowmaail(self):

        nify50_json_obj = self.getopenhighopenlow()
        mail_htmlcontent = """
        <!DOCTYPE html> <html> <head> 
        <style> table, th, td {   border: 1px solid black; border-collapse: collapse; } th, td {   padding: 5px;   text-align: left; } th {background-color: #4CAF50;color: white;}</style>
        </head> <body> <h2>Eligible list of Open High and Open Low</h2>
        <table style="width:100%"> <tr> <th>SYMBOL</th> <th> LAST TRADED PRICE </tr> <th>OPEN</th> <th>HIGH</th> <th>LOW</th> <th>BUY/SELL</th>"""

        noteligiblecound = 0
        eligibletobuy = 0
        eligibletosell = 0

        for value in nify50_json_obj:
            if value['open'] == value['high'] or value['open'] == value['low']:

                mail_htmlcontent += f"""<tr>
                <td>{value['symbol']}</td>
                <td>{value['ltP']}</td>
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
        mail_htmlcontent += f"No of Stock Eligible for Buying : {eligibletobuy} <br> No of Stock Eligible for Selling : {eligibletosell} <br> No of Stock Not Eligible : {noteligiblecound} <br>"
        mail_htmlcontent += "</body></html>"

        sendmailTo = ['rubarajankcs@hotmail.com']
        subject = "Equity Manager : Open High & Open Low Intraday Strategy"
        sendmail.sendmailutility(sendmailTo, subject, mail_htmlcontent, argattachmentfiles=None, argMailType=None)