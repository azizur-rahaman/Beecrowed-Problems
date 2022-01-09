i=1
hn=0
p=0
while i<=100:
    n=int(input())
    
    if n>hn:
        hn=n
        p=i
    i+=1
print(hn)
print(p)
    