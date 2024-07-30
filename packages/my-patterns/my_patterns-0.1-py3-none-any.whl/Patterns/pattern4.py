def pattern4(n):
    for i in range(1, n+1):
        for j in range(n-1, n-i, -1):
            print(end="   ")
        for j in range(0, n + 1 - i):
            print(" * ", end="")
        print("\r")