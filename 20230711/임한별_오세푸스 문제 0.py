n = list(map(int, input().split()))
i = list(range(1, n[0] + 1))

num = n[1]
en = ""
x = 0
while len(i) > 0:
    while num > n[0]:
        num = num - n[0]
        n[0] = len(i)
        x = 0
    
    e = i[num-1-x]
    i.pop(num-1-x)
    x += 1
    en += str(e) + ", "
    num += n[1]
print("<" + en[0:-2] + ">")