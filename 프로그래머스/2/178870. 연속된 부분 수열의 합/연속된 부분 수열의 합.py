def solution(sequence, k):
    answer = []
    # 투포인터
    # total < k right를 +=
    # total > k left -=

    min_length = 1000000000000000
    left, right = 0, 0
    total = sequence[0]
    
    while left <= right and right < len(sequence):
        
        if total == k:
            length = right - left + 1 
            
            if length < min_length: # 더 짧은거 받기
                min_length = length
                answer = [left, right]
                
        if total < k:
            right += 1
            
            if right >= len(sequence):
                break
            
            total += sequence[right]
        
        else :
            total -= sequence[left]
            left += 1
            
    return answer