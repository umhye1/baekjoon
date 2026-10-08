from itertools import permutations 
from collections import deque

def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    
    elif op == "-":
        return num1 - num2
    
    else :
        return num1 * num2
    

def solution(expression):
    
    token = []
    cur_num = 0 
    answer = 0
    
    # 연산자 우선순위 경우의 수 구하기 
    operator = set()
    
    for i in expression:
        # 토큰화하기
        if i.isdigit() : # i가 숫자인 경우
            cur_num = cur_num * 10 + int(i)
            
        else: # 연산자인 경우 - 지금까지 더해놨던 cur_num, 연산자 다 올리기
            token.append(cur_num)
            token.append(i)
            operator.add(i)
            cur_num = 0
        
    token.append(cur_num)
    oplist = list(permutations(operator)) # 연산자 우선 순위 리스트 
    
    for oplist1 in oplist: # 연산자 우선 순위 리스트 조합 순서대로 순회하기
        tokenlist = deque(token) 
        
        for op in oplist1: # 연산자
            queue = deque() # op 선별을 위함
            
            # 큐
            while tokenlist:
                cur = tokenlist.popleft()
                
                if cur == op : # 현재 처리해야할 연산자
                    if queue :
                        num1 = queue.pop()
                        num2 = tokenlist.popleft() 
                        queue.append(calculate(num1, num2, op))

                else :
                    queue.append(cur)
                
            tokenlist = queue
            
        
        answer = max(abs(tokenlist[0]),answer)
    
    return answer