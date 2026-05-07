numlist = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]

def solution(s):
    
    for i in range(len(numlist)):
        s = s.replace(numlist[i],str(i))
        
            
    answer = int(s)
    return answer