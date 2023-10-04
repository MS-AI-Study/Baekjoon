def circle(cx, cy, radius):
    arr = []
    for x in range(cx - radius, cx + radius + 1):
        for y in range(cy - radius, cy + radius + 1):
            if radius**2 == (x - cx) ** 2 + (y - cy) ** 2:
                arr.append(str(x)+str(y))
    return arr
                
        

for _ in range(int(input())):
    x = list(map(int, input().split()))
    if (str(x[0])+str(x[1])+str(x[2])) == (str(x[3])+str(x[4])+str(x[5])):
        print("-1")
    else:
        print(len(list(set(circle(x[0],x[1],x[2])) & set(circle(x[3], x[4],x[5])))))