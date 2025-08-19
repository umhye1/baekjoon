import sys
from collections import deque

k = int(sys.stdin.readline())
stack = deque()
sum = 0

for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0 :
        m = stack.pop()
        sum -= m
    
    else : 
        stack.append(n)
        sum += n

print(sum) 