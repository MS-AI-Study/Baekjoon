dicts = {}
arr = []
for i in range(int(input())):
    arr = list(map(str, input().split()))
    dicts[arr[0]]= arr[1]
arr = sorted(list(dicts.keys()), reverse=True)
for j in arr:
    if dicts[j] == 'enter':
        print(j)