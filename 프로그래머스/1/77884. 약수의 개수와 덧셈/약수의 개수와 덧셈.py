def solution(left, right):
    # 약수의 개수가 짝수면 더하기
    # 약수 개수가 홀수면 뺌
    answer = 0 
    
    for i in range(left, right+1):
        if num(i) % 2 == 0:
            answer += i
            
        else :
            answer -= i
            
    return answer

def num(a):
    count = 0
    
    for i in range(1,a+1):
        # 나누어 떨어지면 i는 a의 약수
        if a % i == 0 :
            count += 1
        
    return count
            