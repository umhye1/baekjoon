def solution(s):
    zero_count = 0
    count = 0
    
    answer = []
    
    while s!="1":
        # x의 모든 0 제거
        zero_count += s.count("0")
        s = s.replace("0","")
        
        # x의 길이 c를 2진법으로 표현한 문자열
        c = len(s)
        s = bin(c)[2:]
        
        count += 1
            
    answer.append(count)
    answer.append(zero_count)
    
    return answer