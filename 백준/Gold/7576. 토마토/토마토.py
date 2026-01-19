from collections import deque

m,n = map(int, input().split()) # 가로, 세로 수
#  정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = []
visited = [[False]*m for _ in range(n)]

for _ in range(n) :
    graph.append(list(map(int, input().split())))

def bfs():
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    
                
    
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            queue.append((i,j))
            visited[i][j] = 1

        if graph[i][j] == -1 and not visited[i][j]:
            visited[i][j] = True

bfs()

result = 0
for row in graph:
    for val in row:
        if val == 0:
            print(-1)
            exit()
    result = max(result, max(row))

print(result-1)