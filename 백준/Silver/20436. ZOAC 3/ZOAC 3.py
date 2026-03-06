str1, str2 = input().split()
str3 = input()

keyboard_left = [['q','w','e','r','t'],['a','s','d','f','g'],['z','x','c','v']]
keyboard_right = [['y','u','i','o','p'],['h','j','k','l'],['b','n','m']]

def time(x,y,a,b):
    return abs(x-a) + abs(y-b)

result = len(str3)

pos = {}


for row in range(len(keyboard_left)): # keyboard_left에 있는지 확인 후 딕셔너리에 넣기
    for col in range(len(keyboard_left[row])):
        pos[keyboard_left[row][col]] = (row,col,'L')

    
for row in range(len(keyboard_right)): # keyboard_right에 있는지 확인
    for col in range(len(keyboard_right[row])):
        if row == 0: c = col + 5    # y, u, i, o, p (5~9열)
        elif row == 1: c = col + 5  # h, j, k, l (5~8열)
        else: c = col + 4
        pos[keyboard_right[row][col]] = (row,c,'R')


lx, ly, _ = pos[str1]
rx, ry, _ = pos[str2]
result = len(str3)

for i in str3:
    x, y, hand = pos[i]
    
    if hand == 'L':
        result += abs(lx-x) + abs(ly-y)
        lx, ly = x, y

    else:
        result += abs(rx-x) + abs(ry-y)
        rx,ry = x,y

print(result)