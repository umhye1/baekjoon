def solution(n, m):
    answer = []
    gcd = sol1(n,m)
    answer.append(gcd)
    lcm = gcd *(n//gcd)*(m//gcd)
    answer.append(lcm)
    
    return answer

# 최대 공약수
def sol1(n,m):
    max_num = max(n,m)
    min_num = min(n,m)
    result = 1
    
    for i in range(2,max_num+1):
        if min_num < i :
            return result
        
        elif max_num % i == 0 and min_num % i == 0:
            result = i
            
    return result