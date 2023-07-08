x = int(input())
for i in range(x):
    a = "*" * ((i+1)*2-1)
    b = " " * (x-i-1)
    print(b+a)
for i in range(x-1)[::-1]:
    a = "*" * ((i+1)*2-1)
    b = " " * (x-i-1)
    print(b+a)