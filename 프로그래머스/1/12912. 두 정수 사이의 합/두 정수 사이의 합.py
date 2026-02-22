def solution(a, b):
    answer = 0
    
    if a == b :
        return a
    
    elif a>b:
        len_num = a - b
        
        for i in range(len_num+1):
            answer += (b+i)
    
        
    else :
        len_num = b - a
        for i in range(len_num+1):
            answer += (a+i)

    return answer