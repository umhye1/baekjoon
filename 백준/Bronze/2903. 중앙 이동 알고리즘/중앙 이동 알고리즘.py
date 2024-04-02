N = int(input())
result =0
side = 2
for i in range(N):
    side = 2*side-1
    result = side*side
print(result)