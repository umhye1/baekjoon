import sys
from collections import deque

n = int(sys.stdin.readline())
graph =[[] for _ in range(n)]
visited =[[False] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = []

def bfs(y,x,h):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True

    while queue :
        ddy, ddx = queue.popleft()
        for i in range(4):
            nx = dx[i] + ddx
            ny = dy[i] + ddy

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] > h :
                    queue.append((ny,nx))
                    visited[ny][nx] = True
                

for i in range(n):
    graph[i]=(list(map(int,sys.stdin.readline().split())))

max_height = max(map(max, graph))
cnt = 0

for h in range(max_height+1):
    count = 0
    visited =[[False] * n for _ in range(n)]
    
    for j in range(n):
        for i in range(n):
            if graph[j][i] > h and not visited[j][i]:
                bfs(j,i,h)
                count += 1

    cnt = max(cnt, count)

print(cnt)
