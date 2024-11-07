# n = 정점의 개수
# m = 간선의 개수
# v = 시작 정점

# dfs
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리함
#   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄

# bfs
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 함
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함

from collections import deque

n,m,v = map(int, input().split())
graph =[[] for _ in range(n+1)]

for i in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()
    

def dfs(x) :
    if x <0 or x>=n+1 :
        return False
    
    visited[x] = True
    print(x,end =" ")

    for i in graph[x]:
        if visited[i] == False :
            dfs(i)

def bfs(x) :
    if x <0 or x>=n+1 :
        return False
    
    queue = deque([x])
    visited[x] = True

    while queue :
        
        front = queue.popleft()
        print(front, end=" ")
        

        for i in graph[front] :
            if visited[i] == False:
                queue.append(i)
                visited[i] =True
                
    
visited = [False] * (n+1) 
dfs(v)
print("")

visited = [False] * (n+1) 
bfs(v)
# print(bfs(v))

# 1 : 2,3,4
# 2 : 1,4
# 3 : 1,4
# 4 : 1,2,3


# 1 : 2,3 
# 2 : 1,5
# 3 : 1,4
# 4 : 3,5
# 5 : 2,4

