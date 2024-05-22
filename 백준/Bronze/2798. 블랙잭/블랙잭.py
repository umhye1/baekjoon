n,m= map(int,input().split())
#여러 개의 값을 공백으로 입력받을 때 리스트에 넣기
arr = list(map(int,input().split()))
arr.sort()

result=[]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = arr[i]+arr[j]+arr[k]
            if sum<=m:
                result.append(sum)


while True:
    if max(result)<=m:
        print(max(result))
        break

    else:
        result.remove(max(result))
        continue