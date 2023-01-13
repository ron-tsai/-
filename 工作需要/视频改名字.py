# -*- coding: utf-8 -*-



import os
'''
读取文件夹下所有文件的名字并把他们用列表存起来
'''
path = '/Users/ccmac/Downloads/C++黑马视频'
datanames = os.listdir(path)
list = []
for i in datanames:
    list.append(i)
print(list)

for name in list:
    name1=name.replace('|','')
    os.rename(os.path.join(path,name), os.path.join(path,name1))
    print(name)