n=int(input())
count=1
check=1
for i in range(n*2):

    if check == 1:
        n2=count*count
        n3=n2*count
        print(f'{count} {n2} {n3}')
        check+=1

    elif check==2:
        n2=count*count
        n3=n2*count
        print(f'{count} {n2+1} {n3+1}')
        check=1
        count+=1

    
