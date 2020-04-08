import requests

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

res_nse = requests.get("https://priceapi-aws.moneycontrol.com/pricefeed/nse/equitycash/TCS")
res_bse = requests.get("https://priceapi-aws.moneycontrol.com/pricefeed/bse/equitycash/TCS")

tcs_nse_lst = res_nse.json()
tcs_bse_lst = res_bse.json()

print(f"BSE: {tcs_bse_lst['data']['pricecurrent']}")
print(f"NSE: {tcs_nse_lst['data']['pricecurrent']}")

# print(tcs_nse_lst['pricecurrent'])
# print(tcs_bse_lst['pricecurrent'])