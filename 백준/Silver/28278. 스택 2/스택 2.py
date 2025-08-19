# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()

for _ in range(n):
    m = list(map(int,sys.stdin.readline().strip().split()))
    if len(m) == 2 and m[0] == 1 :
        stack.append(m[1])
    
    if m[0] == 2 :
        if len(stack) == 0:
            print(-1)
        
        else :
            print(stack[-1])
            stack.pop()
    
    if m[0] == 3:
        print(len(stack))
    
    if m[0] == 4:
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    if m[0] == 5:
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[-1])
 