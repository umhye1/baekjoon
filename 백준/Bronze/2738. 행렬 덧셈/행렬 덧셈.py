N,M = map(int,input().split())

list1 = []
list2 = []


for i in range(N):
    data = list(input().split())
    list1.append(data)
    
for i in range(N):
    data = list(input().split())
    list2.append(data)

for i in range(N):
    for j in range(M):
        a = int(list1[i][j])
        b = int(list2[i][j])
        print(a+b, end=" ")
    print(end="\n")


