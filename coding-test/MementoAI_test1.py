def solution(x,n):
    i = x
    answer = []
    for _ in range(n):
        answer.append(i)
        i += x
    return  answer