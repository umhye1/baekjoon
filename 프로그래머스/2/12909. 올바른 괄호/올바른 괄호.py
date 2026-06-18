def solution(s):
    answer = True
    count = 0
    
    if len(s)%2 != 0 :
        return False
    
    if s[0] == ")":
        return False
    
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        
        else : 
            if count == 0:
                return False
            
            count -= 1
            

    if count == 0:
        return True
    
    return False