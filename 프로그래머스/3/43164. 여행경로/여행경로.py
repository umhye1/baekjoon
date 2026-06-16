def solution(tickets):
    tickets.sort()
    visited = [0] * len(tickets)
    paths = []
    
    def dfs(current_airport, path): # 현재 공항, 지금까지 지나온 경로 배열, 사용한 tickets 카운트한 것
        if len(path) == len(tickets)+1:
            paths.append(path)
            return 
        
        for i in range(len(tickets)):
            
            if visited[i] == 0 and tickets[i][0] == current_airport:
                visited[i] = 1
                result = dfs(tickets[i][1], path + [tickets[i][1]])
                
                if result is not None:
                    return result
                
                visited[i] = 0 
                
        return None
        
    dfs("ICN",["ICN"])
    paths.sort()
    
    return paths[0]