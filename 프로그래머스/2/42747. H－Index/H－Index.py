def solution(citations):
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        h = n - i                  # 현재 원소 c 이상인 논문 수
        if c >= h:                 # c가 그 수(h) 이상이면 h가 H-index
            return h
    return 0