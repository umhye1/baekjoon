import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

def bfs(l,nx,ny,rx,ry):
    visited = [[False]*l for _ in range(l)]
    queue = deque()
    queue.append((nx,ny,0)) # 시작 좌표 x, y, count
    visited[ny][nx] = True

    while queue :
        x,y,count = queue.popleft()

        if x == rx and y == ry :
            return count
        
        for i in range(8):
            nnx = dx[i] + x
            nny = dy[i] + y

            if 0<= nnx < l and 0<= nny < l and not visited[nny][nnx]:
                visited[nny][nnx] = True
                queue.append((nnx,nny,count+1))



for _ in range(T):
    l = int(sys.stdin.readline()) # 체스판 한 변의 길이
    nx,ny = map(int, sys.stdin.readline().split()) # 나이트가 현재 있는 칸, 
    rx,ry = map(int, sys.stdin.readline().split()) # 나이트가 이동하려고 하는 칸

    print(bfs(l, nx, ny, rx, ry))