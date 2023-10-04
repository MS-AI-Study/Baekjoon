ucpc = 'UCPC'
arr = []
for i in list(input()):
    if i.isupper():
        arr.append(i)
num=0
ucpcst = ''
for i in range(len(arr)):
    if arr[i]==ucpc[num]:
        ucpcst += arr[i]
        num+=1
    if ucpcst == ucpc:
        break
if ucpcst == ucpc:
    print('I love UCPC')
else:
    print('I hate UCPC')