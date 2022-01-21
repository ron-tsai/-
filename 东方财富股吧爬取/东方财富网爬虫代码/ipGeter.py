import requests

from time import sleep



def ipGet():
    while True:
        try:
            api_url = 'https://tps.kdlapi.com/api/gettps/?orderid=934258150103132&num=1&pt=1&format=json&sep=1'
            tunnel = "tpsXXX.kdlapi.com:15818"

            # 用户名密码方式
            username = "t14258150103392"
            password = "gc2h5zhq"
            proxies = {
                "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
                "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
            }
            res=requests.get(url=api_url,proxies=proxies).json()
            print(res)
            ip=res["data"]["proxy_list"][0]
            proxies={
                'http':'http://'+ip,
                'https':'http://'+ip
            }
            page=requests.get("https://www.baidu.com",proxies=proxies,timeout=(3,3))
            if page.status_code==200:
                print(ip)
                return proxies
            else:
                print('无效IP')
        except Exception as e:
            print(str(e))
        finally:
            sleep(0.2)


# if __name__ =='__main__':
#     ipGet()
