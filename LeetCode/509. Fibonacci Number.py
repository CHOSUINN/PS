def fib(n: int) -> int:
    memo = {0:0, 1:1}
    for i in range(2, n + 1) :
        memo[i] = memo[i - 2] + memo[i - 1]
    return memo[n]

def fib(n: int) -> int:
    memo = [0, 1]
    for i in range(1, n) :
        memo.append(memo[i - 1] + memo[i])
    return memo[n]
