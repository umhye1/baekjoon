import sys
from collections import deque

t = int(sys.stdin.readline()) # 테스트 케이스 수
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    
    while f_queue :
        y,x = f_queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=ny<h and 0<=nx<w and f_visited[ny][nx] == -1 and graph[ny][nx] != '#' :
                f_queue.append((ny,nx))
                f_visited[ny][nx] = f_visited[y][x] + 1


    while queue:
        y,x = queue.popleft()
        
        if ((y == h-1) or (y == 0) or (x == w-1) or (x == 0)) and (graph[y][x] == "." or graph[y][x] == "@"):
            print(visited[y][x]+1)
            return
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=ny<h and 0<=nx<w and visited[ny][nx] == -1  and graph[ny][nx] != "#":
                if f_visited[ny][nx] == -1 or f_visited[ny][nx] > visited[y][x] + 1:
                    queue.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1


    print("IMPOSSIBLE")
    return


for _ in range(t):
    w,h = map(int, sys.stdin.readline().split()) # 너비와 높이 w와 h
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

    queue = deque()
    f_queue = deque()

    visited = [[-1]*w for _ in range(h)] 
    f_visited = [[-1]*w for _ in range(h)]

    for j in range(h):
        for i in range(w):
            if graph[j][i] == "@" : # 시작 위치
                queue.append((j,i))
                visited[j][i] = 0
            
            if graph[j][i] == "*" : # 불 시작 위치
                f_queue.append((j,i))
                f_visited[j][i] = 0
    
    bfs()