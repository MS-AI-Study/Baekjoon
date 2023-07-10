infected = 0
infection = [True]
for i in range(int(input())-1):
    infection.append(False)
pcList = []
for i in range(int(input())):
    pcList.append(input().split())
for j in range(len(infection)):
    for n in pcList:
        if infection[int(n[0])-1] != infection[int(n[1])-1]:
            infection[int(n[0])-1] = True
            infection[int(n[1])-1] = True

for j in infection:
    if j:
        infected += 1
print(infected-1)