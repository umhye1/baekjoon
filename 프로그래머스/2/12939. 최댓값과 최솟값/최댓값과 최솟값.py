def solution(s):
    arr = list(map(int, s.split()))
    min_arr = min(arr)
    max_arr = max(arr)
    
    return f"{min_arr} {max_arr}"