import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
visited =[-1] * 100001

def bfs(n,k):
    
    visited[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k :
            return visited[x]

        if 0 <= x*2 < 100001 and visited[x*2] == -1 :
            visited[x*2] = visited[x]
            queue.appendleft(x*2)

        for i in (x-1,x+1):
            if 0<=i<100001 and visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)
            
       
print(bfs(n,k))