def solution(a, b):
    sum = 0
    bwn = abs(b - a) + 1
    for i in range(bwn):
        if a <= b:
            sum = sum + a
            a = a + 1
        else:
            sum = sum + a
            a = a - 1
    return sum