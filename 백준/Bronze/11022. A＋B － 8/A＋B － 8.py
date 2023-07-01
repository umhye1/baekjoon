n= int(input())

for i in range(n):
    x,y= input().split()
    x = int(x)
    y = int(y)
    print("Case #"+str(i+1)+":",x,"+",y,"=",str(x+y))