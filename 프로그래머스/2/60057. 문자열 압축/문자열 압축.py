def find(n, s): # n은 현재 단위 값
    
    cur_unit = s[:n] # n만큼 끊기(초기값)
    unit_count = 1 # 동일한 단위 몇개 있는지 확인용
    count = 0
    
    for i in range(n, len(s), n): # n씩 건너 뜀
        nxt_unit = s[i:i+n]
        
        # 동일한 단위가 반복해서 나오는 경우
        if cur_unit == nxt_unit: 
            unit_count += 1 # 동일한 단위 몇개 있는지 count
            
        # 동일한 단위가 반복해서 나오지 않는 경우 (cur_unit != nxt_unit)
        else :
            
            if unit_count == 1: # 동일한 단위가 없는 경우
                count += n # 문자열 길이만큼 더해주기
            
            else :
                count += (len(cur_unit) + len(str(unit_count))) # 동일한 단위가 있으면 - 숫자 + 문자열 길이
            cur_unit = nxt_unit
            unit_count = 1
            
    if unit_count > 1:
        count += (len(cur_unit) + len(str(unit_count)))
    
    else : 
        count += len(cur_unit)
        
    return count
                
           
         

def solution(s):
    
    answer = 10000
    
    if len(s) == 1 :
        return 1
    
    for i in range(1, (len(s)//2) + 1):
        ans = find(i,s)
        answer = min(answer, ans)
            
    return answer