def solution(s):
    answer = []
    
    for i in range(len(s)):
        num = 100001
        
        for j in range(i):
            
            if s[j] == s[i]:
                if num >= i-j:
                    num = i-j
        
        if num != 100001 :
            answer.append(num)
        else:
            answer.append(-1)
            
    return answer