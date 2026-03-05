n = int(input())
graph = []
result  = []
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

# 지뢰판
for i in range(n):
    graph.append(list(input()))

def find(x,y):
    count = 0
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] == '*':
                count += 1
    
    return count


is_dead = False

# 사용자가 플레이한 판
for i in range(n):
    nlist = list(input())
    result.append(nlist)
    for j in range(len(nlist)):
        if nlist[j] == 'x':
            if graph[i][j] == '*':
                is_dead = True
            
            result[i][j] = str(find(i,j))

if is_dead:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '*':
                result[i][j] = '*'

for i in result:
    print(''.join(i))
        
