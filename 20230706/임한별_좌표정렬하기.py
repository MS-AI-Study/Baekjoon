N = int(input())
f = []
for i in range(N):
    x,y = map(int,input().split())
    f.append([x,y])
f.sort()

for i in range(N):
    print(f[i][0], f[i][1])
