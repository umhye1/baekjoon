a=[0 for i in range(30)]

for i in range(28):
    n= int(input())
    a[n-1]=1

b=a.index(0)        
print(b+1)
print(a.index(0,b+1,30)+1)