import sys
from collections import deque

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))

result = [0]*n
stack  = []

for i in range(n):
    current = tower[i]

    while stack and stack[-1][1] < current:
        stack.pop()
    
    if stack :
        result[i] = stack[-1][0] + 1

    
    stack.append((i,current))

print(*result)