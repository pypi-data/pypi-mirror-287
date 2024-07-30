
def pattern14(n):
    for i in range(0, n):
        for j in range(0, i):
            print(end=" ")
        for k in range(0, (n - i) * 2 - 1):
            print("*", end="")
        print("\r")
    for i in range(2, n+1):
        for j in range(n, i, -1):
            print(end=" ")
        for k in range (0, i * 2 - 1):
            print("*", end="")
        print("\r")