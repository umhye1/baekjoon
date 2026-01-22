def solution(n):
    answer = 0
    left = 1
    right = 1
    current_sum =1
    
    while right <= n:
        if current_sum < n :
            right += 1
            current_sum += right
        
        elif current_sum == n :
            answer += 1
            current_sum -= left
            left += 1
        else :
            current_sum -= left
            left += 1
        
    return  answer