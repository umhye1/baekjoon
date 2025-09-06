import sys
from collections import deque
import copy

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
g_graph = copy.deepcopy(graph)

visited = [[False]*n for _ in range(n)]
g_visited = [[False]*n for _ in range(n)]
cnt = []
g_cnt = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for j in range(n):
    for i in range(n):
        if g_graph[j][i] == "G":
           g_graph[j][i] = "R"


def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
    count = 1

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<n :
                if not visited[ny][nx] and graph[y][x] == graph[ny][nx] :
                    queue.append((ny,nx))
                    visited[ny][nx] = True
                    count += 1
    return count
        

def g_bfs(y,x):
    g_queue = deque()
    g_queue.append((y,x))
    g_visited[y][x] = True
    count =1

    while g_queue:
        y,x = g_queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<n :
                if not g_visited[ny][nx] and g_graph[y][x] == g_graph[ny][nx] :
                    g_queue.append((ny,nx))
                    g_visited[ny][nx] = True
                    count+=1
                   
    return count




for j in range(n):
    for i in range(n):
        if not visited[j][i] :
            cnt.append(bfs(j,i))
            
        
        if not g_visited[j][i] :
            g_cnt.append(g_bfs(j,i))

print(len(cnt), len(g_cnt), sep=" ")

            