import sys

num = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a.sort()


result = 0

# 정렬된 인덱스를 얻음
# 리스트 b는 정렬하면 안됨. 값이 큰 순서대로 a의 값과 대응시켜야함
# b 직접 정렬하지 않고 B에서 큰 값을 가진 인덱스 순서대로 정렬된 인덱스 목록 만들어야함

# b의 값을 기준으로 정렬, 인덱스를 정렬된 순서로 추출함
# 정렬할 수 없는 리스트의 정렬된 대응 만들기
b_sorted_idx = sorted(range(num),key=lambda i:b[i],reverse=True)


# b 인덱스 순서에 맞게 a 재배치
new_a = [0] * num
for i in range(num):
    new_a[b_sorted_idx[i]] = a[i]

result = sum(new_a[i] * b[i] for i in range(num))
print(result)
