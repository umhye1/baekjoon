# 모음 
aset =['a','e','i','o','u']

while True:
    password = str(input().rstrip())

    if password == "end":
        break

    acceptable = True

    # 모음이 하나도 없는 경우
    if not any(v in password for v in aset):
        acceptable = False
        

    for i in range(len(password)-1):
        
        # 같은 글자 연속인경우 (ee,oo예외)
        if password[i] == password[i+1] and password[i] not in ['e','o']:
            acceptable = False
            break

        # 모음 3개 / 자음 3개 연속된 경우
        if i < len(password)-2:
            if password[i] in aset and password[i+1] in aset and password[i+2] in aset:
                acceptable = False
                break
            
            if password[i] not in aset and password[i+1] not in aset and password[i+2] not in aset:
                acceptable = False
                break

    if acceptable:
        print(f"<{password}> is acceptable.")
    
    else:
        print(f"<{password}> is not acceptable.")
