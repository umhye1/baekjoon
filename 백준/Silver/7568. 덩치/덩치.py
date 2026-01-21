n = int(input())

graph = []
c = []

for i in range(n):
    x,y = map(int, input().split())
    graph.append((x,y))

for i in range(n):
    cnt = 1
    for j in range(n):
        if graph[i][0] < graph[j][0] and graph[i][1] < graph[j][1]:
            cnt += 1
    
    c.append(cnt)


print(" ".join(map(str,c)))