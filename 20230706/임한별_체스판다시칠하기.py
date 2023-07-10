def paint(list):
    x = "W"
    y = "B"
    countW8 = 0
    countstartW = 0
    for i in list:

        if ((countW8 != 0) and (countW8 % 8 == 0)):
            if (x == "W"):
                x = "B"
            else:
                x = "W"

        if (x != i):
            countstartW += 1
        if (x == "W"):
            x = "B"
        else:
            x = "W"
        countW8 += 1

    countB8 = 0
    countstartB = 0
    for i in list:

        if ((countB8 != 0) and (countB8 % 8 == 0)):
            if (y == "B"):
                y = "W"
            else:
                y = "B"

        if (y != i):
            countstartB += 1
        if (y == "B"):
            y = "W"
        else:
            y = "B"
        countB8 += 1

    if countstartW <= countstartB:
        return countstartW
    else:
        return countstartB

enter = 2500
n, m = map(int,input().split())
sheet = []
for i in range(n):
    sheet.append(list(input()))
for j in range(n-7):
    for s in range(m-7):
        result = ""
        for a in range(j, j+8):
            for b in range(s, s+8):
                result += str(sheet[a][b])

        enterdef = paint(result)
        if (enter > enterdef):
            enter = enterdef
print(enter)
    