from collections import deque

def check(maplist, start, target): # 갈 수 있는지 확인
    if start == target:
        return True
    
    visited ={start} # set사용
    queue = deque()
    queue.append(start) # 다음에 갈 노드 넣기
    
    while queue:
        cur = queue.popleft()
        if cur == target :
            return True
        
        for nxt,cost in maplist[cur]: # 현재 노드랑 연결되어있는 노드 확인 (갈 수 있는 곳)
            if nxt == target :
                return True
            if nxt not in visited :
                visited.add(nxt) # 방문 처리
                queue.append(nxt) # 다음에 갈 노드 설정
    
    return False
        
def solution(n, costs):
    answer = 0
    maplist = [[] for i in range(n)] 
    print(maplist)
    costs.sort(key = lambda x:x[2]) # 비용순서대로 정렬
    
    
    for a,b,cost in costs:
        if not check(maplist, a,b): # 아직 안 지나갔으면
            maplist[a].append((b,cost)) 
            maplist[b].append((a,cost))
            answer += cost # 정렬이 가격순으로 되어있어서 그냥 더해도 됨
    
    
    return answer