from collections import deque


def bfs(computers,visited, n, start):
    
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        x = queue.popleft() # 현재 지점 
        for next_x in range(n): # 현재 지점과 연결되어 있는 노드 찾기
            if visited[next_x] == 0 and computers[x][next_x] == 1 and x!=next_x:
                queue.append(next_x)
                visited[next_x] = 1
                
                
            
    


def solution(n, computers):
    answer = 0 # 네트워크 개수
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            bfs(computers, visited,n,i)
            answer += 1
    
    
    return answer