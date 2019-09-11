def repetitionDecoder(v):
    count1=0
    count0=0
    L=[]
    for i in v:
        if i ==1:
            count1+=1
        else:
            count0+=1
    if count0>count1:
        L.append(0)        
    elif count1>count0:
        L.append(1)
    return L

v=[1, 1, 1, 1,1,1,0,1,1,1]
m=repetitionDecoder(v)
print(m)
