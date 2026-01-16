from collections import deque
N = int(input())
shark = 2
time = 0
cnt = 0 # 물고기 수

graph = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(a,b):
    global time
    global shark
    global cnt
    count = 0

    while True:
        queue = deque()
        queue.append((a,b))
        visited = [[0]*N for _ in range(N)]
        visited[a][b] = 1

        c = []

        while queue:
            x,y = queue.popleft()
        
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] +y
                    
                if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 :

                    if graph[nx][ny] <= shark:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))

                    if 0< graph[nx][ny] < shark :
                        c.append((visited[nx][ny]-1, nx, ny))
        
        if not c:
            return

        c.sort()
        dist, nx, ny = c[0]

        time += dist
        graph[nx][ny] = 0 # 물고기 먹음
        count += 1

        if count == shark : # 크기 개수만큼 먹으면 크기가 1커짐
            shark += 1 
            count =0
                    
        a, b = nx, ny

    

sx,sy =0,0

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N): # 세로
    for j in range(N): # 가로

        if graph[i][j] == 9 : # 아기상어 시작점
            graph[i][j] = 0
            sx = i
            sy = j

bfs(sx,sy)
print(time)