def pattern18(n):
    char = 65
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(char), end=" ")
            char = char + 1
            if char == 91:
                char = 65
        print("\r")