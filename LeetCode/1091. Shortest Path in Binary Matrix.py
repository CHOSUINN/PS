from collections import deque

def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    shoest_path = -1
    row = col = len(grid)
    if grid[0][0] != 0 or grid[row - 1][col - 1] != 0 :
        return shoest_path
    
    visited = [[False]*col for _ in range(row)]
    queue = deque()
    queue.append((0,0, 1))
    visited[0][0] =True
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]  #좌우상하 왼대각 오른대각
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    while queue :
        curr_x, curr_y, curr_len = queue.popleft()
        if curr_x == row - 1 and curr_y == col - 1 :
            shoest_path = curr_len
            break
        for i in range(len(dx)) :
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col :
                if not visited[next_x][next_y] and grid[next_x][next_y] == 0 :
                    queue.append((next_x, next_y, curr_len + 1))
                    visited[next_x][next_y] = True
    return shoest_path


print(shortestPathBinaryMatrix(grid = [[0,1],[1,0]]))
print(shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
print(shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]))