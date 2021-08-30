import pandas as pd
import os
import requests
import re
import math


path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\社会责任\社会责任爬取'
# url = 'http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search&lastPage=index'
url='http://www.cninfo.com.cn/new/hisAnnouncement/query'
for beg in range(8,10):
    end=beg+2

    param={'pageNum': 1,'searchkey': '社会责任报告','pageSize': 30,'seDate': '200{}-01-01~20{}-12-31'.format(beg,end),'column': 'szse','tabName': 'fulltext','isHLtitle': 'true'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"

    }

    response = requests.post(url=url,params=param, headers=headers)

    page_data = response.json()
    print(page_data)
    total_num =math.ceil(page_data['totalRecordNum']/30)
    for page in range(1,total_num+1):
        print(total_num)
        param = {'pageNum': page, 'searchkey': '社会责任报告', 'pageSize': 30,
                 'seDate': '200{}-01-01~20{}-12-31'.format(beg, end), 'column': 'szse', 'tabName': 'fulltext',
                 'isHLtitle': 'true'}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"

        }

        response = requests.post(url=url, params=param, headers=headers)

        page_data = response.json()

        # print(len(page_data['announcements']))
        num=len(page_data['announcements'])
        code_list=[]
        report_list=[]
        date_list=[]
        for i in range(num):
            code_num=page_data['announcements'][i]['secCode']
            code_list.append(code_num)
            report=page_data['announcements'][i]['announcementTitle']
            report_list.append(report)
            date = re.findall(r'\d+[\年]',report)
            if date==[]:
                date_list=date_list+['NAN']
            else:
                print(date)
                date_list.append(date[0])
            # print(date)

        print(len(report_list),len(code_list),len(date_list))
        print(report_list)
        print(code_list)
        print(date_list)
        df=pd.DataFrame({'证券代码':code_list,'社会责任报告名称':report_list,'截止日期':date_list})

        df.to_excel(os.path.join(path,'{}-{}-{}.xlsx'.format(page,beg,end)))
