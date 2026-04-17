def solution(s):
    answer = 0
    # x = 첫 글자 
    x = s[0]
    same_count = 0
    nsame_count = 0
    
    # 왼 -> 오. x와 x가 아닌 다른 글자들이 나온 횟수를 count
    while len(s) > 0:
        for i in range(len(s)):
            if s[i] == x:
                same_count += 1
            if s[i] != x :
                nsame_count += 1

            # 처음으로 두 횟수가 같아지는 순간 멈춤 ->문자열 분리
            if same_count == nsame_count:
                if i!= len(s)-1:
                    s = s[i+1:]
                    x = s[0]
                else :
                    s = ""
                
                answer += 1
                same_count = 0
                nsame_count = 0

                break
                
        if same_count != nsame_count :
            answer += 1
            break
        
    # s에서 분리한 문자열을 빼고 남은 부분에 대해 과정 반복 (count 초기화)
    # 남은 부분 없으면 종료
    # 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면 지금 까지 읽은 문자열 분리, 종료
    
    return answer