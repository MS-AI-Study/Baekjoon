while True:
    try:
        n = int(input())
        lens = 3**n
        arr = '-'
        while len(arr) != lens:
            arr = arr + len(arr)*' ' + arr
        print(arr)
        
    except EOFError:
        break