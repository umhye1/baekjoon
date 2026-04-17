def solution(n):
    answer = 0
    nlist = []
    
    # 3진법 변환
    while n > 0 :
        if n%3 == 0 :
            n//=3
            nlist.append(0)
            
        elif n%3 == 1:
            n//=3
            nlist.append(1)
        
        else :
            n//=3
            nlist.append(2)
        
    # 앞뒤 뒤집기
    n_len = len(nlist)
    for i in range(n_len):
        answer += nlist[n_len-i-1]*(3**i)
    
    return answer