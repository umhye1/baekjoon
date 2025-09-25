import sys
from collections import deque

N, L, R = map(int,sys.stdin.readline().split()) # 땅 크기, l명 이상 r명 이하 
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(r,c):
    queue = deque()
    queue.append((r,c))
    union_list = [(r,c)]  # 좌표 저장
    visited[r][c] = True

    
    while queue:
        x,y = queue.popleft()
    
        for i in range(4):
            nx ,ny = dx[i]+x , dy[i]+y

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L<=abs(graph[x][y] - graph[nx][ny])<=R : # 국경선 열기
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    union_list.append((nx,ny))
                    
    return union_list

      
day = 0
while True:
    visited = [[False]*N for _ in range(N)]
    is_moved = False # 하루동안 인구이동 있었는지?
    for r in range(N):
        for c in range(N):
            if not visited[r][c] :
                union_list = bfs(r,c)
                
                if len(union_list)>1:
                    is_moved = True
                    total_population = sum(graph[x][y] for x, y in union_list)
                    avg_population = total_population//len(union_list)

                    for x,y in union_list:
                        graph[x][y] = avg_population
    if not is_moved :
        break

    day += 1

print(day)

    
