import requests


payload = {'username':'test', 'password':'testing'}

# res = requests.get("https://httpbin.org/get",params=payload)

# res = requests.post("https://httpbin.org/post",data=payload)

res = requests.get("https://httpbin.org/delay/1",timeout=3)

print(res.text)

# print(res.url)

# print(res.json())

# res_dict = res.json()

# print(type(res_dict))

# print(res_dict['form'])