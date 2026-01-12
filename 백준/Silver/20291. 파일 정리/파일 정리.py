n = int(input())
file = {}
for i in range(n):
    s = input().strip()
    new_s = s.split('.')[-1]
    
    if new_s in file:
        file[new_s] += 1
    else :
        file[new_s] = 1
    
sorted_keys = sorted(file.keys())
for key in sorted_keys:
    print(key, file[key])


