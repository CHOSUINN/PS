# python dict
def climbStairs(n: int) -> int:
    memo = {1:1, 2:2}
    for i in range(3, n + 1) :
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

#list
def countStairs(n) :
    memo = [0, 1]
    for i in range(1, n) :
        memo.append(memo[i - 1] + memo[i])
    return memo[n]

print(climbStairs(n = 2))
print(climbStairs(n = 3))
print(climbStairs(n = 8))