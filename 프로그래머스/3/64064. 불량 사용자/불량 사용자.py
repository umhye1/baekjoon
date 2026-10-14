import re

def solution(user_id, banned_id):
    count = 0
    answer = set()
    n = len(banned_id)
    m = len(user_id)
    
    # .로 바꾸기 
    for i in range(len(banned_id)) :
        banned_id[i] = banned_id[i].replace('*','.')
    
    # 방문 여부 
    visited = [False] * m
    
    def dfs(depth,path):
        if depth == n :
            answer.add(tuple(sorted(path)))
            return 
        
        for i in range(m):
            
            if not visited[i] and len(user_id[i]) == len(banned_id[depth]):
                if re.fullmatch(banned_id[depth], user_id[i]):
                    visited[i] = True
                    path.append(user_id[i])
                    dfs(depth + 1, path)
                    path.pop()
                    visited[i] = False
    
    dfs(0, [])
    
    answer = set(answer)
    count = len(answer)
            
                
    return count