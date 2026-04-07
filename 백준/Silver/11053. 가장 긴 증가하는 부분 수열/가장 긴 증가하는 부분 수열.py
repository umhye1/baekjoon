N = int(input())
nlist = list(map(int, input().split()))

dp = [1]*len(nlist)
for i in range(len(nlist)):
    for j in range(i):
        if nlist[i]> nlist[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


