import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split()) # n : 정점의 개수,  m : 간선 개수
graph  = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
        


for _ in range(m):
    u,v = list(map(int,sys.stdin.readline().split())) # 간선의 양 끝점 u,v
    # 인접리스트 생성
    graph[u].append(v)
    graph[v].append(u)


for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i) 
        cnt += 1

print(cnt)