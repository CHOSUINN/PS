from collections import deque
# 풀이 1(BFS)
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    n = len(rooms)
    visited = [False] * n
    queue = deque()
    queue.append(rooms[0])
    visited[0] = True
    while queue :
        obtained_keys = queue.popleft()
        for i in obtained_keys :
            if not visited[i] :
                visited[i] = True
                queue.append(rooms[i])
    if not all(visited) :
        return False
    else :
        return True

# 풀이 2(DFS)
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    n = len(rooms)
    visited = [False]*n
    visited[0] = True
    def dfs(curr_room) :
        for i in curr_room :
            if visited[i] == False :
                visited[i] = True
                dfs(rooms[i])
                
    dfs(rooms[0])
    
    if not all(visited) :
        return False
    else:
        return True

# 풀이 3(Stack)
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms) 
    

print(canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print(canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))