n=int(input())

for i in range(1,n+1):
    x,y=map(int,input().split(' '))

    if y !=0:
        result=x/y
        print(f'{result:.1f}')
    else:
        print('divisao impossivel')