h,w = map(int, input().split())
graph = []
visited = [[-1]*w for _ in range(h)]
cloud = []

for i in range(h):
    graph.append(list(input()))

for i in range(h):
    count = 0
    isCount = False

    for j in range(w):

        if graph[i][j] == 'c':
            visited[i][j] = 0
            isCount = True
            count = 0
        
        if graph[i][j] == '.' and isCount:
            visited[i][j] = count
        count += 1


for i in range(h):
    print(" ".join(map(str,visited[i])))