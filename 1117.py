
sum=0
i=0
while True:

    n=float(input())

    if n>=0 and n<=10:
        sum=sum+n
        i=i+1
    else:
        print('nota invalida')
    if i==2:
        break
    
average=sum/2
print(f'media = {average:.2f}')