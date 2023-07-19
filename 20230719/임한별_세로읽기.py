x = []
for _ in range(5):
    x.append(list(input()))
en = ''
leng = len(max(x, key = lambda s: len(s)))
for i in range(leng):
    for j in x:
        if len(j) >= i+1:
            en += str(j[i])
print(en)