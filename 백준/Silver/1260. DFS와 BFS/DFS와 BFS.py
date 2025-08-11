import sys
from collections import deque
# n : 정점의 개수
# m : 간선 개수
# v : 시작 정점

# dfs
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리함
#   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# g = graph
# v = 방문할 노드(시작노드)

n,m,v = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)] # 연결된 모든 정점 확인용 그래프
visited = [False for _ in range(n+1)] # 방문 확인용 그래프
visited[0] = True

for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()


def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,v,visited)
print("")

# bfs
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 함
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함

visited = [False for _ in range(n+1)] # 방문 확인용 그래프
visited[0] = True

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
  

bfs(graph, v, visited)