import sys
from collections import deque

x = deque()

n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        x.appendleft(command[1])
    
    elif command[0] == "push_back":
        x.append(command[1])

    elif command[0] == "pop_front":
        if len(x) == 0:
            print(-1)
        else:
            print(x.popleft())
    
    elif command[0] == "pop_back":
        if len(x) == 0:
            print(-1)
        else:
            print(x.pop())
    
    elif command[0] == "size":
        print(len(x))

    elif command[0] == "empty":
        if len(x) == 0 :
            print(1)
        else: 
            print(0)

    elif command[0] == "front":
        if len(x) == 0 :
            print(-1)
        else:
            print(x[0])
    
    elif command[0] == "back":
        if len(x) == 0 :
            print(-1)
        else:
            print(x[len(x)-1])