import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split()) # m : 가로(열), n: 세로 (행)
graph = [[] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

# 입력 받기
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

def bfs():
    queue = deque()

    # 익은 토마토 위치 찾기    
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1 :
                queue.append((j,i))

    while queue :

        ddy, ddx = queue.popleft()
        for i in range(4):
            nx = dx[i] + ddx
            ny = dy[i] + ddy

            if 0 <= nx < m and 0 <= ny < n :
                if  graph[ny][nx] == 0:
                    graph[ny][nx] = graph[ddy][ddx] +1
                    queue.append((ny,nx))


bfs()
cnt = 0
for j in range(n):
    for i in range(m):
        if graph[j][i] == 0:
                print(-1)
                sys.exit(0)
            
        cnt = max(cnt, graph[j][i])
print(cnt-1)
            
