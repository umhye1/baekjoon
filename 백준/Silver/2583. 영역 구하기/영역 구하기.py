import sys
from collections import deque
# 사각형 칠하기는 행=y 세로, 열=x 가로

m,n,k = map(int, sys.stdin.readline().split()) # 세로 , 가로, 직사각형 수
graph = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
dirsx = [-1,1,0,0]
dirsy = [0,0,-1,1]
cnt = []

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    count = 1
    
    while queue:
        ddy , ddx = queue.popleft()

        for i in range(4):
            cx = dirsx[i] + ddx
            cy = dirsy[i] + ddy

            if 0 <= cx < n and 0 <= cy < m :
                if not visited[cy][cx] and graph[cy][cx] == 0 :
                    visited[cy][cx] = True
                    queue.append((cy,cx))
                    count += 1
                
    return count

# 기본 맵 세팅
for i in range(k):
    lx,ly,rx,ry = map(int, sys.stdin.readline().split())
    dx = abs(lx-rx)
    dy = abs(ly-ry)

    for y in range(dy):
        for x in range(dx):
            if  graph[ly+y][lx+x] == 0:
                graph[ly+y][lx+x] = 1
    

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            cnt.append(bfs(i,j))

print(len(cnt))
print(*sorted(cnt))
            