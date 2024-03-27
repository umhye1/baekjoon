a,b,c = map(int, input().split())

if a==b==c :
    price = 10000 + a*1000
    print(price)

elif (a==b) |(b==c) :
    price = 1000 + b*100
    print(price)

elif a==c :
    price = 1000 + a*100
    print(price)

else :
    m = (max(a,b,c))
    price = m*100
    print(price)
