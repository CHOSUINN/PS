# bottom-up풀이
import sys

n = int(sys.stdin.readline().rstrip())
memo = {1:0, 2:1}

for i in range(2, n + 1) :
    memo[i] = memo[i - 1] + 1
    if i % 3 == 0 :
        memo[i] = min(memo[i], memo[i//3] + 1)
    if i % 2 == 0 :
        memo[i] = min(memo[i], memo[i//2] + 1)
print(memo[n])


# top-down 풀이
import sys
n = int(sys.stdin.readline().rstrip())
memo = {1:0, 2:1}

def recursion(n) :
    if n == 1 :
        return 0
    
    if n in memo :
        return memo[n]
    
    if n % 3 == 0 and n % 2 == 0 :
        memo[n] = min(recursion(n//3) + 1, recursion(n//2) + 1)
    elif n % 3 == 0 :
        memo[n] = min(recursion(n//3) + 1, recursion(n - 1) + 1)
    elif n % 2 == 0 :
        memo[n] = min(recursion(n//2) + 1, recursion(n - 1) + 1)
    else :
        memo[n] = recursion(n - 1) + 1
    return memo[n]
print(recursion(n))

