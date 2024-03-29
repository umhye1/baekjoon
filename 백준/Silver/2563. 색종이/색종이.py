data = [[0 for j in range(100)]for i in range(100)]
count=0

N = int(input())

for i in range(N):
    x,y = list(map(int, input().split()))
    
    for a in range(x,x+10):
        for b in range(y,y+10):
            data[a][b] = 1


for i in (data):
    count+=i.count(1)

print(count)