import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
visited = [-1]* 1000001

# n : 수빈 위치
# k : 동생 위치
# x 일 때, x-1 / x+1 / 2*x


def bfs(a, target):
    
    queue = deque([a])
    visited[a] = 0

    while queue:
        a = queue.popleft()

        if a == target:
            return visited[a]

        for i in (a-1, a+1, a*2):

            if i < 0 or i >= 1000001:
                continue

            if visited[i] == -1:
                visited[i] = visited[a] + 1
                queue.append(i)

print(bfs(n,k))