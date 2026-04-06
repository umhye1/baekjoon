N = int(input())
nlist = list(map(int,input().split()))

# nlist 복사, 혼자 있을 때가 최소합이므로 복사함
dp = nlist[:]

# 다 저장할 필요 없고 그냥 max값만 찾아서 갱신시키기로 음
for i in range(len(nlist)):
    for j in range(i):
        if nlist[i] > nlist[j]:
            dp[i] = max(dp[i], dp[j]+nlist[i])

print(max(dp))
