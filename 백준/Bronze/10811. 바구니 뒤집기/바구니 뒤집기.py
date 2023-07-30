n,m=map(int,input().split())

a=list()
b=0
for i in range(n):
    a.append(i+1)

for x in range(m):
    i,j= map(int,input().split())
    while i<j:
        b= a[j-1]
        a[j-1]=a[i-1]
        a[i-1]=b
        j-=1
        i+=1
        
        
for x in range(n):
    print(a[x],end=" ")

