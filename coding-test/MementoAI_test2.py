def solution(phone_number):
    last_number = phone_number[-4:]
    secret = '*' * (len(phone_number) - 4)
    answer = secret + last_number
    return answer