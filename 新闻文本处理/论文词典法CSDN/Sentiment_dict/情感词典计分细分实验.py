count_list1=[1,2,'inverse',1,2,1.5]
count_list2=[1,'inverse',2]
count_list3=[-1,'inverse',2]

def find_sent_value(list):
    return [v for i, v in enumerate(list) if (v == 1) | (v == -1)]

def find_all_index(arr):
    return [i for i,v in enumerate(arr) if (v==1)|(v==-1)]
def mutiplication_list(list):
    score=1
    for i,v in enumerate(list):
        if v == 'inverse':
            v = -1
            score=score*v
        else:
            score=score*v
    return score
# 3.情感列表计算情感得分。
def find_degree_words(count_list):
    locate_list=find_all_index(count_list)
    sent_list=find_sent_value(count_list)
    sent_score=mutiplication_list(sent_list)
    if (count_list[-1]==1)|(count_list[-1]==-1):#如果只有一个情绪词
        for i in range(len(locate_list)-1):
            begin=locate_list[i]+1
            end=locate_list[i+1]
            part_degree_list =count_list[begin:end]
            part_degree_score = mutiplication_list(part_degree_list)

    elif len(locate_list)>1:#如果不止一个情绪词
        if (count_list[-1]!=1)&(count_list[-1]!=-1):#如果情绪词不在结尾（不止一个情绪词）
            for i in range(len(locate_list)):
                if i<len(locate_list)-1:#除最后一个情绪词以外的情绪词找程度副词（多个不在结尾的情绪词）
                    begin=locate_list[i]+1
                    end=locate_list[i+1]
                    part_degree_list =count_list[begin:end]
                    part_degree_score = mutiplication_list(part_degree_list)

                else:#最后一个情绪词处理（多个不在结尾的情绪词）
                    begin = locate_list[i] + 1
                    part_degree_list =count_list[begin:]
                    part_degree_score = mutiplication_list(part_degree_list)

        else:#如果情绪词在结尾（不止一个情绪词）
            part_degree_list=count_list[1:]
            part_degree_score=mutiplication_list(part_degree_list)
    return part_degree_score

def degree_calculate(total_list):
    if total_list.count(1)+total_list.count(-1)==1: #如果只有一个情绪词
        degree_list = [i for i, v in enumerate(total_list) if (v != 1) & (v != -1)]
        if 'inverse' in total_list: #如果存在否定词（只有一个情绪词）
            inverse_count = total_list.count('inverse')

            if (total_list.index('inverse') != len(degree_list)-1)&(inverse_count<len(degree_list)): #如果否定词不在结尾且存在程度词（只有一个情绪词&存在否定词）

                score=mutiplication_list(total_list)
                score=0.5*score*(-1)**inverse_count
                return score
            else: #如果否定词在结尾（只有一个情绪词&存在否定词）
                score = mutiplication_list(total_list)
                score = 1.5*score*(-1)**inverse_count
                return score
        else:#如果不存在否定词（只有一个情绪词）
            score = mutiplication_list(total_list)
            return score




    elif total_list.count(1)+total_list.count(-1)>=1:#情感词大于1
        sent_list=[i for i, v in enumerate(total_list) if (v == 1)|(v==-1)]
        for i in sent_list:

print(find_degree_words(count_list1))