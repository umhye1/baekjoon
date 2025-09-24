import sys
from collections import deque
# n*n 크기
# 바이러스 1~k까지
#1초마다 상하좌우 증식
n,k = map(int, sys.stdin.readline().split())
graph =[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
# s 초 지난 후(x,y)에 존재하는 바이러스 종류 출력
s,x,y = map(int, sys.stdin.readline().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus():
    queue = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] !=0: # 0,0 기준으로 들어가있기때문
                v = graph[i][j]
                queue.append((v,i,j,0))
        
    
    queue.sort()
    q = deque(queue)

    while q:
        virus_num,a,b,time = q.popleft()
        if time == s:
            break

        for i in range(4):
            nx,ny = dx[i] + a, dy[i] + b

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny] = virus_num
                q.append((virus_num,nx,ny,time+1))

virus()
print(graph[x-1][y-1])   