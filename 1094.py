
n=int(input())
c=r=s=0
i=1


while i<=n:
    animal = input()

    if animal[1] == 'C':
        c= c + int(animal[0])
    elif animal[1] == 'R':
        r=r + int(animal[0])
    else:
        s= s + int(animal[0])
    i+=1

total = c+r+s
pc= float((c*100)/total)
pr= float((r*100)/total)
ps= float((s*100)/total)

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')

print('Percentual de coelhos: %.2lf %'%pc)
print('Percentual de ratos: %.2lf %'%pr)
print('Percentual de sapos: %.2lf %'% ps)

