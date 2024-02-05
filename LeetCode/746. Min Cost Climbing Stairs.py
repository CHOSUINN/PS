# 풀이 1 : top-down dp
def minCostClimbingStairs(cost: list[int]) -> int:
    memo = {}
    
    def dfs(n) :
        if n == 0 or n == 1 :
            return 0
        if n not in memo :
            memo[n] = min(cost[n-1] + dfs(n - 1), cost[n-2] + dfs(n - 2))
        return memo[n]
    return dfs(len(cost))

# 풀이 2 : bottom-up dp
def minCostClimbingStairs(cost: list[int]) -> int:
    memo = [0]*(len(cost)+1)
    memo[0] = 0
    memo[1] = 0 
    
    for i in range(2, len(cost) + 1) :
        memo[i] = min(cost[i - 1] + memo[i - 1], cost[i - 2] + memo[i - 2])
    return memo[len(cost)]
    

print(minCostClimbingStairs(cost = [10,15,20]))
print(minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
