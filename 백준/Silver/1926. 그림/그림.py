import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split()) # 세로, 가로

graph = [[] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = []

def bfs(graph,y,x): # 세로 가로
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
    count = 1

    while queue:
        cy,cx = queue.popleft()

        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny,nx))
                    count += 1

    return count
            

for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

for j in range(n):
    for i in range(m):
        if graph[j][i] ==1 and  not visited[j][i] :
            cnt.append(bfs(graph,j,i))
            
    
if  not cnt:
    print(0)
    print(0)
else :
    print(len(cnt))
    print(max(cnt))