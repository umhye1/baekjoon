h,m= map(int, input().split())
cook = int(input())

m +=cook

while m>=60:
    h+=1
    m-=60

if h>=24:
    h= h-24
print(h,m)