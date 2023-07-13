for _ in range(int(input())):
    m,n,k = map(int, input().split())
    arr = [[0]*n for _ in range(m)]
    for _ in range(k):
        a,b = map(int, input().split())
        arr[a][b] = 1
    for i in arr:
        for j in i:
            if arr[i][j] == 1:
                if arr[i+1][j] == 1:
                    if arr[i][j+1] == 1:
                        arr[i][j] = 3
                        arr[i][j+1] = 2
                        arr[i+1][j] = 2
                    elif arr[i+2][j] == 1:
                        arr[i][j] = 2
                        arr[i+1][j] = 3
                        arr[i+2][j] = 2
                        if arr[i+1][j+1] == 1:
                            arr[i+1][j+1] = 2
                elif arr[i][j+1] == 1:
                    if arr[i][j+2] == 1:
                        arr[i][j] = 2
                        arr[i][j+1] = 3
                        arr[i][j+2] = 2
                        if arr[i+1][j+1] == 1:
                            arr[i+1][j+1] = 2
    print(arr.count(3)+arr.count(1))