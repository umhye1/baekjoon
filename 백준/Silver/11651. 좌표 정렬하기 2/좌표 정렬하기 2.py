import sys

num = int(sys.stdin.readline())
a = [0] * num
 
for i in range(num):
    a[i] = list(map(int,sys.stdin.readline().split()))

result = sorted(a , key=lambda point:(point[1], point[0]))

for x,y in result:
    print(x,y)