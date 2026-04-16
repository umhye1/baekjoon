def solution(d, budget):
    d_sort = sorted(d)
    answer = 0
    
    for i in d_sort:
        if budget - i >= 0:
            budget -= i
            answer += 1
    return answer