import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
nge = [-1] * n
stack = []

for i in range(n) :
   
    while stack and a[stack[-1]] < a[i]:
        nge[stack.pop()] = a[i]
    stack.append(i) # 아직 오큰수를 못 찾은 원소의 인덱스가 들어감 
        
        
print(*nge)
