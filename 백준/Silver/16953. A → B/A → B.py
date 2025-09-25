import sys
from collections import deque

A,B = map(int, sys.stdin.readline().split())
count =1
while B!=A:

    if B < A:
        count = -1
        break

    if B%2==0:
        B//=2

    elif B%10 == 1:
        B = (B-1)//10
    
    else:
        count = -1
        break
    count += 1

print(count)
    
