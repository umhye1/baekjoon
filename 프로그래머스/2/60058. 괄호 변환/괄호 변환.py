def solution1(w): #분할
    count = 0 
    
    # w를 문자열 u,v로 나눔. u는 최소 균형잡힌 괄호 문자열일 것
    for i in range(len(w)):
        
        # 균형잡힌 괄호 문자열 확인
        if w[i] == '(':
            count += 1
            
        elif w[i] == ')':
            count -= 1
        
        if count == 0 :
            return w[:i+1], w[i+1:] 
        
        
def solution2(w): # 올바른 괄호 판별
    count = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
            
        if w[i] == ')' :
            count -= 1
        
        if count < 0 :
            return False # 올바른 괄호 아님, 균형 잡힌 괄호
    
    return True # 올바른 괄호
        

def solution(p):
    if p == '':
        return p
    
    answer = ''
    u,v =solution1(p)
    
    if solution2(u) == True:     
        return u + solution(v)
    
    
    else :
        answer += '('
        answer += solution(v)
        answer += ')'
        
        # 괄호 뒤집기
        
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else : 
                answer += '('
    
    return answer

