def solution(phone_number):
    length = len(phone_number)
    num = phone_number[-4:]
    answer = f"*"*(length-4)
    answer+= num
    
    return answer