
n=int(input())

for i in range(1,n+1):
    x,y=map(int,input().split(' '))
    
    h=l=0
    if x>y:
        h=x
        l=y
    else:
        h=y
        l=x
    sum=0
    for j in range(l+1,h):

        if j%2!=0:
            sum+=j
    print(sum)
    