import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1) # dp[x] = x를 1로 만드는 최소 연산 수 

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1 # i를 -1한 경우 : 연산 1번 추가

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) 

print(dp[n])
