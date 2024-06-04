n = int(input())
x=list()

for i in range(n):
    m= int(input())
    x.append(m)

x.sort()

for i in range(n):
    print(x[i])