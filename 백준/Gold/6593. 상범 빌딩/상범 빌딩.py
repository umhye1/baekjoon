import sys
from collections import deque

dx = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dz = [-1,1,0,0,0,0]

def bfs():
    while queue:
        z,y,x  = queue.popleft()

        if graph[z][y][x] == "E":
            s = visited[z][y][x]
            print(f"Escaped in {s} minute(s).")
            return
        
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z

            if 0<=nx<C and 0<=ny<R and 0<=nz<L and visited[nz][ny][nx] == -1 and graph[nz][ny][nx] != '#' :
                queue.append((nz,ny,nx))
                visited[nz][ny][nx] = visited[z][y][x] + 1

    print("Trapped!")
    return

while True :
 
    L,R,C = map(int,sys.stdin.readline().split()) #  L, R, C로 시작한다. L빌딩의 층 수. R과 C는 상범 빌딩의 한 층의 행과 열의 개수
    if L == 0 and R == 0 and C == 0:
        break
    
    visited = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    graph = []

    # graph 채우기
    for l in range(L):
        if l > 0:
            sys.stdin.readline()
            
        floor = []

        for r in range(R):
            row = list(sys.stdin.readline().rstrip())
            floor.append(row)

        graph.append(floor)
    
    
    # 시작점 찾기, queue 생성
    for k in range(L): # z
        for j in range(R): # y
            for i in range(C): # x
                if graph[k][j][i] == "S": # 시작
                    queue = deque()
                    queue.append((k,j,i))
                    visited[k][j][i] = 0
    
    bfs()

    line = sys.stdin.readline()
    if not line.strip():  # 빈 줄인 경우 (공백 제거 후 빈 문자열인지 확인)
        continue
