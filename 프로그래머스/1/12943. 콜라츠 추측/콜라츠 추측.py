def solution(num):
    answer = 0
    
    # 결과로 나온 수에 같은 작업을 1이될 때까지 반복
    while num != 1:
    
        # 입력된 수가 짝수라면 2로 나눔
        if num % 2 == 0:
            num //= 2
            answer += 1

        # 입력된 수가 홀수라면 3을 곱하고 1 더함
        elif num % 2 == 1:
            num *= 3
            num += 1
            answer += 1


        if answer == 500 and num != 1:
            return -1
    
    return answer