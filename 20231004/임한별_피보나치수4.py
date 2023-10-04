num = int(input())
x = 0
y = 1
output = 0
if num == 0:
    output = 0
elif num == 1:
    output = 1
else:
    for _ in range(num-1):
            output = x + y
            x = y
            y = output
print(output)