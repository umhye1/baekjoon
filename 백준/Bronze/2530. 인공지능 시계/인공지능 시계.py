a,b,c = map(int,(input().split()))
duck_sec = int(input())
c += duck_sec

while a>=24 or b>=60 or c>=60:
    if c >= 60 :
        c-=60
        b+=1
    elif b>=60:
        b-=60
        a+=1
    elif a>=24:
        a-=24

print(a,b,c)
