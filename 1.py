n = int(input(""))

if n < 46:
    x1 = 0
    x2 = 1

    print(x1,end=" ")
    for i in range(n - 1):
        print(x2,end=" ")
        x3 = x2
        x2 = x2 + x1
        x1 = x3
    print()

