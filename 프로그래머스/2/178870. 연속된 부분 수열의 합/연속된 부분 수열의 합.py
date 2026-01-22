def solution(sequence, k):
    
    answer = []
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    
    for right in range(len(sequence)):
        current_sum += sequence[right]
        
        while current_sum > k :
            current_sum -= sequence[left]
            left += 1
        
        if current_sum == k :
            current_len = right - left + 1
            
            if current_len < min_len:
                min_len = current_len
                answer = [left,right]
            
        
    
    return answer