# 집들이 원형이 아니라 직선으로 있다고 생각해보자
# i번째 집에 도착했을 때 
    # i : 바로 전 집(i-1)은 털 수 없으므로, i-2번째 집까지의 최댓값 + i번째 집의 돈
    # i x : i-1번째 집까지의 최댓값 그대로 유지
    
def rob_line(sub_money):

    length = len(sub_money)
    if length == 1:
        return sub_money[0]
    
    max_money = [0]*length
    # max_money[i] = i번째 집까지 고려했을 때 훔칠 수 있는 최대 금액
    
    max_money[0] = sub_money[0]
    max_money[1] = max(sub_money[0],sub_money[1])
    for i in range(2,length):
        max_money[i] = max(max_money[i-1], max_money[i-2] + sub_money[i])
    
    return max_money[length-1]
    
def solution(money):
    
    # 첫번째 집 터는 경우 - 마지막 집 x -> 0 ~ N-2
    sub_money = money[:-1]
    m = rob_line(sub_money)
    
    
    # 첫번째 집 안 텀 - 마지막 집 o -> 1 ~ N-1
    sub_money = money[1:]
    n = rob_line(sub_money)
    
    return max(m,n)
         
        
            
            
            
    return answer