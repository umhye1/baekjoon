# 이분탐색
def possible(mid, stones, k): # 가능 여부
    count = 0
    
    for i in range(len(stones)):
        if stones[i] < mid:
            count += 1
            if count >= k :
                return False
        
        else : 
            count = 0
    
    return True


def solution(stones, k):
    answer = 0 # 건널 수 있는 최대 사람 수
    
    left = 1
    right = max(stones)

    
    
    while left <= right :
        mid = ( left + right ) // 2
        
        if possible(mid, stones, k):
            answer = mid
            left = mid + 1
        
        else :
            right = mid - 1
        
    
    
    
    
    return answer