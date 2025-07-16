import sys

num = int(sys.stdin.readline())
a=[0]*num

for i in range(num):
    a[i] = list(map(int,sys.stdin.readline().split()))

a.sort()

for x,y in a:
    print(x,y)