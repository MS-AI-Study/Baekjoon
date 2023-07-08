inp = str(input())
while inp != "0":
    inp1 = inp
    inp = list(inp)
    inp.reverse()
    inp = "".join(inp)
    if inp1 == inp:
        print("yes")
    else:
        print("no")
    inp = str(input())