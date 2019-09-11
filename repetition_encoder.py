def repetitionEncoder(m,n):
    new_list=[]
    for i in range (0,n):
        new_list.extend(m)
    return new_list

m=[0]
n=4
c=repetitionEncoder(m,n)
print(c)


