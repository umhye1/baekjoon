

def solution(numbers):
    all_nums = set(range(10))
    missing_nums = all_nums - set(numbers)
    
    answer = sum(missing_nums)
    return answer