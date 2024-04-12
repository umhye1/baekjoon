result =[]
t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())
    if a==b==c : 
        result.append(a*1000+10000)
    elif a==b or c==a:
        result.append(1000+ a*100)
    elif b==c :
        result.append(1000+ b*100)
    else :
        result.append(max(a,b,c)*100)
    
print(max(result))