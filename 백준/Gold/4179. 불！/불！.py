import sys
from collections import deque 

R,C = map(int,sys.stdin.readline().split())#행, 열
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

f_queue = deque()
j_queue = deque()
f_visited = [[-1]*C for _ in range(R)] # 여기에 시간 저장 -> count 따로 둘 필요 없음 
j_visited = [[-1]*C for _ in range(R)]


for j in range(R) :
    for i in range(C):
        if graph[j][i] == "J":
            j_queue.append((j, i))
            j_visited[j][i] = 0

        if graph[j][i] == "F":
            f_queue.append((j, i))
            f_visited[j][i] = 0


def bfs(): # 불의 BFS: 불이 모든 칸에 번지는 시간을 계산

    while f_queue :
        y,x = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < C and 0 <= ny < R and f_visited[ny][nx] == -1 and graph[ny][nx] != '#':
                f_visited[ny][nx] = f_visited[y][x] + 1
                f_queue.append((ny,nx))

    while j_queue :
        y,x = j_queue.popleft()

        if x == 0 or x == (C-1) or y == 0 or y == (R-1):
            print(j_visited[y][x]+1)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] != '#':
                if j_visited[ny][nx] == -1:
                    # 다음 칸에 불이 번지는 시간과 비교
                    if f_visited[ny][nx] == -1 or f_visited[ny][nx] > j_visited[y][x] + 1:
                        j_visited[ny][nx] = j_visited[y][x] + 1
                        j_queue.append((ny, nx))

    print("IMPOSSIBLE")
    return

bfs()