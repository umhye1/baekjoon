def solution(n, results):
    answer = 0
    
    # 4500 - sort로 정렬하는게 더 빠를까..
    # 2차원 배열로 ox 만들어놓고 나중에 count 해서 검증하는 방법?
    # 그런데 4위한테 져서 5위가 되는 경우. -> 모든 배열 업데이트 필요
    # 다 돌아봐야하나
    
    # graph[이김][짐]
    graph = [[False]* n for _ in range(n)]

    for a,b in results:
        graph[a-1][b-1] = True # 이겼다
    
    
    # [i,k] 일 때 [k,j] 면 [i,j] 
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if graph[i][k] == True and graph[k][j] == True:
                    graph[i][j] = True
                
    
    # count
    
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] or graph[j][i] :
                count += 1
            
        if count == n-1 :
            answer += 1
            
    
    return answer