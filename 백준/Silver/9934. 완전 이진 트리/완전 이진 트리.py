# inorder 중위 순회 : left - root - right

K = int(input())
nlist = list(map(int, input().split()))
mlist = [[] for _ in range(K)]

def make_tree(arr, depth):

    if len(arr) != 1 :
        mid = len(arr)//2
        mlist[depth].append(arr[mid])

        make_tree(arr[:mid], depth +1)
        make_tree(arr[mid+1:], depth+1)
        
    else :
        mlist[depth].append(arr[0])
        return

make_tree(nlist,0)

for rows in mlist:
    print(*rows)