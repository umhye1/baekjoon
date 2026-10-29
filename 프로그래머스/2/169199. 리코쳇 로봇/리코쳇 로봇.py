from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solution(board):
    answer = 0
    
    n = len(board) # 행 개수(세로)
    m = len(board[0]) # 열 개수(가로)

    visited = [[False] * m for _ in range(n)] # 방문 확인
    count = 0
    
    def bfs (x, y, count):
        q = deque()
        q.append((x, y, count))
        visited[x][y] = True
        
        while q:
            cx, cy, count = q.popleft()
            
            if board[cx][cy] == 'G':
                return count
            
            
            if 0 <= cx < n and 0 <= cy < m : # 범위 내면
                for i in range(4):
                    nx, ny = cx, cy
                    
                    while True:
                        
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                    
                        if nnx < 0 or nnx >= n or nny < 0 or nny >= m or board[nnx][nny] == 'D': # 장애물 나오면 나오기       
                            break
                
                        nx, ny = nnx, nny
                
                    if visited[nx][ny] :
                        continue
                
                    visited[nx][ny] = True
                    q.append((nx, ny, count+1))
                
        return -1    
    
    # 탐색
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return bfs(i,j, count)
            
    return -1