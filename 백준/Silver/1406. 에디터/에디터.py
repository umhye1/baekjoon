import sys

# 커서를 기준으로 좌측은 left_stack, 우측은 right_stack에 담아두고,
# 명령어에 따라 두 스택 사이를 이동하거나 삽입/삭제하는 방식

l_letter = list(sys.stdin.readline().rstrip())
r_letter = []

num = int(sys.stdin.readline())

for i in range(num):
    command = sys.stdin.readline().split()
    if command[0] == "L" :
        # 비어있으면 false
        if l_letter :
            r_letter.append(l_letter.pop())
    
    elif command[0] == "D" :
        if r_letter :
            l_letter.append(r_letter.pop())

    elif command[0] == "B" :
        if l_letter :
            l_letter.pop()
    
    elif command[0] == "P" :
        l_letter.append(command[1])


print(''.join((l_letter)+(r_letter[::-1])))
        
    


