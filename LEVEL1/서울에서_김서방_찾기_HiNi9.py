def solution(seoul):
    i = 0
    while i < len(seoul):
        if seoul[i] == "Kim":
            answer = "김서방은 " + str(i) + "에 있다"
            break
        i = i + 1
    return answer