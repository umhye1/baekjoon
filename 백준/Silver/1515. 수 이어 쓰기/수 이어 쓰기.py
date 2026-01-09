s = input().rstrip()

n = 0       # 늘려갈 숫자
idx = 0     # 현재 찾아야 할 s의 인덱스

while True:
    n += 1
    n_str = str(n) #  문자열로 변환 
    
    # n의 각 자릿수를 하나씩 확인
    for char in n_str:
        # 우리가 찾는 숫자(s[idx])와 현재 자릿수(char)가 같다면
        if char == s[idx]:
            idx += 1 # 다음 찾을 숫자로 넘어감
            
            # 만약 s의 모든 숫자를 다 찾았다면
            if idx == len(s):
                print(n) # 현재 n을 출력하고
                exit()