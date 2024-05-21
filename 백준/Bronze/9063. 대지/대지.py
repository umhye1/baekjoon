n= int(input())
x =[]
y =[]

for i in range(n):
    a,b= map(int, input().split())
    x.append(a)
    y.append(b)
    
new_x = max(x)-min(x)
new_y = max(y)-min(y)
result =new_x * new_y
print(result)

