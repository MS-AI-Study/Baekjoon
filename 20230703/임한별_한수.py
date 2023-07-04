def d(n):
    enter = True
    if n >= 100:
        num_list = list(map(int, str(n)))
        num = num_list[0] - num_list[1]
        a = 0
        for i in range(len(num_list)):
            if i >= 1:
                if num != num_list[i-1] - num_list[i]:
                    enter = False
    return enter

startNum = int(input())

finishNum = 0
for i in range(startNum):
    if d(i+1):
        finishNum += 1

print(finishNum)