
n=int(input())
c=r=s=0
i=1


while i<=n:
    a,b=map(str,input().split(' '))

    if b == 'C':
        c = c + int(a)
    elif b == 'R':
        r=r + int(a)
    else:
        s= s + int(a)
    i+=1

total = c+r+s
pc= float((c*100)/total)
pr= float((r*100)/total)
ps= float((s*100)/total)

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')

print(f"Percentual de coelhos: {pc:.2f} %")
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')

