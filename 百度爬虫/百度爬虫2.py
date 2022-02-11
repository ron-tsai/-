import datetime

s_startDate='2020-01-01'
s_endDate='2020-12-31'
date_Start=datetime.datetime.strptime(s_startDate,'%Y-%m-%d')
date_End=datetime.datetime.strptime(s_endDate,'%Y-%m-%d')

with open('final.csv','wt') as f_final:
    while date_Start<=date_End:
        s_day=date_Start.strptime('%Y-%m-%d')
        f_final.write(s_day+',')
        date_Start+=datetime.timedelta(days=1)
    f_final.write("\n")
    with open("tb.csv","rt") as f_tb:
        s_tb=f_tb.read()
        f_final.write(s_tb)
    f_final.write("\n")