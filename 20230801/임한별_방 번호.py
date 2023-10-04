num = str(input())
dicts = {}
for i in range(10):
    dicts[i] = num.count(str(i))

if (dicts[6] + dicts[9]) % 2 == 0:
    dicts[6] =  int((dicts[6] + dicts[9]) / 2)
else:
    dicts[6] = ((dicts[6] + dicts[9]) // 2) + 1
dicts[9] = 0
print(max(dicts.values()))