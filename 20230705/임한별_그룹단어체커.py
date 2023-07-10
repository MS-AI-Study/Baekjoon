def d(n):
    num = n
    enter = True
    for j in n:
        num = num.lstrip(j)
        if j in num:
            enter = False
    return enter

num = int(input())
enter = 0
for i in range(num):
    if d(input()):
        enter += 1
        
print(enter)