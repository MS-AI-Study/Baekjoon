X = int(input())
count = 0
def sa(X):
    k = list(map(int,str(X)))
    a = k[0] - k[1]
    b = k[1] - k[2]
    return a == b
for x in range(1, X + 1):
    if (x / 100) < 1:
        count += 1
    elif sa(x):
            count += 1
print(count)

# import math
# X = int(input())
# count = 0
# for i in range(1, X + 1):
#     ln = []
#     a = int(math.log10(i))
#     if a <= 1 :
#         count += 1
#     else:
#         for j in range(a + 1):
#             ln.append(int((i / (10 ** j)) % 10))
#         c = 0
#         for k in range(a):
#             if (ln[0] - ln[1]) == (ln[k] - ln[k + 1]) :
#                 c += 1
#         count += int(c / a)
# print(count)