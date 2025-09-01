import sys

# 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다.

n = int(sys.stdin.readline())
building = []
stack = []

for i in range(n):
    m = int(sys.stdin.readline())
    building.append(m)

count = 0 

for h in building:  # 건물 높이 하나씩 읽기
    while stack and stack[-1] <= h:
        stack.pop()   # 나보다 낮으면 못 본다 → 제거

    count += len(stack)  # 스택에 남아 있는 건물들이 나를 볼 수 있음
    stack.append(h)
    

print(count)
