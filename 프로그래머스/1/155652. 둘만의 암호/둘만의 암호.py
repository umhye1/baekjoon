# alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def solution(s, skip, index):
    answer = ''
    for i in skip:
        alphabet.remove(i)
    
    # 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줌
    # 인덱스 구하기
    
    for i in s:
        answer += alphabet[(alphabet.index(i)+index)%len(alphabet)]

    # index 만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아감
    # skip에 있는 알파벳은 제외하고 건너뜀
    return answer