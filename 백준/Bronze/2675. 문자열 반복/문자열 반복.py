n= int(input())

for i in range (n):
    num,s= input().split()
    num= int(num)
    for j in range(len(s)):
        print(s[j]*num, end="")
    print()