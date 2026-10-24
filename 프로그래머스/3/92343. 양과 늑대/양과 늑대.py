from collections import deque
    
def solution(info, edges):
    
    # bfs
    def bfs(start):
        q = deque()
        sheep, wolf = 0,0
        answer = 0
        
        if info[start] == 0:
            sheep += 1
            
        if info[start] == 1:
            wolf += 1
        
        
        q.append((start, sheep, wolf, graph[start]))
        answer = max(sheep, answer)
        
        while q:
            cur, cur_sheep, cur_wolf, nxt_nodes1 = q.popleft()
            
            for nxt in nxt_nodes1: # 다음에 갈 수 있는 노드들
                
                nxt_sheep = cur_sheep
                nxt_wolf = cur_wolf
                
            
                if info[nxt] == 0: # 양
                    nxt_sheep += 1

                if info[nxt] == 1: # 늑대
                    nxt_wolf += 1
                    
                if nxt_sheep <= nxt_wolf : # 이동 불가
                    continue
                
                answer = max(nxt_sheep, answer)
                
                # 다음에 갈 수 있는 노드 갱신
                nxt_nodes2 = [n for n in nxt_nodes1 if n != nxt] + graph[nxt]
                q.append((cur, nxt_sheep, nxt_wolf, nxt_nodes2))
                    

        return answer
        

    
    # 그래프 연결
    graph = [[] for i in range(len(info))]
    
    for x,y in edges:
        graph[x].append(y)
    
    
    return bfs(0)