from types import SimpleNamespace


n = int(input())
i = 1
for i in range(i,n+1):
    a=b=c=total=0

    a,b,c=map(float,input().split(' '))

    total = ((a*2.0)+(b*3.0)+(c*5))/10.0
    print('%.1f'%total)