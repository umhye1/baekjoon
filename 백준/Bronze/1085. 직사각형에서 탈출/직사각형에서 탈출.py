x,y,w,h = map(int, input().split())

a = w-x
d = h-y

if x>a:
    result_x = a
else :
    result_x = x

if y>d:
    result_y = d
else :
    result_y = y

if result_x>result_y:
    print(result_y)
else:
    print(result_x)
