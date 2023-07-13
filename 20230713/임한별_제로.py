arr = []
for _ in range(int(input())):
    num = int(input())
    if num>0:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))