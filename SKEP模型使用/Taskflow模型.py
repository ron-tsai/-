


from paddlenlp import Taskflow

senta = Taskflow("sentiment_analysis",model="skep_ernie_1.0_large_ch")
data=senta("股灾了又，呵呵，")
print(data)
data2=senta('全往跌停板砸！')
print(data2)