t = int(input())
a=0
b=0

for i in range(t):
    data = input()
    if data =="1":
        a+=1
    elif data =="0":
        b+=1

if a<b:
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")
