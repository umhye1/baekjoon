n,m =map(int,input().split()) #n = 바구니 수, m= 공 넣는 횟수
a=[0 for x in range(n)]

for x in range(m):
    i,j,k= map(int,input().split()) # i~j까지 k번 넣기

    for y in range(j-i+1):
        a[i+y-1]=k
      
 
for x in range(n):
    print(a[x], end=' ') 

