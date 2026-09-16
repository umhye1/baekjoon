# 거리 꺾일 때마다 corner + 1 해주기
# 이전 방향 저장해두기
import heapq

dx = [0,0,-1,1] # 상 하 좌 우
dy = [1,-1,0,0]

def bfs(visited,n,board):
    q = []
    cost = 0
    prev = 0
    new_cost = 0
    x,y = 0,0
    # 0,0에서 방향을 고정하면 안된다함
    for i in range(4):
        heapq.heappush(q,(cost,x,y,i))
        visited[x][y][i] = cost
    

    while q:
        cost,x,y,prev = heapq.heappop(q)
        
        if x == n-1 and y == n-1 :
            return cost
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0: # 이동 조건
                
                if x == 0 and y == 0: # 처음
                    new_cost = cost + 100
                
                elif prev == i: # 방향 같음 - 직선거리
                    new_cost = cost + 100
                
                else: # 방향 다름 - 코너
                    # 비용을 비교해야함. 갱신하지 말 것
                    new_cost = cost + 500 + 100
                
                if new_cost < visited[nx][ny][i] : # 비용이 더 작으면 갱신
                    visited[nx][ny][i] = new_cost
                    heapq.heappush(q,(new_cost,nx,ny,i)) # 방향 갱신 prev = i
                    
    
def solution(board):
    answer = 0
    n = len(board)
    visited =[[[float('inf') for _ in range(4)] for _ in range(n)]for _ in range(n)]  # cost 비교하기 위한 map이라서 방문여부 알 필요 없음
    corner = 0
    answer = bfs(visited,n,board)

    
    return answer          