def solution(sequence):
    answer = -(1e15) # 연속 펄스 부분 수열 합 max
    pulse1 = [-1,1]
    pulse2 = [1,-1]
    length = len(sequence)
    m1, m2 = 0, 0 # 부분 수열 누적합
    
    # sequence * pulse1, sequence * pulse2
    sp1 = [0] * length
    sp2 = [0] * length
    

    # sequence 길이만큼 펄스 수열 늘리기
    pulse1 = pulse1 * (length//2 + 1)
    pulse2 = pulse2 * (length//2 + 1)
    
    # 홀수라면
    if length % 2 == 1:
        pulse1 = pulse1[:length]
        pulse2 = pulse2[:length]
    
    
    # sp 구하기
    for i in range(length):
        sp1[i] = sequence[i] * pulse1[i] 
        sp2[i] = sequence[i] * pulse2[i] 
    
    # sp1, sp2돌면서 부분 수열 구하기
    for i in range(length):
        
        m1 += sp1[i]
        m2 += sp2[i]
        
        if m1 < 0 : 
            m1 = 0

        if m2 < 0 : 
            m2 = 0
    
        answer = max(m1,m2,answer)
    return answer