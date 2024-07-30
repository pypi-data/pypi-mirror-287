def pattern6(n):
    for i in range(n):
        for j in range(n):
            if i + j == 2 or i - j == 2 or j - i == 2 or i + j == n + 1:
                print(" * ", end="")
            else:
                print(end="   ")
        print("\r")