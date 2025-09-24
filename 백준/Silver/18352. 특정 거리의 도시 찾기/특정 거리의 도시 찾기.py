import sys
from collections import deque
# 도시의 개수, 도로의 개수, 거리정보, 출발 도시의 번호
n,m,k,x = map(int,sys.stdin.readline().split())

graph=[[]for _ in range(n+1)]
visited = [-1]*(n+1)
count = []

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

def bfs(x): # 출발 도시 번호 : x  - 1
    queue = deque()
    queue.append(x)
    visited[x] = 0

    while queue:
        a = queue.popleft() # a = 1
      
        for i in graph[a]: # graph[1] = 2,3 

            if 0<i<=n and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[a]+1


bfs(x)

for i in range(1,n+1):
    if visited[i] == k:
        count.append(i)

if len(count) == 0:
    print(-1)
else:
    print(*count, sep="\n")