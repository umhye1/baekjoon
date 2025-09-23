import sys
from collections import deque
from itertools import combinations
import copy

# 새로 세울 수 있는 벽의 수 : 3개
# 0: 빈칸, 1: 벽, 2: 바이러스
# 벽 없으면 바이러스는 퍼져나감

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(temp):
    # 바이러스 시작점 넣기, 바이러스 큐 시작
    queue = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i,j))
    
    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny] == 0:
                temp[nx][ny] =2
                queue.append((nx,ny))


def safe_area(temp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

zeros = [(i,j) for i in range(n) for j in range(m) if graph[i][j]==0]
result = 0
for walls in combinations(zeros,3):
    temp = copy.deepcopy(graph)

    for x,y in walls:
        temp[x][y] = 1
    
    bfs(temp)
    result = max(result, safe_area(temp))

print(result)
  