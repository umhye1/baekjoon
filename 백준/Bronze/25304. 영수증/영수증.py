X = int(input())
n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    X -= a*b

if X==0:
    print("Yes")
else : 
    print("No") 

