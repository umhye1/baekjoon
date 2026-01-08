n = int(input())

for i in range(n):
    word = input()
    cnt = [0]*26

    for c in word:
        if 'a' <= c <= 'z':
            cnt[ord(c)- ord('a')] += 1
    
    max_count = max(cnt)

    if cnt.count(max_count) > 1: # cnt배열에서 3인거 찾기(max값).
        print('?')

    else:
        print(chr(cnt.index(max_count) + ord('a')))