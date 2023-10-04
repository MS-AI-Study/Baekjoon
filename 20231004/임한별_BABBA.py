num = int(input())
a = 1
b = 0
c = 0
d = 0
for _ in range(num):
    c = a
    d = b
    a = d
    b = c + d

print(f"{a} {b}")