def solution(d, budget):
    
    # 최대한 많은 부서에게 지원 - sort()
    d.sort()
    count = 0
    
    for i in range(len(d)):
        if budget - d[i] >= 0:
            budget -= d[i]
            count += 1
        
    
    
    return count