import pandas as pd
# df=pd.DataFrame(columns=['姓名','年龄','成绩','性别'])
# score=pd.Series(name='成绩')
# score.append(1,name='成绩')
# print(score)
# for i in range(10):
#     df.loc[:,'成绩']=score.append(i)
#     print(df)

# a=[]
# a.append(1)
# print(a)

a=[1,2,3,4,5]
b=pd.DataFrame(a,columns=['分数'])
print(b)