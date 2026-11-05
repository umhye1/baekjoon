def solution(progresses, speeds):
    answer = []
    
    # 배포일
    time = [(100-p+s-1)//s for p,s in zip(progresses,speeds)]
    
    max_day = time[0]
    count = 0 # 해당 날짜에 몇개의 기능을 같이 배포?
    
    for t in time :
        if t <= max_day : 
            count += 1 
        
        else :
            max_day = t
            answer.append(count)
            count = 1
            
    answer.append(count)
    return answer