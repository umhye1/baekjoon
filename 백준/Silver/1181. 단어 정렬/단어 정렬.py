import sys

num = int(sys.stdin.readline())
word = [""] * num

# 단어 입력 받기
for i in range(num):
    word[i] = sys.stdin.readline().rstrip()

# 길이가 짧은 것 부터, 길이가 같으면 사전 순으로, 중복 제거해서 출력
# 중복 제거 : set()

# lambda = 이름 없는 함수. 
# def add(x, y):
#   return x + y

# lambda x, y: x + y
# lambda 매개변수 : 반환값
# 파이썬은 튜플 기준으로 정렬, (문자열 길이, 문자열)

new_word = sorted(set(word),key=lambda i:(len(i),i))
print('\n'.join(map(str, new_word)))