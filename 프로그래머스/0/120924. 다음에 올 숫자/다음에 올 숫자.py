def solution(common):
    answer = []
    x = common[1] - common[0] # 공차인지 공비인지 확인
    y = common[2] - common[1]
    
    if x == y : # 공차
        answer = common[len(common)-1] + x
    else :
        x1 = common[0]
        r = (common[1])/x1
        answer = common[len(common)-1] *r
        
    return answer