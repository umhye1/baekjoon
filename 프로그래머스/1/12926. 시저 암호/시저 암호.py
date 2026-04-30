def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == " " :
            answer += " " 
       #(현재 문자 번호 - 시작 문자 번호 + 밀기 정도) % 26 + 시작 문자 번호
        elif s[i].islower() == True:
            answer += chr((ord(s[i])-97 + n)% 26 + 97)
        
        elif s[i].isupper() == True:
            answer += chr((ord(s[i])-65 + n)% 26 + 65)
        
        
    return answer