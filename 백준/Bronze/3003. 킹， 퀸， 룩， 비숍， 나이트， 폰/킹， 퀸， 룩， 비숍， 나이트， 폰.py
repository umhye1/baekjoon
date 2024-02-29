a =[1,1,2,2,2,8]

# 리스트 입력받기
# 공백으로 구분, 리스트로 넣는다
data = list(map(int,input().split()))

for i in range(6):
    print(a[i] - data[i], end=' ')