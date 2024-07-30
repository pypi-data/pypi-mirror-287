def pattern11(n):
    for i in range(1, n+1):
        for j in range(0, i):
            if i != n:
                if j == 0 or j == i - 1:
                    print(" * ", end="")
                else:
                    print(end="   ")
            else:
                print(" * ", end="")
        print("\r")