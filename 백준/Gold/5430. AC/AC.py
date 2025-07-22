import sys 
from collections import deque 

# T : 테스트 케이스 개수
T  = int(sys.stdin.readline())

for i in range(T):
    # p : 수행할 함수
    p = list(map(str, sys.stdin.readline().rstrip()))

    # n : 배열에 들어있는 수의 개수
    n = int(sys.stdin.readline())
    testcase = sys.stdin.readline().rstrip()

    if testcase == "[]":
        raw = deque()

    else :
        raw = deque(map(int,testcase[1:-1].split(",")))

    isError= False
    isReversed = False

    for i in p:
        if i == "R":
            isReversed = not isReversed
        
        elif i == "D" :
            if len(raw)==0:
                isError = True
                break

            if isReversed:
                raw.pop()

            else :
                raw.popleft()

    if isError == True :
        print("error")
    
    else :
        if isReversed == True:
            raw.reverse()
        
        print(f"[{','.join(map(str,raw))}]")
