bowl=[]
bowl=list(input())

result=10

for i in range(len(bowl)-1):

    if bowl[i] == bowl[i+1]:
        result +=5
    else:
        result +=10

print(result)
