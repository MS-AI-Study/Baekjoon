num = str(input())
# 0 또는 1 기준으로 스플릿
def numsplit(num, st):
    numlist = list(num.split(st))
    while '' in numlist:
        numlist.remove('')
    return len(numlist)
zero = numsplit(num, '0')
one = numsplit(num, '1')
# 적은 쪽을 출력
if one <= zero:
    print(one)
else:
    print(zero)