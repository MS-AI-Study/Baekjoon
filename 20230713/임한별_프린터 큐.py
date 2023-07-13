from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    doc = deque(list(map(int, input().split())))
    en = 0
    while True:
        docMax = max(doc)
        first = doc.popleft() #첫 요소를 뽑는다
        m -= 1 # 내 위치가 변경됨
        
        if first != docMax: #뽑은 숫자가 가장 큰 숫자가 아니면
            doc.append(first) #숫자를 뒷 숫서로 넘긴다
            if m < 0: #숫자가 자기 자신이면
                m = len(doc)-1
        
        else: #뽑은 숫자가 가장 큰 숫자면
            en += 1 #그 문서 출력
            if m < 0:
                print(en)
                break