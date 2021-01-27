import requests

# url='https://app.cnstock.com/api/waterfall?callback=jQuery19103301053531158453_1611455329895&colunm=qmt-sns_jg&page=2&num=10&showstock=0&_=1611455329896'
url='https://app.cnstock.com/api/waterfall?callback=jQuery19103301053531158453_1611455329895&colunm=qmt-sns_jg&page=3&num=10&showstock=0&_=1611455329898'

param={
    'colunm': 'qmt-sns_jg',
    'page':'3',
    'num':'10',
    'showstock':'0',}

headers={
    'Referer': 'https://news.cnstock.com/',
    'Cookie': 'temp_uid=tp_16110674451597; Hm_lvt_5f1ddd842219521824ad49f82d8a712c=1611320083,1611326397,1611361229,1611455221; Hm_lpvt_5f1ddd842219521824ad49f82d8a712c=1611455330',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}
response=requests.get(url,headers=headers,params=param)
response.encoding='utf8'

print(response.text)
