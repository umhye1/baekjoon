import sys
from itertools import combinations

while True :
    nums = list(map(int, sys.stdin.readline().split()))

    if nums[0] == 0 :
        break

    k = nums[0]
    s = nums[1:]

    for i in combinations(s,6):
        print(" ".join(map(str,i)))
    
    print()