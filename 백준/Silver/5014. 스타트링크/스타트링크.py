import sys
from collections import deque

F,S,G,U,D = map(int, sys.stdin.readline().split()) #F, S, G, U, D
dirs = [U,-D] # 위로 u 만큼, 아래로 d 만큼 이동
visited = [False] * (F+1)
def bfs(F,S,G) :

    if (S == G):
        print(0)
        return 

    if (S + U) > F and (S - D) < 1 :
        print(0)
        return
    
    queue = deque()
    count = 0
    queue.append((S,count))

    while queue :
        x,count = queue.popleft()


        if x == G :
            print(count)
            return

        for i in range(2):
            nx = dirs[i] + x
        
            if 0 < nx <= F and not visited[nx]:
                visited[nx] = True
                queue.append((nx, count+1))
   
    print("use the stairs")
    return

bfs(F,S,G)