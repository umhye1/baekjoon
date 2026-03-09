N = int(input())
num = int(input())

# 아래 - 오른쪽 - 위 - 왼쪽
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 그래프 초기화
graph = [[0]*N for _ in range(N) ]

max_num = N*N
x,y =0,0
target = [0,0]

z = 0
while max_num > 0 :

    graph[x][y] = max_num
    max_num -= 1

    if max_num == 0:
        if target == [0,0]:
            target=[1,1]
        break

    nx = dx[z] + x
    ny = dy[z] + y


    if (nx < 0 or nx >= N or ny < 0 or ny >= N )or graph[nx][ny] != 0 :  # 유효범위 밖
        z = (z + 1) % 4
        nx = dx[z] + x
        ny = dy[z] + y

    x , y = nx, ny
    if max_num == num:
        target =[ x+1, y+1 ]


for row in graph:
    print(*row)

print(*target)
