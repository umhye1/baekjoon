n,m = map(int,( input().split()))
d = []
b = []

for i in range(n):
    d.append(input())

for j in range(m):
    b.append(input())

d = set(d)
b = set(b)
answer = sorted(d&b)
print(len(answer))
print('\n'.join(answer))