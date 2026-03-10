N = int(input())
nlist = []
max_dist = 0

for i in range(N):
    x,y = map(int, input().split())
    nlist.append((x,y))

t = 0

for i in range(N-1):
    t += abs(nlist[i][0] - nlist[i+1][0])+ abs(nlist[i][1]- nlist[i+1][1])


for i in range(1,N-1):
    before = nlist[i-1]
    current = nlist[i]
    after = nlist[i+1]

    original =(abs(before[0]-current[0])+ abs(before[1]- current[1])) + (abs(current[0]-after[0])+ abs(current[1]-after[1]))
    skip = (abs(before[0]-after[0])+ abs(before[1]- after[1]))

    max_dist = max(original-skip, max_dist)
    
    
print(t-max_dist)