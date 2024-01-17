#Bronze

n = int(input())

for i in range(n) :
    print(" " * (n - 1 - i), end="")
    print("*" * (i + 1))

for i in range(1, n) :
    print(" " * i, end="")
    print("*" * (n - i))