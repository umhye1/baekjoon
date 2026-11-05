import math

def solution(progresses, speeds):
    answer = []
    days = [0]*len(progresses) # 기능 개발 완료까지 걸리는 일 수 
    
    for i in range(len(progresses)):
        num = math.ceil((100 - progresses[i])/speeds[i] )
            
        days[i] = num
        
    max_day = days[0]
    count = 1 # 배포할 기능 수
    for i in range(1,len(progresses)):
        if days[i] <= max_day:
            count += 1
        else :
            answer.append(count)
            count = 1
            max_day = days[i]
    answer.append(count)
    return answer