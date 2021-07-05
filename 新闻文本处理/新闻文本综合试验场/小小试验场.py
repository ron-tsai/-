list=[1, 1.5,'inverse',1.5,-1]
if list==[]:
    score=0
    print(score)
else:
    score=1
    if len(list)==3:
        if list==['inverse',1.5,-1] :
            score=0.75
            print(score)
        elif list==['inverse',1.2,-1]:
            score = 0.6
            print(score)
        else:
            for i,v in enumerate(list):
                if v == 'inverse':
                    v = -1
                    score=score*v
                else:
                    score=score*v
                    print(score)
    elif len(list)>3:


        for i in range(len(list) - 2):

            print(list[i:i+3])
            if list[i:i+3]==['inverse',1.5,-1]:
                score=0.75
                print(score)
            elif list[i:i+3]==['inverse',1.2,-1]:
                score = 0.6
                print(score)
        if score==1:
            for i, v in enumerate(list):
                if v == 'inverse':
                    v = -1
                    score = score * v
                else:
                    score = score * v
                    print(score)

    else:
        for i,v in enumerate(list):
            if v == 'inverse':
                v = -1
                score=score*v
            else:
                score=score*v
                print(score)