def solution(t, p):
    slist = []
    p_len = len(p)
    answer = 0

    for i in range(len(t)):
        s = t[i:i+p_len]
        if len(s) == p_len:
            result_s = int(s)
            slist.append(result_s)
    result_p = int(p)
    for i in slist:
        if result_p >= i:
            answer += 1
        

    return answer