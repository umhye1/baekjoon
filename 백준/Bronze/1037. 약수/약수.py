import sys

n = int(sys.stdin.readline()) # 약수 개수
factor = list(map(int,sys.stdin.readline().split())) # 약수
factor.sort() # 정렬
length = len(factor) # 인덱스 구하기 위함

# 약수의 개수가 1개인 경우, 제곱수
if length == 1 :
    print(factor[0]*factor[0])
    
# 나머지의 경우, 처음과 마지막 약수를 곱하면 값이 나옴
else :
    print(factor[0]*factor[length-1])

