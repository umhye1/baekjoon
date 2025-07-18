import sys


num = int(sys.stdin.readline())
stack = [""]*num
right = 0
left =0

for i in range(num):
    stack[i] = str((sys.stdin.readline()).rstrip())
    is_vaild = True

    for j in range(len(stack[i])):
        if stack[i][j] == "(" :
            left +=1
        elif stack[i][j] == ")":
            if left == right :
                is_vaild = False
                break

            right +=1
            

    if is_vaild and left == right :
        print("YES")
    else :
        print("NO")
    left,right = 0,0