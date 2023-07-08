n = int(input())
list = []
if n%5 == 0:
    list.append(int(n/5))
else:
    for i in range(int(n/5)+1):
        if ((n-i*5)%3==0):
            list.append(int((n - i*5)/3+i))
if (len(list)==0):
    print(-1)
else:
    print(min(list))