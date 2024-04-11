S = int(input())

result =0
i=1

# 1부터 i 까지 합친 값이 입력된 수보다 같거나 작을때까지
while result<=S :
    #총합에 i를 더한다
    result+=i
    
    #만약 총합이 입력된 수보다 작을 경우
    if result <S and result+i+1 <= S  :
        i+=1
    else : 
        break

print(i)
    