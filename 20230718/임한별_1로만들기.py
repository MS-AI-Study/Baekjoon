x = int(input())
y = x
z = x
countery = 0
counterz = 0
while x != 1:
    if x % 3 == 0:
        x = x/3
        countery += 1
    elif x % 2 == 0:
        x = x/2
        countery += 1
    else:
        x -= 1
        countery += 1
print()