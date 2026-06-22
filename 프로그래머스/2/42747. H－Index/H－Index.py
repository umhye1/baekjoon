def solution(citations):
    answer = 0
    # H-index : 발표한 논문 n편 중, h번 이상 인용된 논문이 h 편 이상.
    # 나머지 논문이 h번 이하 인용되었을 때의 최댓값
    h_index = []
    citations.sort(reverse = True)
    

    for idx, c in enumerate(citations):
        # h = 위에서부터 지금까지 세어 내려온 논문의 개수(순위) = idx +1
        if c >= idx + 1:
            answer = idx + 1
        
    return answer