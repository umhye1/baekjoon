def solution(info, n, m):
    
    # 중복 방지를 위한 저장소 - set으로 생성
    memo = {}
    
    def dfs(idx, sum_a, sum_b): # 인덱스, a 흔적 총합, b 흔적 총합
        
        # 종료 조건 - a, b 누적금액이 n,m 넘기면 -1로 종료
        if sum_a >= n or sum_b >= m:
            return -1
        
        # 종료 조건 - 길이만큼 다 돌았다면 a 누적 흔적 최솟값 리턴
        if idx == len(info):
            return sum_a
        
        
        # 이미 계산해 본 상태라면 저장된 값 바로 리턴
        if (idx, sum_a, sum_b) in memo : 
            return memo[(idx, sum_a, sum_b)]
        
        # a 선택
        a = dfs(idx + 1, sum_a + info[idx][0] , sum_b)
        
        # b 선택
        b = dfs(idx + 1, sum_a, sum_b + info[idx][1])
        
        
        # 둘다 -1인 경우 : -1
        if a == -1 and b == -1:
            answer = -1
        
        # a만 -1인 경우 : b
        elif a == -1 and b != -1 :
            answer = b
        
        # b만 -1인 경우 : a
        elif a != -1 and b == -1:
            answer = a
        
        # 둘다 값이 있으면 둘 중 작은 값으로 
        else:
            answer = min(a,b)
            
        
        # 메모이제이션에 넣기 
        memo[(idx, sum_a, sum_b)] = answer
    
        return answer
        
    return dfs(0,0,0)
