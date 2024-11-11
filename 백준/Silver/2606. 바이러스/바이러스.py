n = int(input())
m = int(input())
graph =[[]for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

visited = [False]*(n+1)
count =0 

def dfs(x) :
    global count
    if x<0 and x>n and y<0 and y>n :
        return False
    
    visited[x] = True
    count+=1
    for i in graph[x] :
        if visited[i] == False:
            dfs(i)

dfs(1)
print(count-1)