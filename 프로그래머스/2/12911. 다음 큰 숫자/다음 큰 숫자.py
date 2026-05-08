import math

def solution(n):
    n_count = sol(n)
    
    m = n + 1
    
    while True:
        if sol(m) == n_count:
            return m
        m += 1

def sol(n):
    # 2진수 변환시 1 개수 같음
    count_one = 0
    
    while n > 0:
        if (n%2) == 1 :
            count_one += 1
            
        n//=2
            
    return count_one


# def solution(n):
#     # 1. 원래 숫자 n을 2진수로 바꿨을 때 1의 개수를 셉니다.
#     # bin(n)은 '0b1010' 형태의 문자열을 반환하고, .count('1')은 그중 '1'의 개수를 셉니다.
#     target_count = bin(n).count('1')
    
#     # 2. n보다 큰 숫자를 하나씩 확인합니다.
#     next_n = n + 1
#     while True:
#         # 다음 숫자의 2진수 1의 개수가 target_count와 같다면 정답!
#         if bin(next_n).count('1') == target_count:
#             return next_n
#         next_n += 1