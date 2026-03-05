graph = []

# 빙고판 생성
for i in range(5):
    graph.append(list(map(int, input().split())))


def find_loc(x):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == x :
                graph[i][j] = False

def count_bingo():
    count = 0  
    for i in range(5):
        if graph[i][0] == graph[i][1] == graph[i][2] == graph[i][3] == graph[i][4] == False :
            count += 1

        if graph[0][i] == graph[1][i] == graph[2][i] == graph[3][i] == graph[4][i] == False :
            count += 1 
        
    if graph[0][0] == graph[1][1] == graph[2][2] == graph[3][3] == graph[4][4] == False:
            count  += 1

    if graph[0][4] == graph[1][3] == graph[2][2] == graph[3][1] == graph[4][0] == False:
            count += 1
    
    if count >= 3 :
        return True
    
    return False
    


num = 0
# 수 부르기
for i in range(5):
    nlist = list(map(int, input().split()))
    for j in nlist:
        # 수 위치 찾기 - 엑스 침
        find_loc(j)
        num += 1
        if count_bingo() :
            print(num)
            exit()
