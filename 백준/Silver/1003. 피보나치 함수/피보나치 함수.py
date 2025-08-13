# DP : 다이나믹 프로그래밍
# 1. Top-down - 메모이제이션 사용 : DP에서 계산된 결과를 저장해두고 필요할 때 다시 사용하여 중복 계산을 피하는 기법 
# 2. Bottom-up - for 반복문 사용 : 재귀 호출이 없어서 파이썬의 재귀 깊이 제한이나 호출 스택 부담이 없음 
import sys

def fibonacci(num):
    cnt = [0]*(num+2)

    cnt[0] = [1,0]
    cnt[1] = [0,1]

    for i in range(2,num+1):
        cnt[i] = (cnt[i-1][0] + cnt[i-2][0], cnt[i-1][1] + cnt[i-2][1] )
        
    return cnt[num]
        

t = int(sys.stdin.readline()) # t: 테스트케이스 개수
for _ in range(t):
    n = int(sys.stdin.readline())
    print(*fibonacci(n))
    
