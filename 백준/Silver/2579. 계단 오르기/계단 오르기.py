import sys

n = int(sys.stdin.readline())
stair = [0] * (n + 1)
for i in range(1, n + 1):
    stair[i] = int(sys.stdin.readline())

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = stair[1]
if n >= 2:
    dp[2] = stair[1] + stair[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

print(dp[n])
