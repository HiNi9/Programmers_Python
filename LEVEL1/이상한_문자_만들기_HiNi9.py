def solution(s):
    answer = ''
    flag = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            flag = 0
            
        elif flag == 0:
            answer += s[i].upper()
            flag = 1
            
        elif flag == 1:
            answer += s[i].lower()
            flag = 0
            
    return answer