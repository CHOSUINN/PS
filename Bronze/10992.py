#Bronze

n = int(input())
for i in range(n) :
    print(" " * (n - 1 - i), end="")
    if i == n - 1 :
        print("*" * (2 * n - 1))
    elif 0 < i < n - 1:
        print("*" + " " * (2 * i - 1) + "*")
    else:     # i == 0인 경우
        print("*")
