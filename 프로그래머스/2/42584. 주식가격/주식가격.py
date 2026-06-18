from collections import deque

#  queue로 구현
def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        x = q.popleft()
        count = 0
        
        for i in q:
            count += 1
                
            if i < x:
                break
            
        answer.append(count)
        
        
    
    return answer