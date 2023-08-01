x, y = input().split()

rev = "".join(reversed(x)) # 빈 문자열에 복붙
rev1= "".join(reversed(y))

if(rev<=rev1):
    print(rev1)
else:
    print(rev)
