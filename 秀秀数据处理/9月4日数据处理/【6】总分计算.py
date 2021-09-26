import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.4'
df=pd.read_excel(os.path.join(path,'【6】9月4日数据pandas无量纲化处理.xlsx'),dtype=object,index=False)
list_1=[]
print(df.max())
print(df.min())
for name in df.columns[3:]:
    d_v=df[name].max() - df[name].min()
    print(name)
    print(df[name].max())
    print(df[name].min())
    print(d_v)
    list_1.append(d_v)
print(list_1)
sum=sum(list_1)
print(sum)
w_list=[]
for i in list_1:
    w=i/sum
    w_list.append(w)
print(w_list)

for i,v in enumerate(df.columns[3:]):
    print(i,v)
    df.loc[:,v]=w_list[i]*df[v]
df.loc[:,"score"]=df[df.columns[3]]+df[df.columns[4]]+df[df.columns[5]]+df[df.columns[6]]+df[df.columns[7]]+df[df.columns[8]]+df[df.columns[9]]+df[df.columns[10]]+df[df.columns[11]]+df[df.columns[12]]+df[df.columns[13]]+df[df.columns[14]]+df[df.columns[15]]+df[df.columns[16]]+df[df.columns[17]]+df[df.columns[18]]+df[df.columns[19]]+df[df.columns[20]]+df[df.columns[21]]

df.to_excel(os.path.join(path, '【7】9月4日数据pandas分值计算.xlsx'), index=False)


