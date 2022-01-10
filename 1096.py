i=1
increament=0
j=7

while True:
    print( f'I={i} J={j}')
    increament+=1
    j-=1
    if j<5:
        j=7
    if increament==3:
        increament=0
        i+=2
    if i>9:
        break
    

