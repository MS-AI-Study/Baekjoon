arr = []
n = list(map(int, input().split()))
for _ in range(n[0]):
    arr.append(input())
for _ in range(n[1]):
    i = input()
    if i.isdigit():
        print(arr[int(i)-1])
    else:
        print(arr.index(i)+1)