# import pandas as pd
# from pandas.core.frame import DataFrame
#
# a=[1,2,3,4]#列表a
# b=[5,6,7,8]#列表b
# c=[4,1,4,5]
# d={"a" : a,   "b" : b}#将列表a，b转换成字典
# e={"a" : a,   "b" : c}#将列表a，b转换成字典
#
# data1=DataFrame(d)#将字典转换成为数据框
# data2=DataFrame(e)
#
# print('----',data2)
# print('----',data1)
# df=pd.concat([data1,data2])
# print('----',df)

import pydot
pydot.Dot.create(pydot.Dot())