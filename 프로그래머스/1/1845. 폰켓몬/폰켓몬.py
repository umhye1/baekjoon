from collections import Counter

def solution(nums):
    n = len(nums)//2
    
    answer = len(Counter(nums).most_common(n))
    return answer