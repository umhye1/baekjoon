n = int(input())
nlist = list(map(int, input().split()))

# 누적값의 최소값 저장
min_sum = 0
current_sum = 0
max_sum = -float('inf')

for i in nlist:
    current_sum += i

    if current_sum - min_sum > max_sum:
        max_sum = current_sum -min_sum
    
    if current_sum < min_sum:
        min_sum = current_sum

print(max_sum)