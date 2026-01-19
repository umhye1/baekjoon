from collections import deque

n,m,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
count = []

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    size = 1

    while queue:
        x,y = queue.popleft()
       
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                size += 1

    return size

for _ in range(k):
    r,c = map(int, input().split()) # r은 위에서부터, c는 왼쪽에서부터
    graph[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count.append(bfs(i,j))

print(max(count))
