new_num = ['1','2','4']
def solution(n):
    
    answer = '' 
    while n > 0:
        r = n % 3
        n //= 3
        
        if r == 0 : # 나머지가 0일 경우
            answer += new_num[2]
            print("나머지 0" ,answer)
            
            # 3의 경우 ) 3//3 = 1로 1이 남음 -> n-1해주기
            n -= 1
            
        else : # 나머지 있을 경우
            answer += new_num[r-1]
            print("나머지 있" ,answer)
    

    return answer[::-1]