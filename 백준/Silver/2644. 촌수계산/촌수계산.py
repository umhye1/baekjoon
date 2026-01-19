from collections import deque
n = int(input()) # 전체 사람 수
a,b = map(int, input().split()) #촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) #부모 자식들 간의 관계의 개수 m

graph = [[]for i in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x,y = map(int, input().split()) #앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
    graph[x].append(y)
    graph[y].append(x) # 일촌관계



def bfs(a,b):
    queue = deque()
    queue.append(a)
    visited[a] = 0 

    while queue:
        num = queue.popleft()
    
        for i in graph[num]:

            if i == b and visited[i] == False :
                visited[i] = visited[num] + 1
                break

            elif i!= b and visited[i] == False :
                visited[i] = visited[num] +1
                queue.append(i)
    
    
    if visited[b] == False :
        return -1
    else :
        return visited[b]
    


print(bfs(a,b))
