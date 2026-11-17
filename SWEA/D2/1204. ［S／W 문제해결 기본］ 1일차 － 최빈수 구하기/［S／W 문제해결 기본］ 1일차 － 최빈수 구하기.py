# 최빈수는 특정 자료에서 가장 여러 번 나타나는 값
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.
# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수
                       

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    dict_score = {}

    for i in score:
        dict_score[i] = dict_score.get(i,0) + 1

    ans = max(dict_score, key=lambda x: (dict_score[x], x))
    print(f"#{n} {ans}")
    
