n= int(input())
n_array= list(map(int,input().split()))
n_array.sort()

m = int(input())
m_array=list(map(int,input().split()))


def binary_search(target,data):
    start=0
    end=len(data)-1

    while start<=end:
        mid= (start+end)//2

        if data[mid] == target:
            print(1)
            break
        
        elif data[mid] > target:
            end=mid-1
            continue

        elif data[mid] < target:
            start = mid+1
            continue      
   
    if start>end:
        print(0)



for i in range(m):

    binary_search(m_array[i],n_array)

