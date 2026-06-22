# 문자열 특성 이용하기 - 30과 3비교 위해 문자열*3정도해보기
def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    
    numbers.sort(key = lambda x : x*3, reverse=True)
    answer = "".join(numbers)


    if answer[0] == "0":
        return "0"
    
    return answer
        