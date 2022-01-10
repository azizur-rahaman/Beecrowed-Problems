i=1
increament=0
j=7
hCache=0
lCache=0

while True:
    
    print( f'I={i} J={j}')
    
    if increament==0:
        hCache=j
    increament+=1
    j-=1
    if j<lCache:
        j+=4
    if increament==3:
        increament=0
        
        lCache=j
        j=hCache+2
        
        i+=2
        
        
    if i>9:
        break
    