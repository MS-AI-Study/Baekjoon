a = int(input())
b = int(input())
c = int(input())
res = list(str(a*b*c))
for i in  range(10):
    print(res.count(str(i)))

## 최초에 a, b, c = map(int, input()) 으로 시작했지만
## 런타임에러 발생으로 값을 각각 받게 수정
