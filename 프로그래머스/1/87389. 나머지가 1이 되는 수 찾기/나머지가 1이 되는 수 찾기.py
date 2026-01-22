def solution(n):
    numlist = []
    for i in range(n,1,-1):
        if n % i == 1:
            numlist.append(i)
        
    
    return min(numlist)