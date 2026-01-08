# 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자
def solution(s):
    answer = []
    words = s.split(" ")
    
    for w in words:
        if w:
            answer.append(w.capitalize())
        else:
            answer.append(w)
    
    return " ".join(answer)