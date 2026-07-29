# 입력 변환 → 상태/인덱스 정의 → 조건을 작은 함수로 분리 → 예외 케이스 확인
def solution(s):
    numlist = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    
    for index, value in enumerate(numlist, start = 0):
        idx = str(index)
        s = s.replace(value,idx)
    
    s = int(s)
    return s