word= str(input())
a=[-1 for i in range (26)]

for i in range (len(word)):
    b = ord(word[i])-97 
    if(a[b]==-1):
        a[b]=i

for i in range(26):
    print(a[i], end=" ")