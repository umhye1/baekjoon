def binary_search(array,target):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right)//2
    
        if array[mid] == target:
            print(1)
            return mid
        elif array[mid]<target:
            left = mid+1

        else:
            right = mid-1
    print(0)
    return -1

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
    binary_search(a,b[i])


