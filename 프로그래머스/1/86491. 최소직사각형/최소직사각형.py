def solution(sizes):
    x,y=0,0
    for i in range(len(sizes)):
        sizes[i].sort()
        x = max(x,sizes[i][0])
        y = max(y,sizes[i][1])
    
    result = x*y
    
    
        
        
    return result