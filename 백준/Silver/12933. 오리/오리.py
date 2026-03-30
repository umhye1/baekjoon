duck = str(input())
visited= [False]*len(duck)
count = 0

while False in visited :

    if (len(duck) % 5) != 0 :
        count = -1
        break

    
    temp = ''

    for i in range(len(duck)):
        if duck[i] =='q' and (temp=='' or temp=='k') and visited[i]==False:
            temp = 'q'
            visited[i] = True


        elif duck[i] == 'u' and temp=='q' and visited[i]==False:
            temp = 'u'
            visited[i] = True
        

        elif duck[i] == 'a' and temp == 'u' and visited[i]==False:
            temp = 'a'
            visited[i] = True
        
        
        elif duck[i] == 'c' and temp == 'a' and visited[i]==False:
            temp = 'c'
            visited[i] = True
        
        
        elif duck[i] == 'k' and temp == 'c' and visited[i]==False:
            temp = 'k'
            visited[i] = True

    if temp != 'k':
        count = -1
        break

    count += 1  

print(count)