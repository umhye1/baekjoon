a,b,v= map(int, input().split())
#달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 미리 빼서 나누기

date =int((v-b)/(a-b))
if (v-b)%(a-b)!=0:
    date+=1
    
print(date)
