# n : 지점 개수
# s : 출발지점
# a : A의 도착지점
# b : B의 도착지점
# fares : 지점 사이의 예상 택시요금
# s에서 출발해서 각각의 도착 지점까지 택시, 최저 예상 택시요금?
# 만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.
# fares[0] = 지점 1
# fares[1] = 지점 2
# fares[2] = 지점 1,2 사이의 요금

# 그래프 인접리스트로 연결하고, 흠... bfs 돌리면될거같긴한데 
# 합승하는 조건 : 각자 이동 > 합승 -> min_cost로 비교하면 될 듯?


import heapq

def solution(n, s, a, b, fares):
    answer = 0
    

    # 인접리스트 - 지점 연결 구하기  
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    
    for node1, node2, fare in fares: 
        graph[node1].append((node2, fare))
        graph[node2].append((node1, fare))
        

    
    
    # bfs
    def taxi(start,finish,graph):
        q = []
        heapq.heappush(q,(0, start))
        
        # 리턴할 최단거리 그래프
        INF = int(1e9)
        distances = [INF] * (n+1)
        distances[start] = 0
        
        while q:
            cur_fare, cur = heapq.heappop(q) 
            
            if distances[cur] < cur_fare : # 현재까지의 비용보다 현재 비용이 크면 무시
                continue
            
            for nxt,nxt_fare in graph[cur]:
                cost = cur_fare + nxt_fare
                
                if cost < distances[nxt]: # distances[nxt]에 있는 비용보다 현재 구한 비용이 더 저렴한 경우 최소 갱신
                    distances[nxt] = cost
                    heapq.heappush(q,(cost,nxt))
        
        return distances
        
        
    cost_s = taxi(s,n,graph) # s -> 모든 지점 가는 경우
    cost_a = taxi(a,n,graph) # a -> 모든 지점 가는 경우
    cost_b = taxi(b,n,graph) # b -> 모든 지점 가는 경우
    
    min_cost = int(1e9)
    
    for i in range(1,n+1):
        cost  = cost_s[i] + cost_a[i] + cost_b[i]
        
        if min_cost > cost:
            min_cost = cost
    
    
    
    return min_cost