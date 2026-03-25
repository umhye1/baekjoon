def solution(n, lost, reserve):
    # n : 전체 학생 수
    # lost : 체육복을 도난당한 학생들의 번호가 담긴 배열
    # reverse : 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
    # 체육수업을 들을 수 있는 학생의 최댓값?
    
    nlist = [1]*n
    num = n
    
    for i in reserve:
        nlist[i-1] += 1
    
    for i in lost :
        nlist[i-1] -= 1
    
    for i in range(len(nlist)):
        if nlist[i] == 0:
            # 앞 확인
            if i > 0 and nlist[i-1] >=2 :
                nlist[i-1] -= 1
                nlist[i] = 1
                
            elif i < len(nlist)-1 and  nlist[i+1]>=2:
                nlist[i+1] -= 1
                nlist[i] =1
    
    for i in nlist:
        if i == 0:
            num -= 1

    return num