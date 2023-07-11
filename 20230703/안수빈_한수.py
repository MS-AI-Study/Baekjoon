val = int(input())
count = 0
for i in range(1, val+1):
    a = i%10
    b = (i//10)%10
    c = i//100
    if c == 0 or (c != 0 and c-b == b-a):
        count += 1
print(count)
