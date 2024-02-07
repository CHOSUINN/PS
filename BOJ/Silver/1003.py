#Silver

import sys
t = int(sys.stdin.readline().strip())

memo = {0:[1, 0], 1:[0,1]}   # key-val의 val은 [0의 개수, 1의 개수]

def fibonacci(n:int) -> int:
    for i in range(2, n + 1) :
        if i not in memo :
            memo[i] = [memo[i - 1][0] + memo[i - 2][0] , memo[i - 1][1] + memo[i - 2][1]]
    return memo[n]

for _ in range(t) :
    n = int(sys.stdin.readline().strip())
    answer = fibonacci(n) 
    print(answer[0], answer[1])
    