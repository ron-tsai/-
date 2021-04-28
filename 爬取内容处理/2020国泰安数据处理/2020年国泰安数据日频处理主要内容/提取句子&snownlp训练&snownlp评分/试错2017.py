
import pandas as pd
import csv
import re


names = ['上涨','涨幅','盈利','亏损','有望','下滑','下跌','改善','增强','买入','减值','助力','平稳','新高','下行','增幅','回落','损失','下调','扩张','跌幅','增速','减持','反弹','增持','冲击','暴跌','熔断','大跌','回落','恐慌','复苏','降幅','净流入','流出','涨停','利好','高位','大涨','牛市','流入','收窄','回升','上行','回暖','跌停','熊市']

df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2017国泰安报纸筛选.xlsx')
save_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\试错训练数据提取.txt'


with open(save_path,'a+', newline='',encoding='utf-8') as csvfile:
    for text in df['content']:
        results_list = []
        for name in names:
            text=str(text)
            results = re.findall(r'[^。]*?{}[^。]*?。'.format(name), text)
            if len(results)<50:
                results_list = results_list + results




        results_list = list(set(results_list))  ###去重
        for result in results_list:

            result_list=result.split('。')
            print(result_list)

            csv_write = csv.writer(csvfile)
            csv_write.writerow(result_list)



