#Class name will be the type of stratergy
from NSETraderBot import NSEScrapper
import json

nseData = NSEScrapper.NSEStockSite()

class OpenHighOpenLow:

    def getopenhighopenlow(self):
        nifty50_json_obj = nseData.getnify50Stock()['data']
        return nifty50_json_obj