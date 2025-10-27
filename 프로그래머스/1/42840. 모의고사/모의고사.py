def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1,c2,c3 =0,0,0

    # for i in range(len(answers)):
    #     p1 += p1
    #     p2 += p2
    #     p3 += p3
    count = []
    for i in range(len(answers)):
        if answers[i] == p1[i%len(p1)]:
            c1 +=1
        
        if answers[i] == p2[i%len(p2)]:
            c2 += 1
        
        if answers[i] == p3[i%len(p3)]:
            c3 += 1
    
    count= (c1,c2,c3)
    max_count = max(count)
    max_count_index = count.index(max_count)
    result =[]

    for i in range(len(count)) :
        if max_count == count[i]:
            result.append(i+1)
    
    
    
    

    
    
    
    
    return result