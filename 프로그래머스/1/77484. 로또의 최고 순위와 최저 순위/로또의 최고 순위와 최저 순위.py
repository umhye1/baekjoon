rank = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}
def solution(lottos, win_nums):
    answer = []
    min_count = 0 # 최저 순위
    zero_count = 0 # 최고 순위
    
    for value in lottos:
        if value in win_nums:
            print(value)
            min_count += 1
        
        if value == 0:
            zero_count += 1
    
    max_count = min_count + zero_count
        
    answer = [rank[max_count], rank[min_count]]
    return answer

