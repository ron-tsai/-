# -*- coding:utf-8 -*-
# @time: 2022/1/4 8:35
# @Author: 韩国麦当劳
# @Environment: Python 3.7
import datetime
import requests
import sys
import time
import json

word_url = 'http://index.baidu.com/api/SearchApi/thumbnail?area=0&word={}'

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Host": "index.baidu.com",
        "Referer": "http://index.baidu.com/v2/main/index.html",
    }
    cookies = {
        'Cookie': 'PSTM=1635234875; BAIDUID=0DDD3DC6A59DC198151475F3778B7CD0:FG=1; BAIDUID_BFESS=0DDD3DC6A59DC198151475F3778B7CD0:FG=1; BIDUPSID=8DF4CBEB5D26FCC8E43471D020EE2028; H_PS_PSSID=35106_35773_34584_35490_35801_35796_35315_26350_35765_35746; delPer=0; PSINO=7; BA_HECTOR=808h8kah25a4ah854r1h054610r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=11200015858971444872; BDSFRCVID=wfAOJexroG04GZQD07wKhJAlkcpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKK3mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR30WJbHMTrDHJTg5DTjhPrM5UjCWMT-MTryKKt23McGsKt65URsyx_jMUbjLbvkJGnRh4oNBUJtjJjYhfO45DuZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDUc9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DD6jjDM3e; BCLID_BFESS=11200015858971444872; BDSFRCVID_BFESS=wfAOJexroG04GZQD07wKhJAlkcpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKK3mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR30WJbHMTrDHJTg5DTjhPrM5UjCWMT-MTryKKt23McGsKt65URsyx_jMUbjLbvkJGnRh4oNBUJtjJjYhfO45DuZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDUc9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DD6jjDM3e; __yjs_duid=1_be59b0f9ebdcc024590bceb87cd92a2e1644335300949; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1644335302; BDUSS=BPYVF-UjhZdVFJRnRqeXVNZGNDZGJWb0I0MkpuNktDejAycG96WllGWUNIaXBpSVFBQUFBJCQAAAAAAAAAAAEAAAAqkSAoz-Oy3czsv9VjcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKRAmICkQJieX; BDUSS_BFESS=BPYVF-UjhZdVFJRnRqeXVNZGNDZGJWb0I0MkpuNktDejAycG96WllGWUNIaXBpSVFBQUFBJCQAAAAAAAAAAAEAAAAqkSAoz-Oy3czsv9VjcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKRAmICkQJieX; CHKFORREG=802767c650864bc7ac060ab3e0ad3f3a; bdindexid=kmk6gf97tp9r3um79vn0qvkkk4; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1644335424; __yjs_st=2_MzMyODgwNWQyYjM1NzY4YzE0ODI3YWI4N2QzNDNjYTUwZjFhZDAyZjJiNWFjZWU2NWZhMTA5MGNkYzY5MWU1ZDBlZDIxZDg1MzIyYzNjMjE4NDQwNDI3MGUwNTE4ZDQ3NjAzZmFiMGE2OGViM2EyOTk4YWJkYmVjMGNhYjk0YjUxMDllZWY2MmM4MmEyMjJjY2RkNGZiZTg4YjdkZGIyMTVhNzcxMDFkNzdhNzMyMjI2ZmE3NzhlNmVjNDFjOTM2XzdfZWExYjAyNDg=; ab_sr=1.0.1_NzEzMGQ3YTQyOTU1OGNhMDRlOTlkYzdiYjY3ZDQ3YjA0NDA5OTdhNjg5ZGY2MjQ0ZjJjZTFiNjcxMjU0NzZiM2ZmZjQwYzhhMTg1YTRhMjRiZjc5NmJmYjAyMjZhZWE1ZjA5Nzk3ZGIxNDcxNjlhNGY2ZmY1MDhlNzBjNDk2Y2Y2YjA1YjdhNGRiOTlmNDFjOGM1YjQ2MDVmZWFjOWFjZQ==; RT="z=1&dm=baidu.com&si=qnrxrxzww1r&ss=kzeas5to&sl=g&tt=h77&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=4dy0"'
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.text


def decrypt(t, e):
    n = list(t)
    i = list(e)
    a = {}
    result = []
    ln = int(len(n) / 2)
    start = n[ln:]
    end = n[:ln]
    for j, k in zip(start, end):
        a.update({k: j})
    for j in e:
        result.append(a.get(j))
    return ''.join(result)


def get_ptbk(uniqid):
    url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'
    resp = get_html(url.format(uniqid))
    return json.loads(resp)['data']


def get_data(keyword, start='2011-01-02', end='2022-01-02'):
    url = "https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}&endDate={}".format(keyword, start, end)
    data = get_html(url)
    data = json.loads(data)
    uniqid = data['data']['uniqid']
    data = data['data']['userIndexes'][0]['all']['data']
    ptbk = get_ptbk(uniqid)
    result = decrypt(ptbk, data)
    result = result.split(',')
    start = start_date.split("-")
    end = end_date.split("-")
    a = datetime.date(int(start[0]), int(start[1]), int(start[2]))
    b = datetime.date(int(end[0]), int(end[1]), int(end[2]))
    node = 0
    for i in range(a.toordinal(), b.toordinal()):
        date = datetime.date.fromordinal(i)
        print(date, result[node])
        node += 1


if __name__ == '__main__':
    keyword = "沪深300指数"
    start_date = "2011-01-02"
    end_date = "2022-01-02"
    get_data(keyword, start_date, end_date)

