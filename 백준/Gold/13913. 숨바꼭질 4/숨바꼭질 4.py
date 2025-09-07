import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
visited = [-1] * 1000001
parent = [-1] * 1000001
graph = []

def bfs(x,target): # 수빈 위치, # 동생 위치  
    queue = deque()
    visited[x] = 0
    parent[x] = x
    queue.append(x)

    while queue:
        xx = queue.popleft()

        if xx == target:
            print(visited[xx])
            
            path = []
            current = target

            while current != x:
                path.append(current)
                current = parent[current]
            path.append(x)
            path.reverse()
            print(*path)
            return
        
        for i in (xx-1, xx+1, xx*2):

            if 0<=i<1000001 and visited[i] == -1: 
                visited[i] = visited[xx] + 1
                parent[i] = xx
                queue.append(i)

bfs(N,K)