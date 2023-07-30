
n,m =map(int,input().split()) #n = 바구니 수, 번호 수.  m= 바꾸는 횟수
a=list()
for x in range(n):
    a.append(x+1)

for x in range(m):
    i,j= map(int,input().split()) # i번이랑 j번 안에있는 n번의 공 교환하기
    b= a[i-1]
    a[i-1]=a[j-1]
    a[j-1]=b
      
 
for x in range(n):
    print(a[x], end=' ') 
