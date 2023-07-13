n = list(map(int, input().split()))
dac = list(map(int, input().split()))
en = 0

for i in range(n[0]-2):
    for j in range(i+1, n[0]-1):
        for k in range(j+1, n[0]):
            sumd = dac[i] + dac[j] + dac[k]
            if en < sumd <= n[1]:
                en = sumd
print(en)