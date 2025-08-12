import sys
from collections import deque

t = int(sys.stdin.readline()) # 테스트 케이스 개수
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx >= m or nx < 0 or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 1:
                queue.append((ny,nx))
                graph[ny][nx] = 0

    return count


for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split()) # m : 가로 길이, n :세로 길이, k : 배추가 심어져있는 위치 개수
    graph = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
               bfs(graph,j,i)
               count += 1
    
    print(count)