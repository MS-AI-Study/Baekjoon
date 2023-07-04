cro = "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="
num = str(input())
enter = 0
for i in cro:
    if i in num:
        enter += num.count(i)
        num = num.replace(i, '.')


print(enter+len(num.replace('.','')))