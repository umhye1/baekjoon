# 최대공약수 구해서 
# 모든 간격이 일정해지려면, 기존 간격들을 어떤 일정한 수로 정확히 나눌 수 있어야 합니다.
# 즉, 간격들을 모두 나눌 수 있는 **최대공약수(GCD)**를 찾아야 합니다
import sys
import math

n = int(sys.stdin.readline())
tree = [int(sys.stdin.readline()) for _ in range(n)]

# 간격
distance = [tree[i+1] - tree[i] for i in range(n-1)]

# 간격들의 최대공약수 구하기
gcd_val = distance[0]

for i in range(1, len(distance)):
    gcd_val = math.gcd(gcd_val,distance[i])

new_tree = 0
for i in distance:
    new_tree += (i //gcd_val) -1

print(new_tree) 

