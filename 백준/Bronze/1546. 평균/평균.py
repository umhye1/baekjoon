n=int(input())
m=list(map(int,input().split()))
max=max(m)
avg=0


for i in range(n):
    m[i]= m[i]/max*100
    avg+=m[i]

print(avg/n)