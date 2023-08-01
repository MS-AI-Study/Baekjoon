dicts = {}
n, m = map(int, input().split())
for _ in range(n):
    site, pw = map(str, input().split())
    dicts[site] = pw
for _ in range(m):
    print(dicts[str(input())])
    