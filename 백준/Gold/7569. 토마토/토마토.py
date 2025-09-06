import sys
from collections import deque

M,N,H = map(int, sys.stdin.readline().split())
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수, 쌓아올려지는 상자의 수를 나타내는 H
dx =[0,0,0,0,-1,1]
dy =[0,0,-1,1,0,0]
dz =[-1,1,0,0,0,0]

# visited
visited = [[[False for _ in range(M)]for _ in range(N)]for _ in range(H)]
queue = deque()
cnt = 0

# graph 채우기
graph = []
count = 0 

for h in range(H):
    floor = []

    for n in range(N):
        row = list(map(int,sys.stdin.readline().rstrip().split()))
        floor.append(row)

        for m in range(M):
            if row[m]== 1 :
                queue.append((h,n,m))
                visited[h][n][m] = True

            if row[m] == 0 : # 안 익은 사과 찾기 
                count += 1
                
    graph.append(floor)

if count == 0 : # 안 익은 사과가 없는 경우 (다 익음)
    print(0)


def bfs():
    global cnt

    while queue:
        z,y,x = queue.popleft()

        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z

            if 0<=nx<M and 0<=ny<N and 0<=nz<H and not visited[nz][ny][nx] and graph[nz][ny][nx] != -1:
                queue.append((nz,ny,nx))
                visited[nz][ny][nx] = True
                graph[nz][ny][nx] = graph[z][y][x]+1
    
bfs()

def find(count): 
    max_graph = 0     
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] > max_graph :
                    max_graph = graph[h][n][m]
                
                if graph[h][n][m] == 0 :
                    print(-1)
                    return
    if count != 0:
        print(max_graph-1)
        return             

find(count)

