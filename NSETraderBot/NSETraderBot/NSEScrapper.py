# all_nse_stocks = nseHelper.getallNSEStockName()

from NSETraderBot import Helper, Utility, ConstURLList
from urllib.request import Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import _thread,re,json, requests, os

nse_URLs = ConstURLList.NSEURLList()
nse_Utility = Utility.TraderUtility()
nseHelper = Helper.NSEHelper()
headers = nse_Utility.nse_headers()
opener = nse_Utility.nse_opener()


class NSEStockSite:

    def getstockdetails(self, argthreadstocklist, argstrThrdname):
        for stock_symbol in argthreadstocklist:
            print(f"Log: Thread Name: {argstrThrdname} the stock symbol is {stock_symbol[0]} and the company is {stock_symbol[1]}")
            print(stock_symbol[0])
            print(self.get_stock_detail(stock_symbol[0].upper()))


    def createandsendthreaddata(self, arg_all_nse_stocks):
        start_count = 0
        per_thrd_count = int(len(arg_all_nse_stocks) / 5)
        end_count = per_thrd_count
        first_thrd = list(arg_all_nse_stocks.items())[start_count:end_count]
        first_thrd.pop(0)
        start_count = end_count
        end_count += per_thrd_count
        second_thrd = list(arg_all_nse_stocks.items())[start_count:end_count]
        start_count = end_count
        end_count += per_thrd_count
        third_thrd = list(arg_all_nse_stocks.items())[start_count:end_count]
        start_count = end_count
        end_count += per_thrd_count
        fourth_thrd = list(arg_all_nse_stocks.items())[start_count:end_count]
        start_count = end_count
        fifth_thrd = list(arg_all_nse_stocks.items())[start_count:]
        _thread.start_new_thread(self.getstockdetails, (first_thrd, "First Thread"))
        _thread.start_new_thread(self.getstockdetails, (second_thrd, "second Thread"))
        _thread.start_new_thread(self.getstockdetails, (third_thrd, "Third Thread"))
        _thread.start_new_thread(self.getstockdetails, (fourth_thrd, "Fourth Thread"))
        _thread.start_new_thread(self.getstockdetails, (fifth_thrd, "Fifth Thread"))

        while 1:
            pass


    def build_url_for_quote(self, argstocksymbol):
        if argstocksymbol is not None and type(argstocksymbol) is str:
            encoded_args = urlencode([('symbol', argstocksymbol), ('illiquid', '0'), ('smeFlag', '0'), ('itpFlag', '0')])
            return nse_URLs.getparticularstockdetails + encoded_args
        else:
            raise Exception('code must be string')


    def get_stock_detail(self, argstocksymbol):
        try:
            url = self.build_url_for_quote(argstocksymbol)
            req = Request(url, None, headers)
            res = opener.open(req)
            res = nse_Utility.byte_adaptor(res)
            res = res.read()
            match = re.search( \
                r'<div\s+id="responseDiv"\s+style="display:none">(.*?)</div>',
                res, re.S
            )
            buffer = match.group(1).strip()
            response = nse_Utility.clean_server_response(json.loads(buffer)['data'][0])
            return nse_Utility.render_response(response, as_json=False)
        except IndexError:
            print("Data Not Found Index Error")
        except:
            print("Un Known Exception")


    def getnify50Stock(self):
        try:
            url = nse_URLs.getnsenifty50stock
            headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
            res = requests.get(url,headers=headers,timeout=5)
        except Exception as ex:
            print(f"UnKnown Exception in getnify50stock Exception ( {ex} )")
            return None
        return res.json()


    def getOtherInformationNSEDerivative(self,argstocksymbol):
        if str(argstocksymbol).__contains__("&"):
            argstocksymbol = str(argstocksymbol).replace('&','%26')
        payload = f"?underlying={argstocksymbol}&instrument=FUTSTK&type=-&strike=-&expiry=30APR2020"
        url = nse_URLs.getnsederivativedetail + payload
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
        source_code = requests.get(url, headers=headers).text
        soup = BeautifulSoup(source_code, 'lxml')
        other_information_div = soup.find('div', id='responseDiv').text
        other_information = os.linesep.join([s for s in other_information_div.splitlines() if s])
        rtninfo = json.loads(other_information)
        return rtninfo['data']
