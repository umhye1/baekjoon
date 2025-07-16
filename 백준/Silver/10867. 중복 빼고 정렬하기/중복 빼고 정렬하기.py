import sys

num = int(sys.stdin.readline())

result = list(map(int, sys.stdin.readline().split()))
result = set(result)

new_result = sorted(result, key=lambda x:x)
print(' '.join(map(str,new_result)))