def pattern17(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == n / 2:
                print(" * ", end="")
            else:
                if j == n / 2:
                    print(" * ", end="")
                else:
                    print(end="   ")
        print("\r")