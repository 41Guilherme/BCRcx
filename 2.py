n = int(input(""))

x1 = 1
for i in range(n):
    x1 = n * x1
    n = n - 1

print(x1 , end=" ")