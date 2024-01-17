# 풀이 1
n = int(input())
for i in range(n) :
    print(" " * i, end="")
    print("*" * (n - i))


# print함수를 남발하지 않은 풀이 2
n = int(input())
for i in range(n) :
    print(" " * i + "*" * (n - i))