N = int(input())
olist = []
is_find = False

for _ in range(N):
    option_list = list(map(str, input().split() ))
    
    # 첫 글자 순회
    for i in range(len(option_list)):
        if option_list[i][0].upper() not in olist and option_list[i][0].lower() not in olist and is_find == False:
            olist.append(option_list[i][0])
            r = (f"[{option_list[i][0]}]")
            option_list[i] = r + option_list[i][1:]
            is_find = True
            break
    
    
    # 다른 글자 순회
    if is_find == False :

        for i in range(len(option_list)):
            for j in range(1,len(option_list[i])):
                
                if option_list[i][j].upper() not in olist and option_list[i][j].lower() not in olist:
                    olist.append(option_list[i][j])
                    r = (f"[{option_list[i][j]}]")
                    option_list[i] = option_list[i][0:j] + r + option_list[i][j+1:]
                    is_find = True
                    break
            
            if is_find == True:
                break

    print(*option_list)
    is_find = False