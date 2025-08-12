import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(graph, a,b):

    m = len(graph)

    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1 
    return count

n = int(sys.stdin.readline())

graph = []
for i in range(n):
   graph.append(list(map(int,sys.stdin.readline().strip())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])