
def solution(seoul):
    dir = 0
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            dir = i
            break
    
    
        
            
    
    answer = f"김서방은 {dir}에 있다"
    
    return answer