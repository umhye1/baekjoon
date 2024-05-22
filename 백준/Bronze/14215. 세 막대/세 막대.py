a,b,c = map(int,input().split())
x=[a,b,c]

if max(x)<sum(x)-max(x):
    print(sum(x))
else:
    x.remove(max(x))
    m = sum(x)-1
    x.append(m)
    print(sum(x))