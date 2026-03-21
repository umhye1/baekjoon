# 정렬 중에 가장 빠른 거 - binary search이용
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int,input().split()))

# nlist sort함
nlist.sort()

def search(arr, tar):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == tar:
            print(1)
            return mid

        elif arr[mid]< tar:
            left = mid +1
        
        else:
            right = mid-1
    print(0)
    return -1


for i in range(m):
    search(nlist,mlist[i])
