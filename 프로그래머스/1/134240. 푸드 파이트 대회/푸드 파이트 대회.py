def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        num = food[i] // 2
        
        answer += str(i) * num
    
    full_answer = answer + "0" + answer[::-1]

    return full_answer