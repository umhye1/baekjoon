def solution(A,B):
    sort_a = sorted(A)
    sort_b = sorted(B,reverse=True)
    answer = 0
    
    for i in range(len(sort_a)):
        answer += sort_a[i]*sort_b[i]
            
            
    return answer