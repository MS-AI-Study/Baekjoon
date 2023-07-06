h, m = map(int, input().split())
time = h * 60 + m - 45
if time >= 0 :
    print(str(int(time/60)), str(time % 60), end = " ")
else :
    time = 1440 + time
    print(str(int(time/60)), str(time % 60), end = " ")