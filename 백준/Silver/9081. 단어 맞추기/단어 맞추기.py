# 문자열은 불변이기 때문에 직접 수정 불가 - 리스트 사용하기

def nextPermutation(arr):
    # 가장 큰 인덱스 찾기
    k = -1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1] :
            k=i
            break

    if k == -1:
        return
    
    # 교체할 인덱스 찾기
    l = -1
    for i in range(len(arr)-1,k,-1):
        if arr[i] > arr[k]:
            l = i
            break
    
    arr[k], arr[l] = arr[l], arr[k]
    # k+1부터 뒤집기
    # k 뒷부분은 항상 내림차순 상태이므로, 단순히 순서를 뒤집기만 하면 오름차순
    arr[k+1:] = arr[k+1:][::-1]



T = int(input())

for _ in range(T):
    tc = list(input())
    nextPermutation(tc)
    print(''.join(tc))
