R,S = map(int, input().split())
nlist = [['.']*S for _ in range(R)]
maplist = [list(map(str, input()))for _ in range(R)]
distlist = []
dist = 0

# 열 별로 계산 - X와 #의 거리
for i in range(S):
    x = -1
    y = 9999
    dist = 0

    for j in range(R):
        if maplist[j][i] == 'X':
            x = j
        
        if maplist[j][i] == '#' and y > j:
            y= j

    if x != -1:
        dist = y-x-1
        distlist.append(dist)

dist  = min(distlist) 

for i in range(R):
    for j in range(S):
        if maplist[i][j] == 'X':
            nlist[i+dist][j] = 'X'
        
        if maplist[i][j] == '#':
            nlist[i][j] = '#'

for rows in nlist:
    print("".join(rows))