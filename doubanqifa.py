import requests

if __name__ == "__main__":
    url='https://app.cnstock.com/api/waterfall?callback=jQuery19107681575689867295_1611665421911&colunm=qmt-sns_jg&page=3&num=10&showstock=0&_=1611665421913'
    # param={
    #     'callback':'jQuery191025339350284613116_1611332661002',
    #     'colunm':'qmt-sns_jg',
    #     'page':'100',
    #     'num':'10',
    #     'showstock':'0',
    #     '_': '1611332661100',
    # }
    headers={
        'Referer': 'https://news.cnstock.com/',

        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }
    response=requests.get(url=url,headers=headers)
    response.encoding='utf8'
    page_text=response.text

    print(page_text)