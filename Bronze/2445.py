# Bronze

n = int(input())

for i in range(1, n + 1) :
    print("*" * i, end="")
    print(" " * (2 *(n - i + 1) - 2), end="")
    print("*" * i)
    
for i in range(1, n) :
    print("*" * (n - i), end="")
    print(" " * (2 * (i + 1) - 2), end="")
    print("*" * (n - i))