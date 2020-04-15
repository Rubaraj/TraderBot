import os,json

import requests
from bs4 import BeautifulSoup

stock_symbol = "IOC"
res_nse1_url = f"https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying={stock_symbol}&instrument=FUTSTK&type=-&strike=-&expiry=30APR2020"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
source_code = requests.get(res_nse1_url,headers=headers).text

soup = BeautifulSoup(source_code,'lxml')

other_information = soup.find('div',id='responseDiv').text

other_information = os.linesep.join([s for s in other_information.splitlines() if s])

parsed_json = dict(json.loads(other_information))

print(parsed_json['data'])

########################################################

# payload = {'username':'test', 'password':'testing'}
# res = requests.get("https://httpbin.org/get",params=payload)
# res = requests.post("https://httpbin.org/post",data=payload)
# res = requests.get("https://httpbin.org/delay/1",timeout=3)
# print(res.text)
# print(res.url)
# print(res.json())
# res_dict = res.json()
# print(type(res_dict))
# print(res_dict['form'])

########################################################

# res_nse = requests.get("https://priceapi-aws.moneycontrol.com/pricefeed/nse/equitycash/TCS")
# res_bse = requests.get("https://priceapi-aws.moneycontrol.com/pricefeed/bse/equitycash/TCS")
#
# tcs_nse_lst = res_nse.json()
# tcs_bse_lst = res_bse.json()
#
# print(f"BSE: {tcs_bse_lst['data']['pricecurrent']}")
# print(f"NSE: {tcs_nse_lst['data']['pricecurrent']}")
#
# print(tcs_nse_lst['pricecurrent'])
# print(tcs_bse_lst['pricecurrent'])

########################################################

# payload = {'user_id':'XR4116','password':'bku09630henry'}
# headers = {
#     'Accept':'application/json, text/plain, */*',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language':'en-US,en;q=0.5',
#     'Connection':'keep-alive',
#     'Content-Length':'37',
#     'Content-Type':'application/x-www-form-urlencoded',
#     'Cookie':'__cfduid=d45045e5eac95d41c9fcca3dfc82e628b1586091946; _ga=GA1.2.1430761089.1584513651; csrftoken=uEJaHopPsKpHWwXvVXxQe7ps5vDvULmszKJttcYCNvDLYPTHkFEIOYp1tlAqy5H2; enctoken=2VP6BuS/Nu+gGvvf+rwKdvd6+wqKiAtP2e3EG243wAxCb7ncZOGq9JwZtQ4ULc6BTS7FFx1NbwzCeKkUyDoM+uywMdazaw==; kf_session=5kt2oZZzpQjlC4CgdDuOm47QHnxM7YZJ',
#     'Host':'kite.zerodha.com',
#     'Origin':'https://kite.zerodha.com',
#     'Referer':'https://kite.zerodha.com/',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
# }
# cookies = {'__cfduid':'d45045e5eac95d41c9fcca3dfc82e628b1586091946',
#            '_ga':'GA1.2.1430761089.1584513651',
#            'csrftoken':'uEJaHopPsKpHWwXvVXxQe7ps5vDvULmszKJttcYCNvDLYPTHkFEIOYp1tlAqy5H2',
#            'enctoken':'2VP6BuS/Nu+gGvvf+rwKdvd6+wqKiAtP2e3EG243wAxCb7ncZOGq9JwZtQ4ULc6BTS7FFx1NbwzCeKkUyDoM+uywMdazaw==',
#            'kf_session':'5kt2oZZzpQjlC4CgdDuOm47QHnxM7YZJ'}
# url ="https://kite.zerodha.com/api/twofa"
# res = requests.post(url,data=payload,headers=headers)
#
# print(res.status_code)

########################################################

# headers = {
# 'Host': 'kite.zerodha.com',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
# 'Accept-Language': 'en-US,en;q=0.5',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Content-Type': 'application/json',
# 'X-Kite-Version': '2.4.0',
# 'Authorization': 'enctoken ITUhuigMQvjNUdcKTY6nrC/mOOCnK0sezRTfXBcTq2033+J8Ts453kEnsXfcriAIv910OQy8NuJ7wxD3cUVO5IlNuWUULg==',
# 'Content-Length': '54',
# 'Origin': 'https://kite.zerodha.com',
# 'Connection': 'keep-alive',
# 'Referer': 'https://kite.zerodha.com/holdings',
# 'Cookie': '__cfduid=d45045e5eac95d41c9fcca3dfc82e628b1586091946; _ga=GA1.2.1430761089.1584513651; csrftoken=uEJaHopPsKpHWwXvVXxQe7ps5vDvULmszKJttcYCNvDLYPTHkFEIOYp1tlAqy5H2; enctoken=ITUhuigMQvjNUdcKTY6nrC/mOOCnK0sezRTfXBcTq2033+J8Ts453kEnsXfcriAIv910OQy8NuJ7wxD3cUVO5IlNuWUULg==; kf_session=7lyaIquyqWdJw6VtU7pgNHHrmejcUa4Q; public_token=0ZKjnTxFMBvs0p8aX6RElUsVrmvJUMmh; user_id=XR4116'
# }
# payload = {'instrument_token':261889,'transaction_type':'BUY'}
# url = "https://kite.zerodha.com/oms/nudge/orders"
# res = requests.post(url,params=payload,headers=headers)
#
# print(res.text)