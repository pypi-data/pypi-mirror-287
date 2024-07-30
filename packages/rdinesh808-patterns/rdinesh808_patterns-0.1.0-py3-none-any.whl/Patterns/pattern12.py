def pattern12(n):
    for i in range(1, n+1):
        for j in range(1, n + 1 - i):
            print(end="  ")
        for j in range(1, i+1):
            print("  * ", end="")
        print("\r")