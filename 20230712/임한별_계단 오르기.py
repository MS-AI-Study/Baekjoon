n = int(input())
step=[]
for _ in range(n):
    step.append(int(input()))
flist=[]
for _ in range(n):
    flist.append(0)

if len(step) <= 2:
    print(sum(step))
    exit()
    
flist[0] = step[0]
flist[1] = step[0]+step[1]
for i in range(2, n):
    a = flist[i-2]+step[i]
    b = flist[i-3]+step[i-1]+step[i]
    if a > b :
        flist[i] = a
    else:
        flist[i] = b
        
print(flist[-1])