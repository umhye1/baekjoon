from collections import deque

# 비어있는 곳은 '.'
# 물이 차있는 지역은 '*'
# 돌은 'X'
# 비버의 굴은 'D'
# 고슴도치의 위치는 'S'
dx = [0,0,-1,1]
dy = [-1,1,0,0]


r,c = map(int,input().split())

graph = []
waterlist = [[-1]*c for _ in range(r)]
slist = [[-1]*c for _ in range(r)]

# 입력받기
for _ in range(r):
    graph.append(list(map(str, input())))

wq = deque()
sq = deque()

# 물과 고슴도치 위치 구하기 (이동함), 물이 먼저 이동한다고 생각
for i in range(r):
    for j in range(c):
        
        if graph[i][j] == '*':
            wq.append((i,j))
            waterlist[i][j] = 0

        if graph[i][j] == 'S':
            sq.append((i,j))
            slist[i][j] = 0


def wbfs():

    while wq :
        x,y = wq.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<r and 0<=ny<c :
                # 물

                if graph[nx][ny] == '.' and waterlist[nx][ny] == -1:
                    waterlist[nx][ny] = waterlist[x][y] + 1
                    wq.append((nx,ny))

def sbfs():
    
    while sq :
        x,y = sq.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<r and 0<=ny<c :

                # 고슴도치
                if graph[nx][ny] == 'D' :
                    return slist[x][y] + 1
                
                if graph[nx][ny] == '.' and slist[nx][ny] == -1:
                    if waterlist[nx][ny] ==-1 or slist[x][y] + 1 < waterlist[nx][ny]:
                        slist[nx][ny] = slist[x][y] + 1
                        sq.append((nx,ny))
    return "KAKTUS"
                

                       
wbfs()
print(sbfs())
