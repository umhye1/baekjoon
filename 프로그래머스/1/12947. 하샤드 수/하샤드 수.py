def solution(x):
    answer = False
    
    # x가 자릿수 합으로 나누어 떨어져야함
    xlist = list(str(x))
    
    # 자릿수 합 = num
    num = 0 
    for i in range(len(xlist)):
        num += int(xlist[i])
    
    if x % num == 0:
        answer = True
        
    return answer