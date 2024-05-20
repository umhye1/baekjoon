import math

n,k = map(int, input().split())
d=list()    

for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0:
        d.append(i)
        if i != n // i:
            d.append(n//i)

d.sort()

if len(d)<k:
    print("0")

else:
    print(d[k-1])

