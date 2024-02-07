# Silver

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().strip().split())

graph = {i : [] for i in range(1, n + 1)}
for _ in range(m) :
    vertex_1, vertex_2 = map(int, sys.stdin.readline().strip().split())
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)
    
for i in graph :
    graph[i].sort()


def dfs(v, visited=None) -> list[int] :
    if visited == None :
        visited = []
    if v not in visited :
        visited.append(v)
        for i in graph[v] :
            dfs(i, visited)
    return visited
  
       
def bfs(v) :
    visited = []
    q = deque([v])
    visited.append(v)
    while q :
        current = q.popleft()
        print(current, end=" ")
        for i in graph.get(current, []) :
            if i not in visited :
                q.append(i)
                visited.append(i)

answer = dfs(v)
for i in answer :
    print(i, end=" ")
print()
bfs(v)