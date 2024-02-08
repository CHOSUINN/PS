# Top-down
def uniquePaths(m: int, n: int) -> int:
    memo = [[-1]*n for _ in range(m)]
    def dfs(x, y) :
        if x == 0 and y == 0:
            memo[x][y] = 1
            return memo[x][y]
        
        unique_paths = 0
        if memo[x][y] == -1:
            if x - 1 >= 0 :
                unique_paths += dfs(x-1, y)
            if y - 1 >= 0 :
                unique_paths += dfs(x, y-1)
            memo[x][y] = unique_paths
        return memo[x][y]
    return dfs(m - 1, n - 1)

# bottom-up
def uniquePaths(m: int, n: int) -> int:
    dp = [[-1] * n for _ in range(m)]
    
    for i in range(m) :
        dp[i][0] = 1
    for i in range(n) :
        dp[0][i] = 1
        
    for i in range(1, m) :
        for j in range(1, n) :
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n -1]    
        
print(uniquePaths(m = 3, n = 1))
print(uniquePaths(m = 3, n = 7))
print(uniquePaths(m = 3, n = 2))
print(uniquePaths(m = 23, n = 12))
