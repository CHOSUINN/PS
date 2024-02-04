from collections import deque

def numIslands(grid: list[list[str]]) -> int:
    num_of_island = 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]
    
    def bfs(x, y) :
        visited[x][y] = True
        q = deque()
        q.append((x,y))
        dx = [-1, 1, 0, 0] #좌우상하
        dy = [0, 0, 1, -1]
        
        while q :
            curr_x, curr_y = q.popleft()
            for i in range(len(dx)) :
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col :
                    if not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))
    
    for i in range(row) :
        for j in range(col) :
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                num_of_island += 1
    
    return num_of_island
        

print(numIslands(grid=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))