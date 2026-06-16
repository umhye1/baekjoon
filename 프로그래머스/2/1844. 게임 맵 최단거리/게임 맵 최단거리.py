from collections import deque
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(maps,visited, n,m):
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        x,y = q.popleft()
        
        if x == m-1 and y == n-1 :
            return visited[x][y] 
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < m and 0 <= ny < n :
                if visited[nx][ny] == 0 and maps[nx][ny] == 1: 
                    # 이동 가능 조건  
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
            
    
    
    return -1
    
def solution(maps):
    answer = 0
    
    m = len(maps) # 세로 수 (행 수)
    n = len(maps[0]) # 가로 수 (열 수)
    
    visited = [[0]*n for _ in range(m)]
    
    answer = bfs(maps, visited, n,m)
        
    
    
    return answer