words = input()
answer = ""
word = ""
is_tag = False

for char in words :

    # 태그는 냅둠
    if char == "<":
        answer += word[::-1]
        word = ""

        is_tag = True
        answer += char

    elif char == ">":
        is_tag = False
        answer += char
        

    elif is_tag:
        answer += char
    
    # 태그가 아닌 경우
    else:
        # 공백
        if char == " ":
            answer += word[::-1] + " "
            word = ""

        else: 
            word += char

        

answer += word[::-1]
        
print(answer)