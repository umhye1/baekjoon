T = int(input())
tlist = [0]*(T+1)
plist = [0]*(T+1) 
dp = [0]*(T+2)

for i in range(T):
    tlist[i+1] ,plist[i+1] = map(int, input().split())

# 끝에서 부터 처리가 쉬움
for i in range(T,0,-1):
    if i+tlist[i] > T+1:
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1], plist[i] + dp[i+tlist[i]])
 
print(max(dp))
