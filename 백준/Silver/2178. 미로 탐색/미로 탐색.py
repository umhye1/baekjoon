import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        
            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
        
    return graph[n-1][m-1]

print(bfs(graph,0,0))
            
