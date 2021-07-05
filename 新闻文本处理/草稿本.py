myList = [-1,2,-3,4,-5,6]
absList = list(map(abs, myList)) #对于Python3.x需要用list函数对map的返回值转换为列表
print(absList)