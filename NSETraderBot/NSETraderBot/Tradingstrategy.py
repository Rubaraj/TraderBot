#Class name will be the type of stratergy
from NSETraderBot import NSEScrapper,Utility
from datetime import date
import csv

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
            stocksymbollist = []
            noteligiblecound = 0
            eligibletobuy = 0
            eligibletosell = 0

            for value in nify50_json_obj:
                if value['open'] == value['high'] or value['open'] == value['low']:
                    stockderivativedetail = nseData.getOtherInformationNSEDerivative(value['symbol'])[0];
                    stock_open = value['open'].replace(',','')
                    volatilitycal = 0.00
                    if stockderivativedetail != None:
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
                        stocksymbollist.append(value['symbol'])
                    if value['open'] == value['low']:
                        eligibleup = float(stock_open) + round(volatilitycal,2)
                        print(f"Need to buy {value['symbol']}")
                        mail_htmlcontent += f"<td>{round(eligibleup,2)}</td>"
                        mail_htmlcontent += "<td>BUY</td>"
                        eligibletobuy += 1
                        stocksymbollist.append(value['symbol'])
                    mail_htmlcontent += "</tr>"

                else:
                    noteligiblecound += 1

            mail_htmlcontent += """</table><br>"""
            mail_htmlcontent += f"No of Stock Eligible for Buying : {eligibletobuy} <br> No of Stock Eligible for Selling : {eligibletosell} <br> No of Stock Not Eligible : {noteligiblecound} <br>"
            mail_htmlcontent += "</body></html>"
            sendmailTo = ['rubarajankcs@hotmail.com']
            subject = "Equity Manager : Open High & Open Low Intraday Strategy"
            sendmail.sendmailutility(sendmailTo, subject, mail_htmlcontent, argattachmentfiles=None, argMailType=None)
            self.createzerodhapiworkbench(stocksymbollist)
        except Exception as ex:
            print(f"Something wrong in sendgetopenhighopenlowmaail Exception: {ex}" )


    def createzerodhapiworkbench(self,argstocklist):
        try:
            filename_date = date.today().isoformat()
            with open('instruments.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                tokenlist = []
                for line in csv_reader:
                    if line['instrument_type'] == "EQ" and line['segment'] =="NSE" and argstocklist.__contains__(line['tradingsymbol']):
                        tokenlist.append(line['instrument_token'])

                workspacefile = open("C:\Zerodha\Pi\Workspace"+"\OHOL_"+filename_date+".workspace","w")
                workspace_data = "Symbols\n"
                for token in tokenlist:
                    workspace_data += token + "\n"
                workspace_data += "ColumnList\n1,0,197;1,3,69;1,4,64;1,5,58;1,6,64;1,7,63;0,8,100;1,9,64;1,10,61;1,11,64;1,12,65;1,1,67;1,13,63;1,14,68;0,15,100;0,16,100;0,17,100;0,18,100;1,19,67;1,20,67;0,21,100;0,22,100;0,23,100;0,24,100;0,25,100;0,26,100;0,27,100;0,28,100;1,29,100;1,30,83;1,2,100;\nCharts"

                workspacefile.write(workspace_data)
                workspacefile.close()
        except Exception as Ex:
            print("Something Went wrong in createzerodhapiworkbench "+ Ex)