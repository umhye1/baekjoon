word = list(input())
cnt = {}

# 딕셔너리로 셈
for i in range(len(word)):
    if word[i] in cnt:
        cnt[word[i]] += 1
    else :
        cnt[word[i]] = 1

# 홀수 개수 체크
odd = 0

# 가운데 글자 찾기
mid = ""

sorted_chars = sorted(cnt.keys())

for char in sorted_chars:
    if cnt[char] % 2 == 1:
        odd += 1
        mid = char
    
    if odd  > 1:
        print("I'm Sorry Hansoo")
        exit()

answer = ""
for char in sorted_chars:
    answer += char*(cnt[char]//2)

print(answer + mid +answer[::-1])