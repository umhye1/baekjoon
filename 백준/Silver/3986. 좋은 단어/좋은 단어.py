import sys

n = int(sys.stdin.readline())
count = 0

for i in range(n):
    m = list(sys.stdin.readline().rstrip())
    stack = []
  
    for j in m:
        if stack and stack[-1] == j:
            stack.pop()
        else :
            stack.append(j)

    if not stack :
        count += 1

print(count)

        

