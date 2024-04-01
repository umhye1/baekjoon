# B진법 수 N

N,B = map(str,input().split())

B = int(B)
N = list(N)
result =0
number ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for i in range(len(N)):
   
    for j in range(len(number)):
        
        if number[j] == N[i]:
            result +=B**(len(N)-i-1)*(j)


print(result)
