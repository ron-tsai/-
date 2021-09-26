import jqdatasdk as jd
jd.auth('18359196774','acginor1992CR')
date_init='2013-01-01'
stocks=jd.get_index_stocks('000300.XSHG',date=date_init)
print(len(stocks))