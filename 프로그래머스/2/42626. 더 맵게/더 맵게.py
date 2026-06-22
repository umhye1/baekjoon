import heapq

def solution(scoville, K):
    answer = 0
    # 스코빌 지수가 가장 낮은 두 개의 음식을 섞어서 새로운 음식을 만든다
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    
    heapq.heapify(scoville)
    
    # 가장 앞에 있는게 결국 최소값이므로, 최소값이 k보다 작은지 확인하면 됨
    while scoville[0] < K:
        if len(scoville) == 1 :
            return -1
        
        min_food1 = heapq.heappop(scoville)
        min_food2 = heapq.heappop(scoville)
        
        new_scoville = min_food1 + min_food2 *2
        
        heapq.heappush(scoville,new_scoville)
        answer += 1
    
    
    return answer