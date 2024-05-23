n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   
    num = sum(map(int,str(i)))
    num_sum = i +num

    if num_sum == n:
        print(i)
        break
    else:
        continue

if num_sum!=n:
    print(0)