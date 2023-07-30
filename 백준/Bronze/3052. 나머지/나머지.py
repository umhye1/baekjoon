a=[0 for i in range(10)]
b=[0 for i in range(42)]
result =0

for i in range(10):
    n=int(input())
    a[i]=n%42
    b[n%42]+=1

for i in range(42):
    if (b[i]!=0):
        result+=1

print(result)