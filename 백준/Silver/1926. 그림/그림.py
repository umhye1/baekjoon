from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

graph = []

count = 0
grim = []

n,m = map(int, input().split()) # 세로, 가로
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    g = 1

    while queue:
        x,y = queue.popleft() # 다음에 방문할 x,y좌표
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<m and  graph[nx][ny] == 1:
                g += 1
                graph[nx][ny] = 0
                queue.append((nx,ny))

    return g # 넓이

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 :
            grim.append(bfs(i,j))
            count += 1

if count == 0:
    print(0)
    print(0)
else :
    print(count)
    print(max(grim))



