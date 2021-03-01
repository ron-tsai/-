
import jieba
jieba.setLogLevel(20)
with open("C:\\Users\Administrator\Desktop\爬取内容\聚合.txt",'r',encoding='utf-8') as f:
    text=f.read()


words=jieba.lcut(text)

for ch in ',。?！“”：；、\\n':
    if ch in words:
        for i in range(words.count(ch)):
            words.remove(ch)

counts={}
for word in words:
    if len(word)>=2:
        counts[word]=counts.get(word,0)+1


items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(100):
    word,count=items[i]
    print('{0:<{width}}{1}'.format(word,count,width=10-(len(word.encode('GBK'))-len(word))))


