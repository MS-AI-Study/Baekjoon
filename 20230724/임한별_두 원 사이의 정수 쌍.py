def solution(r1, r2):
    zero = 0
    diag = 0
    for i in range(r2):
        for j in range(r2):
            if i * j ==0:
                if ((i + j) <= r2) and ((i + j) >= r1):
                    zero += 1
            else:
                if  ((i**2 + j**2) <= r2**2) and ((i**2 + j**2) >= r1**2):
                    diag += 1
    answer = zero * 4 + diag*4
    return answer

print(solution(2,3))