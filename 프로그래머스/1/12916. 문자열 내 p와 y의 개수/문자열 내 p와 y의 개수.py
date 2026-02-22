def solution(s):
    s = s.lower()
    pnum = s.count('p')
    ynum = s.count('y')
    if pnum == ynum:
        return True
    
    return False