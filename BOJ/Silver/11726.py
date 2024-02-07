#Silver

import sys

n = int(sys.stdin.readline().strip())

memo = {1:1, 2:2}

def  countBlock(n:int) -> int :
    
    for i in range(3, n + 1) :
        if i not in memo :
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]
print(countBlock(n)%10007)