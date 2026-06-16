def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    # 재귀 이용
    def dfs(index, t):
        nonlocal answer 
        
        if index == n :
            if target == t :
                answer += 1
            return
        
        dfs(index + 1, t - numbers[index])
        dfs(index + 1, t + numbers[index])
            
    dfs(0,0)
    
    return answer