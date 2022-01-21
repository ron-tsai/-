import requests


# API接口
api_url = "https://dev.kdlapi.com/api/getipwhitelist"

# 订单号跟API Key
orderid = 934258150103132
api_key = "sww98bl7nrhlqt3nt171mnkmswdaz054"

# 参数
params = {
        "orderid": orderid,
        "signature": api_key,
        }

res = requests.get(api_url, params=params)
print(res.content)

