# Predefined Libraries
from urllib.request import Request
import json, re, six
from urllib.parse import urlencode

# Created Libraries
from NSETraderBot import ConstURLList, Utility

# Class Initialization
nse_URLs = ConstURLList.NSEURLList()
nse_Utility = Utility.TraderUtility()

# Predefined Methods
headers = nse_Utility.nse_headers()
opener = nse_Utility.nse_opener()


class NSEHelper:

    # Reading CSV MOstly
    def getallNSEStockName(self):
        res_dict = {}
        url = nse_URLs.allNSEstockNameList;
        req = Request(url, None, headers)
        res = opener.open(req)
        if res is not None:
            res = nse_Utility.byte_adaptor(res)
            for line in res.read().split('\n'):
                if line != '' and re.search(',', line):
                    [code, name] = line.split(',')[0:2]
                    res_dict[code] = name
        else:
            raise Exception('no response received')
        return nse_Utility.render_response(res_dict, as_json=False)

    def build_url_for_quote(self, symbol):
        if symbol is not None and type(symbol) is str:
            encoded_args = urlencode([('symbol', symbol), ('illiquid', '0'), ('smeFlag', '0'), ('itpFlag', '0')])
            return nse_URLs.getparticularstockdetails + encoded_args
        else:
            raise Exception('code must be string')


    def clean_server_response(self, resp_dict):
        d = {}
        for key, value in resp_dict.items():
            d[str(key)] = value
        resp_dict = d
        for key, value in resp_dict.items():
            if type(value) is str or isinstance(value, six.string_types):
                if re.match('-', value):
                    try:
                        if float(value) or int(value):
                            dataType = True
                    except ValueError:
                        resp_dict[key] = None
                elif re.search(r'^[0-9,.]+$', value):
                    resp_dict[key] = float(re.sub(',', '', value))
                else:
                    resp_dict[key] = str(value)
        return resp_dict



    def get_stock_detail(self, symbol):
        try:
            url = self.build_url_for_quote(symbol)
            req = Request(url, None, headers)
            res = opener.open(req)
            res = nse_Utility.byte_adaptor(res)
            res = res.read()
            match = re.search( \
                r'<div\s+id="responseDiv"\s+style="display:none">(.*?)</div>',
                res, re.S
            )
            buffer = match.group(1).strip()
            response = self.clean_server_response(json.loads(buffer)['data'][0])
            return nse_Utility.render_response(response, as_json=False)
        except IndexError:
            print("Data Not Found Index Error")
        except:
            print("Un Known Exception")