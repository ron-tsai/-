
import pandas as pd
import csv
import re


names = ['增长','提升','增加','下降','上涨','提高','加快','减少','涨幅','降低','突破','持有','盈利',
'亏损','收益','压力','有望','购买','持股','下滑','下跌','补贴','改善','增强','买入','减值',
'更好','助力','平稳','新高','下行','增幅','回落','损失','下调','扩张','跌幅','增速','减持',
'反弹','增持','冲击','助力','暴跌','带动','熔断','大跌','回落','恐慌','复苏','降幅','净流入',
'流出','涨停','利好','高位','大涨','牛市','增量','流入','收窄','恢复','卖出','回升','看好',
'上行','回暖','受益','跌停']

df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2017预处理数据.xlsx')
save_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\训练数据提取.txt'


score_list = []
for text in df['content']:
    results_list = []
    for name in names:
        text=str(text)
        results = re.findall(r'[^。]*?{}[^。]*?。'.format(name), text)
        results_list = results_list + results


    results_list = list(set(results_list))  ###去重
    for result in results_list:

        result_list=result.split('。')
        print(result_list)
        with open(save_path,'a+', newline='') as csvfile:
            csv_write = csv.writer(csvfile)
            csv_write.writerow(result_list)

    csvfile.close()


