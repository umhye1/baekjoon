def solution(price, money, count):
    # 얼마 모자라는지
    answer = 0
    
    for i in range(1,count+1):
        money -= (price*i)
        
    if money < 0 :
        answer = abs(money)
    
    else : 
        answer = 0 
        
    return answer