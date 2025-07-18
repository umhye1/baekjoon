import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = [] # 앞으로 사용해야하는 수들 모아 놓은 리스트
result = [] # 출력 리스트
current = 1
possible = True

for target in sequence:
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print("NO")
