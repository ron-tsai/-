import re
name = '乔峰' # 选择乔峰 这个词 作为 特定词
text = '''段誉的六卖神贱，虚竹的酒色为善佛祖皆空。乔峰的谁知心爱
... 朱颜消逝烟雨中。降龙无敌手，丐帮帮主乔峰。''' # 文本是这样的
results = re.findall(r'[^。]*?{}[^。]*?。'.format(name), text)
for i, r in enumerate(results, 1):
    print(i,r)#一定要缩进，按一个空格键

