# Predefined Libraries
from urllib.request import Request
import re

# Created Libraries
from NSETraderBot import ConstURLList, Utility

# Class Initialization
nse_URLs = ConstURLList.NSEURLList()
nse_Utility = Utility.TraderUtility()

# Predefined Methods
headers = nse_Utility.nse_headers()
opener = nse_Utility.nse_opener()


class NSEHelper:


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