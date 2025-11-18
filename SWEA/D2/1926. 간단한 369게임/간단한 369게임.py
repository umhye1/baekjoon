n = int(input())
result = []

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, n+1):
    count = 0
    num_str = str(i)
    
    for j in num_str:
        if j in ('3','6','9'):
            count += 1

    if count > 0:
        result.append("-"*count)
    else :
        result.append(num_str)

print(" ".join(result))
    