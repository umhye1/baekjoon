# x1행 y1열부터 x2행 y2열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전, 중앙의 영역은 회전하지 않는다 
# x1,y1 ~ x1,y2 / x1,y1 ~ x2,y1 / x1,y2 ~ x2,y2 / x2,y1 ~ x2,y2 만 회전
# 회전 후 가장 작은 숫자를 배열에 넣기

def solution(rows, columns, queries):
    answer = []
    
    # 그래프 초기화
    graph = [[0]* columns for _ in range(rows)]
    
    for row in range(rows):
        for col in range(columns):
            graph[row][col] = row * columns + (col+1)
    
    
    # 시계방향 회전
    def rotate(query):
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1 
        a = graph[x1][y1]
        min_num = a
        
        
        # 아래로 이동하면서 당겨오기 x1 -> x2
        for i in range(x1,x2):
            graph[i][y1] = graph[i+1][y1]
            min_num = min(min_num,graph[i][y1])
        
    

        # 오른쪽으로 이동하면서 당겨오기 y1-> y2
        for i in range(y1,y2):
            graph[x2][i] = graph[x2][i+1]
            min_num = min(min_num,graph[x2][i])
        
            
        # 위로 이동하면서 당겨오기 x2 -> x1
        for i in range(x2,x1,-1):
            graph[i][y2] = graph[i-1][y2]
            min_num = min(min_num,graph[i][y2])
            
            
        # 왼쪽으로 이동하면서 당겨오기 y2 -> y1
        for i in range(y2,y1,-1):
            graph[x1][i] = graph[x1][i-1]
            min_num = min(min_num,graph[x1][i])
        
        graph[x1][y1+1] = a
        
        return min_num
        
    
    # queries 돌면서 x1,y1 ~ x2,y2범위의 애들만 시계방향 회전
    for i in queries:
        answer.append(rotate(i))
        
    return answer

    
