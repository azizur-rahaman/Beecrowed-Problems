x,y=map(int,input().split(' '))

count=1
tempData=[]
for i in range(1,y+1):
    tempData.append(i)

    if count==x:
        data=' '.join([str(elem) for elem in tempData])
        print(data)
        tempData.clear()
        count=1
    else:
        count+=1
    

