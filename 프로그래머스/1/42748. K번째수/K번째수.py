def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i = commands[a][0] 
        j = commands[a][1]
        k = commands[a][2]
        
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])
        
    
    return answer