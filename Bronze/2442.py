# Bronze

# 풀이1
n = int(input())
for i in range(n) :
    print(" " * (n - (i + 1)), end="")
    print("*" * (2*(i + 1) - 1))
    
#풀이 2 제일 맘에 드는 답
n = int(input())
for i in range(1, n + 1) :
    print(" " * (n - i), end="")
    print("*" * (2*i - 1))
    
# 풀이 3 
n = int(input())
for i in range(1, n + 1) :
    print(" " * (n - i) + "*" * (2*i - 1))