# -*- coding: utf-8 -*-

import requests
import traceback

url = "https://api.haohanfuwu.com/api/v1/ip"

body = {
    "login_name": "2641142611",
    "login_pwd": "PXKXaxxxFSFSAYCa"
}

try:
    res = requests.post(url, data=body, verify=False, timeout=3)
    print(res.json())
    result = res.json()
    code = result['code']
    if code == -1:
        raise Exception("授权失败，请检查账号密码是否正确")
    elif code == -2:
        raise Exception("账号异常")
    elif code == -3:
        raise Exception("请求频率过快")
    elif code == -4:
        raise Exception("服务器错误")

    proxy = result['data']

except:
    print(traceback.format_exc())