N = int(input())
cow = [-1]*11
count = 0

for i in range(N):
    num,location = map(int,input().split())
    if cow[num] == -1:
        cow[num] = location

    elif cow[num] != location:
        count += 1
        cow[num] = location

print(count)

